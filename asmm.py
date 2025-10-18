import csv
# Y1 nhap thong tin nhan vien va luu vao file csv
def nhap_nhanvien():
    with open("asm.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["Mã NV", "Họ và tên", "Lương"])
        n = int(input("Nhập số nhân viên cần thêm: "))
        for i in range(n):
            print(f"Nhập thông tin nhân viên thứ {i+1}: ")
            ma_nv = input("Nhập mã nhân viên: ")
            ten_nv = input("Nhập tên nhân viên: ")
            luong = float(input("Nhập lương: "))
            
            writer.writerow([ma_nv, ten_nv, luong])

    print("==> Dữ liệu đã được lưu vào asm.csv ")

# Y2 xem thông tin nhân viên
def xem_tt_nv():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    print("Thông tin nhân viên:")
    for line in lines:
        print(line.strip())
    return

# Y3 tìm kiếm nhân viên
def tim_kiem_nv():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        f.close()

    if len(data) <= 1:
        print("Chưa có dữ liệu nhân viên.")
        return
    else:
        ma_nv = input("Nhập mã nhân viên cần tìm: ")
        found = False
        for row in data[1:]:
            if row[0] == ma_nv:
                print(f"Tìm thấy nhân viên: Mã NV: {row[0]}, Họ và tên: {row[1]}, Lương: {row[2]}")
                found = True
                break
        if not found:
            print("Không tìm thấy nhân viên với mã đã nhập.")
    return

# Y4 xóa nhân viên 
def xoa_nv():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        f.close()
        if len(data) <= 1:
            print("Chưa có dữ liệu nhân viên.")
        else:
            ma_nv = input("Nhập mã nhân viên cần xóa: ")
            new_data = [data[0]]  # giữ lại header
            found = False
            for row in data[1:]:
                if row[0] != ma_nv:
                    new_data.append(row)
                else:
                    found = True
            if found:
                with open("asm.csv", mode="w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(new_data)
                print(f"Đã xóa nhân viên với mã NV: {ma_nv}")
            else:
                print("Không tìm thấy nhân viên với mã đã nhập.")   

# Y5 cập nhât thông tin nhân viên
def cap_nhat_nv():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        f.close()
    if len(data) <= 1:
        print("Chưa có dữ liệu nhân viên.")
    else:
        cap_nhat_nv = input("Nhập mã nhân viên cần cập nhật: ")
        found = False
        for i in range(1, len(data)):
            if data[i][0] == cap_nhat_nv:
                print(f"Nhân viên hiện tại: Mã NV: {data[i][0]}, Họ và tên: {data[i][1]}, Lương: {data[i][2]}")
                ten_moi = input("Nhập họ và tên mới: ")
                luong_moi = input("Nhập lương mới: ")

                if ten_moi:
                    data[i][1] = ten_moi
                if luong_moi:
                    data[i][2] = luong_moi

                found = True
                break
        if found:
            with open("asm.csv", mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print("Đã cập nhật thông tin nhân viên.")

# Y6 tìm nhân viên theo lương
def tim_nv_theo_luong():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)

    if len(data) <= 1:
        print("Chưa có dữ liệu nhân viên.")
        return
    else:
        luong_can_tim = float(input("Nhập mức lương cần tìm: "))
        found = False
        for row in data[1:]:
            if float(row[2]) == luong_can_tim:
                print(f"Tìm thấy nhân viên: Mã NV: {row[0]}, Họ và tên: {row[1]}, Lương: {row[2]}")
                found = True
        if not found:
            print("Không tìm thấy nhân viên với mức lương đã nhập.")
    return

# Y7 sắp xếp nhân viên theo họ và tên
def sap_xep_nv_theo_ten():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    if len(data) <= 1:
        print("Chưa có dữ liệu nhân viên.")
        return
    else:
        header = data[0]
        nv_data = data[1:]
        nv_data.sort(key=lambda x: x[1])  # sắp xếp theo tên
        print("Danh sách nhân viên sau khi sắp xếp theo họ và tên:")
        print(header)
        for row in nv_data:
            print(row)
        return

# Y8 sắp xếp nhân viên theo thu nhập
def sap_xep_nv_theo_luong():
    with open("asm.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    if len(data) <= 1:
        print("Chưa có dữ liệu nhân viên.")
        return
    else:
        header = data[0]
        nv_data = data[1:]
        nv_data.sort(key=lambda x: float(x[2]), reverse=True)  # sắp xếp theo lương giảm dần
        print("Danh sách nhân viên sau khi sắp xếp theo lương:")
        print(header)
        for row in nv_data:
            print(row)
        return

# Y9 xuất 5 nhân viên có thu nhập cao nhất
def xuat_5_nv_luong_cao_nhat():
    with open("asm.csv", mode="r", encoding="utf8") as f:
        reader = csv.reader(f)
        data = list(reader)
    if len(data) <= 1:
        print("Chưa có dữ liệu nhân viên.")
        return 
    ds_nv = data[1:]
    for row in ds_nv:
        row[2] = float(row[2])
    ds_nv.sort(key=lambda x: x[2], reverse=True)
    print("5 nhân viên có thu nhập cao nhất:")
    print(data[0])
    for row in ds_nv[:5]:
        print(row)