DSLR_camera_cost = 30000

# Percentages should be in float
SGST = 14 / 100
CGST = 14 / 100


print("------- Welcome to DSLR CAMERA STORE--------")
print("------Each DSLR Camera cost : 30,000 INR ---------")

#no.of items required for a costumer
required_items = int(input("Enter the number of cameras you want to buy: "))
 
# Apply discount based on quantity
if 2 <= required_items <= 5:
    discount = 5 / 100
elif 6 <= required_items <= 10:
    discount = 10 / 100
elif 11 <= required_items <= 20:
    discount = 18 / 100
elif 21 <= required_items <= 40:
    discount = 24 / 100
elif required_items >= 41:
    discount = 33 / 100
else:
    discount =  2 / 100

# Calculations
DSLR_total_cost = required_items * DSLR_camera_cost
DSLR_SGST = DSLR_total_cost * SGST
DSLR_CGST = DSLR_total_cost * CGST
DSLR_discount_amount = DSLR_total_cost * discount

#total_cost
total_cost = DSLR_total_cost + DSLR_SGST + DSLR_CGST - DSLR_discount_amount

# Output
print("------------ Billing Summary --------------------")
print("     Total Camera Cost          : ₹",DSLR_total_cost)
print("     SGST (14%)                 : ₹",DSLR_SGST)
print("     CGST (14%)                 : ₹",DSLR_CGST)
print("     Discount Applied(" ,int(discount*100),"%)     : ₹",DSLR_discount_amount)
print("-------------------------------------------------")
print("     Total Payable Amount       : ₹",total_cost)
print("-------------------------------------------------")
print("~~~~~~~~~~    THANK_YOU for shopping with us ! VISIT_AGAIN    ~~~~~~~~~~")