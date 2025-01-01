from pandas import read_csv
import os

dir = './data/in/vnc_matching_challenge'
male_connectome_graph_df = read_csv("./data/in/vnc_matching_challenge/male_connectome_graph.csv.gz")
male_connectome_graph_df = male_connectome_graph_df
male_edges = {(r[0], r[1]): int(r[2]) for _, r in male_connectome_graph_df.iterrows()}
female_edges = {(r[0], r[1]): int(r[2]) for _, r in read_csv("./data/in/vnc_matching_challenge/female_connectome_graph.csv.gz").iterrows()}
matching = {r[0]: r[1] for _, r in read_csv("./data/in/vnc_matching_challenge/vnc_matching_submission_benchmark_5154247.csv.gz").iterrows()}
alignment = 0
for male_nodes, edge_weight in male_edges.items():
  female_nodes = (matching[male_nodes[0]], matching[male_nodes[1]])
  alignment += min(edge_weight, female_edges.get(female_nodes, 0))
print(f"{alignment=}")
