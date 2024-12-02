first=int(input('A: '))
second=int(input('B: '))
third=int(input('C: '))
if first==second==third:
    print('3')
elif first==second or first==third or second==third:
    print('2')
else:
    print('0')

