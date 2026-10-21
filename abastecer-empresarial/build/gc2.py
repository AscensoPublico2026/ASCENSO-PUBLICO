import numpy as np, cv2
from PIL import Image
src='/root/.claude/uploads/88dfebe0-d640-59d8-a378-4bedfd096156/2d412bae-image.png'
im=cv2.cvtColor(cv2.imread(src),cv2.COLOR_BGR2RGB); H,W=im.shape[:2]
x0,y0,x1,y1=396,364,752,950
sub=im[y0:y1,x0:x1].astype(int); gray=sub.mean(axis=2)
bg=np.array([240,239,235]); d=np.abs(sub-bg).max(axis=2)
mask=np.full((H,W),cv2.GC_BGD,np.uint8); m=np.full(gray.shape,cv2.GC_PR_BGD,np.uint8)
m[(d>28)]=cv2.GC_PR_BGD
m[gray<105]=cv2.GC_FGD                      # tela, plástico, ruedas: negro
yy,xx=np.mgrid[y0:y1,x0:x1]
base=(xx>455)&(xx<735)&(yy>770)&(yy<945)&(d>28)&(gray<225)
m[base]=cv2.GC_PR_FGD
mask[y0:y1,x0:x1]=m
cv2.grabCut(cv2.cvtColor(im,cv2.COLOR_RGB2BGR),mask,None,np.zeros((1,65)),np.zeros((1,65)),5,cv2.GC_INIT_WITH_MASK)
fg=((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD)).astype(np.uint8)[y0:y1,x0:x1]
# elimina el pad (abajo a la derecha) y restos del estante (izq.)
fg[(xx-x0>300)&(yy-y0>800-y0+0)]=0
n,lab,st,_=cv2.connectedComponentsWithStats(fg,8); big=1+np.argmax(st[1:,4]); fg=(lab==big).astype(np.uint8)
inv=(1-fg).astype(np.uint8); ff=inv.copy(); mm=np.zeros((fg.shape[0]+2,fg.shape[1]+2),np.uint8); cv2.floodFill(ff,mm,(0,0),2)
fg[ff==1]=1; fg=cv2.erode(fg,np.ones((3,3),np.uint8))
al=cv2.GaussianBlur(fg.astype(np.float32)*255,(0,0),1.0).astype(np.uint8)
rgba=np.dstack([im[y0:y1,x0:x1],al]); ys,xs=np.where(al>10); rgba=rgba[ys.min():ys.max()+1,xs.min():xs.max()+1]
p=Image.fromarray(rgba,'RGBA'); p.save('build/cut/mob_silla.png')
g=Image.new('RGB',p.size,(243,243,243)); g.paste(p,(0,0),p); g.save('build/cut/mob_silla_gris.png'); print(p.size)
