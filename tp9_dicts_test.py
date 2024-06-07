import unittest
from dicts import create_inventory, add_items, decrement_items, remove_item, list_inventory


class InventoryTest(unittest.TestCase):
    
    def test_create_inventory(items):
        
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
    
    def test_add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
    
    def test_decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory
    
    def test_remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventorydef list_inventory(inventory):
    return [(item, quantity) for item, quantity in inventory.items() if quantity > 0]
    
   
