# --------------
class_1 = ['Geoffrey Hinton', 'Andrew  Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
new_class = class_1 + class_2
print("Concatenated class members are:\n", new_class, "\n")
new_class.append('Peter Warden')

print("\n\nAdd of new members:\n", new_class)
new_class.remove('Carla Gentry')

print("\nAfter deletion of members:\n", new_class)
print("---------------------------------------------")
courses= {'Math' : 65 , 'English' : 70, 'History' : 80, 'French' : 70, 'Science' : 60 }
print(courses)
total = sum(courses.values())
print("The sum of subjects is:", total)
percentage = (total / 500)*100
print("Percentage of subjects are:", percentage)
print("---------------------------------------------")
mathematics = {'Geoffrey Hinton' : 78, 'Andrew  Ng' : 95, 'Sebastian Raschka' : 65, 'Yoshua Bengio' : 50, 'Hilary Mason' : 70, 'Corinna Cortes' : 66, 'Peter Warden' : 75}

topper = max(mathematics, key = mathematics.get)
print("Highest scored in Mathematics is:", topper)
print("---------------------------------------------")
first_name = topper.split()[0]
print(first_name)
last_name = topper.split()[1]
print( last_name)

full_name = last_name + " " + first_name
certificate_name = full_name.upper()

print("Certificate Name:", certificate_name)


