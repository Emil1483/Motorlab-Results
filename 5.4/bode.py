import matplotlib.pyplot as plt
import numpy as np

data = [
    # (freq, (a_ut / a_in), phase_shift)
    (0.1, 2.0188 / 2.0186, 1.73),
    (0.4, 2.009 / 2.0188, 7.13),
    (0.8, 2.0188 / 2.0188, 10.0),
    (2, 2.009 / 2.0188, 22.5),
    (4, 1.99 / 2.0188, 46.0),
    (8, 1.79 / 2.0188, 92.75),
    (10, 1.3818 / 2.0188, 149.21),
    (11, 1.205 / 2.0188, 154.9),
    (12, 1.078 / 2.0188, 152.13),
    (15, 0.813 / 2.0188, 158.3),
    (20, 0.607 / 2.0188, 173.0),
    (25, 0.529 / 2.0188, 170.0),
    (30, 0.4704 / 2.0188, 179.26),
    (50, 0.4018 / 2.0188, 180.0),
]


frequencies = [point[0] for point in data]
gain = [point[1] for point in data]
phase_shift = [point[2] for point in data]

gain = [20 * np.log10(g) for g in gain]

# Plot Gain vs Frequency
# Create a plot with two different y-axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot Gain on the primary y-axis
ax1.semilogx(frequencies, gain, marker="o", color="blue")

ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Gain 20 * log10(a_ut / a_in)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(which="both", linestyle="--", linewidth=0.5)

# Create a secondary y-axis for Phase Shift
ax2 = ax1.twinx()
ax2.semilogx(
    frequencies, phase_shift, marker="s", color="orange", label="Phase Shift (degrees)"
)
ax2.set_ylabel("Phase Shift (degrees)", color="orange")
ax2.tick_params(axis="y", labelcolor="orange")

# Add a title
plt.title("Gain and Phase Shift vs Frequency with Dual Y-Axes")

# Show the plot
plt.show()
