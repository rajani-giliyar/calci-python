import math
import random

#define variable
calci_use_again="yes"



#logo design
def logo():
      print("="*50,"welcome to scientific calculation app","="*50)
      for i in range(8):
            for j in range(i+2):
                  print(" ",end="")
            for j in range(1,7-i):
                  print("!",end="")
            for j in range(5-i,0,-1):
                  print(random.randint(0,9),end="")
            for j in range(3-i,0,-1):
                  print("%",end="")
            print(" ")
logo()

def header(i):
      print("")
      option=("percentage","factorail","LCM(least common multiple)","HCF(highest common factor)","square_root","log","exp(x)","x^y","cos(x)+sin(y)")
      print("_"*60,"calculate:",option[i],60*"_")

#methods for calculator
def number():
      num=int(input("enter a number:"))
      return num

def percentage(num, value):
      percentage_output=float(num)*float(value/100)
      print(value,"of",num,"is = ",percentage_output)

def factorial(num):
      factorial=1
      if num<0:
            print("sorry,factorial doesn't exist for negetive number")
      elif num==0:
            print("factorial of 0 is 1")
      else:
            for i in range(1,num+1):
                  factorial=factorial+i
            print("factorial of" ,num, "is = ",factorial)

def LCM(num1,num2):
      if num1>num2:
            greater=num1
      else:
            greater=num2

      while True:
            if ((greater % num1==0) and (greater % num2==0)):
                 lcm_output=greater
                 break
            greater=greater+1
            print("LCM OF", num1 ,"and", num2 ,"is=",lcm_output)

def HCF(num1,num2):
      if num1<num2:
            smaller=num1
      else:
            smaller=num2
      i=1
      while(i<=smaller):
            if (num1 % i ==0 and num2 % i==0):
                  hcf_output=i
            i=i+1
      print("HCF of ",num1 ,"and", num2, "is=" ,hcf_output)

def square_root(num):
      sqrt_output=math.sqrt(num)
      print("sqrt of ",num,"is =",sqrt_output)

def log(num):
      log_output=math.log10(num)
      print("log of ",num ,"is =" ,log_ouput)

def exp(num):
      exp_output=math.exp(num)
      print("exp of ",num  ,"is =" ,exp_output)

def power(num, power_value):
      power_output=math.pow(num,power_value)
      print(num,"to the power of ", power_value ,"is =",power_output)

def cossin(num1,num2):
      cossin_output=math.cos(num1)+math.sin(num2)
      print("the cos({})+sin({})".format(num1,num2),"=", cossin_output)


#main program
#condition use for calculator use again
while calci_use_again in ("yes","YES","Y","y"):
      print ("calculator optiopns: percentage,factorial,LCM(least common multiple)"\
             "HCF(highest common factor),square root,log,exp(x),x^y,cos(x)+sin(Y)")

      calculate=input("select calculator option:")


      count_more_numbers="yes"
      while count_more_numbers in ("yes","YES","Y","y"):

            if calculate=="percentage":
                  header(0)
                  num=number()
                  value=int(input("enter % value: "))
                  percentage(num,value)
                  count_more_numbers=input("do you want to calculate more: ")


            elif calculate=="factorial":
                  header(1)
                  num=number()
                  factorial(num)
                  count_more_numbers=input(" you want to calculate more: ")

            elif calculate=="lcm":
                  header(2)
                  num1=number()
                  num2=int(input("enter another number: "))
                  LCM(num1,num2)
                  count_more_numbers = input(" you want to calculate more: ")

            elif calculate=="hcf":
                  header(3)
                  num1=number()
                  num2=int(input("enter another number: "))
                  HCF(num1,num2)
                  count_more_numbers = input(" you want to calculate more: ")

            elif calculate=="square root":
                  header(4)
                  num=number()
                  square_root(num)
                  count_more_numbers= input(" you want to calculate more: ")

            elif calculate=="log":
                  header(5)
                  num=number()
                  log(num)
                  count_more_numbers= input(" you want to calculate more: ")

            elif calculate=="exp(x)":
                  header(6)
                  num=number()
                  exp(num)
                  count_more_numbers= input(" you want to calculate more: ")

            elif calculate=="x^y":
                  header(7)
                  num=number()
                  power(num,power_value)
                  count_more_numbers= input(" you want to calculate more: ")

            elif calculate=="cos(x)+sin(y)":
                  header(8)
                  num1=number()
                  num2=int(input("enter a number: "))
                  cossin(num1,num2)
                  count_more_numbers= input(" you want to calculate more: ")

            else:
                  print("sorry, entered option is not available in calculator")
                  count_more_numbers="n"

            print("*"*45)
            print("")
            print("")
      calci_use_again=input("do you want to use calculator for other option?: ")