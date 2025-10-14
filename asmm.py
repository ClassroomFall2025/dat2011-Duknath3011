danh_sach_nv = []

def nhap_tt_nv(so_nv):
    for i in range(so_nv):
        print(f"Nhập thông tin cho nhân viên thứ {i+1}:")
        ten = input("Tên: ")
        tuoi = int(input("Tuổi: "))
        dia_chi = input("Địa chỉ: ")
        luong = float(input("Lương: "))
        nv = {
            "Tên": ten,
            "Tuổi": tuoi,
            "Địa chỉ": dia_chi,
            "Lương": luong
        }
        danh_sach_nv.append(nv)
    return danh_sach_nv

# xem thông tin nhân viên
def xem_tt_nv():
    print("Thông tin nhân viên: ")
    for i, nv in enumerate(danh_sach_nv):
        print(f"Nhân viên {i+1}:")
        print(f"Tên: {nv['Tên']}, Tuổi: {nv['Tuổi']}, Địa chỉ: {nv['Địa chỉ']}, Lương: {nv['Lương']}")
    return

# tìm kiếm nhân viên
def tim_kiem_nv():
    print("tiềm kiếm nhân viên theo mã nhân viên")
    return

# xóa nhân viên 
def xoa_nv():
    print("xóa nhân viên theo mã nhân viên")

# cập nhât thông tin nhân viên
def cap_nhat_nv():
    print("cập nhật thông tin nhân viên theo mã nhân viên")

# tìm nhân viên theo lương
def tim_nv_theo_luong():
    print("tìm nhân viên theo mức lương")

# sắp xếp nhân viên theo họ và tên
def sap_xep_nv_theo_ten():
    print("sắp xếp nhân viên theo họ và tên")

# sắp xếp nhân viên theo thu nhập
def sap_xep_nv_theo_luong():
    print("sắp xếp nhân viên theo mức lương")

# xuất 5 nhân viên có thu nhập cao nhất
def xuat_5_nv_luong_cao_nhat():
    print("xuất 5 nhân viên có mức lương cao nhất")