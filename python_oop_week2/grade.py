a = int(input("กรุณากรอกคะแนน : "))
if a < 0 or a > 100 :
    print("กรุณากรอกคะแนนใหม่อีกครั้ง")
elif a < 50:
    print("คุณได้เกรด 0\n")
    print("ต้องการสอบแก้หรือไม่ ถ้าต้องการพิมพ์ 1 ไม่ต้องการพิมพ์ 2")
    c = int(input("เลือก : "))
    if c == 1:
        print("คุณขาดคะแนนอีก ", 50-a ,"คะแนน ถึงคุณจะได้เกรด 1")
    elif c == 2 :
        print("คุณสอบตก")
    else :
        print("กรุณาเลือก 1 หรือ 2")

elif a < 60:
    print("คุณได้เกรด 1")
elif a < 70:
    print("คุณได้เกรด 2")
elif a < 80:
    print("คุณได้เกรด 3")
else :
    print("คุณได้เกรด 4")
    