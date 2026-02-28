class Solution:
    
    def calculate_bill(self, units):
        ## Write your code here along with return keyword
        bill=0
        if(units<=100):
            bill=units*5
        elif(100<units<=300):
            bill=100*5+((units-100)*7)
        else:
            bill=(100*5)+(200*7)+((units-300)*10)
        return bill
