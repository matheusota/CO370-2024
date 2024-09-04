

import gurobipy as gp
from gurobipy import GRB



m = gp.Model("basic")

# Model for the following LP:
# maximize 2 x1 + 4 x2
# s.t.     3 x1 + 2 x2 <= 6
#            x1 + 5 x2 <= 5
#            x1 >= 0
#                   x2 >= 0


# NOTE: By default all variables have LB = 0, UB = infty (float('inf'))
# and are of type GRB.CONTINUOUS. You may change these parameters (they are optional)
x1 = m.addVar( ub=float('inf') , vtype = GRB.INTEGER, name = "x1" )
x2 = m.addVar( vtype = GRB.CONTINUOUS, lb = 0.0, name = "x2"  )

m.setObjective( 2 * x1 + 4 * x2, GRB.MAXIMIZE )

m.addConstr( 3 * x1 + 2 * x2 <= 6, "c1")
m.addConstr( x1 + 5 * x2 <= 5, "c2" )

m.optimize()


if m.status == GRB.OPTIMAL:
   print("\n**** SOLUTION OBTAINED FROM GUROBI ****")
   print("Cost: %g" % m.ObjVal)
   print("Vars:")
   print("  x1: " + str( x1.X ) )
   print("  x2: " + str( x2.X ) )
else:
   print("No solution")





