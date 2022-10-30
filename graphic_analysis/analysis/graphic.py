import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

def graph_analysis(self, df, xAxis, yAxis):
    df.groupby(xAxis)[yAxis].sum().plot.bar(title=f"{xAxis} X {yAxis}")
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.xticks(rotation = "horizontal");