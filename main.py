import numpy as np
print("\nWelcome to HALIA")

def density_profile():
  print("\nA dark matter halo is very dense in the center and gets thinner as you move outwards. We use a common formula called the NFW profile to describe this. In our program, we pick points at different distances from the center and calculate the density at each point to see how the mass is spread in the halo.\n")
  try:
    r = float(input("Enter the radius (r) from the center: "))
    if r <= 0:
      print("Radius must be positive.")
      return None, None
  except ValueError:
    print("Invalid input. Please enter a number.")
    return None, None

  # NFW-like density parameters
  rho_s = 1.0  # scale density
  r_s = 1.0    # scale radius

  # Compute density
  rho = rho_s / ((r / r_s) * (1 + r / r_s)**2)

  # Show result
  print(f"At radius r = {r:.3f}, the density ρ = {rho:.6f}")
  
  return r, rho

# --- Virial Radius and Mass ---
def virial_radius_mass_data():
  print("\nThe virial radius marks roughly the edge of the dark matter halo. Inside this radius, gravity and particle motions are balanced. The virial mass is the total mass inside this edge. We calculate it by adding up all the density from the center out to the virial radius. It's a standard way to define how big and massive a halo is.\n")
  # Ask User
  try:
    R_vir = float(input("Enter the virial radius (R_vir): "))
    if R_vir <= 0:
      print("Virial radius must be positive.")
      return None, None
  except ValueError:
    print("Invalid input. Please enter a number.")
    return None, None

  # Density profile parameters
  rho_s = 1.0
  r_s = 1.0

  # Radial array for integration
  r = np.linspace(0.01, R_vir, 1000)
  rho = rho_s / ((r / r_s) * (1 + r / r_s)**2)

  # Cumulative mass via discrete integration
  dr = r[1] - r[0]
  M_vir = np.sum(4 * np.pi * rho * r**2 * dr)

  print(f"\nVirial Radius: {R_vir:.3f}")
  print(f"Virial Mass (approx): {M_vir:.3f}")
  
  return M_vir, R_vir

def menu():
  while True:
    print("\nLet the learning being\n")
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
    
    if choice == 1:
      r, rho = density_profile()
      if r is not None and rho is not None:
        print("Density profile computed. Arrays r and rho available for further analysis.")
    elif choice == 2:
      virial_mass, virial_radius = virial_radius_mass_data()
      if virial_mass is not None and virial_radius is not None:
        print("Virial radius and mass computed successfully.")
    elif choice == 4:
      print("Exiting program. Goodbye!")
      break
    else:
      print("Feature not yet implemented.")

# Example usage
if __name__ == "__main__":
    menu()
