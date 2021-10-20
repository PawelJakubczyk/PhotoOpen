from tkinter import Label, Tk, Button
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Photo Open")
step = 0


def next_img():
    global step
    global mainImage
    step += 1
    if step == len(imageList):
        step = 0
    mainImage = ImageTk.PhotoImage(Image.open('Image\\'+str(imageList[step])).resize((900, 675), Image.ANTIALIAS))
    imageLabel.config(image=mainImage)


def prew_img():
    global step
    global mainImage
    step -= 1
    if step == -1:
        step = len(imageList)-1    
    mainImage = ImageTk.PhotoImage(Image.open('Image\\'+str(imageList[step])).resize((900, 675), Image.ANTIALIAS))
    imageLabel.config(image=mainImage)


imageList = os.listdir('Image')

mainImage = ImageTk.PhotoImage(Image.open('Image\\'+str(imageList[step])).resize((900, 675), Image.ANTIALIAS))

imageLabel = Label(image=mainImage, height=900, width=675)
imageLabel.grid(row=0, column=0, columnspan=3)


previousButton = Button(root, text="<<<", width=10, heigh=3, borderwidth=4, command=prew_img)
exitButton = Button(root, text="Exit", width=10, heigh=3, borderwidth=4, command=root.quit)
nextButton = Button(root, text=">>>", width=10, heigh=3, borderwidth=4, command=next_img)
previousButton.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)

root.mainloop()

print(imageList)
print(step)
