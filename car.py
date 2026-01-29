class Car:
    """Represents a car in the dealership."""
    
    def __init__(self, car_id, brand, model, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.is_sold = False
    
    def display_info(self):
        """Display car information."""
        status = "SOLD" if self.is_sold else "AVAILABLE"
        print(f"\n--- Car ID: {self.car_id} ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₱{self.price:,.2f}")
        print(f"Status: {status}\n")
    
    def sell_car(self, buyer_name):
        """Sell the car to a buyer."""
        if self.is_sold:
            print(f"✗ This car is already sold!")
            return False
        
        self.is_sold = True
        print(f"✓ {self.brand} {self.model} sold to {buyer_name}!")
        return True


class Dealership:
    """Manages a collection of cars."""
    
    def __init__(self, name):
        self.name = name
        self.cars = {}
        self.next_id = 1
        print(f"\n*** Welcome to {self.name}! ***\n")
    
    def add_car(self, brand, model, price):
        """Add a new car to inventory."""
        try:
            # Validate inputs
            if not brand or not brand.strip():
                raise ValueError("Brand cannot be empty")
            if not model or not model.strip():
                raise ValueError("Model cannot be empty")
            
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be greater than 0")
            
            # Create and add car
            new_car = Car(self.next_id, brand.strip(), model.strip(), price)
            self.cars[self.next_id] = new_car
            print(f"✓ Added: {brand} {model} (ID: {self.next_id})")
            self.next_id += 1
            return new_car
            
        except ValueError as e:
            print(f"✗ Error: {e}")
            return None
    
    def display_all(self):
        """Display all cars in inventory."""
        if not self.cars:
            print("No cars in inventory.")
            return
        
        print(f"\n=== {self.name} Inventory ===")
        for car in self.cars.values():
            status = "SOLD" if car.is_sold else "AVAILABLE"
            print(f"ID {car.car_id}: {car.brand} {car.model} - ₱{car.price:,.2f} [{status}]")
        print()
    
    def find_car(self, car_id):
        """Find a car by ID."""
        try:
            car_id = int(car_id)
            if car_id in self.cars:
                return self.cars[car_id]
            else:
                print(f"✗ Car ID {car_id} not found")
                return None
        except ValueError:
            print("✗ Car ID must be a number")
            return None
    
    def sell_car_by_id(self, car_id, buyer_name):
        """Sell a car by its ID."""
        try:
            if not buyer_name or not buyer_name.strip():
                raise ValueError("Buyer name cannot be empty")
            
            car = self.find_car(car_id)
            if car:
                car.sell_car(buyer_name.strip())
        except ValueError as e:
            print(f"✗ Error: {e}")


def main():
    """Main program."""
    dealership = Dealership("JMC Car Moto")
    
    # Add sample cars
    dealership.add_car("Toyota", "Hiace Super Grandia Elite", 3346000)
    dealership.add_car("Toyota", "Fortuner GR-S 4X4 AT", 2656000)
    dealership.add_car("Toyota", "Hilux GR-S 4X4 AT ", 2480000)
    
    while True:
        try:
            print("\n=== MENU ===")
            print("1. Add car")
            print("2. Display all cars")
            print("3. View car details")
            print("4. Sell a car")
            print("5. Exit")
            
            choice = input("\nChoice (1-5): ").strip()
            
            if choice == '1':
                brand = input("Brand: ")
                model = input("Model: ")
                price = input("Price: ")
                dealership.add_car(brand, model, price)
            
            elif choice == '2':
                dealership.display_all()
            
            elif choice == '3':
                car_id = input("Enter car ID: ")
                car = dealership.find_car(car_id)
                if car:
                    car.display_info()
            
            elif choice == '4':
                car_id = input("Enter car ID: ")
                buyer = input("Buyer name: ")
                dealership.sell_car_by_id(car_id, buyer)
            
            elif choice == '5':
                print("\nThank you! Goodbye!")
                break
            
            else:
                print("✗ Invalid choice! Choose 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()