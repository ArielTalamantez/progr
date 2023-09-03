# Program Name: Lab2.py (use the name the program is saved as)
# Course: IT1114/Section w04
# Student Name: Ariel Talamantez
# Assignment Number: Lab# 2
# Due Date: 09/03/ 2023
# Purpose: What does the program do ? The purpose of this code is to calculte some numbers for for pizza sales at the KSU hackathon.
#The code will give a list of outputs similar to a reciept.
# List Specific resources used to complete the assignment
import math

#Inputs
Pizza_Ordered = float(input("How many people want pizza: "))
Salad_Ordered = float(input("How many people want salad: "))

#pizza cost
a = Pizza_Ordered * 3
b = a / 12
c = math.ceil(b) * 15.99
f = .07

#salad cost
d = Salad_Ordered * 7.99

#Discount for pizza
if Pizza_Ordered > 10:
    Discount = (c * .15)


#Discount for salad
if Salad_Ordered > 10:
    T_Discount = (d * .15)

if Pizza_Ordered == 11:
    Discount = 0


if Pizza_Ordered and Salad_Ordered > 10:
    Discount = Discount + T_Discount
if Pizza_Ordered and Salad_Ordered > 10:
    print("Discount $:", Discount)
else: print("Discount $:", Discount)


#else:
 #   print("Discount :", Discount)



#total before discount
total_BD = c + d

#Delivery_fee


Delivery_fee = .07 * total_BD
if Delivery_fee < 20:
    Delivery_fee = 20

#Outputs

print("Pizzas ordered :", math.ceil(b))
print("Pizza cost $: ",c)
print("Salad Cost $: ",d)
print("Total before dis $: ",total_BD)
print("Delivery fee : ", Delivery_fee)
print("Total Amount Due : ", total_BD + Delivery_fee - Discount)

