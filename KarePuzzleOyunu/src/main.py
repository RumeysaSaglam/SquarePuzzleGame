from tkinter import filedialog, messagebox

import cv2

import random

import self as self

from functools import partial
from tkinter import *
from tkinter import messagebox


button_identities = []
lastButton = None
button_list = []
buttonClik = []
imgShuffle = []
imgList = []
score=None
counter=0

hp=None
wp=None
firsTrueImage=[]


def choseFile(master):
    ftypes = [
        ('image files', '*.jpg'),
        ('image files', '*.png'),
        ('image files', '*.jpeg'),
        ('image files', '*.bmp'),
    ]

    master.filename = filedialog.askopenfilename(filetypes=ftypes)
    print(master.filename)


    return master.filename

def callback():



    global button_identities
    button_identities=[]

    global firsTrueImage
    firsTrueImage=[]

    global score
    score=0

    global counter
    counter=0

    imgPath1 = self.imgPath
    img = cv2.imread(imgPath1)

    h = img.shape[0]
    w = img.shape[1]

    std_size = 786
    a = std_size / max(w, h)
    h = int(a * h)
    w = int(a * w)
    img = cv2.resize(img, (w, h))

    global imgList
    imgList = imageList(img)

    y = 0
    for i in imgList:
        cv2.imwrite("/home/rumeysa/PycharmProjects/KarePuzzleOyunu/slice_images/image" + str(y) + ".png", i) #slice image path
        y += 1

    global imgShuffle
    imgShuffle = listShuffle(imgList)

    y = 0
    for i in imgShuffle:
        cv2.imwrite("/home/rumeysa/PycharmProjects/KarePuzzleOyunu/Suffle_image/image" + str(y) + ".png", i) #shuffle image path
        y += 1





    same = False

    for m in range(0, 16, 1):
        for i in range(0, hp, 1):
            for j in range(0, wp, 1):
                for r in range(0, 3, 1):
                    if imgList[m][i, j, r] == imgShuffle[m][i, j, r]:
                        same = True
                    else:
                        same = False
                        break
                if not same:
                    break
            if not same:
                break
        if same:
            firsTrueImage.append(m)
            counter+=1


    score= score+6.25*counter

    if counter ==0:
        messagebox.showinfo("UYARI", "oyuna baslamak için en az bir puzle parçası dogru olmalı tekrar karıstırın" )

    elif counter==16:
        score=100
        messagebox.showinfo("Score","Scorunuz: "+str(score))
        fname = "/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore" #high score path
        s = file_len(fname)
        if s == 0:
            f = open('/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore', 'w') #high score path
            f.write(str(score) + "\n")
            f.close()
        else:
            f = open('/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore', 'a') #high score path
            f.write(str(score) + "\n")
            f.close()


        puzzle(master, img)


    else:
        #messagebox.showinfo("Title", "counter: " + str(counter))
        puzzle(master, img)



def change(n):
    if n == 0:
        imageP = button_identities[n].image
        buttonClik.append(n)



    elif n == 1:
        buttonClik.append(n)



    elif n == 2:
        buttonClik.append(n)


    elif n == 3:
        buttonClik.append(n)

    elif n == 4:
        buttonClik.append(n)

    elif n == 5:
        buttonClik.append(n)

    elif n == 6:
        buttonClik.append(n)

    elif n == 7:
        buttonClik.append(n)

    elif n == 8:
        buttonClik.append(n)

    elif n == 9:
        buttonClik.append(n)

    elif n == 10:
        buttonClik.append(n)

    elif n == 11:
        buttonClik.append(n)

    elif n == 12:
        buttonClik.append(n)

    elif n == 13:
        buttonClik.append(n)

    elif n == 14:
        buttonClik.append(n)

    elif n == 15:
        buttonClik.append(n)

    substitution()


def substitution():
    if len(buttonClik) >= 2:
        lastindex = buttonClik[-1]
        imageP = button_identities[lastindex].image
        lastindex2 = buttonClik[-2]
        imageP2 = button_identities[lastindex2].image

        button_identities[lastindex].config(image=imageP2)
        button_identities[lastindex].image = imageP2


        button_identities[lastindex2].config(image=imageP)
        button_identities[lastindex2].image = imageP

        del buttonClik[-1]
        del buttonClik[-1]

        temp = imgShuffle[lastindex]
        imgShuffle[lastindex] = imgShuffle[lastindex2]
        imgShuffle[lastindex2] = temp

        control(lastindex, lastindex2)


def control(lastindex,lastindex2):
    flag=0
    flag2=0
    for i in range(0,hp,1):
        for j in range (0,wp,1):
            for r in range(0,3,1):
                if imgList[lastindex][i,j,r]!=imgShuffle[lastindex][i,j,r]:
                    flag=1

    for i in range(0,hp,1):
        for j in range (0,wp,1):
            for r in range(0,3,1):
                if imgList[lastindex2][i,j,r]!=imgShuffle[lastindex2][i,j,r]:
                    flag2=1
    global score
    global counter

    if flag == 1:
        score=score-1
    else:
        button_identities[lastindex].config(state="disabled")
        score= score + 6.25
        counter=counter+1


    if flag2 == 1:
        score=score-1
    else:
        button_identities[lastindex2].config(state="disabled")
        score = score + 6.25
        counter=counter+1

    if counter==16:
        messagebox.showinfo("Title", "Score: " + str(score))
        fname = "/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore" #high score path
        s = file_len(fname)
        if s == 0:
            f = open('/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore', 'w') #high score path
            f.write(str(score) + "\n")
            f.close()
        else:
            f = open('/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore', 'a') #high score path
            f.write(str(score) + "\n")
            f.close()
    else:
        pass


def puzzle(master, img):
    offset = 0.2
    h = img.shape[0]
    w = img.shape[1]

    if h == w:
        rh = offset
        rw = offset
        #print("rw,rh: {}, {}".format(rw, rh))
    elif h > w:
        rh = offset
        rw = rh * (w / h)
        #print("rw,rh: {}, {}".format(rw, rh))
    else:
        rw = offset
        rh = rw * (h / w)
        #print("rw,rh: {}, {}".format(rw, rh))

    global t
    t=0
    p = offset
    k = offset

    for i in range(0, 4):
        for j in range(0, 4):
            btnName = "button" + str(t)
            btnClick = "button" + str(t)

            btnName = Button(master, command=partial(change, t))
            btnName.pack()
            btnName.place(relx=k, rely=p, relheight=rh, relwidth=rw)
            imageP = PhotoImage(
                file="/home/rumeysa/PycharmProjects/KarePuzzleOyunu/Suffle_image/image" + str(t) + ".png") #shuffle image path
            btnName.config(image=imageP)
            btnName.image = imageP
            button_identities.append(btnName)


            k = k + rw
            if k >= (5 * rw):
                k = offset
            t = t + 1

        p = p + rh

    for k in firsTrueImage:
        button_identities[k].config(state="disabled")


    mainloop()


def imageList(img):
    h = img.shape[0]
    w = img.shape[1]

    h1 = int(h / 4)
    w1 = int(w / 4)

    global hp, wp
    hp = h1
    wp = w1


    imgList = []

    for i in range(0, h, h1)[0:4]:
        for j in range(0, w, w1)[0:4]:
            #print(str(i) + " " + str(i + h1))
            #print(str(j) + " " + str(j + w1))

            imgList.append(img[i:i + h1, j:j + w1, :])

    return imgList


def listShuffle(list):
    tmp = []


    for i in list:
        tmp.append(i)


    random.shuffle(tmp)

    return tmp

def compare_images(input_image, output_image):
    if input_image.size != output_image.size:
        return False

    rows, cols = input_image.size

    for row in range(rows):
        for col in range(cols):
            input_pixel = input_image.getpixel((row, col))
            output_pixel = output_image.getpixel((row, col))
            if input_pixel != output_pixel:
                return False

    return True

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


if __name__ == "__main__":
    #print(cv2.__version__)
    master = Tk()
    master.geometry("1000x1000")
    imagePath = choseFile(master)
    self.imgPath = imagePath
    buttonKaristir = Button(master, text="Karistir", command=callback)

    buttonKaristir.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=0.1)

    buttonKaristir.pack()

    f = open("/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore", 'r') #high score path

    lines=[]

    lines = f.readlines()
    fname = "/home/rumeysa/PycharmProjects/KarePuzzleOyunu/EnYuksekScore" #high score path
    s = file_len(fname)
    f.close()
    lines2=[]
    #print(type(lines[0]))
    s = file_len(fname)

    for i in range(s):
        lines2.append(float(lines[i].split("\n")[0]))

    var = StringVar()
    label = Label(master, textvariable=var, relief=RAISED,anchor=NE)

    var.set("En yuksek score: " + str(max(lines2)))
    label.pack()

    mainloop()
