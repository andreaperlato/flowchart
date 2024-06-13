import xml.etree.ElementTree as ET

def create_graphml():
    # Create the root element
    graphml = ET.Element("graphml", 
                         xmlns="http://graphml.graphdrawing.org/xmlns", 
                         attrib={"xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                                 "xsi:schemaLocation": "http://graphml.graphdrawing.org/xmlns "
                                                       "http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd"})

    # Create the graph element
    graph = ET.SubElement(graphml, "graph", id="G", edgedefault="directed")

    # Define nodes
    nodes = ["Start", "Process", "End"]
    node_ids = []
    for i, node in enumerate(nodes):
        node_id = f"n{i}"
        node_ids.append(node_id)
        node_element = ET.SubElement(graph, "node", id=node_id)
        data = ET.SubElement(node_element, "data", key="d0")
        data.text = node

    # Define edges
    edges = [(0, 1), (1, 2)]
    for source, target in edges:
        ET.SubElement(graph, "edge", source=node_ids[source], target=node_ids[target])

    # Write to a GraphML file
    tree = ET.ElementTree(graphml)
    with open("pvalue_usage_v1.graphml", "wb") as f:
        tree.write(f)

if __name__ == "__main__":
    create_graphml()
    print("GraphML file created successfully!")


