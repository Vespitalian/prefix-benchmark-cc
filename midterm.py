import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark_results.csv',index_col=0)

prefix_labels = ['c','ca','car','care','cares']
df.columns = ['slow','medium','fast']
df.index = prefix_labels
df['timediff'] = df['slow'] - df['fast']
print(df.to_markdown())

plt.plot(df['fast'], label='Optimized Loop')
plt.plot(df['medium'], label='Improved Loop')
plt.plot(df['slow'], label='My loop')

plt.ylabel('Time (seconds)')
plt.xlabel('Prefixes')
plt.title('Prefix Benchmark Comparison Over 10,000 Runs')
plt.legend(reverse=True)
plt.savefig('prefix_benchmark.png')
