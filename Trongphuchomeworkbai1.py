

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    else:
        return a / b


print("Cộng: ", cong(5, 3))
print("Trừ: ", tru(5, 3))
print("Nhân: ", nhan(5, 3))
print("Chia: ", chia(5, 3))
