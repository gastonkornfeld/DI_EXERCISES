


# Exercise 1 : Built-In Functions
# Python has many built-in functions, and if you do not know how to use it, you can read document online.
# But Python has a built-in document function for every built-in functions.

# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function


def help_for_abs_int_and_raw_input():
    print(f"abs function: \n {help(abs)} \n int function:\n {help(int)}  \n raw_input:\n {help(input)}")


# help_for_abs_int_and_raw_input()



# Exercise 2: Currencies
# Recreate these results

class Currency():

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def same_currency(self, other):
        return self.currency == other.currency

    def __add__(self, other):
        try:
            self.same_currency(other)
        except:
            return self.amount + other
        else:
            if self.same_currency(other):      
                if isinstance(other, Currency):
                    new_value = self.amount + other.amount
                    return f"{new_value} {self.currency}"
                else:
                    return self.amount + other
            else: 
                return f"sorry cant add between <{self.currency}> and <{other.currency}>"

    def __iadd__(self, other):
        if isinstance(other, Currency):
            self.amount += other.amount
            return self.amount
        else:
            self.amount += other
            return self.amount

    def __repr__(self):
        return f" {self.amount} {self.currency}"

    def __int__(self):
        return self.amount

c1 = Currency("pesos", 1000)
c2 = Currency("pesos", 200)
c3 = Currency("dollar", 300)

c1 += 5
c1 += 5

print(Currency("c1",300) + c2)

# Hint : When you add 2 currencies, if they don’t have the same label raise an error
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>



