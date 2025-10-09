import pandas as pd
from benchmark import prefixes
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark_results.csv',index_col=0) # Need to set index column to 0 because pandas creates a fake empty column.

prefix_labels = prefixes # Grabs the prefixes used in the benchmark.
df.columns = ['slow','medium','fast']
df.index = prefix_labels
df['timediff'] = df['slow'] - df['fast'] # Creates a new colum using vector subtraction to calculate the time difference across columns.
print(df.to_markdown())

plt.plot(df['fast'], label='Optimized Loop', color='green')
plt.plot(df['medium'], label='Improved Loop', color='orange')
plt.plot(df['slow'], label='My loop', color='red')
plt.legend(reverse=True)
plt.grid(True)

plt.xlabel('Prefixes')
plt.ylabel('Time (seconds)')
plt.title('Prefix Benchmark Comparison Over 10,000 Runs')
plt.savefig('prefix_benchmark.png')
