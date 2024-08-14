import tkinter as tk
from tkinter import ttk
    
window = tk.Tk()
window.title("programming homework")
window.geometry('1400x700')

label = ttk.Label(master = window, text = 'programming homeworj',font=('Arial',20,'bold'),foreground='brown')
label.pack()
frame = ttk.Frame(window,width=200,height=200)
frame.pack(padx=10,pady=10)
text = tk.Text(frame,highlightthickness=0)
text.grid(row=0,column=0,sticky='nsew')
text_scrollbar = ttk.Scrollbar(frame,command=text.yview)
text_scrollbar.grid(row=0,column=1,sticky="ns")
text.configure(yscrollcommand=text_scrollbar.set)
#button = ttk.Button(master =  window,text = "fibnocci")
#button.pack()
def inserttext():
    text.delete('1.0','end')
    text.insert("1.0","""def A(num):
    x = abs(num)
    print(x)
A(-7)"""
"""def digit():
    s = [2,4,6,8]
    a = all(x % 2 == 0 for x in s)
    print(a)
digit()"""
"""name = "abuzAr"
y = any(x. isupper() for x in name)
print(y)"""
"""y = "This ً is a symbol \u00A9 "
x = ascii(y)
print(x)"""
"""def intger(num):
    z = bin(num)
    print(z)
intger(7)"""
"""def max_num(x,y):
    return bool(x > y)
print(max_num(4,5))"""
"""int_list = 'abuًzar'
array4  = bytearray(int_list,'utf8','replace')
print(array4)"""
"""def my_function():
    print("hello,world")
class MyClass:
    def __call__(self):
        print("this is MyClass")
obj = MyClass()
print(callable(my_function))
print(callable(obj))
print(callable("my goal"))"""
"""def func(x):
    return chr(x)
print(func(8364))"""
"""class Calculator:
    x = 10
    y = 5
    @classmethod
    def adding(cls):
        print(f"classmethod is used {cls.x * cls.y}")
Calculator.adding()"""
"""source_code = "8 * 9 + 23"
compiled_source_code = compile(source_code,"<string>","eval")
result = eval(compiled_source_code)
print(result)"""
"""def number(x,y):
    return complex(x,y)
print(number(9,4))"""
"""class computer:
    def __init__(self,Ram,Generation,Storage):
        self.Ram = Ram
        self.Generation = Generation
        self.Storage = Storage
i = computer("4GB",10,500)
print(i.Ram)
print(i.Generation)
print(i.Storage)

delattr(i,"Ram")

print("\n After deletion")
#print(i.Ram)
print(i.Generation)
print(i.Storage)"""
"""def first_dic(**a):
    return dict(a)
print(first_dic(name = "abuzar",age = 20,Lname = "ahmadi",))"""
"""num1 = int(input("number1:"))
num2 = int(input("number2:"))
result = divmod(num1,num2)
print(result)"""
"""lst = ["Abuzar","Ali","Mohammad"]
for index , name in enumerate(lst,1):
    print(index,name)"""
"""x = eval("'divisible' if y % 5 == 0 else 'indivisible'" , {'y':55}) 
print(x)"""
'''func ="""
def Adding(x=2,y=3):
    return x + y
"""
exec(func)
print(Adding())'''
    
"""numbers=[2,4,5,64,3,8,9,90,43,12,5,63]
x = filter(lambda x:x % 2 == 0,numbers)
print(list(x))"""
"""def change(x):
    return float(x)
print(change("979899"))"""
"""x = 7
y = "Abuzar"
def my_example():
    z = 8.7
    def my_example2():
        print("it is an example of global() function")
        w = 23
    my_example2()
    print(globals())
my_example()"""
"""class computer:
    def __init__(self,Ram,Generation,Storage):
        self.Ram = Ram
        self.Generation = Generation
        self.Storage = Storage
i = computer("4GB",10,500)
print(hasattr(i,"Ram"))
print(hasattr(i,"Generation"))
print(hasattr(i,"Storage"))
# it returns false
print(hasattr(i,"price"))"""
"""print(hash("Hellow"))"""
"""help(print)"""
"""def num(x):
    return hex(x)
i = int(input("number:"))
print(num(i))"""
"""dic1 = {"name" :"ali","age" :12}
dic2 = {"name":"ali","age":12}
print(dic1==dic2)
print(id(dic1)==id(dic2))"""
"""def converter(x):
    return int(x) + 2
print(converter("49"))# argument can also be decimal"""
"""class Person:
    def __init__(self,name,age,proffession):
        self.name = name
        self.age = age
        self.proffession = proffession

P1 = Person("LeaderAbuzar",40,"compter sciencist")
print(isinstance(P1,Person))"""
"""class Person:
    def person_info(self,name,age):
        self.name = name
        self.age = age
        print(f"my name is {name},I am {age} years old")
        
class Student(Person):
    def student_info(self,field):
        self.field = field
        
        print(f"I study { field } at Kabul university")

x = Student()
x.person_info('abuzar',34)
x.student_info("medicine")
print(issubclass(Student,Person))"""
"""x = iter(['Abuzar',20,'computer science','wristling'])
print("name:",next(x))
print("age:",next(x))
print("field:",next(x))
print("favorite_sport:",next(x))"""
"""names = []
while True:
    name = input("name:")
    if name == '':break
    names.append(name)
x =len(names)
print(x)"""
"""b = "global_var"
a = 20
def func():
    x = 10
    y = "hellow"
    return locals()
print(func())"""
"""num1 = input("number1:")
num2= input("number2:")
x = max(num1,num2)
aprint(x) """
"""x = b'abuzar'
y = memoryview(x)
print(y[3])
print(y.tolist())"""
"""def minimum(num1,num2):
       return min(num1,num2)
num1 = int(input("number:"))
num2 = int(input("number:"))
y = minimum(num1,num2)
print(y)"""
"""m = ('apple','banana','cherry')
x = iter(m)
print(next(x))
print(next(x))
print(next(x))"""
"""z = object()
print(type(z))
print(dir(z))"""
"""def octal(n):
    return oct(n)
i = int(input("number:"))
x = octal(i)
print(x)"""
"""f = open("democlass.txt","w")
f.write('bhkjhk')"""
"""wrong property() function"""
"""for i in range(1,100):
    if i % 3 == 0:
        print("buzz")
    elif i % 5 == 0:
        print("face")
    elif i % 15 == 0:
        print("facebuzz")
    else:
        print(i)"""
"""class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def __repr__(self):
        return "name: {},ID: {}".format(self.name,self.ID)
s = Student('Ali',102123)
print(s)"""
"""i = "abuzar"
j = reversed(i)
for l in j:
    print(l)"""
"""def round_num(n):
    return round(n)
i = float(input("number:"))
x = round_num(i)
print(x)"""
"""fruits = set()
while True:
    i = input("Enter a fruit:")
    if i == '': break
    fruits.add(i)
print(fruits)"""
"""i = ['melon', 'orange', 'cherry', 'watermelon', 'apple', 'banana','pair','cucumber']
x = slice(0,8,3)
print(i[x])"""
"""string = []
while True:
    i = input("Enter a string:")
    if i == '': break
    string.append(i)
    x = sorted(string)
print(x)"""
"""class student:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    @staticmethod
    def check(num1,num2):
        if num1 + num2 / 2 >= 55:
            return "passed"
        else:
            return "failed"
c = student.check(40,50)
print(c)"""
        
"""i = int(input("Enter a number:"))
x = "Car" + str(i)
print(x)"""
"""def adding(*i):
    return sum(i)
s=adding(2,3,4,5,6,7,8)
print(s)"""
"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
        print(f"my name is {name}, I am {age} years old.")
s = Student("Abuzar",20,"100000$")"""
"""def number(*num):
    return tuple(num)
x = number(32,43,5,6,7,7,88,90,)
print(x)"""
"""class Person:
    def __init__(self,name = 'Abuzar',age = 20,job = 'programmer'):
        self.name = name
        self.age = age
        self.job = job
P1 = Person()
x = vars(P1)
print(x)"""
"""lst = ['name','age','job']
tpl = ('Abuzar', 20 , 'programmer')
zipped = zip(lst,tpl)
for i in zipped:
    print(i)

""")
def inserttext1():
    text.delete('1.0','end')
    text.insert("1.0","""def fib(n):
    if n == 0  or n == 1:
        return n
    return fib(n-1) + fib(n-2)
i = int(input("number:"))
print(fib(i))""" )
def inserttext2():
    text.delete('1.0','end')
    text.insert("1.0","""def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)
i = int(input('number:'))
print(factorial(i))
""" )

    
    
menu = tk.Menu(window)
file_menu = tk.Menu(menu,tearoff=False)
file_menu.add_command(label='built in function',command=inserttext)
file_menu.add_separator()
file_menu.add_command(label='fibnocci sequence',command=inserttext1)
file_menu.add_separator()
file_menu.add_command(label='factorial',command=inserttext2)
menu.add_cascade(label='Menu',menu=file_menu)
window.configure(menu=menu)
window.config(bg="red")

window.mainloop()
