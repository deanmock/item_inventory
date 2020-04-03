#main.py
from shop import SumatranBeans, Shopkeeper

def main():
    shop = SumatranBeans(100)
    shopkeeper = Shopkeeper()

    while True:
        print("""
        ====== COFFEE SHOP INVENTORY APP =======
        1. Display available stock
        2. Deplete stock
        3. Replenish stock
        4. Exit
        """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displaystock()
        
        elif choice == 2:
            shopkeeper = shop.SaleMade(shopkeeper.depleteStock())

        elif choice == 3:
            shopkeeper = shop.addStock(shopkeeper.replenishStock())
     
        elif choice == 4:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        



if __name__=="__main__":
    main()