# Car Dealership System - Simplified Version

## Overview
A simplified car dealership management program demonstrating OOP concepts in Python.

**Program Size:** ~120 lines of code

## Features
- **2 Classes:** Car and Dealership
- **6 Methods:** display_info(), sell_car(), add_car(), display_all(), find_car(), sell_car_by_id()
- **Exception Handling:** Input validation and error handling
- **5 Menu Options:** Simple and easy to use

## How to Run
```bash
python car.py
```

## Menu Options
1. **Add car** - Add a new car to inventory
2. **Display all cars** - Show all cars
3. **View car details** - See details of a specific car
4. **Sell a car** - Process a sale
5. **Exit** - Close the program

## Sample Usage

### Adding a Car
```
Choice (1-5): 1
Brand: Ford
Model: Mustang
Price: 35000
✓ Added: Ford Mustang (ID: 4)
```

### Viewing Inventory
```
Choice (1-5): 2

=== Auto World Inventory ===
ID 1: Toyota Camry - $28,000.00 [AVAILABLE]
ID 2: Honda Civic - $24,000.00 [AVAILABLE]
ID 3: BMW X5 - $65,000.00 [AVAILABLE]
```

### Selling a Car
```
Choice (1-5): 4
Enter car ID: 1
Buyer name: John Smith
✓ Toyota Camry sold to John Smith!
```

## Exception Handling Examples

**Empty Brand:**
```
Brand: 
✗ Error: Brand cannot be empty
```

**Invalid Price:**
```
Price: -1000
✗ Error: Price must be greater than 0
```

**Invalid Car ID:**
```
Enter car ID: abc
✗ Car ID must be a number
```

**Car Not Found:**
```
Enter car ID: 999
✗ Car ID 999 not found
```

**Already Sold:**
```
✗ This car is already sold!
```

## OOP Concepts
- ✓ Classes and Objects
- ✓ Encapsulation
- ✓ Methods
- ✓ Attributes
- ✓ Exception Handling
- ✓ User Input

## Files
- `car_simple.py` - Main program
- `SIMPLE_ANSWERS.txt` - Question answers
- `SIMPLE_README.md` - This file

## Why This Version?
- **Less code** (~120 lines vs 500+)
- **Easier to understand**
- **Still meets all requirements**
- **Perfect for learning**
- **Clean and simple**

---
**Simple, Clean, Educational!** 🚗