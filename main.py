import matplotlib.pyplot as plt
import pandas as  pd
data = pd.read_csv('iphone_price.csv')
plt.scatter(data['version'], data['price'])
plt.show()