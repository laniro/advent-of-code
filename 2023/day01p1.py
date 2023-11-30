for i in range(24):
    for j in range(2):
        if i < 10:
            fileName = "day0"+str(i+1)+"p"+str(j+1)+".py"
        else:
            fileName = "day"+str(i+1)+"p"+str(j+1)+".py"
        with open(fileName,"w") as f:
            pass