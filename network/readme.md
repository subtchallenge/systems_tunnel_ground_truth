# Course Topology

This folder provides topology data for the DARPA Subterranean Challenge Tunnel Circuit. The topology of each course is represented as a simple undirected graph with no weights, self loops, or multiple edges.  Nodes were selected to represent navigation decision points in a way that captures the connectivity of the course while abstracting specifics of the geometry.  

### Files
* `data` folder - Contains edgelist data in CSV format.  For an explanation of the format and fields see Data Structure, below.
    * `data/ex_edgelist.csv` - Experimental course edgelist with metadata
    * `data/ex_edgelist_nodata.csv` - Experimental course edgelist without metadata
    * `data/sr_edgelist.csv` - Safety Research course edgelist with metadata
    * `data/sr_edgelist_nodata.csv` - Safety Research course edgelist without metadata
* `img` folder
    * `img/ex_network.png` - Visualization of the Experimental course graph
    * `img/sr_network.png` - Visualization of the Safety Research course graph
    * `img/tunnel_map.png` - Network for Tunnel courses overlaid on course floorplan

### Data Structure
Topologies are provided as edgelists in csv format.  Each edge is represented as a single row; the first and second columns of that row contain IDs for the nodes at either end of the edge. Files `data/{coursename}_edgelist.csv` contain one header row and the following metadata fields: length (`float`; meters) and notes (`string`).  Files `data/{coursename}_edgelist_nodata.csv` contain no headers or metadata.  Node 1 is in the transition area and node 2 is inside the course.

### Data Manipulation
Edgelists are compatible with a wide variety of graph manipulation software, such as Python, Matlab, Cytoscape, etc.  

In Python, packages like NetworkX can be used to visualize the graphs as follows:
```python
import networkx as nx
graph = nx.read_edgelist('data/sr_edgelist_nodata.csv')
nx.draw(graph)
```
Similar visualization is also available in Matlab:
```matlab
edges = readmatrix('data/sr_edgelist_nodata.csv');
startNode = edges(:,1); endNode = edges(:,2);
graph = graph(startNode, endNode);
plot(graph)
```

### Contact Information

If you have any questions or comments about this repository please contact:

* Ryan Halterman - ryhalt@spawar.navy.mil

* Heidi Hurst - heidi.hurst.ctr@darpa.mil

* SubT Challenge Mailbox - SubTChallenge@darpa.mil