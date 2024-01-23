def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items[::-1]


# Input from the user
num_items = int(input("Enter the number of items: "))
values = []
weights = []

for i in range(num_items):
    value = int(input(f"Enter the value of item {i + 1}: "))
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("Enter the capacity of the knapsack: "))

# Call the knapsack function
max_value, selected_items = knapsack_01(values, weights, capacity)

# Display the results
print(f"Maximum value achievable: {max_value}")
print("Selected items:", selected_items)
