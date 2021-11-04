#Amanda Tebo
#October 26, 2021
#Lab 3
#Calculator Class
from collections import deque
from tkinter import *
import math
import re

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.equation = Entry(master, width = 36, borderwidth = 5)
        self.equation.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
        self.createButton()
        self.operatorPriority = {
            '^': 1,
            '*': 2,
            '/': 3,
            '+': 4,
            '-': 5,

        }
        
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

    
    #function to create the button
    def addButton(self, value):
        return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))

    #allows for feedback from buttons being pressed
    def clickButton(self, value):
        current_equation = str(self.equation.get())

        #if the user presses c, clear the current input
        if value == 'c':
            self.equation.delete(0, END)
        
        #if the user presses =, evaluate the current equation
        elif value == '=':
            #This if statement makes sure that the parenthesis are equal, if they aren't, prompts the user
            if self.closeParenCounter != self.openParenCounter:
                self.equation = "Invalid parenthesis"
                self.clickButton('c')
                self.closeParenCounter = 0
                self.openParenCounter = 0
                return
            self.shuntYard(current_equation)
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

    def shuntYard(self, equation):
        #split the inputted equation into tokens
        equationTokens = re.split(r'\b', equation)
        #create two lists: one for the postFix notation, one for storing operators
        operators = []
        postFix = []
        #start organizing the tokens
        for i in equationTokens:
            if i.isdigit():
                postFix.append(i)
            elif i == '':
                #print(i)
                continue
            elif i == '(':
                operators.append(i)
            elif i == ')':
                while operators[len(operators)-1] != '(':
                    postFix.append(operators[len(operators)-1])
                    operators.pop()
            else:
                print(i)
                if len(operators) != 0:
                    while len(operators) != 0 & self.hasHigherPrec(operators[len(operators)-1], i):
                        postFix.append(operators[len(operators)-1])
                        operators.pop()
                    operators.append(i)
        while len(operators) != 0:
            if operators[len(operators)-1] != '(':
                postFix.append(operators[len(operators)-1])
                print(operators(len(operators)-1))
                operators.pop()
            else:
                operators.pop()
        print(postFix)
        return postFix
                
    #def validEquation(self, equation):

    def hasHigherPrec(self, topOfStack, nextOperator):
        return min(topOfStack, nextOperator)

    #def evaluate(self, equation):
    #    operands = []
    #    answer = 0
    #    for i in equation:
    #        if equation[i].isdigit():
    #            operands.append(equation[i])
    #        else:
    #            if equation[i] == '+':
    #                answer += (operands[operands.len()-1] + operands[operands.len()-2])
    #            elif equation[i] == '-':
    #                answer += (operands[operands.len()-1] - operands[operands.len()-2])
    #            elif equation[i] == '*':
    #                answer += (operands[operands.len()-1] * operands[operands.len()-2])
    #            elif equation[i] == '/':
    #                answer += (operands[operands.len()-1] / operands[operands.len()-2])
    #            elif equation[i] == '^':
    #                answer += (operands[operands.len()-1] ** operands[operands.len()-2])
    #            #sin
    #            elif equation[i] == 'sin':
    #            #cos
    #            elif equation[i] == 'cos':
    #            #tan
    #            elif equation[i] == 'tan':
    #            #arcsin
    #            elif equation[i] == 'arcsin':
    #            #arccos
    #            elif equation[i] == 'arccos':
    #            #arctan
    #            elif equation[i] == 'arctan':
    #            #log
    #            elif equation[i] == 'log':
    #            #ln
    #            elif equation[i] == 'ln':
    #            elif equation[i] == 'sqrt':
    #                answer += (math.sqrt(operands[operands.len()-1]))

    #def evaluate(self, equation):


if __name__ == '__main__':
    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()
