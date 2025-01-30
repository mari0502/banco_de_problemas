def fill_square(grip):
    n = len(grip) # Determine the size of the grip
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Alphabet to use for filling empty cells

    # Iterate through each row and each column
    for i in range(n):
        for j in range(n):
            # Check if the cell is empty
            if grip[i][j] == '.':
                # Try filling the cell with a letter from A-Z
                for letter in alphabet:
                    # Check if the letter is used in any adjacent cells (up, down, left, right)
                    if (i > 0 and grip[i-1][j] == letter) or \
                        (i < n-1 and grip[i+1][j] == letter) or \
                            (j > 0 and grip[i][j-1] == letter) or \
                                (j < n-1 and grip[i][j+1] == letter):
                        continue # Skip this letter if it's already adjacent
                    grip[i][j] = letter # Assign the first valid letter
                    break # Stop checking further letters
    
    # Return the updated grip
    return grip 

def main():
    testCases = int(input()) # Read the number of test cases
    grip = [] # Initialize an empty grip

    for _ in range(testCases):
        dimension = int(input()) # Read the dimension of the grip

        # Read the rows of the grip
        for _ in range(dimension):
            row = list(map(str, input().split()))
            grip.append(row)
    
    # Fill the grip with valid letters
    fill_grip = fill_square(grip)
        
    print(f"Case {testCases}") # Print the case number
    for row_grip in fill_grip:
        print(''.join(row_grip)) # Print the filled grip row by row

main() # Execute the program
