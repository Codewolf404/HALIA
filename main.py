import numpy as np
print("\nWelcome to HALIA\n")
def menu():
  while True:
    print("\nLet the learning being")
    print("\nChoose an operation to perform on the Dark Matter Halo:")
    print("1. Density Profile")
    print("2. Virial Radius and Virial Mass")
    print("3. Velocity Dispersion")
    print("4. Exit")
    try:
      choice = int(input("Enter a number (1-4): "))
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 4.")
      continue