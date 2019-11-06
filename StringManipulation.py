a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing
b = "Hello, World!"
print(b[2:5])

#Negative Slicing

b = "Hello, World!"
print(b[-5:-2])


#Length
a = "Hello, World!"
print(len(a))


#The strip() method removes any whitespace from the beginning or the end:

a = " Hello World! "
print(a.strip()) # returns "Hello, World!"

#Replace
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


age = 36
txt = "My name is John, and I am  {}"
print(txt.format(age));

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))