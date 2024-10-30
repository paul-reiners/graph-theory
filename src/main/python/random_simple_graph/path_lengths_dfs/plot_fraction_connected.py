import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

v_exponents = range(2, 9)
vs = [2 ** exponent - 1 for exponent in v_exponents]
df = pd.read_csv('data/out/random_simple_graph/path_lengths_dfs/stats.csv')
labels = []
fig, ax = plt.subplots()
for v in vs:
    df_filtered = df[df['V'] == v]
    sns.lineplot(data=df_filtered, x="E", y="fraction_connected", label=v)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
plt.legend(title="V")

plt.savefig(f'doc/img/RandomSimpleGraph-PathLengthsDFS-fraction-connected.png')
