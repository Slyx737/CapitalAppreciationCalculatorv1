def calculate_future_returns(num_shares, avg_cost, future_price):
    """
    Calculates the future returns of a position based on the number of shares,
    average cost, and future price projections.

    Parameters:
        num_shares (int): The number of shares in the position.
        avg_cost (float): The average cost per share.
        future_price (float): The projected future price per share.

    Returns:
        float: The future returns of the position.
    """
    # Calculate the capital appreciation gain
    capital_appreciation_gain = (future_price - avg_cost) * num_shares

    return capital_appreciation_gain

# Define input values for number of shares, average cost, and future price
num_shares = 2000
avg_cost = 15
future_price = 79.11

# Calculate and print the future returns for the given inputs
future_returns = calculate_future_returns(num_shares, avg_cost, future_price)
print(f"Future returns for {num_shares} shares with average cost ${avg_cost} and future price ${future_price}: ${future_returns:.2f}")

# Repeat the calculation for different quantities of shares and average costs
num_shares_list = [2000, 3000, 5000]
avg_cost_list = [15, 8]

for num_shares in num_shares_list:
    for avg_cost in avg_cost_list:
        future_returns = calculate_future_returns(num_shares, avg_cost, future_price)
        print(f"Future returns for {num_shares} shares with average cost ${avg_cost} and future price ${future_price}: ${future_returns:.2f}")
