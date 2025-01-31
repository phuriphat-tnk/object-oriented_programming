import Function as f
fun = f.fun1(int(input("ใส่เลขที่ 1 ")),int(input("ใส่เลขที่ 2 ")))
print(*fun,sep="\n") # *แยกตัวlist sep= ใช้ตัวอะไรเป็นตัวคั่นระหว่างสมาชิกที่ถูกแสดงผล
print("------------------------------")
sum1 = 0
delsum = 0
while True:
    num = int(input("ใส่เลข : "))
    if num > 0:
        sum1 = f.fun2(num,sum1,delsum)
    elif num < 0:
        delsum = f.fun2(num,sum1,delsum)
    else:
        break
print(f"ผลลัทธ์ทั้งหมด ผลบวก {sum1} ผลลบ {delsum}")