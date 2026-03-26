import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("dual_log_2026-02-18.csv", sep=";")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df_long = df.melt(
        id_vars=["timestamp"],
        value_vars=["KAHL1 [A]", "KAHL2 [A]"],
        var_name="signal",
        value_name="value"
    )

    sns.lineplot(data=df_long, x="timestamp", y="value", hue="signal")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()