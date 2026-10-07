cities = ["Beijing", "Shanghai", "Chengdu"]
for city in cities:
    print(f"I want to go to {city.title()}.")

for i in range(1, 5):
    print(i)

numbers = list(range(1, 6))
print(numbers)

nums = [3, 1, 4, 1, 5, 9]
print(min(nums))
print(max(nums))
print(sum(nums))

squares = [value ** 2 for value in range(1, 5)]
print(squares)  # [1, 4, 9, 16]