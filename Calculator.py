#Amanda Tebo
#October 26, 2021
#Lab 3
#Calculator Class

from tkinter import *
import math


class Calculator:
    def __init__(self, master):
        self.openParenCounter = 0
        self.closeParenCounter = 0
        self.master = master
        master.title("Calculator")
        self.equation = Entry(master, width = 36, borderwidth = 5)
        self.equation.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
        self.createButton()
        
    def createButton(self):
        #creation of the buttons to be used
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('c')
        b_equal = self.addButton('=')
        b_sin = self.addButton('sin')
        b_cos = self.addButton('cos')
        b_tan = self.addButton('tan')
        b_arcsin = self.addButton('arcsin')
        b_arccos = self.addButton('arccos')
        b_arctan = self.addButton('arctan')
        b_log = self.addButton('log')
        b_ln = self.addButton('ln')
        b_expon = self.addButton('^')
        b_sqrt = self.addButton('sqrt')
        b_posneg = self.addButton('+/-')
        b_decimal = self.addButton('.')
        b_openParenthesis = self.addButton('(')
        b_closeParenthesis = self.addButton(')')
        b_bcksp = self.addButton('bcksp')

        #layout of the buttons
        row1 = [b_bcksp, b_openParenthesis, b_closeParenthesis]
        row2 = [b_sin, b_cos, b_tan, b_clear]
        row3 = [b_arcsin, b_arccos, b_arctan, b_sqrt]
        row4 = [b_log, b_ln, b_expon, b_add]
        row5 = [b7, b8, b9, b_sub]
        row6 = [b4, b5, b6, b_mult]
        row7 = [b1, b2, b3, b_div]
        row8 = [b_posneg, b0, b_decimal, b_equal]

        #cycle through layout arrays and create the button grid
        r = 1
        for row in [row1, row2, row3, row4, row5, row6, row7, row8]:
            c = 0
            for buttn in row:
                buttn.grid(row=r, column = c, columnspan = 1)
                c+=1
            r+=1

    

    def addButton(self, value):
        return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))

    def clickButton(self, value):
        current_equation = str(self.equation.get())
        if value == 'c':
            self.equation.delete(0, END)
        
        elif value == '=':
            if self.closeParenCounter != self.openParenCounter:
                self.equation = "Invalid parenthesis"
                self.clickButton('c')
                self.closeParenCounter = 0
                self.openParenCounter = 0
                return
            answer = str(eval(current_equation))
            #answer = evaluate(answer)
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)
        
        elif value == '(':
            self.openParenCounter += 1
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation + value)

        elif value == ')':
            self.closeParenCounter += 1
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation + value)

        #elif value == 'bcksp':
        #    self.equation = self.equation[:-1]
        #    current_equation.set(self.equation)

        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation + value)

    #def shuntYard(self, equation):
    #def evaluate(self, equation):
        
if __name__ == '__main__':
    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()
