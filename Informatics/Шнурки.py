
'''
Задача №3466. Шнурки
ввод:  2
       1
       3
       4
вывод: 26
'''
sum_a=int(input())
sum_b=int(input())
sum_l=int(input())
N=int(input())
cnt1=2*sum_l
cnt2=N-1
cnt3=cnt2*(2*sum_a+2*sum_b)
ans=sum_a+cnt1+cnt3

print(ans)
