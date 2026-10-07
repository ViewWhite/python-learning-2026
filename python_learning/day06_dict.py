# 1. 创建与访问
student = {"name": "Zhang San", "age": 18, "major": "AI"}
print(student["name"])       # Zhang San
print(student.get("age"))    # 18
print(student.get("score", 0))  # 0 (默认值)

# 2. 添加、修改、删除
student["age"] = 19
student["city"] = "Chengdu"
del student["major"]
print(student)  # {'name': 'Zhang San', 'age': 19, 'city': 'Chengdu'}

# 3. 遍历字典
scores = {"Math": 90, "English": 85, "Python": 95}
for subject, score in scores.items():
    print(f"{subject}: {score}")

for subject in scores.keys():
    print(subject)

for score in scores.values():
    print(score)