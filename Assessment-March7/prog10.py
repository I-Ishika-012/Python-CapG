'''
Prog.10
Description
 Product Stock Shortage Report
Problem Description
An inventory system stores product quantities in a dictionary.

A product is considered low in stock if its quantity is less than 10.

Your task is to return a list of all product names that are low in stock.

Input
Dictionary where:

Key → Product Name

Value → Quantity

Output
List of product names with stock < 10.
'''

class Solution:
    def low_stock_products(self, inventory):
        result = []
        for product_name, quantity in inventory.items():
            if quantity<10:
                result.append(product_name)
        return result