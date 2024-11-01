global menu      
import math
import pyfiglet
title = pyfiglet.figlet_format("BIL SHOP", font = "5lineoblique" )
# python3 -m pip install --upgrade pip
print(title)
                 # 10 products for people to choose from
menu={"apples":3.45,
      "bananas":4.34,
      "avocados":6.34,
      "egg":4.30,
      "bell peppers": 3.22,
      "carrots":4.32,
      "broccoli":5.44,
      "garlic":0.13,
      "lemons":0.45,
      "onion":3.86,
     }
     
currency_dict  =  {
    "dollar" : 1.31,
    "euro" : 1.31,
    "cad" : 1.80,
    "yen" : 194.87,
    "HKD":  10.17 }




global item_picked        #array which holds all the items customers picked
item_picked=[]


def num_item():           # Ask the customer how many item they want to buy + input validation
    while True:
        try:
            global num_of_product
            num_of_product=int(input("How many product do you want to buy: "))
        except ValueError:
            print("Please input number only! ")
        else:
            break








def choose_item():           # Ask the customer to choose the item+input validation
    while True:
        try:
            choose=str(input("Enter the name of product: ")).lower()
            if choose not in menu:
                raise TypeError
        except TypeError or ValueError:
            print("Please only type in the name of product from the menu")
        else:
            break #for picking item + validation
    item_picked.append(choose)


       




   
def sum_price():         # Sum price for all items picked +validation
    global total_price  
    total_price=0
    for i in range(0,len(item_picked)):
        PriceForEachItem=menu.get(item_picked[i])
       
        total_price=total_price+PriceForEachItem
       
    return (total_price)
 
print(menu)     #where the code starts to run
num_item()
for i in range (0,int(num_of_product)):
    choose_item()
sum_price()  


print(currency_dict)  #ask user to input the currency they want to pay with
while True:
    try:
        chosen_currency=input("Choose the currency you want to pay with ")
        if chosen_currency not in currency_dict:
            raise TypeError
    except TypeError:
      print("Please only type in the currency in the list")
    else:
         break


import requests
import os


laeLong = -0.067007
laeLat = 51.604252


# Python 3 program for the
# haversine formula
def haversine(lat1, lon1, lat2, lon2):


    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0


    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0


    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


while True:


  try:
    postcode_raw = input("What's your postcode? ")
 
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json() # use api to access info of the postcode entered


    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    area = postcode_resp['result']['admin_district']


  except KeyError: # for if the postcode doesnt exists
    print('Enter a valid postcode ')
 
  else:
    print(f"You live in {area}.\n")
    break




distance = round(haversine(laeLat,laeLong,latitude,longitude),3)


if distance <= 5:
  deliveryPrice = 0
  print('free shipping')
elif distance <= 15:
  deliveryPrice = 3
  print('delivery price is 3 pounds')
elif distance <= 30:
  deliveryPrice = 5
  print('delivery price is 5 pounds')
else:
  deliveryPrice = 7
  print('delivery price is 7 pounds')




total_price = total_price + deliveryPrice
 










def exchange(chosen_currency,total_price):
    if chosen_currency in currency_dict  :


        FP = float(total_price)* currency_dict[chosen_currency]
        FP = round(FP,3)
        print(f"your total price is {FP} {chosen_currency}")
        return FP


    else:
        print(f"{chosen_currency} is not an option")
   


if total_price<=10:
    print("not enought")
elif total_price >=100:
    print("too much")
else:
    exchange(chosen_currency,total_price)


