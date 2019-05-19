"""You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1."""

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    fivec_needed = rupees_to_make//5 
    if(fivec_needed<=no_of_five):
        five_needed = fivec_needed
    else:
        five_needed=no_of_five
    
    if(rupees_to_make==5*five_needed):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", 0)
    else:
        one_needed=rupees_to_make-(5*five_needed)
        if(one_needed<=no_of_one):
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
make_amount(19,3,3)
