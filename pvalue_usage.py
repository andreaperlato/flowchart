import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("t-Tests")
G.add_node("ANOVA")
G.add_node("Chi-Square Tests")
G.add_node("Chi-Square Goodness of Fit")
G.add_node("Regression Analysis")
G.add_node("Used to compare the means of two groups.")
G.add_node("Used to compare means among three or more groups.")
G.add_node("Used for categorical data to assess the association between variables.")
G.add_node("Tests if a sample distribution matches an expected distribution.")
G.add_node("Used to examine the relationship between dependent and independent variables.")

# Add edges to connect nodes to their descriptions
edges = [
    ("t-Tests", "Used to compare the means of two groups."),
    ("ANOVA", "Used to compare means among three or more groups."),
    ("Chi-Square Tests", "Used for categorical data to assess the association between variables."),
    ("Chi-Square Goodness of Fit", "Tests if a sample distribution matches an expected distribution."),
    ("Regression Analysis", "Used to examine the relationship between dependent and independent variables.")
]

G.add_edges_from(edges)

# Define positions for a better layout
pos = {
    "t-Tests": (0, 3),
    "Used to compare the means of two groups.": (1, 3),
    "ANOVA": (0, 2),
    "Used to compare means among three or more groups.": (1, 2),
    "Chi-Square Tests": (0, 1),
    "Used for categorical data to assess the association between variables.": (1, 1),
    "Chi-Square Goodness of Fit": (0, 0),
    "Tests if a sample distribution matches an expected distribution.": (1, 0),
    "Regression Analysis": (0, -1),
    "Used to examine the relationship between dependent and independent variables.": (1, -1),
}

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True, arrowstyle='-|>', arrowsize=12)

# Adding labels to the edges
edge_labels = {edge: edge[1] for edge in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Show the plot
plt.title("Flowchart of Common Statistical Tests Utilizing p-value", fontsize=14)
plt.show()





