'''
Задача №2937. Следующее и предыдущее
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере. 
Пробелы, знаки препинания, заглавные и строчные буквы важны!

Ввод: 179
Вывод: The next number for the number 179 is 180.
       The previous number for the number 179 is 178.
'''
x=int(input())
text1="The next number for the number {} is {}."
text2="The previous number for the number {} is {}."
print(text1.format(x,x+1))
print(text2.format(x,x-1))