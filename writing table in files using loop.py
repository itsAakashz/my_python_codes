
for i in range(2,21):
    with open(f"table/TABLE_of{i}_.txt",  "w") as F:
        for j in range(1,11):
            F.write(f"{i}X{j}={i*j}")
            if j!=10:
                F.write('\n')
