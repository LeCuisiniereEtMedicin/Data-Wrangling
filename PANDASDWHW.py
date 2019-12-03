import pandas as pd
math = {'Student': ['Ice Bear','Panda','Grizzly'],
        'Math': [80,95,79]};
elect = {'Student': ['Ice Bear','Panda','Grizzly'],
        'Electronics': [85,81,83]};
geas = {'Student': ['Ice Bear','Panda','Grizzly'],
        'GEAS': [90,79,93]};
esat = {'Student': ['Ice Bear','Panda','Grizzly'],
        'ESAT': [93,89,88]};
Math = pd.DataFrame(math, columns=['Student','Math'])
Elec = pd.DataFrame(elect, columns=['Student','Electronics'])
Geas = pd.DataFrame(geas, columns=['Student','GEAS'])
Esat = pd.DataFrame(esat, columns=['Student','ESAT'])
m1 = pd.merge(Math,Elec)
m2 = pd.merge(Geas,Esat)
Grades = pd.merge(m1,m2)
Long = pd.melt(Grades,id_vars='Student',var_name='Subject',value_name='Grades')