from scipy.spatial import KDTree

TEST = False
N = 10 if TEST else 1000

with open(f"{'test_' if TEST else ''}input.txt") as file:
    txt = file.read()[:-1]

box_positions = [[int(x), int(y), int(z)] for x, y, z in (line.split(",") for line in txt.split("\n"))]

tree = KDTree(box_positions)
distances, indices = tree.query(box_positions, k=len(box_positions))
edges = set()
for i, (indices, distances) in enumerate(zip(indices, distances)):
    for j, (index, distance) in enumerate(zip(indices[1:], distances[1:])):
        edges.add((min(i, index), max(i, index), distance))

edges = sorted(edges, key=lambda x: x[2])

circuits = {}
circuit_map = {}
next_circuit_id = 0
boxes_in_circuits = 0

def connect_edge(edge):
    global next_circuit_id
    global boxes_in_circuits

    c0 = circuit_map.get(edge[0])
    c1 = circuit_map.get(edge[1])
    if c0 is None and c1 is None:
        circuit_map[edge[0]] = next_circuit_id
        circuit_map[edge[1]] = next_circuit_id
        circuits[next_circuit_id] = 2
        next_circuit_id += 1
        boxes_in_circuits += 2
    elif c0 is not None and c1 is not None:
        if c0 != c1:
            [cid, removed_cid] = sorted([c0, c1])
            for k, v in circuit_map.items():
                if v == removed_cid:
                    circuit_map[k] = cid
                    circuits[cid] += 1
            del circuits[removed_cid]
    else:
        cid = c0 if c0 is not None else c1
        circuit_map[edge[0]] = cid
        circuit_map[edge[1]] = cid
        circuits[cid] += 1
        boxes_in_circuits += 1

for edge in edges[:N]:
    connect_edge(edge)

circuit_sizes = sorted(circuits.values(), reverse=True)

print("Part 1:", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])

for edge in edges[N:]:
    connect_edge(edge)
    if len(circuits) == 1 and boxes_in_circuits == len(box_positions):
        box0 = box_positions[edge[0]]
        box1 = box_positions[edge[1]]
        print("Part 2:", box0[0] * box1[0])
        break