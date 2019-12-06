import tkinter
from tkinter.ttk import Style
from math import *

## first thing that should always be done when working with Tkinter
root = tkinter.Tk()
root.title("Calculator")

#Defining padding setup of rows and columns
root.rowconfigure(0, pad=1)
root.rowconfigure(1, pad=1)
root.rowconfigure(2, pad=1)
root.rowconfigure(3, pad=1)
root.rowconfigure(4, pad=1)
root.rowconfigure(5, pad=1)
root.rowconfigure(6, pad=1)

root.columnconfigure(0, pad=2)
root.columnconfigure(1, pad=2)
root.columnconfigure(2, pad=2)
root.columnconfigure(3, pad=2)
root.columnconfigure(4, pad=2)

# tkinter.ttk.Style().configure('TButton', padding=(0, 0, 0, 0))


#global variable setup
fNum = None
math = None

e = tkinter.Entry(root, width=40, borderwidth=6)
e.grid(row=0, column=0, columnspan=6, padx = 25, pady = 15)

def buttonClick(value):
    # e.delete(0, END) only works for one number
    current = e.get()
    e.delete(0, tkinter.END)
    print(current)
    e.insert(0, str(current) + str(value))

def buttonDecimal():
    current = e.get()
    
    butt = current.count('.')
    print(butt)
    if (butt >= 1):
        pass
    else:
       e.insert(tkinter.END, '.')

def buttonClear():
    fNum = None
    math = None
    e.delete(0, tkinter.END)

def buttonCancel():
    e.delete(0, tkinter.END)

def buttonBackspace():
    current = e.get()
    print(current)
    e.delete(0, None)

def buttonAddition():
    firstNumber = e.get()
    global fNum
    global math
    math = "addition"
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)

def buttonSubtraction():
    firstNumber = e.get()
    global fNum
    global math
    math = "subtraction"
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)

def buttonMultiplication():
    firstNumber = e.get()
    global fNum
    global math 
    math = "multiplication"
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)

def buttonDivision():
    firstNumber = e.get()
    global fNum
    global math
    math = "division"
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)

def buttonMinus():
    firstNumber = e.get()
    global fNum
    global math
    math = "subtraction"
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)

def buttonPercentage():
    number = e.get()
    if number == '':
        return ''
    e.delete(0,tkinter.END)
    e.insert(0, float(number) / 100)

def buttonNegate():
    negative = '-'
    number = e.get()
    print(number)
    try:
        if float(number) > 0:
            e.insert(0, negative)
            number = e.get()
        elif float(number) == 0:
            pass
        elif number == '':
            return ''
        else:
            e.delete(0)
    except:
        e.insert(0, '')
    
def buttonSine():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    e.insert(0, sin(fNum * pi / 180))


def buttonCosine():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    e.insert(0, cos(fNum * pi / 180))


def buttonTangent():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    e.insert(0, tan(fNum * pi / 180))

def buttonExponential():
    firstNumber = e.get()
    global fNum
    global math
    math = "exp"
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)

def buttonSqrt():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    try:
        e.insert(0, sqrt(fNum))
    except ValueError:
        e.insert(0, 'invalid input')

def buttonSq():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    e.insert(0, pow(fNum, 2))

def buttonLogBase10():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    try:
        e.insert(0, log10(fNum))    
    except ValueError:
        e.insert(0, 'invalid input')
    

def buttonNaturalLog():
    firstNumber = e.get()
    global fNum
    fNum = float(firstNumber)
    print(fNum)
    e.delete(0, tkinter.END)
    try:
        e.insert(0, log(fNum))
    except ValueError:
        e.insert(0, 'invalid input')

def buttonEqual():
    secondNumber = e.get()
    print(secondNumber)
    e.delete(0, tkinter.END)
    if math == "addition":
        e.insert(0, float(fNum) + float(secondNumber))
    if math == "subtraction":
        e.insert(0, float(fNum) - float(secondNumber))
    if math == "multiplication":
        e.insert(0, float(fNum) * float(secondNumber))
    if math == "division":
        try:
            e.insert(0, float(fNum) / float(secondNumber))
        except ZeroDivisionError:
            e.insert(0, 'invalid input')
        

    if math == "exp":
        e.insert(0, float(fNum) ** float(secondNumber))

#Define Buttons
##don't use the parentheses as it will run immediately

buttonDecimal = tkinter.Button(root, text=".", padx=70, pady=20, bg = "white smoke", command = buttonDecimal)
button0 = tkinter.Button(root, text="0", padx=150, pady=20,bg = "white smoke", command=lambda: buttonClick(0))
button1 = tkinter.Button(root, text="1", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(1)) 
button2 = tkinter.Button(root, text="2", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(2)) 
button3 = tkinter.Button(root, text="3", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(3)) 
button4 =tkinter.Button(root, text="4", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(4)) 
button5 = tkinter.Button(root, text="5", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(5)) 
button6 = tkinter.Button(root, text="6", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(6)) 
button7 = tkinter.Button(root, text="7", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(7)) 
button8 = tkinter.Button(root, text="8", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(8)) 
button9 = tkinter.Button(root, text="9", padx=70, pady=20,bg = "white smoke", command=lambda: buttonClick(9))

buttonAdd = tkinter.Button(root, text="+", padx=70, pady=20, bg="PeachPuff2", command=buttonAddition)
buttonMinus = tkinter.Button(root, text="-", padx=70, pady=20, bg="PeachPuff2", command=buttonSubtraction)
buttonMultiply = tkinter.Button(root, text="x", padx=70, pady=20, bg="PeachPuff2", command=buttonMultiplication)
buttonDivide = tkinter.Button(root, text="÷", padx=70, pady=20, bg="PeachPuff2", command=buttonDivision)
buttonEqual = tkinter.Button(root, text="=", padx=70, pady=20, bg="PeachPuff2", command=buttonEqual)

buttonClear = tkinter.Button(root, text="C", padx=70, pady=20, bg="gray54", command=buttonClear)
buttonNegate = tkinter.Button(root, text="±", padx=70, pady=20, bg="gray54", command=buttonNegate)
buttonPercent = tkinter.Button(root, text="%", padx=70, pady=20, bg="gray54", command=buttonPercentage)
buttonBackspace = tkinter.Button(root, text="->", padx=70, pady=20, bg="gray54", command=buttonBackspace)
buttonCancel = tkinter.Button(root, text="CE", padx=70, pady=20, bg="gray54", command=buttonCancel)

buttonSin = tkinter.Button(root, text="sin", padx =70, pady=20, bg="PeachPuff2", command=buttonSine)
buttonCos = tkinter.Button(root, text="cos",padx =70, pady=20, bg="PeachPuff2", command=buttonCosine)
buttonTan = tkinter.Button(root, text="tan",padx =70, pady=20, bg="PeachPuff2", command=buttonTangent)

buttonLogBase10 = tkinter.Button(root, text="log", padx=70, pady=20, bg="PeachPuff2", command=buttonLogBase10)
buttonNaturalLog = tkinter.Button(root, text="ln", padx=70, pady=20, bg="PeachPuff2", command=buttonNaturalLog)

buttonSqrt = tkinter.Button(root, text="sqrt", padx=70, pady=20, bg="PeachPuff2", command=buttonSqrt)
buttonSq = tkinter.Button(root, text="sq", padx=70, pady=20, bg ="PeachPuff2", command=buttonSq)
buttonExponential = tkinter.Button(root, text="exp", padx=70, pady=20, bg="PeachPuff2", command=buttonExponential)



#Put the buttons on the screen
buttonNegate.grid(row=1, column=0)
buttonClear.grid(row=1, column=1)
buttonCancel.grid(row=1, column=2)
buttonPercent.grid(row=1, column=3)
buttonBackspace.grid(row=1, column=4)

buttonNaturalLog.grid(row=2, column=0)
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
button9.grid(row=2, column=3)
buttonDivide.grid(row=2, column=4)

buttonLogBase10.grid(row=3, column=0)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
buttonMultiply.grid(row=3, column=4)

buttonSqrt.grid(row=4, column=0)
button1.grid(row=4, column=1)
button2.grid(row=4, column=2)
button3.grid(row=4, column=3)
buttonMinus.grid(row=4, column=4)


buttonSq.grid(row=5, column = 0)
button0.grid(row=5, column= 1, columnspan=2)
buttonDecimal.grid(row=5, column=3)
buttonAdd.grid(row=5, column=4)

buttonExponential.grid(row=6, column=0)
buttonSin.grid(row=6, column=1)
buttonCos.grid(row=6, column=2)
buttonTan.grid(row=6, column=3)
buttonEqual.grid(row=6,column=4)

root.mainloop()