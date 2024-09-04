

import gurobipy as gp
from gurobipy import GRB


# Model for the following LP:
# maximize sum_{i=1}^n objs[i] * x[i]
# s.t.     sum_{i=1}^n coeffs[i] * x[i] <= rhs
#            x >= 0



# Receives as input:
##  The gurobi model (already initialized)
##    the number of variables (n)
##    the objective function coefficients,
##    the constraint coefficients
##    the RHS
# returns the optimal value
def solveProblem( model, n, objcoeffs, constrcoeffs, rhs ):
    # Here we are creating n variables that are continuous, with name x...
    x = model.addVars( n, vtype = GRB.CONTINUOUS, name = "x" )

    model.setObjective( x.prod( objcoeffs ), GRB.MAXIMIZE )


    c1 = model.addConstr( x.prod( constrcoeffs ) <= rhs, "c1")

    model.optimize()

    if model.status == GRB.OPTIMAL:
        print("\n**** SOLUTION OBTAINED FROM GUROBI ****")
        print("Cost: %g" % model.ObjVal)
        print("Vars:")
        for i in range( n ):
            print(x[i].VarName +  " : " + str( x[i].X ) )
    else:
        print("No solution")

    return model.ObjVal






m = gp.Model("gendata2")


f = open("data2.txt", "rt")

data = f.readlines()

n = len( data )

objs = []
coeffs = []

for line in data:
    [ varobj, varcoeff ] = line.split(",")
    objs.append( float( varobj ) )
    coeffs.append( float( varcoeff ) )


objval = solveProblem( m, n, objs, coeffs, 10.0 )
print(" LEFT THE FUNCTION: RETURNED VALUE " + str(objval) )





