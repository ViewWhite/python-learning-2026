age = 18
print(age == 18)
print(age != 18)
print(age > 15 and age < 25)
print(age < 10 or age > 60)

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

cities = ["Beijing", "Shanghai", "Chengdu"]
if "Chengdu" in cities:
    print("成都在列表里！")
if "Shenzhen" not in cities:
    print("深圳不在列表里！")