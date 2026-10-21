import sys, glob, numpy as np, cv2
from PIL import Image, ImageDraw
out=[]
for f in sorted(glob.glob('pages/r*.png')):
    pg=f.split('/')[-1][1:].split('-')[0]
    im=Image.open(f).convert('RGB'); a=np.array(im).astype(np.int16)
    h,w=a.shape[:2]
    bg=np.array([243,242,242])
    dist=np.abs(a-bg).max(axis=2); hsv=cv2.cvtColor(np.array(im),cv2.COLOR_RGB2HSV)
    fg=((dist>26)|(hsv[...,1]>70)).astype(np.uint8)
    fg[:110]=0; fg[h-90:]=0                      # quita encabezado/pie
    fg=cv2.morphologyEx(fg,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(fg,8)
    k=0
    for i in range(1,n):
        x,y,ww,hh,ar=st[i]
        if ww>70 and hh>70 and ar>5000 and ww<500 and hh<400:
            k+=1; box=(max(x-6,0),max(y-6,0),min(x+ww+6,w),min(y+hh+6,h))
            out.append((pg,k,box))
            ImageDraw.Draw(im).rectangle(box,outline=(255,0,0),width=3)
            ImageDraw.Draw(im).text((box[0]+4,box[1]+4),f'{pg}.{k}',fill=(255,0,0))
    im.resize((w//2,h//2)).save(f'auto/mark{pg}.png')
for o in out: print(o)
