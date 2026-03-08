'''
Prog.12
Description
Unique Product Purchase Analyzer
Problem Description
An e-commerce company records the products purchased by customers during a sale. However, some products appear multiple times in the purchase list because multiple customers bought them.

The company wants to generate a list of unique products that were purchased only once during the sale.

You are given a list of product names representing purchases. Your task is to return a list containing products that appear exactly once in the list.

Input
A list of product names.

Example

["Laptop","Mouse","Keyboard","Mouse","Monitor","Keyboard","Tablet"]
Output
["Laptop","Monitor","Tablet"]

'''

class Solution:
    def unique_products(self, products):
        result = []
        count={}
        for item in products:
            count[item]=count.get(item, 0)+1
        for item in products:
            if count[item]==1:
                result.append(item)

        return result