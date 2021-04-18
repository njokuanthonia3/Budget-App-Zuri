class Budget:
    def __init__(self, categories, balances):
        self.categories = categories
        self.balances = balances
        

    def deposit(self, category, amount):
        index = self.categories.index(category)
        self.balances[index] += amount
        print("Deposit Successful!")
        print('New balance is ',self.balances[index] )

        

    def withdraw(self, category, amount):
        index = self.categories.index(category) 
        self.balances[index] -= amount
        print("Withdrawal Successful")
        print('New balance ', self.balances[index])

    def get_balance(self, category):
        try:        
            index = self.categories.index(category)
            return self.balances[index]
        except:
            
            print("Error: Category not found")
            

    def transfer(self, source_category, amount, destination_category):        
        source_index = self.categories.index(source_category) 
        destination_index = self.categories.index(destination_category)
           
        self.balances[source_index] -= amount   
        self.balances[destination_index] += amount
         
        print("New balance for ", source_category, "is ", self.balances[source_index])


        




cat = ['food', 'clothing', 'entertainment']
bal = [1500, 1500, 0]
bjet = Budget(cat, bal)
print(bjet.get_balance('foood'))
print(bjet.deposit('food',500))
print(bjet.withdraw('food', 350))
print(bjet.transfer('food', 200, 'clothing'))