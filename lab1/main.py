from data import generateprob
from plotting import create_plot
import matplotlib.pyplot as plt


def main():
    x, y = generateprob()
    create_plot(x, y)


if __name__ == "__main__":
    main()