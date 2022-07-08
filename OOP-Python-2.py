import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Label1")
label2 = tkinter.Label(main_window, text = "Label2")

tombol1 = tkinter.Button(main_window, text = "Button1")
tombol2 = tkinter.Button(main_window, text = "Button2")

label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

main_window.mainloop()