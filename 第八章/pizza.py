def make_pizza(size, * toppings):
    """
    概述要制作的pizza
    """
    print('\nMaking a '+str(size) +
          ' pizza with the following toppings:')
    for topping in toppings:
        print('-'+topping)
