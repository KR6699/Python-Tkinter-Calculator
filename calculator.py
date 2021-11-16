import tkinter as tk 
from tkinter import *
from tkinter import font

root = tk.Tk()
root.geometry('400x500+300+300')
root.title("Calculator")

#-----------------------------------------------------------------------------------------------------------------

expression = ""
def input_number(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)
def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("0")
def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Enter a valid expression")
        expression = ""

#-------------------------------------------------------------------------------------------------------------------

# equation = StringVar()
# lbl = Label(root,text = 'label', textvariable=equation,anchor=E,font = ('arial',30,font.BOLD))
# lbl.pack(expand=True , fill = 'both')
row0 = Frame(root,bg='black')
row0.pack(expand=True , fill = 'both')

equation = StringVar()
input_field = Entry(row0,textvariable=equation,font = ('arial',30,font.BOLD),justify=RIGHT,foreground='white' , background='red')
input_field.pack(expand = True , fill = 'both',padx = 10 , pady = 10)

equation.set("Enter Expression")

row1 = Frame(root,bg='black')
row1.pack(expand=True , fill = 'both')

row2 = Frame(root,bg='black')
row2.pack(expand=True , fill = 'both')

row3 = Frame(root,bg='black')
row3.pack(expand=True , fill = 'both')

row4 = Frame(root,bg='black')
row4.pack(expand=True , fill = 'both')

#---------------------------------------------------------------------------------------------------------

btn1 = Button(row1 , text = '1' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(1, equation))
btn1.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn2 = Button(row1 , text = '2' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(2, equation))
btn2.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn3 = Button(row1 , text = '3' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(3, equation))
btn3.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btnplus = Button(row1 , text = '+' , font = ('arial',20,font.BOLD),foreground='white' , background='blue', command=lambda: input_number('+', equation))
btnplus.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

#---------------------------------------------------------------------------------------------------------

btn4 = Button(row2 , text = '4' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(4, equation))
btn4.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn5 = Button(row2 , text = '5' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(5, equation))
btn5.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn6 = Button(row2 , text = '6' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(6, equation))
btn6.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btnminus = Button(row2 , text = '-' , font = ('arial',20,font.BOLD),foreground='white' , background='blue', command=lambda: input_number('-', equation))
btnminus.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

#----------------------------------------------------------------------------------------------------------

btn7 = Button(row3 , text = '7' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(7, equation))
btn7.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn8 = Button(row3 , text = '8' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(8, equation))
btn8.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn9 = Button(row3 , text = '9' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(9, equation))
btn9.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btnmul = Button(row3 , text = '*' , font = ('arial',20,font.BOLD),foreground='white' , background='blue', command=lambda: input_number('*', equation))
btnmul.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

#---------------------------------------------------------------------------------------------------------------

btnc = Button(row4 , text = 'C' , font = ('arial',20,font.BOLD),foreground='white' , background='red', command=lambda: clear_input_field(equation))
btnc.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btn0 = Button(row4 , text = '0' , font = ('arial',20,font.BOLD),foreground='white' , background='green', command=lambda: input_number(0, equation))
btn0.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btnequal = Button(row4 , text = '=' , font = ('arial',20,font.BOLD),foreground='white' , background='red', command=lambda: evaluate(equation))
btnequal.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

btndiv = Button(row4 , text = '/' , font = ('arial',20,font.BOLD),foreground='white' , background='blue', command=lambda: input_number('/', equation))
btndiv.pack(side = LEFT , expand=True , fill = 'both',padx=10,pady=10)

root.mainloop()