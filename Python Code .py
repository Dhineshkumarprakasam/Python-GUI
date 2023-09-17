#simple calculator
from tkinter import *
from tkinter import messagebox as mb
import os 

class dhinesh:
    def __init__(self):
        self.root=Tk()
        self.root.minsize(386,336)
        self.root.maxsize(367,336)
        self.root.title("Calculator")
        self.his=open('calhistory.txt','a')
    def window(self):
        def calculator(exp):
            while True:
                try:
                    self.ans=str(eval(exp))
                    mb.showinfo('Answer',self.ans)
                    break
                except SyntaxError or NameError:
                    mb.showerror('Error','Something went wrong try again')
                    break
            return
        def history(exp,ans):
            text=exp+' = '+str(ans)+'\n'
            self.his.write(text)
            self.his.flush()
        def answer():
            exp=textbox.get()
            calculator(exp)
            history(exp,self.ans)
        def clear():
            textbox.delete(0,END)
            return
        def hisop():
            os.startfile('calhistory.txt')
        def click(val):
            current=textbox.get()
            textbox.delete(0,END)
            textbox.insert(0,current+val)
            return 
            
            
        textbox=Entry(self.root,width=30,font='arial 16 bold',fg='blue',selectbackground='red',selectforeground='yellow')
        textbox.grid(row=0,column=0,columnspan=5,pady=20)

        b1=Button(self.root,text='1',padx=30,pady=20,font='arial 10 bold',command=lambda:click('1'))
        b2=Button(self.root,text='2',padx=30,pady=20,font='arial 10 bold',command=lambda:click('2'))
        b3=Button(self.root,text='3',padx=30,pady=20,font='arial 10 bold',command=lambda:click('3'))
        b4=Button(self.root,text='4',padx=30,pady=20,font='arial 10 bold',command=lambda:click('4'))
        b5=Button(self.root,text='5',padx=30,pady=20,font='arial 10 bold',command=lambda:click('5'))
        b6=Button(self.root,text='6',padx=30,pady=20,font='arial 10 bold',command=lambda:click('6'))
        b7=Button(self.root,text='7',padx=30,pady=20,font='arial 10 bold',command=lambda:click('7'))
        b8=Button(self.root,text='8',padx=30,pady=20,font='arial 10 bold',command=lambda:click('8'))
        b9=Button(self.root,text='9',padx=30,pady=20,font='arial 10 bold',command=lambda:click('9'))
        b0=Button(self.root,text='0',padx=30,pady=20,font='arial 10 bold',command=lambda:click('0'))
        bdot=Button(self.root,text='.',padx=31,pady=20,font='arial 10 bold',command=lambda:click('.'))
        
        bplus=Button(self.root,text='+',padx=30,pady=20,font='arial 10 bold',fg='white',bg='#ff8b3d',activeforeground='yellow',activebackground='#ff9d5c',command=lambda:click('+'))
        bminus=Button(self.root,text='-',padx=30,pady=20,font='arial 10 bold',fg='white',bg='#ff8b3d',activeforeground='yellow',activebackground='#ff9d5c',command=lambda:click('-'))
        bmul=Button(self.root,text='*',padx=31,pady=20,font='arial 10 bold',fg='white',bg='#ff8b3d',activeforeground='yellow',activebackground='#ff9d5c',command=lambda:click('*'))
        bdiv=Button(self.root,text='/',padx=30,pady=20,font='arial 10 bold',fg='white',bg='#ff8b3d',activeforeground='yellow',activebackground='#ff9d5c',command=lambda:click('/'))
        equalb=Button(self.root,text='=',padx=28,pady=20,font='arial 10 bold',bg='green',fg='white',activebackground='#26d701',activeforeground='yellow',command=answer)
        acb=Button(self.root,width=13,text='AC',padx=21,font='arial 10 bold',fg='white',bg='#F85C4D',activeforeground='yellow',activebackground='#FF6C5C',pady=20,command=clear)
        hisb=Button(self.root,text='History',padx=20,pady=20,font='arial 10 bold',width=13,bg='blue',fg='white',activebackground='black',activeforeground='yellow',command=hisop)


        b7.grid(row=1,column=0)
        b8.grid(row=1,column=1)
        b9.grid(row=1,column=2)
        b4.grid(row=2,column=0)
        b5.grid(row=2,column=1)
        b6.grid(row=2,column=2)
        b1.grid(row=3,column=0)
        b2.grid(row=3,column=1)
        b3.grid(row=3,column=2)
        b0.grid(row=4,column=0)
        bplus.grid(row=3,column=3) 
        bminus.grid(row=3,column=4)
        bmul.grid(row=2,column=3)
        bdiv.grid(row=2,column=4)
        bdot.grid(row=4,column=1)
        equalb.grid(row=4,column=4)
        acb.grid(row=4,column=2,columnspan=2)
        hisb.grid(row=1,column=3,columnspan=2)

        self.root.mainloop()
        
        
obj=dhinesh()
obj.window()
