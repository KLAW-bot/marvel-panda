import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [23,39,90,69,44,30]
y = [10,20,29,21,17,70]

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.bar(x,y,color=['Red','Blue','Green','Pink','Black','Orange'])
plt.show()