for i in range(24):
    for j in range(2):
        if i < 10:
            fileName = "day0"+i+"p"+j+".py"
        else:
            fileName = "day"+i+"p"+j+".py"
        with open(fileName,"w") as f:
            pass