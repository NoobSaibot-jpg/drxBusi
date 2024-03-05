import os
from tkinter import Tk, Label, Entry, Button, Checkbutton, IntVar, messagebox
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
pdfPath = config['Config']['BookScannedPath']

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.geometry('800x600')

        self.x = int(config['Scan']['X'])
        self.y = int(config['Scan']['Y'])

        self.var1 = IntVar(master) 
        self.var1.trace("w", lambda *args: self.update_preview())

        self.image_files = [os.path.join('img', filename) for filename in os.listdir('img') if filename.endswith('.jpg')]
        self.image1_path = self.image_files[0] if self.image_files else None
        self.image2_path = self.image_files[1] if len(self.image_files) > 1 else None

        self.image1 = self.load_image(self.image1_path, size=(250, 350))
        self.image2 = self.load_image(self.image2_path, size=(250, 350))

        self.label1 = Label(master, image=self.image1)
        self.label1.grid(column=1, row=1)

        self.label2 = Label(master, image=self.image2)
        self.label2.grid(column=3, row=1)

        self.NumInput = Entry(master)
        self.NumInput.grid(column=1, row=3)

        self.CitieInput = Entry(master)
        self.CitieInput.grid(column=2, row=3)

        self.DateInput = Entry(master)
        self.DateInput.grid(column=3, row=3)

        self.c1 = Checkbutton(master, text='Single', variable=self.var1)
        self.c1.grid(column=4, row=3)

        self.btn = Button(master, text='Convert', command=self.convertation)
        self.btn.grid(column=5, row=3)

        self.update_preview()

    def update_preview(self):
        if self.var1.get() == 1:
            self.image2 = self.load_image('img1.jpg', size=(250, 350))
        else:
            self.image2 = self.load_image(self.image2_path, size=(250, 350))
        self.label2.config(image=self.image2)

    def load_image(self, file_path, size):
        if file_path and os.path.exists(file_path):
            image = Image.open(file_path)
            image = image.resize(size)
            tk_image = ImageTk.PhotoImage(image)
            return tk_image
        return None

    def convertation(self):
        input_text = f'{self.NumInput.get()} {self.CitieInput.get()} {self.DateInput.get()}'
        if self.NumInput.get() and self.CitieInput.get() and self.DateInput.get():
            pdf_filename = f'{input_text}.pdf'
            if self.image_files:
                if len(self.image_files) >= 2:
                    c = canvas.Canvas(pdf_filename, pagesize=letter)
                    for img_file in self.image_files[:2]:
                        c.drawImage(img_file, self.x, self.y, width=letter[0], height=letter[1])
                        c.showPage()
                        os.remove(img_file)  
                    c.save()
                    messagebox.showinfo('Success', f'PDF created: {pdf_filename}')
                    
                    self.image_files = [filename for filename in self.image_files if filename not in self.image_files[:2]]
                    self.image1_path = self.image_files[0] if self.image_files else None
                    self.image2_path = self.image_files[1] if len(self.image_files) > 1 else None
                    
                    self.image1 = self.load_image(self.image1_path, size=(250, 350))
                    self.image2 = self.load_image(self.image2_path, size=(250, 350))
                    self.label1.config(image=self.image1)
                    self.label2.config(image=self.image2)

                    if not self.image_files:
                        messagebox.showinfo('Info', 'No more images left in the folder')
                        self.master.quit()
                else:
                    messagebox.showerror('Error', 'Insufficient images in the folder')
            else:
                messagebox.showerror('Error', 'No images found in the folder')
        else:
            messagebox.showerror('Error', 'Not description')

root = Tk()
app = ImageConverterApp(root)

if __name__ == '__main__':
    root.mainloop()










