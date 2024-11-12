number = []
num = int(input('ใส่จำนวนตัวเลขที่จะหาค่าเฉลี่ย : '))
for i in range(num):
    Numm = int(input("ใส่จำนวน : "))
    number.append(Numm)
    a = sum(number) // len(number)
print('ค่าเแลี่ยที่ได้คือ : ',(a))