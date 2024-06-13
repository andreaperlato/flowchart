import networkx as nx

# Creazione del grafo
G = nx.DiGraph()

# Aggiunta dei nodi
G.add_node("P-Value Utilization Across Fields")
G.add_node("Medicine and Healthcare")
G.add_node("Clinical Trials")
G.add_node("Medical Research")
G.add_node("Treatment Efficacy")
G.add_node("Social Sciences")
G.add_node("Psychology")
G.add_node("Sociology")
G.add_node("Education")
G.add_node("Behavioural Hypotheses")
G.add_node("Economics and Business")
G.add_node("Market Research")
G.add_node("Policy Evaluation")
G.add_node("Economic Modelling")
G.add_node("Biology and Environmental Science")
G.add_node("Genetic Variations")
G.add_node("Environmental Impacts")
G.add_node("Ecological Data")
G.add_node("Common Statistical Tests Utilizing p-value")
G.add_node("t-Tests")
G.add_node("Compare Means of Two Groups")
G.add_node("ANOVA (Analysis of Variance)")
G.add_node("Compare Means Among Three or More Groups")
G.add_node("Chi-Square Tests")
G.add_node("Categorical Data")
G.add_node("Association Between Variables")
G.add_node("Chi-Square Goodness of Fit")
G.add_node("Sample Distribution vs. Expected Distribution")
G.add_node("Regression Analysis")
G.add_node("Relationship Between Dependent and Independent Variables")

# Aggiunta degli archi
G.add_edges_from([
    ("P-Value Utilization Across Fields", "Medicine and Healthcare"),
    ("Medicine and Healthcare", "Clinical Trials"),
    ("Medicine and Healthcare", "Medical Research"),
    ("Medical Research", "Treatment Efficacy"),
    ("P-Value Utilization Across Fields", "Social Sciences"),
    ("Social Sciences", "Psychology"),
    ("Social Sciences", "Sociology"),
    ("Social Sciences", "Education"),
    ("Education", "Behavioural Hypotheses"),
    ("P-Value Utilization Across Fields", "Economics and Business"),
    ("Economics and Business", "Market Research"),
    ("Economics and Business", "Policy Evaluation"),
    ("Economics and Business", "Economic Modelling"),
    ("P-Value Utilization Across Fields", "Biology and Environmental Science"),
    ("Biology and Environmental Science", "Genetic Variations"),
    ("Biology and Environmental Science", "Environmental Impacts"),
    ("Biology and Environmental Science", "Ecological Data"),
    ("P-Value Utilization Across Fields", "Common Statistical Tests Utilizing p-value"),
    ("Common Statistical Tests Utilizing p-value", "t-Tests"),
    ("t-Tests", "Compare Means of Two Groups"),
    ("Common Statistical Tests Utilizing p-value", "ANOVA (Analysis of Variance)"),
    ("ANOVA (Analysis of Variance)", "Compare Means Among Three or More Groups"),
    ("Common Statistical Tests Utilizing p-value", "Chi-Square Tests"),
    ("Chi-Square Tests", "Categorical Data"),
    ("Categorical Data", "Association Between Variables"),
    ("Common Statistical Tests Utilizing p-value", "Chi-Square Goodness of Fit"),
    ("Chi-Square Goodness of Fit", "Sample Distribution vs. Expected Distribution"),
    ("Common Statistical Tests Utilizing p-value", "Regression Analysis"),
    ("Regression Analysis", "Relationship Between Dependent and Independent Variables")
])

# Salvataggio del grafo in formato GraphML
nx.write_graphml(G, "/Users/andreaperlato/Documents/code_repository/flowchart/p_value_utilization.graphml")
