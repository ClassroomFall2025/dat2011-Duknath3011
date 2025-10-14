class sanpham:
    def __init__(self,ten,gia,giamgia,thue):
        self.ten = ten
        self.gia = gia
        self.giamgia = giamgia
        self.thue = thue
    
    def tinhthue(self):
        return self.gia * 0.1
    def nhapsp(self):
        self.ten = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.giamgia = float(input("Nhập giảm giá sản phẩm: "))
        self.thue = self.tinhthue()
    
    def xuatthongtin(self):
        return f"Tên sản phẩm: {self.ten}, Giá: {self.gia}, Giảm giá: {self.giamgia}, Thuế: {self.thue}"
    