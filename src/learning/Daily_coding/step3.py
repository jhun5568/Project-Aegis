# 10000원에 대한 부가세 10%
def get_vat():
    price = 10000
    vat_rate = 0.1
    print(price*vat_rate)
get_vat()

# 입력한 금액에 대한 부가세 10%
def get_vat(price):
    vat_rate = 0.1
    print(price*vat_rate)
get_vat(10000)
get_vat(20000)

# 입력한 금액과 부가세 요율을 함께 입력
def get_vat(price, vat_rate):
    print(price*vat_rate)
get_vat(10000,0.2)
get_vat(20000,0.3)
print('___')

# 요율을 입력하지 않으면 10%로 계산 
def get_vat(price, vat_rate=0.1):
    print(price*vat_rate)
get_vat(10000)
get_vat(20000,0.3)

# 함
def get_vat(price,vat_rate=0.1):
    return price*vat_rate
print(get_vat(10000))
#email.send('Aegis_BIMer@gmail.com',get_vat(20000*0.2))