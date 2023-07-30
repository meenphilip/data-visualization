from matplotlib import pyplot as plt

# Median Developer Salaries by Age
# x - axis
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# y - axis
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y)

# Add labels.
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Ages")
plt.show()
