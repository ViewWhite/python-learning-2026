def main():
    # 获取用户输入的时间
    time = input("What time is it? ").strip()
    
    # 调用转换函数，得到小数形式的时间
    hours = convert(time)
    
    # 判断时间范围
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    # 把 "7:30" 拆分成 ["7", "30"]
    hours, minutes = time.split(":")
    
    # 把分钟转换成小时的小数部分：30 / 60 = 0.5
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()