import tkinter
#import tkMessageBox
import random
from tkinter import *
from tkinter import filedialog
import pyscreenshot as ImageGrab
from turtle import *

root = tkinter.Tk()
C = tkinter.Canvas(root,bg="snow")

menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)

menu=Menu()
root.config(menu=menu)

		##
submenu=Menu(menu)
menu.add_cascade(label="Triangular",menu=submenu)

a=submenu.add_command(label="  Pink-Yellow  ",command=lambda:shapet(fp,pink2))
a=submenu.add_command(label="  Blue-Green  ",command=lambda:shapet(fp,bl_gr))
a=submenu.add_command(label="  Blue-Pink  ",command=lambda:shapet(fp,bl_rd))
a=submenu.add_command(label="  Blue-Yellow  ",command=lambda:shapet(fp,bl_yl))
a=submenu.add_command(label="  Blue-White  ",command=lambda:shapet(fp,bl_wh))
b=submenu.add_command(label="Red-Yellow",command=lambda:shapet(fp,red2))

		##
b1=menu.add_command(label="       Save          ",command=lambda:getter())

		##
submenu2=Menu(menu)
menu.add_cascade(label="Circular",menu=submenu2)

b1=submenu2.add_command(label="       Mix          ",command=lambda:reloadp(fc,mix))
b1=submenu2.add_command(label="       Proffesional          ",command=lambda:reloadp(fc,colorful))
b1=submenu2.add_command(label="       Clean          ",command=lambda:reloadp(fc,clean))
b1=submenu2.add_command(label="       Clean2          ",command=lambda:reloadp(fc,clean2))
b1=submenu2.add_command(label="       Dark Blue          ",command=lambda:reloadp(fc,dark_blue))
b1=submenu2.add_command(label="       Pink          ",command=lambda:reloadp(fc,pink))
b1=submenu2.add_command(label="       Red          ",command=lambda:reloadp(fc,red))
b1=submenu2.add_command(label="       Medium         ",command=lambda:reloadp(fc,medium_blue))
b1=submenu2.add_command(label="       Light Green         ",command=lambda:reloadp(fc,light_green))

		##
submenu2=Menu(menu)
menu.add_cascade(label="Square",menu=submenu2)

b1=submenu2.add_command(label="       Mix          ",command=lambda:reloadp(fr,mix))
b1=submenu2.add_command(label="       Mix2          ",command=lambda:reloadp(fr,mix2))
b1=submenu2.add_command(label="       Fun          ",command=lambda:reloadp(fr,Fun))
b1=submenu2.add_command(label="       Proffesional          ",command=lambda:reloadp(fr,colorful))
b1=submenu2.add_command(label="       Clean          ",command=lambda:reloadp(fr,clean))
b1=submenu2.add_command(label="       Clean2          ",command=lambda:reloadp(fr,clean2))
b1=submenu2.add_command(label="       Dark Blue          ",command=lambda:reloadp(fr,dark_blue))
b1=submenu2.add_command(label="       Medium Blue         ",command=lambda:reloadp(fr,medium_blue))
b1=submenu2.add_command(label="       Light Blue         ",command=lambda:reloadp(fr,medium_blue))
b1=submenu2.add_command(label="       Pink          ",command=lambda:reloadp(fr,pink))
b1=submenu2.add_command(label="       Red          ",command=lambda:reloadp(fr,red))
b1=submenu2.add_command(label="       Light Green         ",command=lambda:reloadp(fr,light_green))

root.config(menu=b1)

o=0

def getter():
    x2=root.winfo_rootx()+C.winfo_x()
    y2=root.winfo_rooty()+C.winfo_y()
    x1=x2+C.winfo_width()
    y1=y2+C.winfo_height()
    print(x2,y2,x1,y1)
    I=ImageGrab.grab().crop((x2,y2,x1,y1))

    filename=filedialog.askdirectory()
    print(filename)
    I.save(str(filename)+"/test.jpg")

# color schemes
mix=["darkorange","orange","deeppink","darkorange","darkturquoise","hotpink","deeppink","darkturquoise","aqua","orangered","turquoise","cyan"]

light_blue=["cyan","darkturquoise","aquamarine","turquoise","silver","deepskyblue","dodgerblue","aqua","cyan","darkturquoise","aquamarine","turquoise","deepskyblue","dodgerblue"]

mix2=["yellow","orange","hotpink","lavender","deepskyblue","lightgreen","yellow","orange","hotpink","lavender","deepskyblue","lightgreen","yellow","orange","hotpink","lavender","deepskyblue","lightgreen","yellow","orange","lemonchiffon","yellow","gold","orange","orangered","darkorange","pink","hotpink","crimson","deeppink","palevioletred","magenta","indigo","greenyellow","limegreen","springgreen","lightgreen","springgreen","indigo","cadetblue","navy","aqua","darkcyan","turquoise","violet","dodgerblue","deepskyblue","powderblue","darkviolet","mediumslateblue","grey","silver"]

red=['firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3','OrangeRed2','OrangeRed3', 'OrangeRed4','red', 'red2', 'red3', 'red4']

purple=['purple', 'medium purple','DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4']

pink=['hotpink','maroon', 'medium violet red', 'violet red','maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4']

dark_blue=['midnight blue', 'navy', 'cornflower blue', 'dark slate blue','RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4' ]

medium_blue=['DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2','cyan3','cyan4',]

light_green=['lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4']

Fun=['#4abdac','#e34234','#ffe400','#d8d8d4','#4abdac','#e34234','#4abdac','#ffe400','#d8d8d4','#4abdac','#4abdac','#e34234','#ffe400','#d8d8d4','#4abdac','#e34234','#ffe400','#d8d8d4']

clean=['#f28500','#008080','#b0e0e6','#ffffff','#f28500','#008080','#b0e0e6','#ffffff','#f28500','#008080','#b0e0e6','#ffffff','#f28500','#008080','#b0e0e6','#ffffff']

clean2=['#625D5D','#FF3B3F','#EFEFEF','#CAEBF2','#625D5D','#FF3B3F','#EFEFEF','#CAEBF2','#625D5D','#FF3B3F','#EFEFEF','#CAEBF2','#625D5D','#FF3B3F','#EFEFEF','#CAEBF2']

colorful=['#445bce','#dddddd','#f9e900','#f19f04','#445bce','#dddddd','#f9e900','#f19f04','#445bce','#dddddd','#f9e900','#f19f04','#445bce','#dddddd','#f9e900','#f19f04']


col1=[]

pink2=[129,171,0,230,230,231,9,5]
red2 =[0,254,0,190,254,255,6,5]
bl_pi=[135,136,0,5,0,255,9,5]
bl_gr=[0,0,100,0,400,0,9,6]
bl_rd=[0,0,100,500,0,0,10,4]
bl_yl=[0,0,100,500,300,0,10,4]
bl_wh=[0,0,120,300,300,300,10,4]
blk_wh=[0,0,0,500,500,500,10,4]

fc=C.create_oval
fr=C.create_rectangle
fl=C.create_line
fa=C.create_arc
fp=C.create_polygon
f=fc

def shape(f,col):
	o=0
	Lx1=[]
	a=2000
	for m in range(0,500):

	    Lx1.append(a)
	    a=a-10
	Lx=Lx1

	Ly1=[]
	a=2000
	for m in range(0,500):
	    Ly1.append(a)
	    a=a-10
	Ly=Ly1
	
	for k in range (0,500):
	    x1=random.randint(0,len(Lx)-1)

	    x=Lx[x1]
	    Lx.pop(x1)

	    y1=random.randint(0,len(Ly)-1)
	    y=Ly[y1]
	    Ly.pop(y1)

	    r=random.randint(0,9)

	    c=[col[r],col[(r-1)],col[(r+1)]]
	    
	    L=[5,10,15,20]
	    r=random.randint(0,3)
	    i=L[r]
	    Lcord=[]
	    Lc=[]
	    
	    for j in range(0,7):
	    	crd=x+j*i,y+j*i,x+200-j*i,y+200-j*i
	    	Lcord.append(crd)
        	
        
	    for j in range(0,7):
	    	crd=x+j*i,y+j*i
	    	Lc.append(crd)
        

	    for j in range(0,k%5):
	        for i in range(0,j+4):
    		    x=i
    		    y=i%3
    		    if f!=fl and f!=fa:
    		    	arc = f(Lcord[x],outline=col[r],fill=c[y])
    		    else:
    		    	if f==fl:
    		    		arc=f(Lcord[x],width=10,fill=c[y])
    		    	if f==fa:
    		    		arc=f(Lc[x],1000+i,1000+i,width=10)
def reloadp(f,col):
	C.create_rectangle(0,0,1920,1080,fill="snow")
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)
	shape(f,col)

def shapet(f,lcc):
	print(lcc)
	col1=[]
	for i in range(lcc[0],lcc[1]):
		for j in range(lcc[2],lcc[3]):
			for k in range(lcc[4],lcc[5]):
				T=(k,j,i)
				col1.append('#%02x%02x%02x' % T)

	T=(lcc[0],lcc[1],lcc[2])
	for i in range(400):	
		l1=(lcc[0]-lcc[3])//256
		l2=(lcc[1]-lcc[4])//256
		l3=(lcc[2]-lcc[5])//256
		T=(T[0]-l1,T[1]-l2,T[2]-l3)
		col1.append('#%02x%02x%02x' % T)
		col1.append('#%02x%02x%02x' % T)
		print(T)


	col3=[]
	lY12=200

	for i in range(30,lY12//8*10):
		col3.append(col1[i])
	col3=col3+col3+col3
	

    #Lx,Ly
	X12=[]
	Y12=[]
	x=-200
	y=0
	l=0
	for m in range(lY12):

	    X12.append(random.randint(99,125)+x)
	    Y12.append(0)
	    x=X12[m]
	
	Yr=[20,100,200,300,400,500,600,700,800,900,1000,1100]
	X34=X12
	Y34=Y12
	x=-200
	y=0
	for i in range(len(Yr)):
		x=-200
		y=0
		Y34=[]
		X34=[]
		for j in range(len(Y12)):
		
			Y34.append(Yr[i]+random.randint(0,100))
			X34.append(random.randint(99,125)+x)
			x=X34[j]
		
		for k in range((len(Y12)-1)//8-6):
			x1=X12[k]
			x2=X12[k+1]
			x3=X34[k]
			x4=X34[k+1]
			y1=Y12[k]
			y2=Y12[k+1]
			y3=Y34[k]
			y4=Y34[k+1]
			print(len(col3),k*lcc[6],(len(Y12)-1)*lcc[6])
			c=col3[k*lcc[6]+i*lcc[7]+random.randint(0,10)]
			try:
				C.create_polygon(x1,y1,x3,y3,x4,y4,x2,y2,fill=c,width=1)    #,outline="snow"

			except:
				C.create_polygon(x1,y1,x3,y3,x4,y4,x2,y2,fill="white",width=1,outline="black") 
			l=int((lY12-1)/8)
			print(c)
		Y12=Y34
		X12=X34

C.pack(fill="both",expand=1)

C.wait_visibility(root)

root.wm_attributes('-alpha',1.0)

root.mainloop()
