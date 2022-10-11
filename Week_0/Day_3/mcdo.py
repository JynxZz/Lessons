menu = {
    'Hamburger' : 250,
    'Cheese Burger' : 300,
    'Big Mac' : 540,
    'McChicken' : 350,
    'French Fries' : 230,
    'Salad' : 15,
    'Coca Cola' : 150,
    'Sprite' : 150
}

def poor_calories_counter(item1="", item2="", item3=""):
    item_prompt = '{} not found'
    items = [item1, item2, item3]
    cal = 0

    for i in items:
        if i not in menu:
            return item_prompt.format(i)
        else:
            cal += menu[i]
            
    return cal