#!/usr/bin/env python3
"""
Simple Calculator in Python
Supports basic arithmetic operations: +, -, *, /, %, ** (power)
"""

import math
import sys

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication"""
        return a * b
    
    def divide(self, a, b):
        """Division"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def modulo(self, a, b):
        """Modulo operation"""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero!")
        return a % b
    
    def power(self, a, b):
        """Power operation"""
        return a ** b
    
    def square_root(self, a):
        """Square root"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(a)
    
    def calculate(self, expression):
        """Calculate a mathematical expression"""
        try:
            # Replace common math functions
            expression = expression.replace('sqrt(', 'math.sqrt(')
            expression = expression.replace('^', '**')
            
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": {}, "math": math})
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
    
    def show_history(self):
        """Show calculation history"""
        if not self.history:
            print("No calculations in history.")
            return
        
        print("\n--- Calculation History ---")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
        print()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        print("History cleared.")

def print_menu():
    """Print the calculator menu"""
    print("\n" + "="*50)
    print("           PYTHON CALCULATOR")
    print("="*50)
    print("Options:")
    print("1. Basic Operations (+, -, *, /, %, **)")
    print("2. Expression Calculator")
    print("3. Square Root")
    print("4. Show History")
    print("5. Clear History")
    print("6. Help")
    print("7. Exit")
    print("="*50)

def print_help():
    """Print help information"""
    print("\n--- HELP ---")
    print("Basic Operations:")
    print("  Addition: 5 + 3")
    print("  Subtraction: 10 - 4")
    print("  Multiplication: 6 * 7")
    print("  Division: 15 / 3")
    print("  Modulo: 17 % 5")
    print("  Power: 2 ** 3")
    print()
    print("Expression Calculator:")
    print("  You can enter complex expressions like:")
    print("  - (5 + 3) * 2")
    print("  - 2 ** 3 + sqrt(16)")
    print("  - 10 / 2 + 3 * 4")
    print()
    print("Available functions:")
    print("  - sqrt(x): Square root")
    print("  - Use ^ or ** for power")
    print()

def get_two_numbers():
    """Get two numbers from user input"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        raise ValueError("Please enter valid numbers!")

def main():
    """Main calculator function"""
    calc = Calculator()
    
    print("Welcome to Python Calculator!")
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                print("\nBasic Operations:")
                print("Available operations: +, -, *, /, %, **")
                
                try:
                    a, b = get_two_numbers()
                    op = input("Enter operation (+, -, *, /, %, **): ").strip()
                    
                    if op == '+':
                        result = calc.add(a, b)
                    elif op == '-':
                        result = calc.subtract(a, b)
                    elif op == '*':
                        result = calc.multiply(a, b)
                    elif op == '/':
                        result = calc.divide(a, b)
                    elif op == '%':
                        result = calc.modulo(a, b)
                    elif op == '**':
                        result = calc.power(a, b)
                    else:
                        print("Invalid operation!")
                        continue
                    
                    print(f"Result: {a} {op} {b} = {result}")
                    calc.history.append(f"{a} {op} {b} = {result}")
                    
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '2':
                print("\nExpression Calculator:")
                print("Enter a mathematical expression (e.g., (5+3)*2, sqrt(16), 2**3)")
                
                try:
                    expression = input("Enter expression: ").strip()
                    if expression:
                        result = calc.calculate(expression)
                        print(f"Result: {result}")
                    else:
                        print("Please enter a valid expression!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '3':
                print("\nSquare Root Calculator:")
                try:
                    num = float(input("Enter number: "))
                    result = calc.square_root(num)
                    print(f"Result: √{num} = {result}")
                    calc.history.append(f"√{num} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '4':
                calc.show_history()
            
            elif choice == '5':
                calc.clear_history()
            
            elif choice == '6':
                print_help()
            
            elif choice == '7':
                print("Thank you for using Python Calculator!")
                print("Goodbye!")
                sys.exit(0)
            
            else:
                print("Invalid choice! Please enter a number between 1-7.")
        
        except KeyboardInterrupt:
            print("\n\nExiting calculator...")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()