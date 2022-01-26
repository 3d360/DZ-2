print(" ---------------------- №1 ---------------------")
#var i,n,dig(integer)
#DZ 2 - Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
n=i=1

while i <=5:
    print(str(i)," 0")
    i += 1

print(" ---------------------- №2 ---------------------")
print("Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5")
i=d=cifra=0
print('Введите данные...')
while i<10:
    i += 1
    print('№', i, ':')
    if int(input(cifra)) == 5:
        d += 1

print('Из ',i,' - цифр 5:', d,'шт.')
#Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
print(" ---------------------- №3 ---------------------")
sum = 0
for i in range(1,101):
    sum+=i
print('Сумма 1-100:',sum)

print(" ---------------------- №4 ---------------------")
#Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран
sum = i = 0
for i in range(1,10):
    if i==1:
        sum=1
    sum = sum * i
print('Произведение 1-10:',sum)
print(" ---------------------- №5 ---------------------")
#Вывести цифры числа на каждой строчке.

integer_number = 12345
print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

print(" ---------------------- №6 ---------------------")
#Найти сумму цифр числа.
sum=0
integer_number = i =52645
print('Найти сумму цифр числа(',integer_number,') : ',integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    sum = sum + integer_number % 10
    integer_number = integer_number//10

print('Сумма цифр числа',i,':',sum)

print(" ---------------------- №7 ---------------------")
#Найти произведение цифр числа.
sum=1
integer_number = i = 25376
print('Найти произведение цифр числа (',integer_number,') : ',integer_number%10,integer_number//10,sum)
#sum = sum * integer_number%10
while integer_number>0:
    n=integer_number%10
    print(n)
    #if integer_number % 10 == 0:
    #sum = sum * 1
    sum = sum * n
    integer_number = integer_number//10
print('Произведение цифр числа',i,':',sum)

print(" ---------------------- №8 ---------------------")
#Дать ответ на вопрос: есть ли среди цифр числа 5?
integer_number: int = 215513
i=0
print('В числе',integer_number,'найти цифры 5.')
while integer_number>0:
    n=integer_number%10
    if n == 5:
        i += 1
    integer_number = integer_number//10

if i>0: print('ДА - есть. Цифр 5 -',i,'шт.')
elif i==0: print('НЕТ. Цифр 5 - 0шт.')
print(" ---------------------- №9 ---------------------")
# Найти максимальную цифру в числе
integer_number: int
integer_number = sum = 8215613
i=0
print('В числе',integer_number,'найти максимальную цифру')
while integer_number>0:
    n=integer_number%10
    if n > i:
        i = n
    integer_number = integer_number//10

print('В числе',sum,'MAX число:',i)

print(" ---------------------- №10 ---------------------")
integer_number: int = 216613
i=0
print('В числе',integer_number,'найти цифры 5.')
while integer_number>0:
    n=integer_number%10
    if n == 5:
        i += 1
    integer_number = integer_number//10

if i>0: print('Цифр 5 -',i,'шт.')