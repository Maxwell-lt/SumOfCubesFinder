# Change this to print more values (default: 10)
NUMBER_TO_PRINT = 10
# Change this to modify the search space. Larger search spaces will take more time and memory. (default:100)
SEARCH_RANGE = 100

found2Ways = {}     # Dictionary with numbers that fit the criteria, mapped to the pairs of cubes they consist of
all_sums = {}       # Dictionary used to track every single sum of two cubes within the search range


# Helper function
def cube_and_sum(a, b):
    return (a**3) + (b**3)


# Helper function to prettify numbers
def pair_to_string(a, b):
    return str(a) + ", " + str(b)


# Nested for loops used to iterate over every unique combination of two numbers from 1 to SEARCH_RANGE
for i in range(1, SEARCH_RANGE):
    for j in range(i, SEARCH_RANGE):    # i is used as the lower bound to avoid commutative duplicates
        # Check whether the result of summing the cubes of the two numbers is already tracked
        if str(cube_and_sum(i, j)) in all_sums.keys():
            # Retrieve the previous pair so that the current pair can be appended
            old_pairstring = all_sums[str(cube_and_sum(i, j))]
            # Append the new set of pairs
            new_pairstring = old_pairstring + " 2nd pair: " + pair_to_string(i, j)
            # Update all_sums with the new list of pairs
            all_sums[str(cube_and_sum(i, j))] = new_pairstring
            # Save found taxicab number, along with its cube pairs
            found2Ways[cube_and_sum(i, j)] = all_sums[str(cube_and_sum(i, j))]
        else:
            # First time this number has been generated, add it to all_sums as the first pair
            all_sums[str(cube_and_sum(i, j))] = "\t1st pair: " + pair_to_string(i, j)

num_printed = 0     # Tracks the count of printed taxicab numbers
# Iterate through the found taxicab numbers in ascending order
for i in sorted(found2Ways.keys()):
    # Skip first taxicab number
    if i == 1729:
        continue
    # Increment printed counter
    num_printed += 1
    # Break the loop when NUMBER_TO_PRINT numbers have been printed
    if num_printed > NUMBER_TO_PRINT:
        break
    # Print taxicab number and its pairs
    print(i, found2Ways[i])
