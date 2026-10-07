cities = ["Beijing", "Shanghai", "Chengdu", "Guangzhou"]
print(cities[0])
print(cities[-1])

cities[1] = "Shenzhen"
cities.append("Hangzhou")
cities.insert(1, "Wuhan")
del cities[0]
popped = cities.pop()
cities.remove("Chengdu")
print(cities)

nums = [3, 1, 4, 1, 5, 9]
print(sorted(nums))
nums.sort(reverse=True)
print(nums)
print(len(nums))