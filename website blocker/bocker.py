from tabnanny import check
from tkinter import *
from turtle import color

root = Tk()
root.geometry('500x300')
root.resizable(0,0) 
root.configure(bg='black')
root.title("Website blocker")
Label(root,text='Website blocker',font='timesnewroman 22 bold',fg='pink',bg='black').pack()
host = 'C:\Windows\System32\drivers\etc\hosts'
z = 0
re = '127.0.0.1'
websites = Text(root,font='arial 13',height='2',width='37')
websites.place(x = 140,y=64)
Label(root,text='Website Name:',font='timesnewroman 13 bold',fg='pink',bg='black').place(x=5,y=70)
web = websites.get(1.0,END)
website = list(web.split())
def blocker():
    web = websites.get(1.0,END)
    website = list(web.split())
    with open(host,'r+') as file:
        con = file.read() 
        for i in website:
            if i not in con:
                file.write(re+' '+i+'\n') 
                Label(root,text = 'Blocked',font= 'arial 20 bold',fg='pink',bg='black').place(x = 170,y = 220)

                
def unblocker():
    web = websites.get(1.0,END)
    website = list(web.split())
    check = 0
    with open(host,'r+') as file:
        con = file.readlines()
        file.seek(0)
        for i in con:
            if not any(web in i.split() for web in website):
                file.write(i)
            else:
                check = 1 
        file.truncate() 
    if check == 1:
        Label(root,text = 'UnBlocked',font= 'arial 20 bold',fg='pink',bg='black').place(x = 170,y = 220)
block = Button(root,text='block',font='arial 12 bold',pady = 5,command = blocker,width=6,bg = 'royal blue', activebackground='blue')
block.place(x = 170, y= 150)
unblock = Button(root,text='unblock',font='arial 12 bold',pady = 5,command = unblocker,width=6,bg = 'royal blue', activebackground='blue')
unblock.place(x = 250, y= 150)
root.mainloop()