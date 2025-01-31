# ตัวอย่างเรียกใช้ fun1
result = fun1(1, 10)
print("ผลลัพธ์ของ fun1:", result)

# ตัวอย่างเรียกใช้ fun2
sum1 = 0
delsum = 0
result1 = fun2(5, sum1, delsum)  # เลขบวก
result2 = fun2(-3, sum1, delsum)  # เลขลบ
result3 = fun2(0, sum1, delsum)  # เลขเป็น 0

print("ผลลัพธ์ fun2 (บวก):", result1)
print("ผลลัพธ์ fun2 (ลบ):", result2)
print("ผลลัพธ์ fun2 (เลข 0):", result3)
