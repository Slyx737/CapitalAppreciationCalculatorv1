# Capital Appreciation Calculator

Capital Appreciation Calculator is a Python script that calculates the future returns of an investment position based on the number of shares, average cost, and future price projections. The script provides investors with a tool to estimate potential gains from their investments, taking into account the average cost of acquiring the shares and the projected future price of the asset.

## Features

- Calculates the future returns (capital appreciation gain) of an investment position.
- Allows users to input the number of shares, average cost per share, and projected future price per share.
- Supports calculations for different quantities of shares and average costs.

## Usage

To use the Capital Appreciation Calculator, simply input the following values into the script:

- `num_shares`: The number of shares in the investment position.
- `avg_cost`: The average cost per share.
- `future_price`: The projected future price per share.

The script will then calculate the future returns (capital appreciation gain) for the given inputs and display the result.

## Example

```python
# Define input values for number of shares, average cost, and future price
num_shares = 2000
avg_cost = 15
future_price = 79.11

# Calculate and print the future returns for the given inputs
future_returns = calculate_future_returns(num_shares, avg_cost, future_price)
print(f"Future returns for {num_shares} shares with average cost ${avg_cost} and future price ${future_price}: ${future_returns:.2f}")

# Disclaimer
The Capital Appreciation Calculator is intended for educational and informational purposes only. It is not intended to provide investment advice or recommendations. Investors should conduct their own research and consult with a financial advisor before making investment decisions.