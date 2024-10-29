import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

v_exponents = range(1, 9)
vs = [2 ** exponent - 1 for exponent in v_exponents]
df = pd.read_csv('data/out/erdos_renyi_graph/path_lengths_dfs/stats.csv')
data_preproc = pd.DataFrame({
    'E': E, 
    'A': np.random.randn(num_rows).cumsum(),
    'B': np.random.randn(num_rows).cumsum(),
    'C': np.random.randn(num_rows).cumsum(),
    'D': np.random.randn(num_rows).cumsum()})
for v in vs:
    df_filtered = df[df['V'] == v]
    print(df_filtered)
    sns.lineplot(data=df_filtered, x="E", y="fraction_connected")
    plt.savefig(f'V-{v}.png')
