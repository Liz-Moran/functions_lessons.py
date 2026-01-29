def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print(" - Add", arg)
    for key, value in kwargs.items():
        print(" -Add", key, ":", value)

print(tea_order("Alice", "chamomile"))
print(tea_order("Bob","black", milk ="oat"))
print(tea_order("Tony", "black", milk ="oat", sweetner = "honey"))


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_sqaures(*args): 
    sum = 0 #Intialize sum to 0
    for num in args: #Iterate through each argument
        sum+= num ** 2 #Square the number and add it to the sum
    return sum 

print(sum_sqaures(1,2,3)) #Output: 14
#1st time through: sum = 0 +1^2 = 1
#2nd time: sum = 1 + 2^2 = 5
#3rd time: sum = 5 + 3^2 = 14

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0 #Intializes total to zero
    for num in args: #Interate through each argument
        total += abs(num) #Add the absoulte value of the number
    return total
#1st time: total = 0 +abs(-1)=1
#2nd time: total = 1 +abs(-2) =3
#3rd time: total= 3 + abs (-3)=6
print(absolute_sum(-1,-2,-3))#Output: 6



# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum_numbers = 0
    for arg in args:
        sum_numbers += arg
    return f"{name}, the sum of your numbers is {sum_numbers}"
print(personal_numbers("Lizbeth", 1,2,3,4))
print(personal_numbers("Jocelyn", 10, 30,40,1))
