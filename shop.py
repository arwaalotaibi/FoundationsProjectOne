####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

cupcake_shop_name = "Get Baked"
signature_flavors = ["tuna", "salmon", "red herring" ]
order_list = []
total = int()
def print_menu():
    """
        Print the items in the menu dictionary.
        """
    # your code goes here!
    print("Our menu:")
    for key in menu:
     print(key,"(KD %s )" % (menu[key]))

def print_originals():
    """
        Print the original flavor cupcakes.
        """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for n in original_flavors:
        print(n)
def print_signatures():
   print("Our signature flavor cupcakes (KD %s each):" % signature_price)
   for x in signature_flavors:
    print(x) 
    # your code goes here!
def is_valid_order(order):
  return order in menu or order in original_flavors or order in signature_flavors 

def get_order():
 order_list = []
 
 x = input("What's your order? (Enter the exact spelling of the item you want. Type exit to end order \n")
 while x != "exit":   
  if is_valid_order(x) == True :
    order_list.append(x)
  x =input()
 return order_list



def get_total_price(order_list):
   
   total = 0

   for n in order_list:
      if n in menu :
        total += menu[n]
      elif n in original_flavors:
        total += original_price
      elif n in signature_flavors:
        total += signature_price
  
   return total

def accept_credit_card(total):
  if total >= 5 :
    print("The order is eligible for credit card payment")
  elif total < 5:
    print("The order is not eligible for credit card payment")



def print_order(order_list):
  
    print()
    print("Your order is: ")
    for n in order_list:
        print(n)
    print("That'll be KD",get_total_price(order_list))
    accept_credit_card(get_total_price(order_list))
    print("Thank you for shoping at",cupcake_shop_name)
  


