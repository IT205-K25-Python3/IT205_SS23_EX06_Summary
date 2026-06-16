from tabulate import tabulate as tbl

def display_records(data):
    table = []
    for emp in data:
        clock_out_val = emp["times"][1] if emp["times"][1] else "[Đang làm việc]"
        table.append([emp["id"], emp["name"], emp["times"][0], clock_out_val])
    
    print("\n--- BẢNG CHẤM CÔNG ---")
    print(tbl(table, headers=["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"], tablefmt="grid"))