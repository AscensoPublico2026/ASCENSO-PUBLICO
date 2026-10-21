import sys, numpy as np, cv2
from PIL import Image
base = sys.argv[1]
items = {
 "bota": ("q43-43.png", (470,170,790,400)),
 "alturas": ("q27-27.png", (520,585,785,832)),
 "cono": ("q47-47.png", (180,118,318,405)),
}
_old = {
 "overol":   ("p21-20.png", (225, 900, 470, 1355)),
 "casco":    ("p4-03.png",  (175, 240, 645, 605)),
 "chaleco":  ("p50-49.png", (130, 262, 572, 682)),
 "extintor": ("p53-52.png", (225, 205, 388, 602)),
 "guantes":  ("p39-38.png", (735, 895, 1240, 1305)),
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
