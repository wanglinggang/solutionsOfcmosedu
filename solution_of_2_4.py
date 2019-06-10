#This is the solution of 2.4
t = 1e-6
R_square_min = 1.6e3
R_square_std = 2.0e3
R_square_max = 2.2e3
Resistivity_min = R_square_min * t
Resistivity_std = R_square_std * t
Resistivity_max = R_square_max * t
print("Resistivity_min = {0:2e},Resistivity_std = {1:2e},Resistivity_max = {2:2e}".format(Resistivity_min,Resistivity_std,Resistivity_max))
