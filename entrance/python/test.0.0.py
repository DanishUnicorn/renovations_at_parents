# ---------- This script is only to see if we can shorten the total to appx. 57 meters ---------- 

# Import the necessary libraries
import math

# Define the lengths of the tubing in meters
A_length = 8.8
B_length = 8.2
C_length = 1.0
D_length = 0.8

# Define length to installation point
installation_length = 10.0

# Define the radius of the bends in meters
r = 0.1

# Define the angles as part of a circle (b_1 and b_3 from the figure = b_90, b_2 and b_4 from the figure = b_180).
b_90 =  0.25
b_180 = 0.5

# Define the lengths of the tubing in bends
b_90_length =   b_90 * ( 2 * math.pi * r )
b_180_length =  b_180 * ( 2 * math.pi * r )

# Define quantities of each factor
straight_section_quantities = {
    "A_length": 1,
    "B_length": 5,
    "C_length": 1,
    "D_length": 2,
}

bend_quantities = {
    "b_90": 2,
    "b_180": 6,
}

# Calculate the total length of tubing needed
total_length_straight_sections = (
    straight_section_quantities["A_length"] * A_length +
    straight_section_quantities["B_length"] * B_length +
    straight_section_quantities["C_length"] * C_length +
    straight_section_quantities["D_length"] * D_length
)

total_length_bends = (
    bend_quantities["b_90"] * b_90_length +
    bend_quantities["b_180"] * b_180_length
)

total_length = (
    total_length_straight_sections +
    total_length_bends +
    installation_length
)


# Print the total length of tubing needed
print(f"Total length of tubing needed in straight sections: {total_length_straight_sections:.2f} m")
print(f"Total length of tubing needed in bends: {total_length_bends:.2f} m")
print(f"Total length of tubing needed: {total_length:.2f} m")


# ---------- Conclusion: By shaving off 2 B sections