from timeit import default_timer as timer

if __name__ == "__main__":
    start = timer()
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = test
    with open(file_path, "r") as f:
        f = f.readlines()
    f = [list(y) for y in f][0]

    free = []
    main_list = []
    mode = 'file'
    id = 0
    files = {}

    for i in range(len(f)):
        x = int(f[i])
        print(f"Initialising drive... {int(i/len(f)*100)}% complete.")
        match mode:
            case 'file':
                mode = 'free'
                for i in range(x):
                    main_list.append(str(id))
                files.update({id: x})
                id += 1
            case 'free':
                mode = 'file'
                if x > 0:
                    main_list.append('.' * x)
    print(f"Initialising drive... 100% complete.")
    print(f"Took {timer() - start} seconds.")

    frees = {}
    starting_length = len(main_list)
    for i in range(len(main_list)):
        print(f"Reorganising array... {int(i/starting_length*100)}% complete")
        if '.' not in main_list[i]: continue
        if i in frees.keys(): continue
        
        length = len(main_list[i])
        for j in range(length):
            frees.update({i+j:length})
        main_list.pop(i)

        for x in range(length):
            main_list.insert(i, '.')
    print(f"Reorganising array... 100% complete")
    print(f"Took {timer() - start} seconds.")

    for key in list(files.keys())[::-1]:
        if files[key] > max(frees.values()): 
            print(f"File {key} larger than all free space on disk. Skipping")
            continue
        for i in range(main_list.index('.'),len(main_list)):
            if '.' not in main_list[i]: 
                #print("No '.' at ", i,", Continuing")
                continue
            if i not in frees.keys(): 
                #print("No free space at index ",i)
                continue
            if files[key] > frees[i]: 
                #print("File bigger than free space at index ", i)
                continue

            print(f"File {key} moved to index {i}. File of length {files[key]}, free space of length {frees[i]}")
            
            ind = main_list.index(str(key))
            for j in range(10):
                if ind+j >= len(main_list): break
                if main_list[ind + j] == str(key):
                    main_list[ind+j] = '.'
            
            for j in range(files[key]):
                main_list[i+j] = str(key)
                frees[i+j] = 0
                if i+j+1 not in frees.keys(): break
                frees[i+j+1] -= files[key]
            break
        else:
            print(f"No space was found for file {key} of length {files[key]}")

    checksum = 0
    
    for i in range(len(main_list)):
        if '.' in main_list[i]: continue
        checksum += i * int(main_list[i])
    print(checksum)
    print(f"Took {timer() - start} seconds.")