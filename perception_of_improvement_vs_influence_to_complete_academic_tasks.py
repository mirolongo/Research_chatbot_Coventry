import matplotlib.pyplot as plt
import numpy as np

perception_of_improvement = [
    3, 3, 2, 2, 3, 2, 3, 1, 2, 2, 3, 3, 2, 1, 1, 2, 3, 3, 3, 2, 3, 1, 1, 2, 3, 1, 2, 2, 2, 3, 3, 2, 2, 1, 3, 3, 3, 3, 2, 3, 2, 2, 3, 2, 2
]
influence_to_complete_academic_tasks = [
    4, 4, 2, 1, 3, 1, 3, 3, 2, 2, 3, 3, 1, 2, 2, 3, 3, 3, 1, 3, 1, 4, 4, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 1, 3, 2, 3, 3, 3, 3, 2, 3, 2, 3
]

plt.scatter(perception_of_improvement, influence_to_complete_academic_tasks, color='blue', label='Data Points')
slope = 0.14
intercept = 2.66
plt.plot(np.array(perception_of_improvement), slope * np.array(perception_of_improvement) + intercept, color='red', label='Regression Line')

plt.xlabel('Perception of Improvement')
plt.ylabel('Influence to Complete Academic Tasks')
plt.title('Perception of Improvement vs. Influence to Complete Academic Tasks')
plt.legend()
plt.grid(True)
plt.show()
