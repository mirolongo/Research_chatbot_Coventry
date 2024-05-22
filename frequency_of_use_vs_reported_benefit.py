import matplotlib.pyplot as plt
import numpy as np

frequency_of_use_clean = [
    4.0, 4.0, 5.0, 3.0, 5.0, 4.0, 3.0, 5.0, 3.0, 5.0, 3.0, 4.0, 3.0, 4.0, 4.0, 3.0, 5.0, 4.0, 3.0, 4.0, 3.0, 4.0, 3.0, 4.0, 3.0, 3.0, 4.0, 3.0, 4.0
]
reported_benefits_clean = [
    4.0, 4.0, 3.0, 4.0, 4.0, 4.0, 3.0, 5.0, 4.0, 5.0, 3.0, 3.0, 3.0, 4.0, 4.0, 3.0, 3.0, 4.0, 3.0, 4.0, 4.0, 4.0, 3.0, 4.0, 4.0, 4.0, 4.0, 3.0, 4.0
]

frequency_of_use_np = np.array(frequency_of_use_clean)
reported_benefits_np = np.array(reported_benefits_clean)

slope, intercept = np.polyfit(frequency_of_use_np, reported_benefits_np, 1)

plt.bar(frequency_of_use_clean, reported_benefits_clean, color='blue', label='Reported Benefits')

plt.plot(frequency_of_use_np, slope * frequency_of_use_np + intercept, color='red', label='Trend Line')
