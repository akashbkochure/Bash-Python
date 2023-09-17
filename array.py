
array = ["apple", "pipe", "cherry", "strawberry"]

result = ' '.join(array[3].split())

print(result)


******

array = ["apple", "pine", "cherry", "strawberry"]

num = int(input())

print('\n'.join(array[num].split()) if 0 <= num < len(array) else "Invalid input.")
