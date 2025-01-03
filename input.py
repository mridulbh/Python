name = input("What is your name: ")
print(f"Hi {name}!, Pleasure to meet you.")
print(name)

age = int(input("Enter you age: "))
if age > 18 and age<70:
    print ("You are an adult")
elif age>70 and age <80:
    print("You are old")
elif age>80:
    print("Invalid input")
else:
    print("You are a minor")

fruits =["apple", "banana","orange"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print ("Iteration: ",i) 