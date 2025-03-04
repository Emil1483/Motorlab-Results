import os
import pandas as pd
import matplotlib.pyplot as plt
import re


def format_greek_subscript(text: str) -> str:
    greek_letters = {
        "omega": "ω",  # ω
        "theta": "θ",  # θ
    }

    # Replace Greek letter names with symbols
    for name, symbol in greek_letters.items():
        text = re.sub(name, symbol, text)

    # Convert underscores to subscripts
    SUB = str.maketrans(
        "0123456789aehijklmniprstuvxy",
        "₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙᵢₚᵣₛₜᵤᵥₓᵧ",
    )

    def to_subscript(match):
        return match.group(1).translate(SUB)

    text = re.sub(r"_(\w+)", lambda m: "_" + to_subscript(m), text)
    text = text.replace("_", "")  # Remove remaining underscores

    return text


def plot_csv(ax, file_path, label=None, color=None):
    try:
        # Load the CSV file into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Ensure the CSV has exactly two columns
        if len(data.columns) != 2:
            raise ValueError("CSV file must contain exactly two columns.")

        # Extract column names for x and y axes
        x_label = data.columns[0]
        y_label = data.columns[1]

        # Plot the data on the provided axes
        ax.plot(
            data[x_label],
            data[y_label],
            color=color,
            marker="",
            linestyle="-",
            label=label,
        )
    except Exception as e:
        print(f"An error occurred with {file_path}: {e}")


# Create a single figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

path = "3.6d"


def iter_csv_files(path):
    for file in os.listdir(path):
        if file.endswith(".csv"):
            yield f"{path}/{file}"


colors = ["blue", "green", "orange", "red"]

for i, current_path in enumerate(iter_csv_files(path)):
    label = current_path.split("/")[-1].split(".")[0]
    label = format_greek_subscript(label)
    plot_csv(ax, current_path, label=label)


ax.set_title("P-regulator respons")
ax.set_xlabel("Tid [s]")
ax.set_ylabel("Spenning [V]")

ax.legend()
ax.grid(True)
plt.show()


fig.savefig(f"plot-{path}.png")
