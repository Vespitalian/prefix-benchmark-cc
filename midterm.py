import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark_results.csv')

pre_labels = ['c','ca','car','care','cares']
columns = ['slow','medium','fast']

plt.ylabel('Time in seconds over 10,000 runs')
plt.title('Prefix Benchmark Comparison')
plt.savefig('prefix_benchmark.png')
