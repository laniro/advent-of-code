if __name__ == "__main__":
    test = "C:/Users/tyler/Documents/advent of code/2024/test.txt"
    inp = "C:/Users/tyler/Documents/advent of code/2024/inp.txt"
    file_path = inp
    with open(file_path, "r") as f:
        f = f.readlines()
    f = [list(y) for y in f][0]

    free = []
    main_list = []
    mode = 'file'
    id = 0
    for i in range(len(f)):
        x = int(f[i])
        match mode:
            case 'file':
                mode = 'free'
                for i in range(x):
                    main_list.append(str(id))
                id += 1
            case 'free':
                mode = 'file'
                for i in range(x):
                    main_list.append('.')

    
    for i in range(len(main_list)):
        if main_list[i] != '.': continue
        free.append(i)
    

    periods_removed = 0
    for i in range(len(main_list)):
        print(i, len(main_list))
        if main_list[i] != '.': continue
        while main_list[-1] == '.':
            main_list.pop(-1)
            periods_removed += 1
        if i >= len(main_list): break
        main_list[i] = main_list[-1]
        main_list.pop(-1)
        periods_removed+=1
    for i in range(periods_removed): main_list.append('.')
    

    checksum = 0
    for i in range(len(main_list)):
        if main_list[i] == '.': break
        checksum += i * int(main_list[i])
    print(checksum)