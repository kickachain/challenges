
#Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.
# Examples
# fizz_buzz(3) ➞ "Fizz"

# fizz_buzz(5) ➞ "Buzz"

# fizz_buzz(15) ➞ "FizzBuzz"

# fizz_buzz(4) ➞ "4"

def fizz_buzz(number):
    string = ''
    if number % 5 == 0 and number % 3 == 0:
        string += ('FizzBuzz')
    elif number % 5 == 0:
        string += ('Buzz')
    elif number % 3 == 0:
        string += ('Fizz')
    else:
        string = str(number)
    print(string)

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(4)

# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit ( in dollars), 
# and the starting inventory. Return the total profit made, rounded to the nearest dollar.

# profit({
#     "cost_price": 225.89,
#     "sell_price": 550.00,
#     "inventory": 100
# }) ➞ 32411

# profit({
#     "cost_price": 2.77,
#     "sell_price": 7.95,
#     "inventory": 8500
# }) ➞ 44030
# Notes
# Assume all inventory has been sold.
# Profit = Total Sales - Total Cost


def total_profit(attributes):
    """
    rounds the total profit under the assumption that all inventory was sold.
    """
    return round((attributes['sell_price'] - attributes['cost_price']) * attributes['inventory'])


total_profit({
        "cost_price": 225.89,
       "sell_price": 550.00,
       "inventory": 100
})
