menu = {
    'Hamburger' : 250,
    'Cheese Burger' : 300,
    'Big Mac' : 540,
    'McChicken' : 350,
    'French Fries' : 230,
    'Salad' : 15,
    'Coca Cola' : 150,
    'Sprite' : 150,
    'Happy Meal': ['Cheese Burger', 'French Fries', 'Coca Cola'],
    'Best Of Big Mac': ['Big Mac', 'French Fries', 'Coca Cola'],
    'Best Of McChicken': ['McChicken', 'Salad', 'Sprite']
}

def advanced_calories_counter(orders):
    item_prompt = '{} not found'
    cal = 0

    for i in orders:
        if i not in menu:
            return item_prompt.format(i)
        elif type(menu[i]) == list:
            for j in menu[i]:
                if j not in menu:
                    return item_prompt.format(j)
                else:
                    cal +=menu[j]
        else:
            cal += menu[i]
            
    return cal