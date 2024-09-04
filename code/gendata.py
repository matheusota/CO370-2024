

import gurobipy as gp
from gurobipy import GRB



m = gp.Model("gendata")


f = open("data2.txt", "rt")

data = f.readlines()

n = len( data )

objs = []
coeffs = []

for line in data:
    [ varobj, varcoeff ] = line.split(",")
    objs.append( float( varobj ) )
    coeffs.append( float( varcoeff ) )

print( data )
print( objs )
print( coeffs )

# Model for the following LP:
# maximize sum_{i=1}^n objs[i] * x[i]
# s.t.     sum_{i=1}^n coeffs[i] * x[i] <= rhs
#            x >= 0


# NOTE: By default all variables have LB = 0, UB = infty (float('inf'))
# and are of type GRB.CONTINUOUS. You may change these parameters (they are optional)

# Here we are creating n variables that are continuous, with name x...
x = m.addVars( n, vtype = GRB.CONTINUOUS, name = "x" )

m.setObjective( x.prod( objs ), GRB.MAXIMIZE )

rhs = 10.0

c1 = m.addConstr( x.prod( coeffs ) <= rhs, "c1")

m.optimize()

if m.status == GRB.OPTIMAL:
   print("\n**** SOLUTION OBTAINED FROM GUROBI ****")
   print("Cost: %g" % m.ObjVal)
   print("Vars:")
   for i in range( n ):
      print(x[i].VarName +  " : " + str( x[i].X ) )
else:
   print("No solution")





