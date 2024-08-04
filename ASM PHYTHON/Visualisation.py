import matplotlib.pyplot as plt
import pandas as pd
# Create sample data
data = {
'Month': ['January', 'February', 'March', 'April', 'May'],
'Product A': [150, 200, 250, 300, 350],
'Product B': [80, 100, 120, 140, 160],
'Product C': [200, 220, 240, 260, 280]
}

# Convert to DataFrame
df = pd.DataFrame(data)