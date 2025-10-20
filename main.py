import numpy as np
print("\nWelcome to HALIA")

#All About Dark Matter Halos and Helia

def dark_matter_halos():
  print("\nAll About Dark Matter Halos and Helia\n")
  print("What Are Dark Matter Halos\n")
  print("Dark matter halos are large invisible clouds made mostly of dark matter. They surround galaxies and hold them together with gravity. The center of a halo is the densest part, and the outer region is much thinner. Even though we cannot see dark matter, its gravity shows that most of a galaxy's mass lies inside this hidden halo.\n")
  print("Why They Exist\n")
  print("\nAfter the Big Bang, the universe was full of small uneven spots in matter. Over time, gravity pulled dark matter together around those spots. These clumps became halos. Normal matter followed the dark matter and formed stars and galaxies inside those halos. Without dark matter halos, galaxies would not exist at all. They are the base on which every galaxy is built.\n")
  print("Who Defined Them and How\n")
  print("""The idea of dark matter halos started with Fritz Zwicky in the 1930s. He saw that galaxies in the Coma Cluster moved too fast to be held by the visible mass and said there must be "dark matter."
In the 1970s, Vera Rubin and Kent Ford studied the motion of stars in galaxies and found the same problem. The outer stars were moving too fast, which meant there was invisible mass around each galaxy - the halo.
Later in the 1990s, Julio Navarro, Carlos Frenk, and Simon White used computer simulations to show how halos form and what shape they have. Their model is now called the NFW profile, and it describes how the density of dark matter changes from the center outward.
""")
  print("Why We Created HALIA\n")
  print("Helia is made to explore this hidden side of the universe. It shows how halos hold galaxies together and how the mass spreads from the center to the edge. It helps people see what dark matter does instead of just reading about it. Helia connects theory and imagination, letting users understand the structure that keeps the universe in balance.")

#Density Profile

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

# --- Velocity Dispersion ---
def velocity_dispersion_data():
  print("\nVelocity dispersion tells us how fast particles are moving randomly inside the dark matter halo. It's a measure of the spread in their velocities, some particles move slower, others faster, depending on how strong gravity is in that region.\n")
  G = 4.302e-6  # Gravitational constant in (kpc * km^2) / (Msun * s^2)
  
  try:
    M_vir = float(input("Enter the Virial Mass (in solar masses): "))
    R_vir = float(input("Enter the Virial Radius (in kiloparsecs): "))
    
    if M_vir <= 0 or R_vir <= 0:
      print("Values must be positive.")
      return None
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    return None

  sigma_v = np.sqrt(G * M_vir / (2 * R_vir))
  print(f"\nEstimated Velocity Dispersion: {sigma_v:.3f} km/s")
  
  return sigma_v

# --- Extra Dimension Potential Simulation ---
def extra_dimension_potential():
  print("\n--- Extra Dimension Potential Simulation ---")
  print("This feature simulates how dark matter halos would behave if gravity had access to extra dimensions.\n")
  try:
    r_input = float(input("Enter radius (r) for Extra Dimension simulation: "))
    if r_input <= 0:
      print("Radius must be positive.")
      return None
  except ValueError:
    print("Invalid input. Please enter a number.")
    return None

  # Placeholder values for demonstration
  rho_std = 1.0 / ((r_input / 1.0) * (1 + r_input / 1.0)**2)
  rho_extra = rho_std * 1.2  # Slightly higher in extra dimensions
  
  m_std = 10.0
  m_extra = m_std * 1.15
  
  r_vir_std = 5.0
  r_vir_extra = r_vir_std * 0.95
  
  v_std = 100.0
  v_extra = v_std * 1.1

  # Print results
  print(f"\nDensity at r = {r_input}: Standard = {rho_std:.3f}, Extra Dimension = {rho_extra:.3f}")
  if rho_extra > rho_std:
    print("Explanation: Density increases slightly because gravity is stronger in extra dimensions at small scales.")
  else:
    print("Explanation: Density decreases slightly because gravity is weaker in extra dimensions at this scale.")

  print(f"\nVirial Mass: Standard = {m_std:.2f}, Extra Dimension = {m_extra:.2f}")
  print("Explanation: Mass increases because stronger gravity binds more matter within the halo.")

  print(f"\nVirial Radius: Standard = {r_vir_std:.2f}, Extra Dimension = {r_vir_extra:.2f}")
  print("Explanation: Radius decreases slightly because stronger binding pulls particles inward.")

  print(f"\nVelocity Dispersion: Standard = {v_std:.2f} km/s, Extra Dimension = {v_extra:.2f} km/s")
  print("Explanation: Particles move faster because stronger gravity increases kinetic energy.")
  
  return True

def menu():
  while True:
    print("\nLet the learning being\n")
    print("\nChoose an operation to perform on the Dark Matter Halo:")
    print("1. All About Dark Matter Halos and Helia")
    print("2. Density Profile")
    print("3. Virial Radius and Virial Mass")
    print("4. Velocity Dispersion")
    print("5. Extra Dimension Potential")
    print("6. Exit")
    try:
      choice = int(input("Enter a number (1-6): "))
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 6.")
      continue
    
    if choice == 1:
      dark_matter_halos()
    elif choice == 2:
      r, rho = density_profile()
      if r is not None and rho is not None:
        print("Density profile computed. Arrays r and rho available for further analysis.")
    elif choice == 3:
      virial_mass, virial_radius = virial_radius_mass_data()
      if virial_mass is not None and virial_radius is not None:
        print("Virial radius and mass computed successfully.")
    elif choice == 4:
      sigma_v = velocity_dispersion_data()
      if sigma_v is not None:
        print("Velocity dispersion computed successfully.")
    elif choice == 5:
      result = extra_dimension_potential()
      if result is not None:
        print("Extra dimension simulation completed successfully.")
    elif choice == 6:
      print("Exiting program. Goodbye!")
      break
    else:
      print("Feature not yet implemented.")

# Example usage
if __name__ == "__main__":
    menu()
