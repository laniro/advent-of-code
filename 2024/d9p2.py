from timeit import default_timer as timer

if __name__ == "__main__":
    start = timer()
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readlines()
    f = [list(y) for y in f][0]

    free = []
    disk = []
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
                    disk.append(str(id))
                files.update({id: x})
                id += 1
            case 'free':
                mode = 'file'
                if x > 0:
                    disk.append('.' * x)
    print(f"Initialising drive... 100% complete.")
    print(f"Took {timer() - start} seconds.")

    frees = {}
    starting_length = len(disk)
    for i in range(len(disk)):
        print(f"Reorganising array... {int(i/starting_length*100)}% complete")
        if '.' not in disk[i]: continue
        if i in frees.keys(): continue
        
        length = len(disk[i])
        for j in range(length):
            frees.update({i+j:length-j})
        disk.pop(i)

        for x in range(length):
            disk.insert(i, '.')
    print(f"Reorganising array... 100% complete")
    print(f"Took {timer() - start} seconds.")

    for key in list(files.keys())[::-1]:
        ind = disk.index(str(key))
        if len(frees.values()) == 0: 
            print("No free space on disk. Breaking")
            break
        if files[key] > max(frees.values()): 
            print(f"File {key} larger than all free space on disk. Skipping")
            continue
        
        for i in range(disk.index('.'),len(disk)):
            if i > ind: 
                print(f"Trying to move file {key} right. Skipping")
                break
            if '.' not in disk[i]: 
                #print("No '.' at ", i,", Continuing")
                continue
            if i not in frees.keys() or files[key] > frees[i]: 
                #print("File bigger than free space at index ", i)
                continue

            print(f"File {key} moved to index {i}. File of length {files[key]}, free space of length {frees[i]}")
            
            for j in range(files[key]):
                if disk[ind + j] == str(key):
                    disk[ind+j] = '.'
                    frees.update({ind+j:files[key]-j})
                disk[i+j] = str(key)
                frees.pop(i+j)
            break
        else:
            print(f"No space was found for file {key} of length {files[key]}")

    checksum = 0
    
    for i in range(len(disk)):
        if '.' in disk[i]: continue
        checksum += i * int(disk[i])
    print(checksum)
    print(f"Took {timer() - start} seconds.")