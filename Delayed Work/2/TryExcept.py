pricelist = 0
while True:
    try:
        Purchase = (input('รับราคาสินค้า : '))
        if Purchase == 'exit':
            print(f"ยอดขายรวมทั้งหมด = {pricelist}")
            break
        Purchase = int(Purchase)
        if Purchase == 0:
            raise(ZeroDivisionError)
        elif Purchase < 0:
            raise(Exception)
        else:
            pricelist += Purchase
            print(pricelist)
    except ValueError:
        print('กรุณาใส่ตัวเลขเท่านั้น')
    except ZeroDivisionError:
        print('ราคาสินค้าต้องมากกว่า 0')
    except:
        print('ราคาสินค้าต้องไม่ติดลบ')