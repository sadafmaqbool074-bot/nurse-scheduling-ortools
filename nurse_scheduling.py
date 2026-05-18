!pip install ortools
from ortools.sat.python import cp_model
num_nurses = 5
num_days = 7
num_shifts =3
all_nurses = range(num_nurses)
all_days = range(num_days)
all_shifts = range(num_shifts)
model = cp_model.CpModel()
shifts = {}
for n in all_nurses:
  for d in all_days:
    for s in all_shifts :
      shifts[(n,d,s)] = model.NewBoolVar(f"shifts_{(n,d,s)}")
#Constraints
# Each shift has exactly one nurse
for d in all_days:
  for s in all_shifts:
    model.AddExactlyOne(shifts[(n,d,s)] for n in all_nurses)
    #Each Nurse work at most 1 shift per day
    for n in all_nurses:
      for d in all_days :
        model.AddAtMostOne(shifts[(n,d,s)] for s in all_shifts)
#Rest Constraints
for n in all_nurses:
    for d in range(num_days -1):
     model.Add(shifts[(n,d,2)]+ shifts[(n,d+1,2)]<=1)
for n in all_nurses:
    for d in range(num_days-1):
     model.Add(shifts[(n,d,2)] +shifts[(n,d+1,0)]<=1)

# Constraints: Nurse 0 and Nurse 1 cannot work night shifts
for d in all_days:
  model.Add(shifts[(0,d,2)] == 0)
  model.Add(shifts[(1,d,2)] == 0)

# Calculate workloads for each nurse 
workloads = []
for n in all_nurses:
   w= model.NewIntVar(0,num_days*num_shifts,f"workloads_{n}")
   # Workload for nurse 'n' is the sum of all shifts they work
   model.Add(w == sum(shifts[(n,d,s)] for d in all_days for s in all_shifts))
   workloads.append(w)

ideal = num_days*num_shifts/num_nurses
deviations =[]
for n in all_nurses:
  diff =model.NewIntVar(0,num_days*num_shifts,f"diff_{n}")
model.AddAbsEquality(diff,workloads[n]-int(ideal))
deviations.append(diff)
model.Minimize(sum(deviations)) # Minimize added once after all deviations are collected
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE: 
    print("schedule")
    for d in all_days:
      print(f"Day{d}:")
      for n in all_nurses:
        for s in all_shifts:
          if solver.Value(shifts[(n,d,s)]) == 1:
            shift_name = ["Morning", "Afternoon", "Night"][s]
            print(f"  {shift_name}: Nurse {n}") 
else:
  print("no solution ")
