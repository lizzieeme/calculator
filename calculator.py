from tkinter import *
import ast

root = Tk()
i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    display.insert(i, operator)
    lenght = len(operator)
    i += lenght

def clearAll():
    display.delete(0,END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, "<string>", "eval"))
        clearAll()
        display.insert(0, result)
    except Exception:
        clearAll()
        display.insert(0, "Error")

def clear():
    string = display.get()
    if len(string):
        new_string = string[:-1]
        clearAll()
        display.insert(0, new_string)
    else:
        clearAll()
        display.insert(0, "")


display = Entry(root)
display.grid(row=1, columnspan=6)

numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button = Button(root, text=numbers[counter], width=2, height=2, command= lambda text=numbers[counter]:get_number(text))
        button.grid(row=x+2, column=y)
        counter+=1

button0 = Button(root, text='0', width=2, height=2, command= lambda :get_number(0))
button0.grid(row=5, column= 1)

counter = 0
operations= ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
for x in range(4):
     for y in range(3):
         if counter<len(operations):
            buttonOp = Button(root, text=operations[counter], width=2, height=2, command= lambda text=operations[counter]:get_operation(text))
            buttonOp.grid(row=x+2, column=y+3)
            counter+=1

buttonClearAll = Button(root, text='C', width=2, height=2, command= clearAll).grid(row=5, column=0)
buttonEqual = Button(root, text='=', width=2, height=2, command= calculate).grid(row=5, column=2)
buttonClear = Button(root, text='<-', width=2, height=2, command= lambda :clear()).grid(row=5, column=4)

root.mainloop()