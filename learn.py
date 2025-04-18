from math import *
print(' maii')
print(" manar ")
x='manar' 
print("welcome "+x)
# to do commect ctrl+ظ
print("\" manar\" ")
print(" 'mnar' ")
name=' manora' 
#if you need print one char 
print(name[0])# print space 
print(name[1])# print m 
print(name[6])# print a
print(name[-1 ])# print a last char or first char from last
print(name[-2])# print r
print(name[0:4])# print  man
print(name[4:7])# print  ora
# string method 
y='manora' 
print(y.format())
print(y.capitalize())
print(y.upper())
print(y.lower())
#to convert from string to list use split
pro_lang='html dart python php css js '
print(pro_lang.split()) # ['html', 'dart', 'python', 'php', 'css', 'js'] 
print(pro_lang.split("h",3))# ['', 'tml dart pyt', 'on p', 'p css js ']
pro_lang2='html_dart_python_php_css_js '
print(pro_lang2.split("_"))    #['html', 'dart', 'python', 'php', 'css', 'js ']
print(pro_lang2.split("_", 4))  #['html', 'dart', 'python', 'php', 'css_js ']
##############rsplit from last 
print(pro_lang2.rsplit("_", 4))  #['html_dart', 'python', 'php', 'css', 'js ']
print(pro_lang2.index("css")) #21
print(pro_lang.index('html'))  # 0
print(len(pro_lang))  #28
print(len('manar ali'))  #9
#### replace
x='manar'
print(x.replace('m',"o"))  #oanar

################################### number
print(str(5*5)+" "+"years")
print(str(10)+" "+"years")
print(float(10))
print(str('hgf'))
print(complex(10)) #(10+0j)
print(round(7.9)) #if .5 to .9 ll a3la  8
print(round(7.4))  # 7
print(floor(7.9)) ## 7
print(ceil(7.9)) ## 8
print(pow(3,3)) ##  3 power 3  27
print(pow(4,3)) ##  4 power 3  64
print(abs(-3)) ##  القيمه المطلقه3 
print(min(8,3)) ##   8
print(max(8,3)) ##  3  
##################################### input 

name=input ("please enter your name :")
print("you won " +name)

num1=input ("please enter num1 :")
num2=input ("please enter num2 :")
res=int(num1)+int(num2)
print(res)
res2=float(num1)+float(num2)
print(res2)

################# list 
lista =[1,"manar",True,False,"ALI",[1,2,3,4]] 
print(lista[0]) #1
print(lista[5]) # [1, 2, 3, 4]
print(lista[5][0]) # 1
# if replace value to other value
lista[0]='mhmd'
print(lista) # ['mhmd', 'manar', True, False, 'ALI', [1, 2, 3, 4]]

## append for add value  in list
lista.append( 'mai')  
print(lista)  ## ['mhmd', 'manar', True, False, 'ALI', [1, 2, 3, 4], 'mai']

lista.insert(0,"ayman")
print(lista) ##['ayman', 'mhmd', 'manar', True, False, 'ALI', [1, 2, 3, 4], 'mai'] 

##### add list to list  extend
x=[1,2,3,4,5]
y=[6,7,8,9,10]
x.extend(y)
print(x) ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

######## sort 
z=[5,3,1,9,5]
z.sort()
print(z) ## [1, 3, 5, 5, 9]
z.remove(1)
print(z) #[3, 5, 5, 9]
z.clear()
print(z) #[]

########  tuples 
 # cant edit tuple unlike list  
tuple=(1,2,5)  
print(tuple)

##############dictionary
info={
    'name':'manar',
    'countary' :'egypt',
     'age' :22
    }
print(info["name"]   ) ## manar
###########  set 
mySet= {'Ali','manar ','alex'}
print(mySet) #### not sort 
#### set method

 ######################################## Funcation
def printInfo(name,age):  
    print('my name is '+name +' and my age is '+ age)
printInfo('manar',"22") ##### my name is manar and my age is 22

def clec(num1,num2):
    print(num1+num2)
clec(2,6)   # 8

def clec(num1,num2):
    return num1+num2 
print(clec(2,6)   ) #8
 
######################### calc age 
def calcAge(age):
    return "your age with hours " + str(age*365*24) +" hrs" 
print(calcAge(22 )   )  ##### your age with hours 192720 hrs 
 #### function input from user  
def inputAge(age):
    return "your age with hours " + str(age*365*24) +" hrs" 
print(inputAge(int(input('enter your age '))))  # da b implment first before  return el foa2 
 
#################################  if 
 
grade = 80
if grade >= 90:
    print('A+')
elif grade >= 80:
    print('B+')  
elif grade >= 70:
    print('B ')  
elif grade >= 60:
    print('c+')     
elif grade >= 50:
    print('c')  
else :
    print('f')           

####################### calculator

n1=float(input('ENTER number1'))
opertor= input('ENTER opertor') 
n2=float(input('ENTER number2'))
if opertor== '+':
    print(n1+n2)
elif opertor== '*':
    print(n1*n2)    
elif opertor== '/':
    print(n1/n2) 
elif opertor== '-':
    print(n1-n2)     
elif opertor== '%':
    print(n1%n2)     
  
############################################  loops    
i=1
while i<=10:
    print(i)
    i += 1







 

