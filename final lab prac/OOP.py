class Number:
    def __init__(self, value):
        self.__value = value

    #Getter method for value
    @property
    def value(self):
        return self.__value
    
    #Setter methofd for value
    @value.setter
    def value(self, new_value):
        self.__value = new_value

    #Getter for sign, parity, and primality
    #1. sign
    @property
    def sign(self):
        if self.__value > 0:
            return "positive"
        elif self.__value < 0:
            return "negative"
        else:
            return "zero"
        
    #2.parity
    @property
    def parity(self):
        return "even" if self.__value % 2 == 0 else  "odd"
    
    #3. primality
    @property
    def primality(self):
        if self.__value <= 1:
            return "neither"
        for i in range(2, int(abs(self.__value)**0.5) + 1):
            if self.__value % i == 0:
                return "composite"
        return "prime"
    

    # dunder str how to show your object as a string
    def __str__(self):
        return(f"value: {self.value}, Sign: {self.sign}, "
            f"Parity: {self.parity}, Primality: {self.primality}")
    
#Get input from the user
try:
    user_input = int(input("Enter a number: "))
    num = Number(user_input)
    print(num)

    #ask if user wants to modify value
    while True:
        response = input("\nChange the value? (y/n) ").strip().lower()
        if response == 'y':
            new_value = int(input("ENter new value: "))
            num.value = new_value 
            print(num)
        elif response == 'n':
            print("Thank you!")
            break
        else:
            print("Enter a valid response (y/n).")
except ValueError:
    print("INvalid input. Pkease enter a valid integer.")

