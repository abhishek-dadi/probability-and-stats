import matplotlib.pyplot as plt


def plot(x,y):
    plt.plot(x, y, color='blue', marker='o', linestyle='--')
    plt.axhline(y=0.5, color='green', linestyle='-', label='50%')
    plt.axvline(x=23, color='red', linestyle='--', label='50% probability at 23 people')


    plt.title("Simple Line Graph")
    plt.xlabel("no of people")
    plt.ylabel("probability")
    plt.show()