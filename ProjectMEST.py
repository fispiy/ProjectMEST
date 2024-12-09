import math

# Constants
c = 3.0 * 10**8  # Speed of light 
G = 6.67430 * 10**-11  # Gravitational constant 
M = 5.972 * 10**24  # Mass of Earth 
R_earth = 6371 * 1000  # Radius of Earth 
time_on_earth = 86400  # Seconds in a day

# Welcome message and user inputs
print("Welcome to the Time Dilation Calculator!")
print("Ever wondered how time behaves for satellites in orbit? Let’s find out!")
altitude_km = float(input("First, tell me the altitude of the satellite above Earth (in kilometers): "))
velocity_kms = float(input("Now, what’s the satellite’s orbital velocity (in kilometers per second): "))

# Convert inputs to meters and meters per second
altitude = altitude_km * 1000
velocity = velocity_kms * 1000

# Check if the velocity is realistic
if velocity >= c:
    print("Oops! The velocity can't be equal to or greater than the speed of light. Try again.")
else:
    # Distance from Earth's center to the satellite
    R_satellite = R_earth + altitude

    # Calculate time dilation due to Special Relativity (SR)
    sr_factor = math.sqrt(1 - (velocity**2 / c**2))
    time_dilation_sr = time_on_earth * sr_factor

    # Calculate time dilation due to General Relativity (GR)
    gr_factor = math.sqrt(1 - (2 * G * M) / (R_satellite * c**2))
    time_dilation_gr = time_on_earth * gr_factor

    # Compute the net time difference per day
    net_time_discrepancy = time_dilation_gr - time_dilation_sr
    net_time_discrepancy_microseconds = net_time_discrepancy * 1e6

    # Calculate the total effect over six months 
    days_in_6_months = 182.5
    total_discrepancy_seconds = net_time_discrepancy * days_in_6_months
    total_discrepancy_milliseconds = total_discrepancy_seconds * 1000

    # Presenting the results in a friendly way
    print("\nTime Dilation Results:")
    print(f"1. Every day, the satellite loses about {time_on_earth - time_dilation_sr:.6f} seconds due to its high speed.")
    print(f"2. However, it gains/loses {time_dilation_gr - time_on_earth:.6f} seconds because it's farther from Earth's gravity.")
    print(f"3. The net effect per day is a discrepancy of {net_time_discrepancy_microseconds:.2f} microseconds.")

    print("\nWhat happens over six months?")
    print(f"In total, the satellite’s clock will differ by {total_discrepancy_seconds:.9f} seconds.")
    print(f"That’s about {total_discrepancy_milliseconds:.3f} milliseconds!")
    print("Pretty cool, right?")
