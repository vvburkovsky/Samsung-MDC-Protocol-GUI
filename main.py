import tkinter as tk
from tkinter.ttk import Combobox


main_Window = tk.Tk()
main_Window.title("Light MDC Protocol GUI")
#main_Window.geometry("500x500")

dropbox_ip = Combobox(main_Window)
dropbox_ip['values'] = ('192.168.1.1', '192.168.1.2', '192.168.1.3')
dropbox_ip.current(0)

on_btn  = tk.Button(main_Window, text='ON', height=2, width=15, command=lambda: print('ON' + dropbox_ip.get()))
off_btn = tk.Button(main_Window, text='OFF', height=2, width=15, command=lambda: print('OFF' + dropbox_ip.get()))
dp_btn = tk.Button(main_Window, text='DP', command=lambda: print('DP' + dropbox_ip.get()))
hdmi_btn = tk.Button(main_Window, text='HDMI', command=lambda: print('HDMI' + dropbox_ip.get()))

dropbox_ip.grid(column=0, row=0)
on_btn.grid(column=0, row=5)
off_btn.grid(column=1, row=5)
dp_btn.grid(column=0, row=8)
hdmi_btn.grid(column=1, row=8)


main_Window.mainloop()