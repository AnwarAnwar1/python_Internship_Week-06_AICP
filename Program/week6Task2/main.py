# Function to check the contents and weight of a single sack
def check_sack(contents, weight):
    # Constants for weight ranges
    MIN_GRAVEL_WEIGHT = 49.9
    MAX_GRAVEL_WEIGHT = 50.1
    MIN_CEMENT_WEIGHT = 24.9
    MAX_CEMENT_WEIGHT = 25.1

    # Check contents and weight
    if contents in ['C', 'G', 'S']:
        if (contents in ['G', 'S'] and MIN_GRAVEL_WEIGHT < weight < MAX_GRAVEL_WEIGHT) or \
           (contents == 'C' and MIN_CEMENT_WEIGHT < weight < MAX_CEMENT_WEIGHT):
            return True
        else:
            return False, "Invalid weight for the given contents."
    else:
        return False, "Invalid contents. Use 'C' for cement, 'G' for gravel, or 'S' for sand."

# Function to check a customer's order for delivery
def check_order(order):
    total_weight = 0
    rejected_sacks = 0

    for sack in order:
        contents_input = sack[0]
        weight_input = sack[1]

        # Check the sack and update total weight and rejected sack count
        result = check_sack(contents_input, weight_input)
        if result is True:
            total_weight += weight_input
        else:
            rejected_sacks += 1
            print(f"Rejected sack - Contents: {contents_input}, Weight: {weight_input}. Reason: {result[1]}")

    return total_weight, rejected_sacks

# Input data for a customer's order
num_sacks_cement = int(input("Enter the number of cement sacks required: "))
num_sacks_gravel = int(input("Enter the number of gravel sacks required: "))
num_sacks_sand = int(input("Enter the number of sand sacks required: "))

# Create a list of sacks based on user input
customer_order = [('C', 25.0)] * num_sacks_cement + [('G', 50.0)] * num_sacks_gravel + [('S', 50.0)] * num_sacks_sand

# Check the customer's order and display output
order_result = check_order(customer_order)
print(f"\nTotal weight of the order: {order_result[0]} kilograms.")
print(f"Number of rejected sacks: {order_result[1]}")
