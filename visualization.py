import matplotlib.pyplot as plt

def plot_expense(trend):
    plt.plot(trend.index, trend.values)
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()
