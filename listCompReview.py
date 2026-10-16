import random
# use list comprehension to create a new list of surnames
surnames = ["GOAT", "Rememberer", "Banada", "Living Being", "Impressionist"]
students = ["Isaac", "Paul", "Anthony", "Mr. Freeman", "Ethan", "Gordon"]

# use list comprehension to create a new list with the names added with a random surname
randomNames = [student + " the " + random.choice(surnames) for student in students]

print(randomNames)