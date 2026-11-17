from base64 import b85decode as X
Q=[(b-128)*9 for b in X('fPjF2fPjF2goT2HgN1>BfPjI4f`Wm6e}I62fq;R3e}I61fq;O2e}I61fPjI3e}I2~e}RF2fPjF2fPjF2fPjF2fPjF2hlYlQg@uNPgM@>Ef`WsCfq{U4fPjI4fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2dVPO>f_#5`eSU+1fr5a4eu9C5gN1{FfPsO6frEj8fPjI3fq{X5e}I61fq{X4e|~^~fPsI1e1Cp_e}8{}et&>}e}8^_e}I30fPa5}e}900fPjB~e}I93fq;O2e}I93fq{U3e}I62fPjC0et&>~fPa5}e|~>|e}8^{e}H{|e|~^~e}R91fr5d4e}RI5fr5d6fPjI5fq{U4fPjF3fq;O3fPsO5fq{X5fPsO4fPsO4e}I2~fPjC0e}900fPjC0fPjF2fPjF1fPjF2fPjF2fPjF2fq;O3fPjF3fPjF2fPjF2fPjF1e}900fPjC0e}I30fPa90fr5d8f`Ea7fq{a8gMxvAfPsO5fr5g8e}I62fq{U3e}900fPjF1et&;|fPjF1et&;}fPjE~e}I62fq;L1fPjI4fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF2fPjF1fPjF2fPjF2fPjF2fPjF1e}I92f`WpAe}900e}aL6fPa91fr5g9e}8{}fPsL3fPa91fPjF2e}I61fPjI3e}I61fPsL3fPa91e}8{|fPsO5fq{U5e}RF5f`Ng6e}I63f`Ng6fPsO6f`Nj8e}RF5fq{X6e}931fPsL3e}8{}e}8{}e}8{|fPa5}eu061et&>~fq;L2fPjC0fPsL2e}I91e}8~~e}8{}et>^}etv&`e}8{|et&;|fPjF0et&>~e}RC0fPaC3eSd#{fPsL2fPsO5fq{X5fPsO5fr5g7fPsO5fq{X5e}I62fq{U4e}I61fPjF1e}I61fPjC0et&;|e}I2}')]
MG_P=Q[0:64]
EG_P=Q[64:128]
MG_N=Q[128:192]
EG_N=Q[192:256]
MG_B=Q[256:320]
EG_B=Q[320:384]
MG_R=Q[384:448]
EG_R=Q[448:512]
MG_Q=Q[512:576]
EG_Q=Q[576:640]
MG_K=Q[640:704]
EG_K=Q[704:768]
import base64
import os,json,urllib.request
M=999999
F="abcdefgh"
V=[0,100,320,330,500,900,20000]
KN=[[]for _ in range(128)]
KG=[[]for _ in range(128)]
for s in range(128):
 if s&0x88:continue
 r,f=s>>4,s&7
 for a,b in((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
  x,y=r+a,f+b
  if 0<=x<8 and 0<=y<8:KN[s].append(x*16+y)
 for a in(-1,0,1):
  for b in(-1,0,1):
   if a or b:
    x,y=r+a,f+b
    if 0<=x<8 and 0<=y<8:KG[s].append(x*16+y)
DG=(-17,-15,15,17)
OR=(-16,-1,1,16)
A8=(-17,-16,-15,-1,1,15,16,17)
MT=[None,MG_P,MG_N,MG_B,MG_R,MG_Q,MG_K]
ET=[None,EG_P,EG_N,EG_B,EG_R,EG_Q,EG_K]
IW=[0]*128
IB=[0]*128
for s in range(128):
 if s&0x88:continue
 IW[s]=(7-(s>>4))*8+(s&7)
 IB[s]=(s>>4)*8+(s&7)
Z=[[((i*128+j)*0x9E3779B97F4A7C15+0x1234567)&0xFFFFFFFFFFFFFFFF for j in range(128)]for i in range(15)]
ZP=[((i*0xC2B2AE3D27D4EB4F+0x9E37)&0xFFFFFFFFFFFFFFFF)for i in range(256)]
PH=[0,0,1,1,2,4,0]
def parse(fn):
 b=[0]*128
 p=fn.split()
 r,f=7,0
 for ch in p[0]:
  if ch=="/":r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   c="PNBRQK".index(ch.upper())+1
   if ch.islower():c+=8
   b[r*16+f]=c;f+=1
 side=0 if p[1]=="w" else 1
 cast=0
 if len(p)>2 and p[2]!="-":
  for ch in p[2]:
   if ch=="K":cast|=1
   elif ch=="Q":cast|=2
   elif ch=="k":cast|=4
   elif ch=="q":cast|=8
 ep=-1
 if len(p)>3 and p[3]!="-":ep=(int(p[3][1])-1)*16+F.index(p[3][0])
 return b,side,cast,ep
def hk(b,side,cast,ep):
 h=0
 for s in range(128):
  q=b[s]
  if q:h^=Z[q][s]
 h^=ZP[side]^ZP[2+cast]
 if ep>=0:h^=ZP[34+ep]
 return h
def atk(b,sq,w):
 if w:
  if not(sq-15)&0x88 and b[sq-15]==1:return 1
  if not(sq-17)&0x88 and b[sq-17]==1:return 1
  for t in KN[sq]:
   if b[t]==2:return 1
  for t in KG[sq]:
   if b[t]==6:return 1
  bt,rt,qt=3,4,5
 else:
  if not(sq+15)&0x88 and b[sq+15]==9:return 1
  if not(sq+17)&0x88 and b[sq+17]==9:return 1
  for t in KN[sq]:
   if b[t]==10:return 1
  for t in KG[sq]:
   if b[t]==14:return 1
  bt,rt,qt=11,12,13
 for d in DG:
  t=sq+d
  while not t&0x88:
   q=b[t]
   if q:
    if q==bt or q==qt:return 1
    break
   t+=d
 for d in OR:
  t=sq+d
  while not t&0x88:
   q=b[t]
   if q:
    if q==rt or q==qt:return 1
    break
   t+=d
 return 0
def ksq(b,w):
 k=6 if w else 14
 for s in range(128):
  if b[s]==k:return s
 return 0
def gen(b,side,cast,ep,caps=0):
 o=[]
 ap=o.append
 w=(side==0)
 col=0 if w else 8
 for s in range(128):
  p=b[s]
  if not p:continue
  if (p<9)!=w:continue
  if p==1+col:
   d=16 if w else -16
   one=s+d
   if one>=0 and one<128 and not b[one]:
    if (one>>4)==(7 if w else 0):
     ap((s,one,5,0));ap((s,one,4,0));ap((s,one,3,0));ap((s,one,2,0))
    elif not caps:
     ap((s,one,0,0))
     st=(1 if w else 6)
     if (s>>4)==st and not b[s+2*d]:ap((s,s+2*d,0,0))
   for dd in(d-1,d+1):
    t=s+dd
    if t&0x88:continue
    q=b[t]
    if q and ((q>8)if w else(q<8)):
     if (t>>4)==(7 if w else 0):
      ap((s,t,5,0));ap((s,t,4,0));ap((s,t,3,0));ap((s,t,2,0))
     else:ap((s,t,0,0))
    elif not q and t==ep:ap((s,t,0,1))
  elif p==2+col:
   for t in KN[s]:
    q=b[t]
    if not q:
     if not caps:ap((s,t,0,0))
    elif((q>8)if w else(q<8)):ap((s,t,0,0))
  elif p==6+col:
   for t in KG[s]:
    q=b[t]
    if not q:
     if not caps:ap((s,t,0,0))
    elif((q>8)if w else(q<8)):ap((s,t,0,0))
  else:
   ty=p-col
   for dd in(DG if ty==3 else(OR if ty==4 else A8)):
    t=s+dd
    while not t&0x88:
     q=b[t]
     if not q:
      if not caps:ap((s,t,0,0))
     else:
      if((q>8)if w else(q<8)):ap((s,t,0,0))
      break
     t+=dd
 if not caps:
  if w:
   if cast&1 and b[4]==6 and b[7]==4 and not b[5]and not b[6] and not atk(b,4,0)and not atk(b,5,0)and not atk(b,6,0):ap((4,6,0,0))
   if cast&2 and b[4]==6 and b[0]==4 and not b[1]and not b[2]and not b[3] and not atk(b,4,0)and not atk(b,3,0)and not atk(b,2,0):ap((4,2,0,0))
  else:
   if cast&4 and b[116]==14 and b[119]==12 and not b[117]and not b[118] and not atk(b,116,1)and not atk(b,117,1)and not atk(b,118,1):ap((116,118,0,0))
   if cast&8 and b[116]==14 and b[112]==12 and not b[113]and not b[114]and not b[115] and not atk(b,116,1)and not atk(b,115,1)and not atk(b,114,1):ap((116,114,0,0))
 return o
def mk(b,m,cast,ep,side):
 s,t,pr,ef=m
 p=b[s]
 cap=b[t]
 cs=t
 if ef:
  cs=t-16 if side==0 else t+16
  cap=b[cs];b[cs]=0
 u=(p,cap,cast,ep,cs)
 b[s]=0
 b[t]=(pr+(8 if side else 0))if pr else p
 if not ef and (p&7)==6 and abs((t&7)-(s&7))==2:
  if t==6:b[5]=b[7];b[7]=0
  elif t==2:b[3]=b[0];b[0]=0
  elif t==118:b[117]=b[119];b[119]=0
  elif t==114:b[115]=b[112];b[112]=0
 nc=cast
 if s==4:nc&=12
 elif s==7:nc&=14
 elif s==0:nc&=13
 elif s==116:nc&=3
 elif s==119:nc&=11
 elif s==112:nc&=7
 if t==7:nc&=14
 elif t==0:nc&=13
 elif t==119:nc&=11
 elif t==112:nc&=7
 ne=-1
 if (p&7)==1 and abs((t>>4)-(s>>4))==2:ne=(s+t)>>1
 return u,nc,ne
def um(b,m,u):
 s,t,pr,ef=m
 p,cap,cast,ep,cs=u
 b[s]=p
 b[t]=0
 b[cs]=cap
 if not ef and (p&7)==6 and abs((t&7)-(s&7))==2:
  if t==6:b[7]=b[5];b[5]=0
  elif t==2:b[0]=b[3];b[3]=0
  elif t==118:b[119]=b[117];b[117]=0
  elif t==114:b[112]=b[115];b[115]=0
def ev(b,side):
 mg=eg=ph=0
 wb=bb=0
 wp=[0]*8
 bp=[0]*8
 for s in range(128):
  q=b[s]
  if not q:continue
  t=q&7
  ph+=PH[t]
  if q==3:wb+=1
  elif q==11:bb+=1
  if t==1:
   if q==1:wp[s&7]+=1
   else:bp[s&7]+=1
 if wb>1:mg+=23;eg+=40
 if bb>1:mg-=23;eg-=40
 for s in range(128):
  q=b[s]
  if not q:continue
  t=q&7
  if q<8:
   i=IW[s]
   mg+=V[t]+MT[t][i]
   eg+=V[t]+ET[t][i]
   if t==1 and wp[s&7]==1:
    r=s>>4;f=s&7;bl=0
    for rr in range(r+1,8):
     for ff in(f-1,f,f+1):
      if 0<=ff<8 and b[rr*16+ff]==9:bl=1;break
     if bl:break
    if not bl:eg+=12+r*9
  else:
   i=IB[s]
   mg-=V[t]+MT[t][i]
   eg-=V[t]+ET[t][i]
   if t==1 and bp[s&7]==1:
    r=s>>4;f=s&7;bl=0
    for rr in range(r-1,-1,-1):
     for ff in(f-1,f,f+1):
      if 0<=ff<8 and b[rr*16+ff]==1:bl=1;break
     if bl:break
    if not bl:eg-=12+(7-r)*9
 if ph>24:ph=24
 v=(mg*ph+eg*(24-ph))//24
 return v if side==0 else -v
ND=[0]
LM=[100000]
TT={}
KL=[[None,None]for _ in range(64)]
HS={}
def qs(b,side,cast,ep,al,be,d):
 ND[0]+=1
 st=ev(b,side)
 if st>=be:return be
 if st>al:al=st
 if d<=-5 or ND[0]>LM[0]:return al
 ms=gen(b,side,cast,ep,1)
 ms.sort(key=lambda m:-(V[b[m[1]]&7]*8-V[b[m[0]]&7]))
 for m in ms:
  u,nc,ne=mk(b,m,cast,ep,side)
  if atk(b,ksq(b,side==0),side!=0):um(b,m,u);continue
  sc=-qs(b,1-side,nc,ne,-be,-al,d-1)
  um(b,m,u)
  if sc>=be:return be
  if sc>al:al=sc
 return al
def ab(b,side,cast,ep,dep,al,be,ply,nl):
 ND[0]+=1
 if ND[0]>LM[0]:return ev(b,side)
 w=(side==0)
 ck=atk(b,ksq(b,w),not w)
 if ck:dep+=1
 if dep<=0:return qs(b,side,cast,ep,al,be,0)
 ms=gen(b,side,cast,ep)
 if not ms:return -M+ply if ck else 0
 if ply>0 and not ck and nl and dep>=3 and be<M-500:
  mt=0
  for s in range(128):
   q=b[s]
   if q:
    t=q&7
    if t>1:mt+=V[t]
  if mt>2200:
   oe=ep;ep=-1;side=1-side
   sc=-ab(b,side,cast,ep,dep-4,-be,-be+1,ply+1,0)
   side=1-side;ep=oe
   if sc>=be:return be
 h=hk(b,side,cast,ep)
 e=TT.get(h)
 tm=None
 if e:
  ed,ef,evv,em=e
  tm=em
  if ed>=dep and ply>0:
   if ef==0:return evv
   if ef==1 and evv<=al:return al
   if ef==2 and evv>=be:return be
 k1,k2=KL[ply]if ply<64 else(None,None)
 def ky(m):
  if tm is not None and m==tm:return -9999999
  q=b[m[1]]
  v=0
  if q:v=900000+100*V[q&7]-V[b[m[0]]&7]
  elif m==k1:v=800000
  elif m==k2:v=700000
  if m[2]:v+=600000
  return -v-HS.get((m[0],m[1]),0)
 ms.sort(key=ky)
 be0=-M;bm=None;og=al;i=0
 for m in ms:
  u,nc,ne=mk(b,m,cast,ep,side)
  if atk(b,ksq(b,w),not w):um(b,m,u);continue
  qt=(b[m[1]]==0 and not m[2] and not m[3])
  rd=0
  if qt and dep>=3 and i>=3 and not ck:
   rd=1+(i>=8)+(dep>=6)
   if rd>=dep:rd=dep-1
  if i==0:sc=-ab(b,1-side,nc,ne,dep-1,-be,-al,ply+1,1)
  else:
   sc=-ab(b,1-side,nc,ne,dep-1-rd,-al-1,-al,ply+1,1)
   if al<sc<be:sc=-ab(b,1-side,nc,ne,dep-1,-be,-al,ply+1,1)
   elif rd and sc<=al:
    sc=-ab(b,1-side,nc,ne,dep-1,-al-1,-al,ply+1,1)
    if sc>al:sc=-ab(b,1-side,nc,ne,dep-1,-be,-al,ply+1,1)
  um(b,m,u)
  if sc>be0:be0=sc;bm=m
  if sc>al:al=sc
  if al>=be:
   if qt:
    if ply<64:
     if KL[ply][0]!=m:KL[ply][1]=KL[ply][0];KL[ply][0]=m
    kk=(m[0],m[1]);HS[kk]=HS.get(kk,0)+dep*dep
   break
  i+=1
 if bm is None:return -M+ply
 fl=0 if og<be0<be else(2 if be0>=be else 1)
 if len(TT)<500000:TT[h]=(dep,fl,be0,bm)
 return be0
def u2m(u,b):
 s=(int(u[1])-1)*16+F.index(u[0])
 t=(int(u[3])-1)*16+F.index(u[2])
 pr="PNBRQK".index(u[4].upper())+1 if len(u)==5 else 0
 p=b[s]
 ef=1 if(p and (p&7)==1 and not b[t]and(s&7)!=(t&7))else 0
 return(s,t,pr,ef)
def pick(fen,legal):
 b,side,cast,ep=parse(fen)
 TT.clear();HS.clear()
 for i in range(64):KL[i]=[None,None]
 ND[0]=0
 mv=[(u,u2m(u,b))for u in legal]
 if len(mv)==1:return mv[0][0]
 ms=sorted(mv,key=lambda x:-(V[b[x[1][1]]&7]*8-V[b[x[1][0]]&7]))
 bt=ms[0][0]
 for d in range(1,24):
  if ND[0]>LM[0]:break
  cur=None;cs=-M-1;al=-M-1
  for u,m in ms:
   if ND[0]>LM[0]:break
   x,nc,ne=mk(b,m,cast,ep,side)
   if cs<=-M+200:sc=-ab(b,1-side,nc,ne,d,-M,M,1,1)
   else:
    sc=-ab(b,1-side,nc,ne,d,-al-60,-al+1,1,1)
    if sc>al:sc=-ab(b,1-side,nc,ne,d,-M,-al+1,1,1)
   um(b,m,x)
   if sc>cs:cs=sc;cur=u;al=sc
  if cur is None:break
  bt=cur
  ms=[(u,m)for u,m in ms if u!=cur]
  ms.insert(0,(cur,u2m(cur,b)))
  if cs>M-1000 or cs<-M+1000:break
 return bt
import os,json,urllib.request as U
E=os.environ["MAKEFUN_ENV_URL"]
def P(p,b):
 r=U.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 with U.urlopen(r)as x:return json.load(x)
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":pick(g["fen"],g["legal_moves"])})