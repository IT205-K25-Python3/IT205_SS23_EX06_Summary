from datetime import datetime as dt

def evaluate_flex_time(data):
    fmt = "%H:%M"
    limit_time = dt.strptime("10:00", fmt)
    
    for emp in data:
        if emp["times"][1] is None:
            print(f"{emp['id']} - Đang làm việc, chưa thể đánh giá.")
            continue
            
        in_time = dt.strptime(emp["times"][0], fmt)
        out_time = dt.strptime(emp["times"][1], fmt)
        
        # Kiểm tra muộn
        if in_time > limit_time:
            print(f"{emp['id']} - Vi phạm: Đến muộn quá 90 phút.")
        else:
            # Tính thời gian làm việc
            duration = (out_time - in_time).total_seconds() / 3600
            if duration < 9:
                print(f"{emp['id']} - Vi phạm: Về sớm, chưa đủ 9 tiếng.")
            else:
                print(f"{emp['id']} - Hợp lệ: Hoàn thành ca.")