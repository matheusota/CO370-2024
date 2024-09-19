import gurobipy as gp
from gurobipy import GRB

m = gp.Model("flights")

f = open("../data/flights.txt", "r")

data = f.readlines()

# First line contains number of canceled flights and number of partner flights.
line_index = 0
L = data[0].strip().split(" ")
n_canceled = int(L[0])
n_flights = int(L[1])
line_index += 1

# Construct the set of vertices.
vertices = []
for i in range(n_canceled):
    vertices.append("s" + str(i))
    vertices.append("t" + str(i))
for j in range(n_flights):
    vertices.append("f" + str(j))

# Now we have lines for each of the canceled flights with the number of passengers.
passengers = []
for i in range(n_canceled):
    L = data[line_index].strip().split(" ")
    line_index += 1
    passengers.append(int(L[1]))

# Next, we have the lines with the partner flights and the number of seats.
seats = []
for i in range(n_flights):
    L = data[line_index].strip().split(" ")
    line_index += 1
    seats.append(int(L[1]))

# To ease the implementation, we create dictionaries of out-neighbors and in-neighbors
# and we initialize these with empty lists.
out_neighbors = {}
in_neighbors = {}
for v in vertices:
    out_neighbors[v] = []
    in_neighbors[v] = []

# We also have a dictionary to store the gurobi flow variables.
flow = {}

# Now we read the arcs.
while line_index < len(data):
    [u, v] = data[line_index].strip().split(" ")
    line_index += 1

    # Create the Gurobi variables.
    for i in range(n_canceled):
        flow[(u, v, i)] = m.addVar(
            lb=0,
            ub=passengers[i],
            vtype=GRB.INTEGER,
            name="f_" + u + "," + v + "," + str(i),
        )

    # Add entries to the in/out neighbor dictionaries.
    out_neighbors[u].append(v)
    in_neighbors[v].append(u)

# Set objective function.
obj_expr = 0
for u in vertices:
    if u[0] == "s":
        for v in out_neighbors[u]:
            i = int(u[1:])
            obj_expr += flow[(u, v, i)]

m.setObjective(obj_expr, GRB.MAXIMIZE)

# Set flow conservation constraints.
for i in range(n_canceled):
    for u in vertices:
        if u == "s" + str(i) or u == "t" + str(i):
            continue

        expr = 0
        for v in in_neighbors[u]:
            expr += flow[(v, u, i)]
        for v in out_neighbors[u]:
            expr -= flow[(u, v, i)]
        m.addConstr(expr == 0.0)

# Set seat capacity constraints.
for j in range(n_flights):
    expr = 0
    for v in in_neighbors["f" + str(j)]:
        for i in range(n_canceled):
            expr += flow[(v, "f" + str(j), i)]
    m.addConstr(expr <= seats[j])

m.write("test.lp")
m.optimize()

if m.status == GRB.OPTIMAL:
    print("Optimal solution found!")

    # Print objective value
    print("Objective value:", m.objVal)

    # Print decision variable values that are non-zero
    for v in m.getVars():
        if v.x != 0:
            print(v.varName, "=", v.x)

else:
    print("Optimal solution not found.")
