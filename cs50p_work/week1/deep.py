# 接收输入，并统一转成小写，去掉首尾空格
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# 只要满足其中之一，就输出 Yes
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")