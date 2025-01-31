try:
    Purchase = int(input('โปรดใส่ยอดซื้อของ : '))
    discount1 = Purchase*(100-20)//100
    discount2 = Purchase*(100-10)//100
    if Purchase >= 5000:
        print(f'จะได้รับส่วนลด 20% {discount1} จากราคาเดิม {Purchase}')
    elif Purchase >= 2000:
        print(f'จะได้รับส่วนลด 10% {discount2} จากราคาเดิม {Purchase}')
    elif Purchase == 0:
        raise(ZeroDivisionError)
    elif Purchase < 0:
        raise(Exception)
    else :
        print(f'ไม่ได้ส่วนลด {Purchase}')
except ValueError:
    print('ใส่เฉพาะตัวเลข')
except ZeroDivisionError:
    print('ห้ามใส่ 0')
except:
    print('ห้ามป้อนค่าติดลบ')
