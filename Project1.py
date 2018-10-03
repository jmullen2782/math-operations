'''
Created on Oct 2, 2018

@author: jenniemullen
'''
name= input('Please enter your name')
phonenumber= input('Please enter your phone number')
product = input('Please enter name of the product you would like to purchase')
price= float(input('Please enter price of item'))
quantity=float(input('Please enter quantity of purchase'))

subtotal=price*quantity
tax= price*.06
total= subtotal+tax

print(name)
print(phonenumber)
print('Purchase Information:')
print(product)
print('Qty:', quantity)
print('Price:', price)
print('Subtotal:', subtotal)
print('Tax:', tax)
print('Total:', total)
                                 

