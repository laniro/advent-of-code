total = 0
indices = [1,2,3,4,5,6,7,8,9,"one","two","three","four","five","six","seven","eight","nine"]
list = []

with open("2023/test.txt","r") as f:
    for line in f.readlines():
        list = []
        for item in indices:
            if str(item) in line:
                list.append(item)

        # convert words to numbers

        # iterate through presence list and find indices

        # generate new list with indices. both lists match ie present numbers [1,2,9] matches to indices [3,0,4]

        # get index in presence list of lowest and highest indices ie lowest = 0 --> 2, highest = 4 --> 9

        # concatenate lowest + highest number

        # add to total

        print(list)

