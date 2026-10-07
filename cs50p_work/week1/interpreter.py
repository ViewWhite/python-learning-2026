expression = input("Expression: ").strip()

# 把 "1 + 1" 拆分成 ["1", "+", "1"]，然后分别赋值给 x, y, z
x, y, z = expression.split()

# 把字符串转成浮点数
x = float(x)
z = float(z)

# 判断运算符并计算
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# 输出结果，保留一位小数
print(f"{result:.1f}")