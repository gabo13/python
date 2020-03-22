line = '2020;9;2020.02.29.;0;0 Ft;105;952 080 Ft;8033;12 940 Ft;208011;1 325 Ft;13;15;17;23;37'
print(line)
temp=list(line.rstrip().split(';'))
print(temp)
print(list(map(int,temp[0:2]+temp[11:16])))
#3287 Libre Calc utolsó sort