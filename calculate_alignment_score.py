import pandas as pd

# Define file paths
DATA_DIR = '/users/9/reine097/projects/graph-theory/data/in/vnc_matching_challenge'
MALE_GRAPH_FILE = f"{DATA_DIR}/male_connectome_graph.csv.gz"
MALE_EDGES = None
FEMALE_GRAPH_FILE = f"{DATA_DIR}/female_connectome_graph.csv.gz"
FEMALE_EDGES = None
MATCHING_FILE = f"{DATA_DIR}/vnc_matching_submission_benchmark_5154247.csv.gz"
MATCHING_EDGES = None


def get_male_edges():
    if MALE_EDGES == None:
        MALE_EDGES = load_edges(MALE_GRAPH_FILE)
    
    return MALE_EDGES

def get_matching_edges():
    if MATCHING_EDGES == None:
        MATCHING_EDGES = load_edges(MATCHING_FILE)

    return MATCHING_EDGES


def get_female_edges():
    if FEMALE_EDGES == None:
        FEMALE_EDGES = load_edges(FEMALE_GRAPH_FILE)
    
    return FEMALE_EDGES


def load_edges(file_path):
    """Load edges from a CSV file into a dictionary."""
    df = pd.read_csv(file_path)
    return {(row[0], row[1]): int(row[2]) for _, row in df.iterrows()}


def load_matching(file_path):
    """Load matching data from a CSV file into a dictionary."""
    df = pd.read_csv(file_path)
    return {row[0]: row[1] for _, row in df.iterrows()}


def calculate_alignment(male_edges, female_edges, matching):
    """Calculate the alignment score based on edges and matching."""
    alignment = 0
    for (male_node1, male_node2), edge_weight in male_edges.items():
        female_nodes = (matching.get(male_node1), matching.get(male_node2))
        alignment += min(edge_weight, female_edges.get(female_nodes, 0))
    return alignment


# Main execution
if __name__ == "__main__":
    male_edges = load_edges(MALE_GRAPH_FILE)
    female_edges = load_edges(FEMALE_GRAPH_FILE)
    matching = load_matching(MATCHING_FILE)

    alignment = calculate_alignment(male_edges, female_edges, matching)
    print(f"{alignment=}")
