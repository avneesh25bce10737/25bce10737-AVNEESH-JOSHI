import number_theory
import data_analysis

def print_menu():
    print("\n--- Python Algorithmic Toolkit ---")
    print("1: Find GCD of two numbers")
    print("2: Find Prime Factors of a number")
    print("3: Convert number to another Base")
    print("4: Calculate Fast Power (a^b)")
    print("5: Find Max in a list of numbers")
    print("6: Remove Duplicates from a list")
    print("7: Find K-th Smallest in a list")
    print("8: Generate N Fibonacci Numbers")
    print("0: Exit")
def get_list_from_user():
    raw_input = input("Enter numbers separated by spaces: ")
    str_list = raw_input.split()
    num_list = []
    for s in str_list:
        num_list.append(int(s)) 
    return num_list    
def main():
      while True:
        print_menu()   
        choice = input("Enter your choice (0-8): ")
        if choice == '1':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(number_theory.find_gcd(a, b))
            
        elif choice == '2':
            n = int(input("Enter number: "))
            print(number_theory.find_prime_factors(n))
            
        elif choice == '3':
            n = int(input("Enter number: "))
            base = int(input("Enter new base (e.g., 2, 8, 16): "))
            print(number_theory.base_conversion(n, base))
            
        elif choice == '4':
            a = int(input("Enter base: "))
            b = int(input("Enter power: "))
            print(number_theory.fast_power(a, b))
            
        elif choice == '5':
            user_list = get_list_from_user()
            print(data_analysis.find_max(user_list))
            
        elif choice == '6':
            user_list = get_list_from_user()
            print(data_analysis.remove_duplicates(user_list))
            
        elif choice == '7':
            user_list = get_list_from_user()
            k = int(input("Enter k: "))
            print(data_analysis.kth_smallest_number(user_list, k))
            
        elif choice == '8':
            n = int(input("How many Fibonacci numbers to generate? "))
            print(data_analysis.fibonacci_sequence(n))
            
        elif choice == '0':
            print("Exiting toolkit. Goodbye!")
            break 
            
        else:
            print("Invalid choice. Please try again.")
