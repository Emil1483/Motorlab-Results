import matplotlib.pyplot as plt
import numpy as np

data = [
    # (freq, (a_ut / a_in), phase_shift)
    (10, 272 / 264, 1),
    (100, 270 / 263, 1),
    (1000, 271 / 264, 6),
    (5000, 255 / 280, 28),
    (10_000, 202 / 278, 48),
    (50_000, 71 / 275, 86),
    (100_000, 46 / 275, 95),
    (500_000, 25 / 275, 120),
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
