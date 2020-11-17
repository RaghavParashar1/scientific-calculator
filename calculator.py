from tkinter import*
import math
import parser
import tkinter.messagebox

calculator = Tk()
calculator.title("Scientific Calculator")
calculator.configure(background="powder blue")
calculator.resizable(width=False,height=False)
calculator.geometry("500x520+0+0")

calc = Frame(calculator)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result = False

    def numberenter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum= str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op=="add":
            self.total += self.current
        if self.op=="sub":
            self.total -= self.current
        if self.op=="multi":
            self.total *= self.current
        if self.op=="divide":
            self.total /= self.current
        if self.op=="mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)

    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def clear_entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def all_clear_entry(self):
        self.clear_entry()
        self.total=0

    def mathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)

    def sq(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result=False
        self.current=math.log(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def exp(self):
        self.result=False
        self.current=math.exp(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def expm1(self):
        self.result=False
        self.current=math.expm1(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def lgamma(self):
        self.result=False
        self.current=math.lgamma(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def degree(self):
        self.result=False
        self.current=math.lgamma(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log2(self):
        self.result=False
        self.current=math.log2(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log10(self):
        self.result=False
        self.current=math.log10(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def loglp(self):
        self.result=False
        self.current=math.loglp(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def acosh(self):
        self.result=False
        self.current=math.acosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def asinh(self):
        self.result=False
        self.current=math.asinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

added_value=Calc()

txtDisplay = Entry(calc, font=('arial',20,'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"]= lambda x = numberpad[i]: added_value.numberenter(x)
        i+=1

#======================================#======================================================#

btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.clear_entry).grid(row=1, column=0, pady=1)
btnAllClear = Button(calc, text=chr(67)+chr(69), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)
btnsq = Button(calc, text="√", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.sq).grid(row=1, column=2, pady=1)
btnadd = Button(calc, text="+", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)
btnsub = Button(calc, text="-", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
btnmul = Button(calc, text="×", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)
btndiv = Button(calc, text="÷", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)
btnzero = Button(calc, text="0", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.numberenter(0)).grid(row=5, column=0, pady=1)
btndot = Button(calc, text=".", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.numberenter(".")).grid(row=5, column=1, pady=1)
btnpm = Button(calc, text=chr(177), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= added_value.mathsPM).grid(row=5, column=2, pady=1)
btneq = Button(calc, text="=", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

#====================================Scientific================================================#

btnpi = Button(calc, text="π", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.pi).grid(row=1, column=4, pady=1)
btncos = Button(calc, text="cos", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.cos).grid(row=1, column=5, pady=1)
btntan = Button(calc, text="tan", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.tan).grid(row=1, column=6, pady=1)
btnsin = Button(calc, text="sin", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.sin).grid(row=1, column=7, pady=1)
btn2pi = Button(calc, text="2π", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.tau).grid(row=2, column=4, pady=1)
btncosh = Button(calc, text="cosh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.cosh).grid(row=2, column=5, pady=1)
btntanh = Button(calc, text="tanh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.tanh).grid(row=2, column=6, pady=1)
btnsinh = Button(calc, text="sinh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.sinh).grid(row=2, column=7, pady=1)
btnlog = Button(calc, text="log", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.log).grid(row=3, column=4, pady=1)
btnexp = Button(calc, text="Exp", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.exp).grid(row=3, column=5, pady=1)
btnmod = Button(calc, text="Mod", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)
btnE = Button(calc, text="e", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue",  command = added_value.e).grid(row=3, column=7, pady=1)
btnlog2 = Button(calc, text="log2", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.log2).grid(row=4, column=4, pady=1)
btndeg = Button(calc, text="deg", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.degree).grid(row=4, column=5, pady=1)
btnacosh = Button(calc, text="acosh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.acosh).grid(row=4, column=6, pady=1)
btnasinh = Button(calc, text="asinh", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.asinh).grid(row=4, column=7, pady=1)
btnlog10 = Button(calc, text="log10", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.log10).grid(row=5, column=4, pady=1)
btnCos = Button(calc, text="loglp", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.loglp).grid(row=5, column=5, pady=1)
btnexpm1 = Button(calc, text="expm1", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.expm1).grid(row=5, column=6, pady=1)
btnlgamma = Button(calc, text="lgamma", width=6, height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command = added_value.lgamma).grid(row=5, column=7, pady=1)

lbldisplay=Label(calc, text="Scientific Calculator", font=('arial',30,'bold'), justify=CENTER)
lbldisplay.grid(row=0, column=4, columnspan=4)

#==============================MENU and FUNCTION==============================================#

def iexit():
    iexit= tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iexit > 0:
        calculator.destroy()
        return

def scientific():
    calculator.resizable(width=False, height=False)
    calculator.geometry("1000x520+0+0")

def standard():
    calculator.resizable(width=False, height=False)
    calculator.geometry("500x520+0+0")

menubar = Menu(calc)

filemenu =  Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command = standard)
filemenu.add_command(label="Scientific", command = scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = iexit)

editmenu =  Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu =  Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")

calculator.config(menu=menubar)
calculator.mainloop()
