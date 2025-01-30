# Infinite loop to continuously take input
while True:
    n = int(input()) # Read an integer form the user
    
    # If the input is 0, exit the loop
    if n == 0:
        break

    # Convert the number to binary and remove the '0b prefix
    binary_representation = bin(n)[2:]
    # Count the number of '1's in the binary representation
    count_ones = binary_representation.count('1') 
    # Print the binary representation and its parity (number of 1s mod 2)
    print("The parity of", binary_representation, "is", count_ones, "(mod 2).")