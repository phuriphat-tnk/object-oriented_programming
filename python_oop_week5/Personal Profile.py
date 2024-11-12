a = ()
num = int(input('ใส่จำนวนคนที่จะป้อน : '))
for i in range(num):
    me = {}
    print("กรุณากรอกข้อมูลคนที่ ",(i+1))
    a = input("กรุณากรอกชื่อ : ")
    me["name"] = a
    a = input("กรุณากรอกชื่อเล่น : ")
    me["nickname"] = a
    a = int(input("กรุณากรอกรหัสประจำตัวนักศึกษา : "))
    me["stdid"] = a
    a = input("กรุณากรอกงานอดิเรก : ")
    me["hobby"] = a
    a = input("กรุณากรอกสีที่ชอบ : ")
    me["color"] = a
    print("ข้อมูลคนที่ ",(i+1))
    print(me)