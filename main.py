from hrm_package.attendance_logic import attendance_book, clock_in, clock_out
from hrm_package.ui_display import display_records as show
from hrm_package.time_calc import evaluate_flex_time as check

def main():
    while True:
        print("\n=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===")
        print("1. Xem bảng chấm công\n2. Chấm công Vào\n3. Chấm công Ra\n4. Đánh giá vi phạm\n5. Thoát")
        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            show(attendance_book)
        elif choice == "2":
            uid = input("Mã NV: ")
            name = input("Tên NV: ")
            time = input("Giờ vào (HH:MM): ")
            if clock_in(uid, name, time): print("Thành công!")
            else: print("Mã NV đã tồn tại!")
        elif choice == "3":
            uid = input("Mã NV: ")
            time = input("Giờ ra (HH:MM): ")
            if clock_out(uid, time): print("Ghi nhận giờ ra thành công!")
            else: print("Không tìm thấy NV!")
        elif choice == "4":
            check(attendance_book)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()