#для заданной строки подсчитать количество вхождений в неё символа,
#считываемого с клавиатуры
s = 'Здесь могла быть Ваша реклама!'    #дана строка s
print(s)                                #вывод строки
a = input('Введите символ: ')           #ввод какого-нибудь символа a
n = 0                                   #нулевое значение кол-ва символа a
for i in s:                             #проверка каждого символа в строке 
    if i == a:                          #если символ в строке равен a 
        n += 1                          #подсчёт встречающего символа a 
    else:                               #если символ a не встречается
        pass                            #ничего не делать
if n >= 1:                              #если символ встречается печатать
    print('Символ %s встречается в строке %d раз' % (a, n))
else:                                   #если не встречается печатать
    print('Символ %s в строке не встречается' %a)