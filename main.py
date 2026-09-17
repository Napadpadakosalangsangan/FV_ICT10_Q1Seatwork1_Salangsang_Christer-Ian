from pyscript import document, display

# String
name = "Christer Ian Salagsang"

# Integer
age = 16 

# Float
he1ght = 170.18

# List
countries_to_visit = ["France", "Italy", "Netherlands"]

# Boolean
student_type = False

# Dictionary
favorites = {'color':'Light Blue', 'Car_brand':'a', 'shoe_size':'9.5 US', 'Best_friend':'Ethan'}

# Set
fruits = set(["Apples", "Oranges", "Watermelons"])

# Tuple
day_ranks = ("Friday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday", "Monday")

display(f"My name is {name}. I am currently {age} years old, with a height of {he1ght}cm. In the future, I would like to visit the following countries: {str(countries_to_visit)}. You think I'm a new student? {student_type}! Some of my preferences are: {favorites}, and my favorite fruits are {fruits}. Based on my personal experiences, I would rank the days in the week from best to boring in this order: {day_ranks}.", target="div1")



def add(e):

  num1 = float(document.getElementById("num1"))
  num2 = float(document.getElementById("num2"))

  document.GetElementById("adding").innerTEXT = num1 + num2

  


