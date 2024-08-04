import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Time': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'Inventory': [120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65],
    'Material Consumption': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}

df = pd.DataFrame(data)

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Inventory'], marker='o', label='Inventory')
plt.plot(df['Time'], df['Material Consumption'], marker='s', label='Material Consumption')
plt.xlabel('Time')
plt.ylabel('Quantity')
plt.title('Line Chart Illustrating Inventory Levels and Material Consumption Over Time')
plt.legend()
plt.grid(True)
plt.show()
