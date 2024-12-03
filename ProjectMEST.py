import math

# Constants
c = 3.0 * 10**8  # Speed of light in m/s
G = 6.67430 * 10**-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 5.972 * 10**24  # Mass of Earth in kg
R_earth = 6371 * 10**3  # Radius of Earth in meters
time_on_earth = 86400  # Seconds in one day

# Input: Altitude (in km) and velocity (in km/s)
print("Welcome to the time dilation calculator for MEST!:")
altitude_km = float(input("Enter the altitude of the satellite above Earth (in km): "))
velocity_kms = float(input("Enter the orbital velocity of the satellite (in km/s): "))

# Convert inputs to meters and m/s
altitude = altitude_km * 10**3
velocity = velocity_kms * 10**3

# Check if velocity is less than the speed of light
if velocity >= c:
    print("Error: The velocity must be less than the speed of light.")
else:
    # Distance from the center of Earth to the satellite
    R_satellite = R_earth + altitude

    # 1. Special Relativity (SR) Time Dilation
    time_dilation_sr = time_on_earth * math.sqrt(1 - (velocity**2 / c**2))

    # 2. General Relativity (GR) Time Dilation
    time_dilation_gr = time_on_earth * math.sqrt(1 - (2 * G * M) / (R_satellite * c**2))

    # Calculate the total time difference per day
    net_time_discrepancy = time_dilation_gr - time_dilation_sr
    net_time_discrepancy_microseconds = net_time_discrepancy * 10**6  # Convert to microseconds

    # Display the results
    print("\nTime dilation effects for the given satellite parameters:")
    print(f"Special Relativity time dilation per day (seconds): {time_on_earth - time_dilation_sr:.6f}")
    print(f"General Relativity time dilation per day (seconds): {time_dilation_gr - time_on_earth:.6f}")
    print(f"Net time discrepancy per day (microseconds): {net_time_discrepancy_microseconds:.2f}")
