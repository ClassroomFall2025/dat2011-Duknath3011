class sinhvienpoly: 
    def __init__(self, ten, nganh, diem):
        self.__ten = ten
        self.__nganh = nganh
        self.__diem = diem
    def get_ten(self):
        return self.__ten
    def set_ten(self, ten):
        self.__ten = ten
    def get_nganh(self):
        return self.__nganh
    def set_nganh(self, nganh):
        self.__nganh = nganh
    def get_diem(self):
        return self.__diem
    def set_diem(self, diem):
        self.__diem = diem
    def nhap_thong_tin(self):
        self.__ten = input("nhap ten sinh vien: ")
        self.__nganh = input("nhap nganh sinh vien: ")
        self.__diem = float(input("nhap diem sinh vien: "))
    def xuat_thong_tin(self):
        print("ten sinh vien la: ", self.__ten)
        print("nganh sinh vien la: ", self.__nganh)
        print("diem sinh vien la: ", self.__diem)
    def hoc_luc(self):
        if self.__diem < 5:
            print("hoc luc yeu")
        elif 5 <= self.__diem < 6.5:
            print("hoc luc trung binh")
        elif 6.5 <= self.__diem < 7.5:
            print("hoc luc kha")
        elif 7.5 <= self.__diem < 9:
            print("hoc luc gioi")
        else:
            print("hoc luc xuat sac")