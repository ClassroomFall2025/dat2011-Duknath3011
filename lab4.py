def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500,8800,12000,24000)
    if so_nuoc < 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc-10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] +(so_nuoc -20) *gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] +(so_nuoc-30) *gia_ban_nuoc[3]
    return tien_nuoc

# tinh tien nguyen lieu 
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"duong:":0.04, "dau:":0.07}
    banh_thap_cam = {"duong:":0.06, "dau:":0}
    banh_deo = {"duong:":0.05, "dau:":0.02}
    nguyen_lieu ={}
    duong_hop_banh = sl_bdx * banh_dau_xanh["duong:"] + sl_btc * banh_thap_cam["duong:"] + sl_bd * banh_deo["duong:"]
    dau_hop_banh = sl_bdx * banh_dau_xanh["dau:"] + sl_btc * banh_thap_cam["dau:"] + sl_bd * banh_deo["dau:"]
    nguyen_lieu = {"sugar": duong_hop_banh, "bean": dau_hop_banh}
    return nguyen_lieu

# may tinh bo tui 

import math
import datetime

# Lưu lịch sử tính toán
history = []

def phep_tinh_co_ban():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    op = input("Chọn phép tính (+, -, *, /): ")
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            result = "Lỗi: chia cho 0"
        else:
            result = a / b
    else:
        result = "Phép tính không hợp lệ"
    history.append(f"{a} {op} {b} = {result}")
    print("Kết quả:", result)

def luy_thua():
    x = float(input("Nhập x: "))
    y = float(input("Nhập y: "))
    result = x ** y
    history.append(f"{x}^{y} = {result}")
    print("Kết quả:", result)

def can_bac_hai():
    x = float(input("Nhập số: "))
    if x < 0:
        result = "Lỗi: Không thể căn bậc 2 số âm"
    else:
        result = math.sqrt(x)
    history.append(f"√{x} = {result}")
    print("Kết quả:", result)

def ham_luong_giac():
    x = float(input("Nhập góc (độ): "))
    rad = math.radians(x)
    result = f"sin({x})={math.sin(rad)}, cos({x})={math.cos(rad)}, tan({x})={math.tan(rad)}"
    history.append(result)
    print("Kết quả:", result)

def logarit():
    x = float(input("Nhập số: "))
    choice = input("Chọn log (log10, ln, loga): ")
    if choice == "log10":
        result = math.log10(x)
    elif choice == "ln":
        result = math.log(x)
    elif choice == "loga":
        a = float(input("Nhập cơ số a: "))
        result = math.log(x, a)
    else:
        result = "Lựa chọn không hợp lệ"
    history.append(f"log: {result}")
    print("Kết quả:", result)

def giai_pt_bac_1():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if a == 0:
        if b == 0:
            result = "Vô số nghiệm"
        else:
            result = "Vô nghiệm"
    else:
        result = -b / a
    history.append(f"PT bậc 1: {a}x+{b}=0 => {result}")
    print("Kết quả:", result)

def giai_pt_bac_2():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    delta = b**2 - 4*a*c
    if a == 0:
        result = "Đây là PT bậc nhất"
    elif delta < 0:
        result = "Vô nghiệm"
    elif delta == 0:
        result = f"Nghiệm kép: x = {-b/(2*a)}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        result = f"x1 = {x1}, x2 = {x2}"
    history.append(f"PT bậc 2: {a}x²+{b}x+{c}=0 => {result}")
    print("Kết quả:", result)

def xem_lich_su():
    print("=== Lịch sử tính toán ===")
    for h in history:
        print(h)

def thoi_gian():
    now = datetime.datetime.now()
    print("Thời gian hiện tại:", now.strftime("%H:%M:%S %d-%m-%Y"))
