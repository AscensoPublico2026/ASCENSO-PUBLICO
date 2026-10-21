import sys, numpy as np, cv2
from PIL import Image
base = sys.argv[1]
import glob
def P(p): return glob.glob(f"pages/r{p}-*.png")[0].split("/")[-1]
items = {
 "dot_camibuso": (P(19), (506,141,703,396)),
 "dot_pantalon": (P(20), (552,139,684,468)),
 "epp_gafas": (P(8), (493,207,785,417)),
 "epp_orejeras": (P(7), (108,153,361,458)),
 "cal_tenis": (P(43), (108,615,403,793)),
 "cal_botapvc": (P(44), (147,540,366,805)),
 "alt_arnes": (P(26), (103,185,277,457)),
 "alt_mosq": (P(28), (127,122,301,395)),
 "sen_cinta": (P(46), (77,176,433,429)),
 "eme_botiquin": (P(55), (77,190,395,408)),
 "eme_camilla": (P(54), (130,200,275,810)),
}
for name,(pg,box) in items.items():
    im = Image.open(f"{base}/pages/{pg}").convert("RGB").crop(box)
    a = np.array(im).astype(np.int16)
    # local background estimate from border ring
    ring = np.concatenate([a[:6].reshape(-1,3), a[-6:].reshape(-1,3), a[:,:6].reshape(-1,3), a[:,-6:].reshape(-1,3)])
    bg = np.median(ring, axis=0)
    dist = np.abs(a - bg).max(axis=2)
    hsv = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2HSV)
    fg = ((dist > 22) | (hsv[...,1] > 60)).astype(np.uint8)
    fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((5,5),np.uint8))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(fg, 8)
    keep = np.zeros_like(fg)
    big = max(stats[1:,4])
    for i in range(1,n):
        if stats[i,4] >= 0.04*big: keep[lab==i] = 1
    # fill holes
    inv = (1-keep).astype(np.uint8); h,w = inv.shape
    ff = inv.copy(); mask = np.zeros((h+2,w+2),np.uint8)
    cv2.floodFill(ff,mask,(0,0),2)
    keep[(ff==1)] = 1
    keep = cv2.erode(keep, np.ones((3,3),np.uint8))
    alpha = cv2.GaussianBlur(keep.astype(np.float32)*255,(0,0),1.1)
    rgba = np.dstack([np.array(im), alpha.astype(np.uint8)])
    ys,xs = np.where(alpha>10)
    rgba = rgba[ys.min():ys.max()+1, xs.min():xs.max()+1]
    Image.fromarray(rgba,"RGBA").save(f"{base}/build/cut/{name}.png")
    # flat-gray preview
    out = Image.new("RGB",(rgba.shape[1],rgba.shape[0]),(243,243,243))
    out.paste(Image.fromarray(rgba,"RGBA"), (0,0), Image.fromarray(rgba,"RGBA"))
    out.save(f"{base}/build/cut/{name}_gris.png")
    print(name, rgba.shape, bg)
