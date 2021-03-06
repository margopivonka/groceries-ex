# groceries.py

#from pprint import pprint

#this is a list composed of dictionaries -- the {} give it away
    #
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)


# TODO: write some Python code here to produce the desired output



print("----------------------")

#print("THERE ARE 20 PRODUCTS:")
#instead of hard coding the number 20, count the actual number of products in the list

print("THERE ARE", len(products), "PRODUCTS:")
#print(f"THERE ARE {len(products)} PRODUCTS:")
#print("THERE ARE " + str(len(products)) + " PRODUCTS:")
    #to concatinate you have to convert the list to a string

print("----------------------")


def sort_by_name(any_product):
    return any_product["name"]
sorted_products = sorted(products, key=sort_by_name)



for product in sorted_products:
   # print(product["name"],product["price"])
    #print("+ All-Seasons Salt ($4.99)")
    #price_usd = product["price"]
    #price_usd = "${0:.2f}".format(product["price"])
    price_usd = " (${0:.2f})".format(product["price"])
    
    print("+ " + product["name"] + price_usd)

departments = []

for product in products:
    #print(product["department"])
 
    if product["department"] not in departments:
        departments.append(product["department"])
        #conditionally appends departments to department list

department_count = len(departments)

print("----------------------")
print("THERE ARE "+str(department_count) + " DEPARTMENTS:")
print("----------------------")

departments.sort()
#sort departments alphabetically

for d in departments:
    matching_products = [product for product in products if product["department"] == d]
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = " products"
    else:
        label = " product"
    print(d.title() + " (" + str(matching_products_count) + label + ")") 
    #prints department names in title format

