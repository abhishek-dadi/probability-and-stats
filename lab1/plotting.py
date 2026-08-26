import matplotlib.pyplot as plt


def create_plot(x,y):
    plt.plot(x, y, color="blue", linestyle="--")
    plt.axhline(y=0.5, color="green", linestyle="-", label="50% Probability")
    plt.axvline(x=23, color="red", linestyle="--", label="23 People Threshold")

    plt.title("Birthday Paradox Probability")
    plt.xlabel("Number of People")
    plt.ylabel("Probability of at least 1 shared birthday")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()