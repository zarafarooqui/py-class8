#Empty Tuple
my_tuple=()
print(my_tuple)

#Tuple having integers
my_tuple=(1,2,3)
print(my_tuple)

#Tuple with mixed datatype
my_tuple=(1,"Hello",3,4)
print(my_tuple)

#Nested Tuple
my_tuple=("mouse",[8,9,6],(1,2,3))
print(my_tuple)

#Accessing Tuple Elements using Indexing
my_tuple=('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])

#Nested Tuple
n_tuple=("mouse",[8,4,6],(1,2,3))

#Nested  Index
print(n_tuple[0][3])
print(n_tuple[1][1])

#Slicing
print("Sliced:",my_tuple[1:4])

#Iterarting through tuple
for letter in (my_tuple):
    print("Hello",letter)