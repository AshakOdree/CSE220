class FinalQ:
    def print(self,array,idx=0):
        if(idx==len(array)):
            return 0

        if(idx>=0 and idx<=len(array)-1):
            profit = self.calcProfit(array[idx])
            print(f"{idx+1}. Investment: {array[idx]}; Profit: {profit}")
            return self.print(array,idx+1)
        else:
            print("Please enter valid index.")
            return

    def calcProfit(self,investment):
        coUNt= 0
        if investment<=25000:
            return 0

        if 100000 >= investment > 25000:
            return 45 + self.calcProfit(investment - 1000)

        elif 100000 > investment<=101000:
            return 8+self.calcProfit(investment-100)

        else:
            return 80+self.calcProfit(investment-1000)



array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)