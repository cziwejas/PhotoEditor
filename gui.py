from customtkinter import *
from PIL import Image
from tkinter import messagebox
from algorytmy import histogram
from algorytmy import krawedzie
from algorytmy import kontrast
from algorytmy import liniowe
from algorytmy import max
from algorytmy import mix
from algorytmy import min
from algorytmy import Mediana
from algorytmy import potegowa
from algorytmy import negatyw

'''''
Michał Sajewicz
Projekt2
'''''

window = CTk()
window.title("Michał Sajewicz Projekt")
window.resizable(False, False)
window.geometry("800x500")
set_appearance_mode("System")
set_default_color_theme("green")


class GUI:
    def __init__(self, window):
        self.chooseButton = CTkButton(master=window, text="Choose file", width=80, command=self.chooseFile)
        self.chooseButton.place(x=10, y=20)

        self.linearUpButton = CTkButton(master=window, text="Linear Filter 1", width=80, height=30, command=self.linear1)
        self.linearUpButton.place(x=60, y=140)

        self.linearDownButton = CTkButton(master=window, text="Linear Filter 2", width=80, height=30, command=self.linear2)
        self.linearDownButton.place(x=60, y=190)

        self.contrastButton = CTkButton(master=window, text="Contrast", width=90, height=30, command=self.contrast)
        self.contrastButton.place(x=60, y=240)

        self.imageLabel = CTkLabel(master=window, text="", width=625, height=325, fg_color=("black", "black"))
        self.imageLabel.place(x=160, y=90)

        self.minButton = CTkButton(master=window, text="Min Filter", width=80, height=50, command=self.minFilter)
        self.minButton.place(x=160, y=20)

        self.maxButton = CTkButton(master=window, text="Max Filter", width=80, height=50, command=self.maxFilter)
        self.maxButton.place(x=260, y=20)

        self.powButton = CTkButton(master=window, text="Power Filter", width=80, height=24, command=self.powFilter)
        self.powButton.place(x=360, y=20)

        self.powEntry = CTkEntry(master=window, width=80, height=24, placeholder_text="wykladnik")
        self.powEntry.place(x=360, y=50)

        self.medianButton = CTkButton(master=window, width=80, height=50, text="Median Filter",
                                      command=self.medianFilter)
        self.medianButton.place(x=460, y=20)

        self.resetButton = CTkButton(master=window, text="Reset Image", width=80, command=self.reset)
        self.resetButton.place(x=10, y=450)

        self.negativeButton = CTkButton(master=window, text="Negative", width=80, height=50, command=self.negatyw)
        self.negativeButton.place(x=570, y=20)

        self.robertsButton = CTkButton(master=window, text="Roberts Filter", width=100, height=24, command=self.roberts)
        self.robertsButton.place(x=230, y=430)

        self.robertsUpButton = CTkButton(master=window, text="Roberts Filter", width=100, height=24, command=self.roberts2)
        self.robertsUpButton.place(x=230, y=456)

        self.prewittButton = CTkButton(master=window, text="Prewitt Filter", width=100, height=24, command=self.prewitt)
        self.prewittButton.place(x=370, y=430)

        self.prewittUpButton = CTkButton(master=window, text="Prewitt Filter", width=100, height=24, command=self.prewitt2)
        self.prewittUpButton.place(x=370, y=456)

        self.sobelButton = CTkButton(master=window, text="Sobel Filter", width=100, height=24, command=self.sobel)
        self.sobelButton.place(x=510, y=430)

        self.sobelUpButton = CTkButton(master=window, text="Sobel Filter", width=100, height=24, command=self.sobel2)
        self.sobelUpButton.place(x=510, y=456)

        self.laplaceButton = CTkButton(master=window, text="Laplace Filter", width=100, height=24, command=self.laplace)
        self.laplaceButton.place(x=650, y=430)

        self.laplaceUpButton = CTkButton(master=window, text="Laplace Filter", width=100, height=24, command=self.laplace2)
        self.laplaceUpButton.place(x=650, y=456)

        self.mixMenu = CTkOptionMenu(master=window, values=["mix1", "mix2", "mix3", "mix4", "mix5", "mix6"], width=90, command=self.mix)
        self.mixMenu.place(x=60, y=290)

        self.histogramButton = CTkButton(master=window, text="Show histogram", width=80, height=50, command=self.histogram)
        self.histogramButton.place(x=680, y=20)

        self.selectedImage = ""
        self.currentImageCTk = ""
        self.currentImage = ""

    def chooseFile(self):
        self.selectedImage = filedialog.askopenfilename()
        self.currentImage = Image.open(self.selectedImage)
        self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
        self.imageLabel.configure(image=self.currentImageCTk)

    def minFilter(self):
        try:
            self.currentImage = min.minFilter(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def linear1(self):
        try:
            self.currentImage = liniowe.rozjasnienie(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def linear2(self):
        try:
            self.currentImage = liniowe.przyciemnienie(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def maxFilter(self):
        try:
            self.currentImage = max.maxFilter(self.currentImage)
            self.currentImageCTk = CTkImage(min.minFilter(self.currentImage), size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def powFilter(self):
        try:
            self.currentImage = potegowa.potegowa(self.currentImage, self.powEntry.get())
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")
        except ValueError:
            messagebox.showinfo("wrong value", "Enter power value")

    def medianFilter(self):
        try:
            self.currentImage = Mediana.medianFilter(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def negatyw(self):
        fun = getattr(negatyw, "negatyw")

        try:
            self.currentImage = fun(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def roberts(self):
        try:
            self.currentImage = krawedzie.roberts(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def roberts2(self):
        try:
            self.currentImage = krawedzie.roberts2(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def prewitt(self):
        try:
            self.currentImage = krawedzie.prewitt(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def prewitt2(self):
        try:
            self.currentImage = krawedzie.prewitt2(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def sobel(self):
        try:
            self.currentImage = krawedzie.sobel(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def sobel2(self):
        try:
            self.currentImage = krawedzie.sobel2(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def laplace(self):
        try:
            self.currentImage = krawedzie.laplace(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def laplace2(self):
        try:
            self.currentImage = krawedzie.laplace2(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def contrast(self):
        try:
            self.currentImage = kontrast.kontrast(self.currentImage)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def mix(self, choice):
        fun = getattr(mix, choice)

        try:
            secondImage = filedialog.askopenfilename()
            secondImageCTk = Image.open(secondImage)
            self.currentImage = fun(self.currentImage, secondImageCTk)
            self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
            self.imageLabel.configure(image=self.currentImageCTk)
        except AttributeError:
            messagebox.showinfo("no image!", "No image selected")

    def reset(self):
        self.currentImage = Image.open(self.selectedImage)
        self.currentImageCTk = CTkImage(self.currentImage, size=(625, 325))
        self.imageLabel.configure(image=self.currentImageCTk)

    def histogram(self):
        histogram.histogram(self.currentImage)


start = GUI(window)
window.mainloop()
