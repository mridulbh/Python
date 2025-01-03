#!bin/python

# name = "My name is Jerry! and I'm a beast"
# words = name.split()
# words_length=[]

# for word in words:
#     if word != "My":
#         words_length.append(len(word))

# print(words)
# print(words_length)


# # Using the list comprehension
# words_len=[len(Words) for Words in words if Words != "name"]

# print(words_len)


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(i) for i in numbers if i>0]

# for i in numbers:
#     if i>0: 
#         print(i)
print(newlist)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list = [print(x,y,z) for i in range if sum(x+y+z)!=n]

print(x,y,z,n)