import numpy as np
from halia_source import sources

print("\nWelcome to HALIA")

# --- All About Dark Matter Halos and Helia ---
def dark_matter_halos():
    print("\nAll About Dark Matter Halos and HALIA\n")
    print("What Are Dark Matter Halos\n")
    print("Dark matter halos are large invisible clouds made mostly of dark matter. They surround galaxies and hold them together with gravity. The center of a halo is the densest part, and the outer region is much thinner. Even though we cannot see dark matter, its gravity shows that most of a galaxy’s mass lies inside this hidden halo.\n")
    print("Why They Exist\n")
    print("After the Big Bang, the universe was full of small uneven spots in matter. Over time, gravity pulled dark matter together around those spots. These clumps became halos. Normal matter followed the dark matter and formed stars and galaxies inside those halos. Without dark matter halos, galaxies would not exist at all. They are the base on which every galaxy is built.\n")
    print("Who Defined Them and How\n")
    print("""The idea of dark matter halos started with Fritz Zwicky in the 1930s. He saw that galaxies in the Coma Cluster moved too fast to be held by the visible mass and said there must be "dark matter."
In the 1970s, Vera Rubin and Kent Ford studied the motion of stars in galaxies and found the same problem. The outer stars were moving too fast, which meant there was invisible mass around each galaxy "the halo." Later in the 1990s, Julio Navarro, Carlos Frenk, and Simon White used computer simulations to show how halos form and what shape they have. Their model is now called the NFW profile, and it describes how the density of dark matter changes from the center outward.""")
    print("Why We Created HALIA\n")
    print("HALIA is made to explore this hidden side of the universe. It shows how halos hold galaxies together and how the mass spreads from the center to the edge. It helps people see what dark matter does instead of just reading about it. Helia connects theory and imagination, letting users understand the structure that keeps the universe in balance.")

# --- Density Profile ---
def density_profile():
    print("\nA dark matter halo is very dense in the center and gets thinner as you move outwards. We use a common formula called the NFW profile to describe this.\n")
    try:
        r = float(input("Enter the radius (r) from the center: "))
        if r <= 0:
            print("Radius must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    rho_s = 1.0
    r_s = 1.0

    rho = rho_s / ((r / r_s) * (1 + r / r_s)**2)
    print(f"At radius r = {r:.3f}, the density ρ = {rho:.6f}")

# --- Virial Radius and Mass ---
def virial_radius_mass_data():
    print("\nThe virial radius marks roughly the edge of the dark matter halo. Inside this radius, gravity and particle motions are balanced.\n")
    try:
        R_vir = float(input("Enter the virial radius (R_vir): "))
        if R_vir <= 0:
            print("Virial radius must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    rho_s = 1.0
    r_s = 1.0

    r = np.linspace(0.01, R_vir, 1000)
    rho = rho_s / ((r / r_s) * (1 + r / r_s)**2)
    dr = r[1] - r[0]
    M_vir = np.sum(4 * np.pi * rho * r**2 * dr)

    print(f"\nVirial Radius: {R_vir:.3f}")
    print(f"Virial Mass (approx): {M_vir:.3f}")

# --- Velocity Dispersion ---
def velocity_dispersion():
    print("\nVelocity dispersion tells us how fast particles move randomly inside the dark matter halo.\n")
    G = 4.302e-6  # kpc km^2 / Msun s^2
    try:
        M_vir = float(input("Enter the Virial Mass (in solar masses): "))
        R_vir = float(input("Enter the Virial Radius (in kiloparsecs): "))
        if M_vir <= 0 or R_vir <= 0:
            print("Values must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    sigma_v = np.sqrt(G * M_vir / (2 * R_vir))
    print(f"Estimated Velocity Dispersion: {sigma_v:.3f} km/s")

# --- String Theory and Helia ---
def string_theory():
    print("\nString Theory And HALIA\n")
    print("What is String Theory?\n")
    print("""String theory is a theoretical framework in which the fundamental building blocks of the universe are not point particles, but tiny one-dimensional “strings.” These strings vibrate at different frequencies, and each vibration corresponds to a different particle. String theory aims to unify all forces of nature, including gravity, in a single framework.\n""")
    print("Why String Theory Matters for Dark Matter Halos\n")
    print("In conventional physics, gravity determines how dark matter halos form and hold galaxies together. String theory introduces the possibility of extra dimensions and modified gravity at very small scales. These changes could slightly alter how mass is distributed in halos, how fast particles move inside them, or how halos interact with each other. Exploring these effects allows us to think beyond classical models and consider new ways the universe might work.\n")
    print("Connecting String Theory with HALIA\n")
    print("HALIA is designed to simulate and explore dark matter halos. By including string theory concepts, such as extra dimensions or modified gravitational potentials, Helia can estimate how halo properties like density, virial mass, radius, or velocity dispersion might be affected. For practical calculations, string theory effects can be modeled as small corrections to gravity or density. For example, in extra dimensions, the gravitational potential may slightly change from the standard 1/r² law. Helia can show how these corrections affect standard halo values, giving a numerical perspective on otherwise abstract ideas.\n")


# --- Extra Dimension Potential Helpers ---
def density_standard(r):
    return 1 / (r * (1 + r)**2)

def density_extra_dim(r, n=0.05):
    return 1 / (r * (1 + r)**(2 - n))

def virial_mass_standard():
    return 2000.0

def virial_mass_extra_dim():
    return virial_mass_standard() * 1.025

def virial_radius_standard():
    return 0.85

def virial_radius_extra_dim():
    return virial_radius_standard() * 0.975

def velocity_dispersion_standard():
    return 200.0

def velocity_dispersion_extra_dim():
    return velocity_dispersion_standard() * 1.01

# --- Extra Dimension Simulation ---
def extra_dimension_potential():
    try:
        r_input = float(input("Enter radius (r) for Extra Dimension simulation: "))
        if r_input <= 0:
            print("Radius must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    rho_std = density_standard(r_input)
    rho_extra = density_extra_dim(r_input)
    m_std = virial_mass_standard()
    m_extra = virial_mass_extra_dim()
    r_vir_std = virial_radius_standard()
    r_vir_extra = virial_radius_extra_dim()
    v_std = velocity_dispersion_standard()
    v_extra = velocity_dispersion_extra_dim()

    print("\n--- Extra Dimension Potential Simulation ---")
    print(f"Density: Standard = {rho_std:.3f}, Extra Dimension = {rho_extra:.3f}")
    print(f"Virial Mass: Standard = {m_std:.2f}, Extra Dimension = {m_extra:.2f}")
    print(f"Virial Radius: Standard = {r_vir_std:.2f}, Extra Dimension = {r_vir_extra:.2f}")
    print(f"Velocity Dispersion: Standard = {v_std:.2f} km/s, Extra Dimension = {v_extra:.2f} km/s")
# ___Sources___
def show_sources():
    print("\nHALIA Sources\n")
    for topic, refs in sources.items():
        print(f"{topic.replace('_', ' ').title()}:")
        for ref in refs:
            print(f" - {ref}")
        print()  
# blank line for spacing
# --- Main Menu ---
def menu():
    while True:
        print("\nChoose an operation:")
        print("1. All About Dark Matter Halos and HALIA")
        print("2. Density Profile")
        print("3. Virial Radius and Virial Mass")
        print("4. Velocity Dispersion")
        print("5. String Theory and HALIA")
        print("6. Extra Dimension Potential")
        print("7. Show Sources")
        print("8. Exit")

        try:
            choice = int(input("Enter a number (1-8): "))
        except ValueError:
            print("Invalid input. Enter a number 1-8.")
            continue

        if choice == 1:
            dark_matter_halos()
        elif choice == 2:
            density_profile()
        elif choice == 3:
            virial_radius_mass_data()
        elif choice == 4:
            velocity_dispersion()
        elif choice == 5:
            string_theory()
        elif choice == 6:
            extra_dimension_potential()
        elif choice == 7:
            show_sources()
        elif choice == 8:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-8.")

# --- Run Program ---
if __name__ == "__main__":
    menu()