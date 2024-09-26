def make_pizza(*toppings,base):   # Multiple base not allowed only one * allowed
        print(toppings,base)
print("program started")
Harika =make_pizza("cheese","panner",base="Thin Crust")
Pavani =make_pizza("onion","corn",base="Crust")
print("program end")






# second method
def make_pizza1(*toppings, base):  # Multiple toppings allowed here because using two def functions
    print(toppings, base)

def make_pizza2(*toppings, base):   # star needs to start first
    print(toppings, base)


make_pizza1("cheese", "panner", base="Thin Crust")
make_pizza2("onion", "corn", base="Crust")
