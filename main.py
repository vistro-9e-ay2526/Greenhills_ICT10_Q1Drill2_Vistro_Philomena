# Working with Numabers
from pyscript import display, document

#def greetings(e):     # creating function
    #username = document.getElementById('inputN').value   #getting a value from a textbox
    #display(f'Hello {username}!', target='output')   

def add_numbers(e):
    document.getElementById('output').innerHTML = " "    # clearing the previous output
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    sum = no_1 + no_2

    display(f'The sum of {no_1} and {no_2} is {sum}', target='output')

def subtract_numbers(e):
    document.getElementById('output').innerHTML = " "
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    difference = no_1 - no_2

    display(f'The difference of {no_1} and {no_2} is {difference}', target='output')

def multiply_numbers(e):
    document.getElementById('output').innerHTML = " "
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    product = no_1 * no_2

    display(f'The product of {no_1} and {no_2} is {product}', target='output')

def raise_numbers(e):
    document.getElementById('output').innerHTML = " "
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    power = no_1 ** no_2

    display(f'The power of {no_1} and {no_2} is {power}', target='output')

def divide_numbers(e):
    document.getElementById('output').innerHTML = " "
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    quotient = no_1 / no_2

    display(f'The quotient of {no_1} and {no_2} is {quotient}', target='output')

def floordivide_numbers(e):
    document.getElementById('output').innerHTML = " "
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    quotient = no_1 // no_2

    display(f'The quotient of {no_1} and {no_2} is {quotient}', target='output')

def modulo_numbers(e):
    document.getElementById('output').innerHTML = " "
    no_1 = float(document.getElementById('num1').value)
    no_2 = float(document.getElementById('num2').value)
    remainder = no_1 % no_2

    display(f'The remainder of {no_1} and {no_2} is {remainder}', target='output')