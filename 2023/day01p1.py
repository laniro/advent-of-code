for i in range(24):
    for j in range(2):
        if i < 10:
            fileName = "day0"+str(i)+"p"+str(j)+".py"
        else:
            fileName = "day"+str(i)+"p"+str(j)+".py"
        with open(fileName,"w") as f:
            pass