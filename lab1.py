# MSSV: [Nhập MSSV của bạn]
# Họ tên: Vũ Thanh Tùng
# Lớp: [Nhập tên lớp]

def bai1():
    print("-" * 30)
    print("BÀI 1: XUẤT DỮ LIỆU")
    print("Chào mừng bạn đến với FPT Polytechnic!")
    print("Chúc bạn học tốt môn Nhập môn lập trình (ITA105).")

def bai2():
    print("-" * 30)
    print("BÀI 2: TÍNH TỔNG HIỆU TÍCH THƯƠNG")
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    print(f"Tổng: {a + b}")
    print(f"Hiệu: {a - b}")
    print(f"Tích: {a * b}")
    print(f"Thương: {a / b if b != 0 else 'Không thể chia cho 0'}")

def bai3():
    print("-" * 30)
    print("BÀI 3: TÍNH DIỆN TÍCH CHU VI HÌNH CHỮ NHẬT")
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    print(f"Chu vi: {(dai + rong) * 2}")
    print(f"Diện tích: {dai * rong}")

# Chạy các bài tập
if __name__ == "__main__":
    bai1()
    bai2()
    bai3()
    print("-" * 30)
    print("HOÀN THÀNH LAB 1")