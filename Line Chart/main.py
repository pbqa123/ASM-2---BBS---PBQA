import matplotlib.pyplot as plt
import pandas as pd

# Create sample data
data = {
    'Date': pd.date_range(start='1/1/2022', periods=100),
    'Value': np.random.randn(100).cumsum()
}

df = pd.DataFrame(data)

# Draw line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], label='Value over Time', color='blue')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Line Chart Example')
plt.legend()
plt.show()
