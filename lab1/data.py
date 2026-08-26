
def birth(n):
    prob = 1.0
    for i in range(n):
        prob *= (365 - i) / 365
    return 1 - prob


def generateprob():
    x = list(range(100))
    res = [birth(i) for i in x]
    return x, res
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
def main():
    x, y = generateprob()
    create_plot(x, y)
main()