import matplotlib.pyplot as plt
import numpy as np

frequency_of_use = [
    4, 4, 5, 2, 3, 5, 2, 4, 3, 5, 3, 2, 5, 3, 5, 4, 4, 4, 3, 4, 2, 4, 5, 4, 3, 4, 3, 2, 4, 4, 4, 3, 4, 3, 2, 2, 4, 2, 4, 2, 4, 5, 4, 5, 4
]
advancement_in_studies = [
    4, 4, 3, 5, 4, 4, 3, 4, 4, 5, 3, 3, 5, 3, 3, 4, 4, 4, 3, 4, 2, 4, 5, 4, 3, 4, 3, 3, 5, 4, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 5, 4, 5, 4
]

plt.scatter(frequency_of_use, advancement_in_studies, color='blue', label='Data Points')
slope = 0.09
intercept = 3.22
plt.plot(np.array(frequency_of_use), slope * np.array(frequency_of_use) + intercept, color='red', label='Regression Line')

plt.xlabel('Frequency of Use')
plt.ylabel('Advancement in Studies Perception')
plt.title('Frequency of Use vs. Advancement in Studies Perception')
plt.legend()
plt.grid(True)
plt.show()
