#Python Code Academy course

#+= adds on to a string

price = 0
shoes = 3
price += shoes
top = 5
price += top
print(price)


# use three ' to close off string with a lot of line breakers

to_you = '''somethine something not something? not something something'''
print(to_you)

####################################
# block letters

#Mohine
#Alam
#I like languages

print('MM    MM')
print('MM    MM')
print('M M  M M')
print('M   M  M')
print('M      M')

MA = '''
MM    MM    AAA
MM    MM   A   A
M M  M M  AAAAAAA
M  M M M  A     A
M   M  M  A     A
M      M  A     A 
  '''
print(MA)

########################################
#trying out user input and converting string to lower case but first letter with upper case using .lower() and .title()

user_input = input('Enter your name:')
user_input_lower = user_input.lower()
print(user_input_lower.title())

# Booleans give back True or Flase
baby_bool = True
print(type(baby_bool))

#lists
motorbikes = ['honda','yamaha']
motorbikes.append('something else')
motorbikes.insert(0,'something')
print(motorbikes)

###############################################
# boleans operators : and

credits = 120
gpa = 3.5

if credits >= 120 and gpa >=2.0:
    print('you have passed!')

# bolean operator : or

if credits >= 120 or gpa >=2.0:
    print('you have succeeded')

# booleans operator : not and else statements

if not gpa >=2.0 and not credits >= 120:
    print('you do not have sufficient points')
else:
    print('you have met requirments to graduate')

#elif statements with if and else, students want letter grades

grade = 86
 
if grade >=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
else:
    print("D")
#######################################
# just a reminder that = is not a relaitonal operator so will not work in if statements

# producing a random number using random and .randint() operation - Magic8Ball

import random
random_number = random.randint(1,9)
answer = 'Yes'
answer_two ='No'
answer_three = 'Try again'
name = input('what is your name:')
Question = input('Write your question:')

if len(name) > 0:
    print(name, 'asks:', Question)
elif name == "" or len(name) == 0:
    print('Question:', Question)
if Question == '':
    print('You have not entered a question.')


print('Your random number is:', random_number)

if random_number == 1 and len(Question) > 13:
    print('Magic 8 balls answer:', answer)
elif random_number == 2 and len(Question) > 13:
    print('Magic 8 balls answer:', answer_two)
elif random_number == 3 and len(Question) > 13:
    print('Magic 8 balls answer:', answer_three)
else:
    print('Error, try again')

###############################

weight = 41.5

# Ground Shipping

if weight <= 2:
  cost_o = weight * 1.5 + 20
  print('Your ground shipping cost is $', cost_o)
elif weight > 2 and weight <= 6:
  cost_t = weight * 3 + 20
  print('Your ground shipping cost is $', cost_t)
elif weight >=6 and weight <= 10:
  cost_th = weight * 4 + 20
  print('Your ground shipping cost is $', cost_th)
else:
  cost = weight * 4.50 + 20
  print('Your ground shipping cost is $', cost)

# Ground Shipping Premium

gs_premium = 105.00
print('The premium ground shipping flat charge costs and addition of $', gs_premium, 'ontop.')

# Drone Shipping
if weight <2:
  cost = weight * 4.5 
  print('Or your drone shipping cost is', cost)
elif weight >=2 and weight <=6:
  cost = weight * 9
  print('Or your drone shipping cost is', cost)
elif weight >=6 and weight <=10:
  cost = weight * 12
  print('Or your drone shipping cost is:', cost)
else:
  cost = weight * 14.25
  print('Or your drone shipping cost is', cost)

##########################
#lists. Replacing items in a list

garden_waitinglist = ['Adam','Calla']
garden_waitinglist[1] = 'Bob'
print(garden_waitinglist)

###########
#accessing 2d list
class_name_test = [['Jenny', 90],['Alexus', 85.5],['Sam', 83],['Ellie',101.5]]

sams_score = class_name_test[2][1]
ellies_score = class_name_test[-1][-1]
print(class_name_test)
print(sams_score)
print(ellies_score)

##############
# Review of lists
first_names = ['Ainsley','Ben','Chani','Depak']
preferred_size = ['Small','Large','Medium']
preferred_size.append('Medium')
print(preferred_size)

customer_data = [['Ainsley','Small',True],['Ben','Large',False], ['Chani','Medium',True],['Depak','Medium', False]]
customer_data[2][2] = False
customer_data[1].remove(False)
print(customer_data)

extra_customers = [['Amit','Large', True],['Karim','X-Large',False]]
customer_data_final = customer_data + extra_customers
print(customer_data_final)

################
#more list work with appending, removing and inserting
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ['Physics', 'Calculus', 'Poetry', 'History']
grades = [98,97,85,88]

grade_book = [['physics',98],['calculus',97],['Poetry',85],['history',88]]

grade_book.insert(0,['computer science',100])
grade_book.insert(0,['visual arts', 93])
grade_book[0][1] = 93 + 5
grade_book[4].remove(85)
grade_book[4].append('Pass')

print(grade_book)

full_gradebook = last_semester_gradebook + grade_book

print(full_gradebook)

#########
#.pop() function

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
data_science_topics.pop(3)
print(data_science_topics)

#######################
#range.() and list() function with range

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

#differences between range of number using last number 
range_five_three = range(5, 15, 3)
print(list(range_five_three))

range_diff_five = range(0,40,5)
print(list(range_diff_five))

#slicing lists
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

print(beginning)

middle = ['pants', 'pants']
print(middle)

###############

# slicing using negative integers
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

##########
#Count

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count('Jake')
print(jake_votes)

#######################

#sorting lists

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses)


names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)

print(sorted_cities)

###########################
# project with list manipulations

toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print('We sell', num_pizzas, 'different kinds of pizza!')

pizza_and_prices = [[2,'pepperoni'],[6,'pineapple'],[1,'cheese'],[3,'sausage'],[2, 'olives'],[7,'anchovies'],[2,'mushrooms']]
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.insert(4,[2.5,'peppers'])
three_cheapest = pizza_and_prices[:3]
print(pizza_and_prices)
print(three_cheapest)
toppings_and_prices_two = zip(toppings,prices)
print(list(toppings_and_prices_two))

######################
# loop iterations using for

for promise in range(5):
  print("I will finish the python loops module!")

for loop in range(5):
 print('this is loop number' + str(loop + 1))

 ######################
 # while loop iteration

 countdown = 10

while countdown >= 0:
  print(countdown)
  countdown -= 1
print('We have liftoff!')

###############################
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 

length = len(python_topics)
index = 0

while index < length:
  print('I am learning about ' + python_topics[index])
  index += 1
print('Thats all')

##################
# loops, if statements and breaks

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
   break
print('They have the dog I want!')

###############
# continue in if loop
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age <= 20:
    continue
  print(age)

  #######################
  # nested loops
  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
print(scoops_sold)


################
# list comprehension with for loops

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = []

for grade in grades:
  scaled_grades.append(grade + 10)
print(scaled_grades)

# same as

scaled_grades = [grade + 10 for grade in grades]

print(scaled_grades)

#########
# list comprehension conditionals

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

###########

# summary
single_digits = [9,1,2,3,4,5,6,7,8,0]
single_digits.sort()
squares = []

loop = [digit for digit in single_digits]
print(loop)

for digit in single_digits:
  print(digit)
for digit in single_digits:
  squares.append(digit ** 2)
print(squares)

cubes = [digit ** 3 for digit in single_digits]

print(cubes)


####################
# list comprehensions and loops

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
  print(total_price)

average_price = total_price / len(prices)
print('Average haircute price:', average_price)

new_prices = [price + 5 for price in prices]
print(new_prices)

#######

total_revenue = 0

for i in range(len(hairstyles)):
 total_revenue = prices[i] * last_week[i]
 print('Total revenue is:', total_revenue)
 average_daily_revenue = total_revenue / 7
 print('Average daily revenue is:', average_daily_revenue)
 
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print(cuts_under_30)

########################
# Parameters and Arguments in functions and calling functions
def generate_trip_instructions(location):
  print('Looks like you are planning a trip to visit', location)
  print('You can use the public subway system to get to', location)

generate_trip_instructions('Grand Central Station')

#########################
# Multiple Parameters
def calculate_expenses(plane_ticket_price,car_rental_rate,hotel_rate,trip_time):
  car_rental_total = car_rental_rate *   trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  print('Hello customer! Your grand total from car rental, hotel, and plane ticket comes to:', (hotel_total + car_rental_total + plane_ticket_price) )

calculate_expenses(200,100,100,5)

############
# more

def trip_planner(first_destination, second_destination, final_destination = 'Codecademy HQ'):
  print('Here is what your trip will look like!')
  print('First, we will stop in', first_destination,', then', second_destination,', and lastly', final_destination)

trip_planner('Brooklyn','Queens')

#more
def trip_planner(first_destination, second_destination, final_destination = 'Codecademy HQ'):
  print('Here is what your trip will look like!')
  print('First, we will stop in', first_destination,', then', second_destination,', and lastly', final_destination)

trip_planner(first_destination = 'Brooklyn', final_destination = 'Germany',second_destination = 'India')

################
# inbuilt functions
max_price = max(tshirt_price,shorts_price,mug_price,poster_price)
min_price = min(tshirt_price,shorts_price,mug_price,poster_price)
rounded_price = round(tshirt_price,1)

print(max_price)
print(min_price)
print(rounded_price)

#####################
# scope issue fixed

# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

#################
# Returns with functions, parameters, and arguments

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense
shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

print('Your remaining budget after T-shirt investment is:' + str(new_budget_after_shirt))

###################

# multiple returns in functions
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

############
# review

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome(" <YOUR NAME HERE> ")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")


destination_setup(" <PICK AN ORIGIN> ", "<PICK A DESTINATION > ", estimate, "Car")

###################

# functions projects with Physics


train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# F to C or C to F 
def f_to_c(f_temp):
 c_temp = (f_temp - 32) * 5/9
 return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Force
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass,train_acceleration)
print('The GE train supplies',train_force,' Newtons of force')

#energy
def get_energy(mass,c = 3*10**8):
  return mass * c**2
bomb_energy = get_energy(bomb_mass)
print('A 1kg bomb supplies',bomb_energy,'Joules')

# work

def get_work(mass,acceleration,distance):
  work = get_force(mass,acceleration) * distance
  return work
train_work = get_work(train_mass,train_acceleration,train_distance)
print('Train work is mass x acceleration x,distance, which equals:',train_work)
print('The GE train does',train_work,'Joules of work over Y meters')

################

# control flow using functions: powers

def large_power(base,exponent):
  x = base ** exponent
  if x > 5000:
   return True
  else:
   return False
x = large_power(5,10000)
print(x)
print(large_power(2, 13))
print(large_power(2, 12))

# budget true or false

def budget_calculator(budget,food_bill,electricity_bill,internet_bill,rent):
 bills_total = food_bill + electricity_bill + internet_bill + rent
 budget_left_over = budget - bills_total
 if budget < budget_left_over:
  return True
 else:
  return False
my_budget = budget_calculator(100,10,20,20,4)

print('My budget after bills is equal to my starting budget:', my_budget)


# more functions challenges: using lists

def append_size(my_list):
 my_list.append(len(my_list))
 return my_list
print(append_size([23, 42, 108]))

def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  return my_list
print(append_sum([1, 1, 2]))

# more function challenges: using if statements

def larger_list(my_list1,my_list2):
  if len(my_list1) > len(my_list2):
    return my_list1[-1]
  elif len(my_list2) > len(my_list1):
    return my_list2[-1]
  elif len(my_list2) == len(my_list1):
    return my_list1[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# functions and lists to return range of numbers

def every_three_nums(start):
 return list(range(start,101,3))
print(every_three_nums(91))

# function with slicing elements

def remove_middle(my_list,start,end):
  return my_list[:start] + my_list[end+1:]

print(remove_middle([24,14,16,8,9,10,11],1,3))

# functions with count in list

def more_frequent_item(my_list,item1,item2):
  if my_list.count(item1) > my_list.count(item2):
    return item1
  else:
    return item2
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# functions and splicing: returning change of one element in list

def double_index(my_list,index):
 if index > len(my_list):
  my_list
 else:
  new_list = my_list[0:index]
  new_list.append(my_list[index]*2)
  return new_list + my_list[index+1:]
print(double_index([3, 8, -10, 12], 2))

# functions: returning the middle number using int(len()) function

def middle_element(my_list):
  if len(my_list) % 2 != 0:
    return my_list[int(len(my_list)/2)]
  else:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1] 
    return sum/2
print(middle_element([5, 2, -10, -4, 4, 5]))


# functions: divisible by 10

def divisible_by_ten(nums):
  for number in nums:
   if number % 10 == 0:
    print(number)
print(divisible_by_ten([20, 25, 30, 35, 40]))

# returning count of number that are divisible by 10
def divisible_by_ten(nums):
 count = 0
 for number in nums:
  if number % 10 == 0:
   count += 1
 return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

# functions with lists

def add_greetings(names):
  each_greeting = []
  for name in names:
     hello_and_name = 'Hello ' + name
     each_greeting.append(hello_and_name)
  return each_greeting
print(add_greetings(["Owen", "Max", "Sophie"]))

# splicing lists. Indexing is a practice to access elements in lists
# list[initial : end : index jump]
# while loop continues as long as two conditions are met: 1 = as long as first element is even and 2 = the list is not empty
# my_list[1:] indicates slicing of the list starts from index 1 to the end, this removes the first element from the list
# the loop continues to execute as long the first element of the list is even and the list is not empty
# once the condtions of the while loop are no longer met the loop exits and the modified list with removed evens is returned

def delete_starting_evens(my_list):
  while (my_list[0] % 2 == 0) and len(my_list) > 0:
    my_list = my_list[1:]
  return my_list
list1 = [0,1,2,3,4,5]
print(list1[::])
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

# returning odd indices

def odd_indices(my_list):
  odd_indicies = []
  for odd_number in range(1,len(my_list),2):
    odd_indicies.append(my_list[odd_number])
  return odd_indicies

print(odd_indices([4, 3, 7, 10, 11, -2]))

# bases and powers giving back list of answers using nested loops

def exponents(bases,powers):
  new_list = []
  for base in bases:
   for power in powers:
    multiplication = base ** power
    new_list.append(multiplication)
  return new_list

  # functions and accessing sum of total elements in lists and returning bigger list or the first list if both lists are equal

  def larger_sum(lst1,lst2):
   total1 = sum(lst1[0:])
   total2 = sum(lst2[0:])
   if total1 > total2:
    return lst1
   elif total2 > total1:
    return lst2
   else:
    return lst1
print(larger_sum([1, 9, 5], [2, 3, 7]))

#same output written in different code

def larger_sum(lst1,lst2):
  size1 = 0
  size2 = 0
  for number in lst1:
    size1 += number
  for number in lst2:
    size2 += number
  if size1 > size2:
    return lst1
  elif size2 > size1:
    return lst2
  elif size2 == size1:
    return lst1
print(larger_sum([1, 9, 5], [2, 3, 7]))

# returning sum of elements once it has reached above 9000, or sum of list if it is below 9000, or return of 0 if the list has nothing
def over_nine_thousand(lst):
  lst_sum = 0
  for number in lst:
    lst_sum += number
    if sum(lst[0:]) < 9000:
      return sum(lst)
    elif len(lst) == 0 :
      return 0
    elif (lst_sum > 9000):
       break
  return lst_sum
print(over_nine_thousand([8000, 900, 120, 5000]))

# Returning largest number in a list using a function

def max_num(nums):
  numbers = nums[0]
  for number in nums:
   if number > numbers:
    maximum = number
  return maximum
print(max_num([50, -10, 0, 75, 20]))

# function returning idexes from two lists that show the same element at that index
def same_values(lst1,lst2):
  new_list = []
  for number in range(len(lst1)):
    if lst1[number] == lst2[number]:    
       new_list.append(number)
  return new_list
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# function comparing two lists, one is reversed

def reversed_list(lst1,lst2):
  lst1.sort(reverse = True)
  if lst1 == lst2:
    return True
  else:
      return False
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# function giving back the tenth power
def tenth_power(num):
  return num ** 10
print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))

# finding square root with functions

def square_root(num):
  return num ** 0.5
print(square_root(16))
print(square_root(100))

# calculating % wins 

def win_percentage(wins,losses):
  percentage_wins = wins/(wins + losses) * 100
  return percentage_wins
print(win_percentage(5, 5))
print(win_percentage(10, 0))

# average returned
def average(num1,num2):
    return (num1+num2) / 2
print(average(1, 100))
print(average(1, -1))

# giving back remainder
def remainder(num1,num2):
  remainder = (num1 * 2) % (num2 / 2)
  return remainder
print(remainder(15, 14))
print(remainder(9, 6))

# returning first three multiples
def first_three_multiples(num):
  first_multiple = num * 1
  second_multiple = num * 2
  third_multiple = num * 3
  first_three_multiple = [first_multiple,second_multiple,third_multiple]
  return first_three_multiple
print(first_three_multiples(10))
print(first_three_multiples(0))

# returns % of tip
def tip(total,percentage):
   tip =  total / 100 * percentage 
   return(tip)
print(tip(10, 25))
print(tip(0, 100))

# returning an introduction
def introduction(first_name,last_name):
  print(last_name + ', ' + first_name + ' ' + last_name)
introduction("James", "Bond")
introduction("Maya", "Angelou")

# same output slightly differet code
def introduction(first_name,last_name):
  return last_name + ', ' + first_name + ' ' + last_name
print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

# returning dog years in a string
def dog_years(name,age):
  return name + ', you are ' + str(age*7) + ' years old in dog year'
print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

# different mathmatical operations given back
def lots_of_math(a,b,c,d):
  total_ab = a + b
  total_cd = c - d
  ab_cd = total_ab * total_cd
  remainder = total_ab % total_cd
  return [total_ab,total_cd,ab_cd,remainder]
print(lots_of_math(1, 2, 3, 4))

# Strings and accessing letters 

my_name = 'Mohine'
first_initial = my_name[0]
print(first_initial)

# Slicing strings
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]
print(new_account)
print(temp_password)

# more slicing with functions
def account_generator(first_name,last_name):
  first3 = first_name[:3]
  last3 = last_name[:3]
  new_account = first3 + last3
  return new_account
print(account_generator("Julie","Blevins"))

# more slicing with function creating password

first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name,last_name):
  concatenation = first_name[-3:] + last_name[-3:]
  return concatenation
temp_password = password_generator(first_name,last_name)
print(temp_password)

# creating new concatenated and spliced string to replace immutable first string
first_name = "Bob"
fixed_first_name = "R" + first_name[1:3]
print(fixed_first_name)

# using back slashes to add quotation marks within strings
password = "theycallme\"crazy\"91"
print(password)

# iterating through a string and returning the length of the string
def get_length(string):
  word = 0
  for character in string:
   word += 1
  return word
print(get_length('test'))

# strings and conditionals, if a letter is in the word it will return true
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

# using in: this is a boolean expression which will return either true or false

def contains(big_string,little_string):
  if little_string in big_string:
    return True
  else:
    return False
print(contains('watermelon','melon'))
print(contains("watermelon", "berry"))

# returning number of common letters between two strings

def common_letters(string_one,string_two):
  common = 0
  for letter in string_one:
   for element in string_two:
    if letter == element:
      common += 1
  return common
print(common_letters("banana", "cream"))

# returning specific letter in two strings using strings and conditionals
def common_letters(string_one,string_two):
  common = []
  for letter in string_one:
    if letter in string_two and not letter in common:
      common.append(letter)
  return common
print(common_letters('manhattan', 'san francisco'))

# user name and password generator
def username_generator(first_name,last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    return first_name + last_name
  else:
   user_name = first_name[:3] + last_name[:4]
  return user_name
print(username_generator('Abe','Simpson'))


def password_generator(user_name):
   password = user_name[-1] + user_name[:-1]
   return password
print(password_generator('AbeSimp'))

# different code but same output of password generator
def password_generator(user_name):
  password = ""
  for index in range(0,len(user_name)):
    password += user_name[index-1]
  return password
print(password_generator('AbeSimp')) 

# code takes index of length of the word and divides it by 2 and gives back remainder, if the remainder is 0 it will print the letter


def right_letter(word):
 for letter in range(len(word)):
  if letter % 2 == 0:
   print(word[letter])
print(right_letter('watermelon'))

# ammeding strings, using title upper lower and split

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

# Splitting strings in lists to remove mistakes or return specific elements in lists
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

# \n = new line splits multiple line string by line break
# \t = horizontal tab, allows to split strings by tabs - useful when dealing with certain datasets because it is not uncommon for data points to be sepearated by tabs
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

# joining elements in a list to form a string using .join()

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

# joining the list of strings into one string seperated on different lines
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# stripping strings from white space or an arguement and joining separate strings into one and putting them onto different lines
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for lines in love_maybe_lines:
  love_maybe_lines_stripped.append(lines.strip())
  love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# fixing words in strings, replacing a word/name with another
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer','Toomer')
print(toomer_bio_fixed)

# finding what the index of the string is starting from
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)
# using the .format() function to add arguments specified by parameters in the body of a funciton
def poem_title_card(title,poet):
  return 'The poem \"{}\" is written by {}.'.format(title,poet)
print(poem_title_card("I Hear America Singing", "Walt Whitman"))

# format() and using key words
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc
my_beard_description = poem_description("1974","Shel Silverstein","My Beard","Where the Sidewalk Ends")
print(my_beard_description)

# editing a string into comprehensive lists to return loops of strings
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')
highlighted_poems_stripped = []
for lines in highlighted_poems_list:
  highlighted_poems_stripped.append(lines.strip())
highlighted_poems_details = []
for lines in highlighted_poems_stripped:
 highlighted_poems_details.append(lines.split(':'))

titles = []
poets = []
dates = []
for lines in highlighted_poems_details:
  titles.append(lines[0])
  poets.append(lines[1])
  dates.append(lines[2])
  
for i in range(0,len(highlighted_poems_details)):
    poem_desc =  'The poem {} was published by {} in {}'.format()
print(poem_desc)

####################################################################################
# thread shed project
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

#------------------------------------------------
#

daily_sales_replaced = daily_sales.replace(';,;',':')
daily_transactions = daily_sales_replaced.split(',')
#
daily_transactions_split = []
for transactions in daily_transactions:
  daily_transactions_split.append(transactions.split(':'))
#
transactions_clean = []
for lists in daily_transactions_split:
  transaction_clean_individual = []
  for elements in lists:
   transaction_clean_individual.append(elements.replace('\n','').strip(' '))
  transactions_clean.append(transaction_clean_individual)
#print(transactions_clean)
#
customers = []
sales = []
thread_sold = []
for lists in transactions_clean:
  customers.append(lists[0])
  sales.append(lists[1])
  thread_sold.append(lists[2])
#print(customers)
#print(sales)
#print(thread_sold)


removed_sign = []
for elements in sales:
  removed_sign.append(elements.replace('$',''))
sales_as_floats = []
total_sales = 0
for string in removed_sign:
  floats = float(string)
  sales_as_floats.append(floats)
for num in sales_as_floats:
  total_sales += num
print(total_sales)

thread_sold_split = []
for thread in thread_sold:
  threads = thread.split('&')
  for thread in threads:
   thread_sold_split.append(thread.split(','))

# making the list of lists into one flat list
thread_sold_split_flat = [one_list for lists in thread_sold_split for one_list in lists]
print(thread_sold_split_flat)
def colour_count(thread):
  count = 0
  for colour in thread_sold_split_flat:
     if colour == thread:
      count += 1
  return count
print(colour_count('white'))

colours = ['red','yellow','green','white','black','blue','purple']
for colour in colours:
 print('{0} threads is how many of {1} threads were sold today'.format(colour_count(colour),colour))

import random
random_list = [random.randint(1,100) for i in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)

# using matplotlib and pyplot to plot a graph with x and y values
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random
numbers_a = range(1,13) #x
numbers_b = random.sample(range(1000),12) #y
plt.plot(numbers_a,numbers_b)
plt.show()

# returning specified number of decimal places
from decimal import Decimal
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)
four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

#zipped dictionary - dict comprehension
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}
print(zipped_drinks)

# editing dictionaries and dict comprehension
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}
plays.update({'Purple Haze':1})
plays['Respect'] = 94
library = {'The Best Songs':plays, 'Sunday Feelings': {}}
print(library)
# accessing values using keys from dictionaries
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['earth'])
print(zodiac_elements['fire'])

# using .get() to find values from keys, if no value or key is found then you can return what you indicate in the function
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get('teraCoder')
print(tc_id)
stack_id = user_ids.get('superStackSmash',100000 )
print(stack_id)

# Video game: using dictionaries to show how health points increase after taking elements from the inventory (dictionary)
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop('stamina grains',0)
health_points += available_items.pop('power stew',0)
health_points += available_items.pop('mystic bread',0)
print(available_items,health_points)

# only returning keys from a dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

# accessing only values from a dictionary
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for value in num_exercises.values():
  total_exercises += value
print(total_exercises)

# accessing dictionaries using for loops and .item() returning both key and value

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for role, value in pct_women_in_occupation.items():
  print('Women make up', str(value), 'percent of', role +'\'s')


# using dictionaries to return tarot cards drawn and put them into a new dictionary of drawn cards. Then using for iteration to print string with arguements
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}
spread['past'] = tarot.pop(13)
spread['present'] = tarot.pop(22)
spread['future'] = tarot.pop(10)
for key, value in spread.items():
  print('Your {key} is the {value} card.'.format(key=key,value=value))

# making a scabble scorer with dictionaries, dict comprehension, loops, lists and functions

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters,points)}

letter_to_points[' '] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return point_total
print('Your word score is:',score_word('brownie'.upper()))
#-----
players_to_Words = {'player1':['BLUE','TENNIS','EXIT'], 'wordNerd': ['earth','eyes', 'machine'], 'Lexi Con': ['eraser','belly', 'husky'], 'Prof Reader':['zap','coma','period']}

player_to_points = {}
for player, words in players_to_Words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word.upper())
  player_to_points[player] = player_points
print(player_to_points)


# opening files and reading them using 'with', open(), and read()

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

# single lines of tests in files using .readlines()
with open('how_many_lines.txt') as lines_doc:
  for lines in lines_doc.readlines():
    print(lines)

# taking one single line from the text
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
print(first_line,second_line)

# wiritng in a file using open('','w') and .write()
with open('bad_bands.txt', 'w') as bad_bands_doc:
 bad_bands_doc.write('Def Leapords')
# appending lines to a file without deleting the file
with open('cool_dogs.txt','a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy\n')

# using with instead of not using it and opening the file and having to use .close() is avoided

with open('fun_file.txt') as close_this_file:
setup = close_this_file.readline()
punchline = close_this_file.readline()
print(setup)

# comma separated values  = CSV files, reading CSV files
with open('logger.csv') as log_csv_file:
  read = log_csv_file.read()
print(read)

# reading a csv file with importing csv library to use .dictreader() function
import csv
with open('cool_csv.csv') as cool_csv_file:
 csv_file_dict = csv.DictReader(cool_csv_file)
 for row in csv_file_dict:
  print(row["Cool Fact"])

# Reading different CSV files, using with, open(), import csv, csv,DictReader() and list comprehension to print rows of ISBN
import csv
with open('books.csv') as books_csv:
 books_reader = csv.DictReader(books_csv,delimiter = '@')
 isbn_list = [row['ISBN'] for row in books_reader]
print(isbn_list)

# writing a CSV file using .DictWriter() to access field names, writeheader() to writing headers through writing fields passed through fieldnames, writerow() writes each line from dictionary to CSV file
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('logger.csv','w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv,fieldnames=fields)
  log_writer.writeheader()
  for line in access_log:
    log_writer.writerow(line)

# json files, using json.load() to parse data, creating a python dicitonary allowing us to interact with the data. printing the variable sotring the load file and keying it at the end
import json
with open('message.json') as message_json:
  message = json.load(message_json)
print(message['text'])

# converting python files or data into Json files
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open('data.json','w') as data_json:
  json.dump(data_payload,data_json)
  

# opening csv files, editing them and rewriting using csv and json to read, edit, communicate with json and return the edited csv file
import csv

compromised_users = []
with open('passwords.csv') as password_file:
# read_file =  password_csv.read()
#print(read_file) # to see headers
 password_csv = csv.DictReader(password_file)
 for row in password_csv: 
    compromised_users.append(row['Username'])
 print(compromised_users)

with open('compromised_users.txt','w') as compromised_user_file:
  for users in compromised_users:
    compromised_user_file.write(users)
print(compromised_user_file)

import json
with open('boss_message.json','w') as boss_message:
  boss_message_dict = {'recipient':'The Boss','message':'Mission Sucess'}
  json.dump(boss_message_dict,boss_message)

with open("new_passwords.csv",'w') as new_passwords_obj:
  slash_null_sig = """_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/ """
  new_passwords_obj.write(slash_null_sig)

# type() function tells us the type of data we are looking at
# a class is a template for a data type
class Facade:
  pass
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

# defining a class and creating a method inside the class
class Rules:
  def washing_brushes(rule):
    return "Point bristles towards the basin while washing your brushes."

# defining methods in classes with arguements - giving back the area from circle radius
class Circle:
  pi = 3.14
  def area(self,radius):
    return self.pi * radius ** 2
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area((11460/2))
print(pizza_area,teaching_table_area,round_room_area)

# dunder methods or using constructors, __init__() method is used to initialise a newly created object
class Circle:
  pi = 3.14
  # constructor here:
  def __init__(self,diameter):
   print('New circle with diameter: {}'.format(diameter))
Teaching_table = Circle(36)

# class is a schematic/template for data type and an object is an instance for a class
# looking at instance variable
class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# hasattr() will tell us true of false if an object has been given an attribute
# getattr() this will give us actual value of an attribute (this tells us that dictionaries and integers do not have this function)
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  if hasattr(element,'count'):
   print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# self key word refers to the object and not the class being called
# object orientated programmes, writing classes to structure the data that we need and writing methods that will interact with the data in a meaningful way
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  def circumference(self):
    return 2 * self.pi * self.radius 

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print('Circumference of the medium Pizza is:',medium_pizza.circumference())
print('Circumference of the teaching table is:',teaching_table.circumference())
print('Circumference of the round room is:',round_room.circumference())


#using the dir() function to show an objects attributes during run time
def this_function_is_an_object(x):
  print('anything I like')
print(dir(this_function_is_an_object))


# __repr__() gives us the string representation of a class, it only takes one parameter and must return a string

#   def __repr__(self):
#    return 'Circle with radius {radius}'.format(radius=self.radius)
  
  
#medium_pizza = Circle(12)
#teaching_table = Circle(36)
#round_room = Circle(11460)

#print(medium_pizza)
#print(teaching_table)
#print(round_room)

# object orientated programming
class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score

roger = Student('Roger van der Weyden',10)
sandro = Student('Sandro Botticelli',12)
pieter = Student('Pieter Bruegel the Elder',8)
pieter.add_grade(Grade(100))

##### Basta fazoolin project
class Menu:

  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return 'the {name} menu is available from {start_time} to {end_time}'.format(name=self.name,start_time=self.start_time,end_time=self.end_time)

  def calculate_bill(self,purchased_items):
    bill = 0
    for items in purchased_items:
      if items in self.items:
        bill += self.items[items]
    return bill

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return 'Franchise address is {address}'.format(address = self.address)

  def available_menus(self,time):
    available_menus = []
    self.time = time
    for menu in self.menus:
      if time <= menu.end_time and time >= menu.start_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

brunch = Menu('brunch',{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},1100, 1600)
early_bird = Menu('Ealy bird',{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},1500,1800)
dinner = Menu('Dinner',{
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},1700,2300)
kids = Menu('kids',{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},1100,2100)

#print(brunch)
#print(brunch.calculate_bill(['pancakes','home fries','coffee']))
#print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

menus = [brunch,early_bird,dinner,kids]
flagship_store = Franchise("1232 West End Road",menus)
new_installment = Franchise("12 East Mulberry Street",menus)

#print(flagship_store.available_menus(1700))

Basta = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take A' arepa",arepas_items,1000,2000)
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

arepa = Business("Take a' Arepa",[arepas_place])

print(arepa.franchises[0])

## returning unique letter count using a function
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  count = 0
  for letter in letters:
   if letter in word:
    count += 1
  return count
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


# returning how many times the letter occurs in the word
def count_char_x(word,x):
  count = 0
  for letter in word:
   if letter == x:
    count += 1
  return count
print(count_char_x("mississippi", "s"))

# returnign how many times x is in word, by splitting the word by x . len(split) gives us the number of occurences the split is found in the word, -1 makes sure and extra sbstring is not added and the actual ammount of 'delimiters' or aka the substring
def count_multi_char_x(word,x):
 split =  word.split(x)
 return (len(split)-1)
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# returning the characters in the word that are between start and end, first I find the positiions of start and end and give back the sliced 'list' of the word between those points. +1 to make sure we dont give back the first charcater
def substring_between_letters (word,start,end):
  starts = word.find(start)
  ends = word.find(end)
  if starts > -1 and ends > -1:
    return(word[starts+1:ends]) 

print(substring_between_letters("apple", "p", "e"))

# returning true or false if the words in the scentence is smaller or greater than x
def x_length_words(sentence,x):
  word = sentence.split(' ') 
  for letters in word:
   if len(letters) < x:
    return False
  return True
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

# returning true or false when name is withing a sentence
def check_for_name(sentence,name):
  sentence = sentence.lower()
  name = name.lower()
  if sentence.find(name) > 0:
    return True
  else:
    return False
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))

# printing every other letter from element 1 of the string
def every_other_letter(word):
  remaining_letters = []
  remaining_letters.append(word[::2])
  return(remaining_letters)
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# another way to do the same
def every_other_letter(word):
  return word[::2]
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))

# reversing strings
def reverse_string(word):
  reversed_string = ''
  for i in range(len(word)-1,-1,-1):
   reversed_string += word[i]
  return reversed_string
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))

# the same with simpler code

def reverse_string(word):
  return word[::-1]
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))


#returning the sum of all the values in a dictionary by accessing values only
def sum_values(my_dictionary):
  sum_of_values = 0
  for values in my_dictionary.values():
   sum_of_values += values
  return sum_of_values
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# returning values of only even keys using .items()
def sum_even_keys(my_dictionary):
  sum_of_even_values = 0
  for key,values in my_dictionary.items():
    if key % 2 == 0:
        sum_of_even_values += values
  return sum_of_even_values
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# editing values by defining the keys in the dicitionary and using [key] in the dictionary variable and chaning the value of the key
def add_ten(my_dictionary): 
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# returning values that are also keys, searching for each value in the dictionary and comparing the values in the dictionaries against keys
def values_that_are_keys(my_dictionary):
  values = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      values.append(value)
  return values
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# using float('-inf') giving us negative infinity, we can use this to compare and see what the biggest key/value is and return it
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# returning a zipped dicitonary from manipulating a list
def word_length_dictionary(words):
  key = []
  values = []
  for word in words:
     values.append(len(word))
     key.append(word)
  dictionary = {key:value for key,value in zip(key,values)}
  return dictionary
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# counting the number of items in a list and returning a dictionary
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}

## returning unique values in a dictionary into a list
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2

## returning first letter and the number of values with that key represented as a first letter
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}

# playing with updating methods in classes
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    

    def control_bot(self,new_speed,new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction
    def adjust_sensor(self,new_sensor_range): 
      self.sensor_range = new_sensor_range
robot_1 = DriveBot()

robot_1.motor_speed = 10
robot_1.direction = 180
robot_1.sensor_range = 20
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)
