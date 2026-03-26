import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# načítanie dát
df = pd.read_csv("dual_log_2026-02-18.csv", sep=";")
df["timestamp"] = pd.to_datetime(df["timestamp"])

sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(10, 5))


def update(frame):
    ax.clear()

    # vezmeme len časť dát do aktuálneho frame
    df_part = df.iloc[:frame]

    df_long = df_part.melt(
        id_vars=["timestamp"],
        value_vars=["KAHL1 [A]", "KAHL2 [A]"],
        var_name="signal",
        value_name="value"
    )

    sns.lineplot(data=df_long, x="timestamp", y="value", hue="signal", ax=ax)

    ax.set_title("Animácia dát")
    ax.tick_params(axis='x', rotation=45)


ani = FuncAnimation(fig, update, frames=len(df), interval=100) # interval pre rychlost vypisovania

plt.tight_layout()
plt.show()