# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['Clinda', 'Bobert', 'Schmicheal']
print(students[1] )
print(students[2])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = ('steak tartar', 'hakarl', 'balut'  )
for key in foods:
    print(f'{key} is a good food')


# Exercise 3
# Using a for loop, print just the last two food strings from foods.

for key in foods[-2:]:
#                 ^-- didnt think to add the [-2] there. almost had it with [2:] placed elsewhere
    print(key)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city': 'Metropolis',
    'state': 'Delaware',
    'population': 8380000
}

#                               ------------My attempt-------------------
# for city, state, population in home_town.items():
#     print(f'I was born in {city}, {state} - population of {population}')

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

for key in home_town:
    print(f"{key} = {home_town[key]}")


# Exercise 6
# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.


cohort = []

#     -----------------------apparently i was WAAAAAAAAAAAAAYYYYYYYYYYY off here-----------------------------
# cohort.extend([{'student': 'Clinda', 'fav_food' 'steak tartar'}, {'student': 'Bobert', 'fav_food' 'hakarl'}, {'student': 'Schmichael', 'fav_food' 'balut'}])
# print(cohort)


#    -------------------------looking a littler closer----------------------------------
# for student in cohort:
#     {
#         'student': 'Clinda',
#         'fav_food': 'steak tartar'
#     },
#     {
#         'student': 'Bobert',
#         'fav_food': 'hakarl'
#     },
#     {
#         'student': 'Schmicheal',
#         'fav_food': 'balut'
#     }
    # cohort.append()

for index, student in enumerate(students):
    cohort.append({
            # ^--- had this in the wrong place
            'student': student,
            'fav_food': foods[index]
        })
for student in cohort:
            print(student)


# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.


#         ----------------------------first attempt-------------------------------
# awesome_students = {
#     'student': student
# }
# awesome_students.insert(students)
# print(f"{student} is awesome!")

awesome_students = [f"{name} is awesome!" for name in students]

for student in awesome_students:
    print(student)


# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.


# ------first attempt-------
# if "a" in foods:
#     print(food)
# --------second attempt-----
# print("{foods}" == foods[a])

letter = input("a")
for word in foods:
    if letter in word:
        print(word)
