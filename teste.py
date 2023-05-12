import json
from pyvis.network import Network


# create network
nodes = [
    {"id": 1, "label": "Node 1", "color": "blue"},
    {"id": 2, "label": "Node 2", "color": "red"},
    {"id": 3, "label": "Node 3", "color": "green"}
]
edges = [
    {"from": 1, "to": 2},
    {"from": 1, "to": 3}
]
options = {
    "height": "600px",
    "width": "100%",
    "physics": {"enabled": False}
}
network = Network("container", options=options)
network.add_nodes(nodes)
network.add_edges(edges)

# create legend
legend = [
    {"color": "blue", "label": "Category 1"},
    {"color": "red", "label": "Category 2"},
    {"color": "green", "label": "Category 3"}
]

# add legend to network
margin_top = "-150px"
network.set_options("""
var div = document.createElement("div");
div.style.position = "absolute";
div.style.top = "{}";
div.style.left = "50px";
div.style.width = "150px";
div.style.padding = "10px";
div.style.backgroundColor = "#f4f4f4";
div.style.border = "1px solid #ccc";
div.innerHTML = "<h4>Legend</h4>";
document.body.appendChild(div);
""".format(margin_top))

for item in legend:
    network.set_options("""
    var div = document.createElement("div");
    div.style.backgroundColor = "{}";
    div.style.width = "20px";
    div.style.height = "20px";
    div.style.border = "1px solid black";
    div.style.display = "inline-block";
    div.style.marginRight = "5px";
    div.innerHTML = "{}";
    document.querySelector("#container > div > div:nth-child(1)").appendChild(div);
    """.format(item["color"], item["label"]))
