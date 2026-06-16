attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)},
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]

def clock_in(id, name, time):
    # Kiểm tra trùng ID
    for emp in attendance_book:
        if emp["id"] == id:
            return False
    attendance_book.append({"id": id, "name": name, "times": (time, None)})
    return True

def clock_out(id, time):
    for emp in attendance_book:
        if emp["id"] == id:
            # Ghi đè tuple vì tuple là immutable
            emp["times"] = (emp["times"][0], time)
            return True
    return False