import matplotlib.pyplot as plt


def plot_class_distribution(class_distribution):

    ax = class_distribution.plot(
        x="Class",
        y="Count",
        kind="bar",
        legend=False,
        color=["#d9534f", "#5cb85c"] 
    )

    plt.title("Class Distribution (Breast Cancer Dataset)")
    plt.xlabel("Class Name")
    plt.ylabel("Sample Count")
    plt.xticks(rotation=0)

    for p in ax.patches:
        ax.annotate(
            f"{int(p.get_height())}",
            (p.get_x() + p.get_width() / 2., p.get_height() / 2),
            ha='center', va='center', color='white', fontweight='bold'
        )

    plt.tight_layout()
    plt.show()


def plot_metric_curve(metrics_df, x_col="Threshold", y_cols=None):

    if y_cols is None:
        y_cols = ["Accuracy", "Precision", "sensitivity", "F1_Score"]

    plt.figure()
    for col in y_cols:
        plt.plot(metrics_df[x_col], metrics_df[col], marker="o", label=col)

    plt.title("Metrics vs Threshold")
    plt.xlabel(x_col)
    plt.ylabel("Score")
    plt.legend()
    plt.tight_layout()
    plt.show()
