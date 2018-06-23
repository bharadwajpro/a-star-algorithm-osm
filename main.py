import xml.etree.ElementTree
import requests
import random
API_KEY = '<API_KEY_HERE>'
GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'


class Node:
    def __init__(self, node_id, lat, lon):
        self.nid = node_id
        self.lat = lat
        self.lon = lon
        self.neighbours = set()
        self.parent = None
        self.H = 0
        self.G = 0


def matrix_api(point1, point2, dis_time):
    payload = {
        'origins': point1.lat + ',' + point1.lon,
        'destinations': point2.lat + ',' + point2.lon,
        'key': API_KEY
    }
    r = requests.get(GOOGLE_API_URL, params=payload)
    output = r.json()
    if dis_time == 'distance':
        return output["rows"][0]["elements"][0]["distance"]["value"]
    else:
        return output["rows"][0]["elements"][0]["duration"]["value"]


def a_star(network_graph, start, goal, dis_time):
    start = network_graph[start]
    goal = network_graph[goal]
    open_set = set()
    closed_set = set()
    current = start
    open_set.add(current)
    while open_set:
        print('Current', current.nid, current.lat, current.lon)
        current = min(open_set, key=lambda n: n.G + n.H)
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        open_set.remove(current)
        closed_set.add(current)
        for n_node in current.neighbours:
            n_node = node_dict[n_node]
            if n_node in closed_set:
                continue
            if n_node in open_set:
                new_g = current.G + matrix_api(current, n_node, dis_time)
                if n_node.G > new_g:
                    n_node.G = new_g
                    n_node.parent = current
            else:
                n_node.G = current.G + matrix_api(current, n_node, dis_time)
                n_node.H = matrix_api(n_node, goal, dis_time)
                n_node.parent = current
                open_set.add(n_node)
    raise ValueError('No Path Found')


def connect_two_nodes(node1, node2):
    node_dict[node1].neighbours.add(node2)
    node_dict[node2].neighbours.add(node1)


tree = xml.etree.ElementTree.parse('bits-dsnr.osm')
nodes = tree.findall('node')
ways = tree.findall('way')

node_dict = dict()
for node in nodes:
    nid = int(node.get('id'))
    n_lat = node.get('lat')
    n_lon = node.get('lon')
    node_dict[nid] = Node(nid, n_lat, n_lon)


for way in ways:
    nodes = way.findall('nd')
    for i in range(len(nodes) - 1):
        node_a = int(nodes[i].get('ref'))
        node_b = int(nodes[i+1].get('ref'))
        connect_two_nodes(node_a, node_b)

no_nodes = len(node_dict.keys())
# source = list(node_dict.keys())[random.randint(0, no_nodes)]
# destination = list(node_dict.keys())[random.randint(0, no_nodes)]
source = 2234830423
destination = 3612562109
final_path = a_star(node_dict, source, destination, 'distance')
print('Final Path')
for p in final_path:
    print(p.nid, p.lat, p.lon, end=', ')
