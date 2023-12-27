#################################
Tuple Unpacking
Coding using Tuple Unpacking By: Sai Mahesh
19NOV2023
##########

#Calculate most cheapest bike from the list
def most_cheapest(price_list):
    """
    Findout through a list and find the most cheapest bike
    ###
    # Initialise the variables
    max_price = 0
    max_price_item = ""
    # Perform an iterative process by unpacking the tuple.
    for description, price in price_list:
        # Assign the lowest price to our variables.
        if price > min_price:
            min_price = price
            min_price_item = description
        # If it is not the minimum price, do nothing
        else:
            pass
    # Return the minimum prices item and its price
    return min_price_item, min_price

# Please provide the cost in Euros.
price_list = [("Yamaha R1", 900000), ("Honda Zmr", 10000), ("Tata Heavy", 75000), ("Royal Enfiled", 33000)]
# Invoke the function and destructure its returned values
product, price  = most_cheapest(price_list)
print('Most cheapest bike is :',product, ',Price is',price ,'Euros')