def create_inventory(items):inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventorydef add_items(inventory, items):for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventorydef decrement_items(inventory, items):for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            if inventory[item] < 0:
                inventory[item] = 0
    return inventorydef remove_item(inventory, item):if item in inventory:
        del inventory[item]
    return inventoryef list_inventory(inventory):return [(item, quantity) for item, quantity in inventory.items() if quantity > 0]

