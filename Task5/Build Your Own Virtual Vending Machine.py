# -------------------------------
# Virtual Vending Machine
# -------------------------------

# Item class to represent each product
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Vending Machine class
class VendingMachine:
    def __init__(self):
        # Inventory with 3 sample items
        self.inventory = {
            1: Item("Coke", 50, 5),
            2: Item("Chips", 30, 5),
            3: Item("Water", 20, 5)
        }
        self.cart = []  # User's selected items
    
    def show_items(self):
        """Display all available items with stock"""
        print("\nAvailable Items:")
        for idx, item in self.inventory.items():
            print(f"{idx}. {item.name} - ₹{item.price} (Stock: {item.stock})")
    
    def add_to_cart(self, choice):
        """Add an item to the cart if available"""
        if choice in self.inventory:
            item = self.inventory[choice]
            if item.stock > 0:
                self.cart.append(item)
                item.stock -= 1
                print(f"{item.name} added to cart!")
            else:
                print("Sorry, out of stock.")
        else:
            print("Invalid choice.")
    
    def checkout(self):
        """Handle payment and dispense items"""
        if not self.cart:
            print("Cart is empty!")
            return
        
        total = sum(item.price for item in self.cart)
        print(f"\nTotal cost: ₹{total}")
        
        inserted = 0
        while inserted < total:
            try:
                money = int(input("Insert money: "))
                if money <= 0:
                    print("Invalid amount.")
                    continue
                inserted += money
                print(f"Inserted so far: ₹{inserted}")
            except:
                print("Invalid input! Enter a number.")
        
        change = inserted - total
        print("\nDispensing items:")
        for item in self.cart:
            print(f"- {item.name}")
        
        if change > 0:
            print(f"Returning change: ₹{change}")
        
        self.cart.clear()  # Empty the cart after purchase

# CLI Menu for Vending Machine
def run_vending_machine():
    vm = VendingMachine()
    while True:
        print("\n--- Vending Machine Menu ---")
        print("1. Show Items")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            vm.show_items()
        elif choice == "2":
            try:
                item_choice = int(input("Enter item number: "))
                vm.add_to_cart(item_choice)
            except:
                print("Invalid input!")
        elif choice == "3":
            vm.checkout()
        elif choice == "4":
            print("Exiting Vending Machine")
            break
        else:
            print("Invalid choice!")

# Run the vending machine
run_vending_machine()
