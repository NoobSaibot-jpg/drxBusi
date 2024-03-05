import os
import configparser
from tkinter import *
from tkinter import messagebox

config = configparser.ConfigParser()

config.read('config.ini')

def create_folder(folder_name):
    main_path = config['Config']['BookScannedPath']
    try:
        full_path = os.path.join(main_path, folder_name)

        if not os.path.exists(full_path):
            # Создаем папку
            os.makedirs(full_path)
            print(f"Папка {full_path} успешно создана")
        else:
            messagebox.showwarning('Warning', f"Папка {full_path} уже существует")
    except Exception as e:
        messagebox.showerror('Error', f"Ошибка при создании папки {full_path}: {e}")

root = Tk()
root.geometry('250x500')

optionsVar = ["Встановлення батьківства", "Народження", "Смерть", "Шлюб", "Заміна Імені", "Розірвання шлюбу", "Усиновлення"]
optionsDistr = ["Луганська", "Донецька"]
selected_var = StringVar(root)
selected_var.set("")
selected_dist = StringVar(root)
selected_dist.set("")

dropdown1 = OptionMenu(root, selected_var, *optionsVar)
dropdown1.config(width=80)
dropdown1.pack(padx=10, pady=10)

numInput = Entry(root)
numInput.config(width=80)
numInput.pack(padx=10, pady=10)
startDateInput = Entry(root)
startDateInput.config(width=80)
startDateInput.pack(padx=10, pady=10)
endDateInput = Entry(root)
endDateInput.config(width=80)
endDateInput.pack(padx=10, pady=10)

dropdown2 = OptionMenu(root, selected_dist, *optionsDistr)
dropdown2.config(width=80)
dropdown2.pack(padx=10, pady=10)

def set_folder_name():
    first = selected_var.get()
    sec = numInput.get()
    thrid = startDateInput.get()
    four = endDateInput.get()
    five = selected_dist.get()
    full_name = f'{first}-{sec}-{thrid}-{four} ({five})'
    if first != '' and sec!='' and thrid!='' and four!='' and five!='':
        create_folder(full_name)
    else:
        messagebox.showerror('Error', create_folder())

btn = Button(root, text='Convert', command=set_folder_name)
btn.pack(padx=10, pady=10)

# new_folder_name = "новая_папка"
# create_folder(main_path, new_folder_name)

if __name__ == '__main__':
    root.mainloop()