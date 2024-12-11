with open("day 7\dayseven.txt") as temp:
  f = temp.read().split('\n')

dirs = {'/': []}
dirsizes = {'/': 0}

current = ''

for item in f:
  if '$ cd' in item:
    if '..' not in item: # $ cd x , move in one
      current = item[5:]
    elif '/' in item: # $ cd / , outermost directory
      current = '/'
    else: # $ cd .. , move out one
      for item in dirs:
        if 'dirs' + current in dirs[item]:
          current = item
  elif 'dir' in item:
    dirs[current].append(item)
    dirs[item[4:]] = []
    dirsizes[item[4:]] = 0
  elif '$' not in item:
    dirs[current].append(item)
  elif 'ls' in item:
    if dirs[current] == []:
      pass#print("Directory", current, "is empty")
    else:
      for item in dirs[current]:
        z = item.split()
        if 'dir' not in item:
          pass#print("Currently in", current+":", z[1],z[0])
        else:
          pass#print(z[0],z[1])



for dkey in dirs:
  for obj in dirs[dkey]:
    if 'dir' not in obj: 
      dirsizes[dkey] += int(obj.split()[0])

        
def help(inp):
  if 'dir' in inp:
    for item in dirs[inp[4:]]:
      if 'dir' in dirs[inp[4:]]:
        help(inp)
      else:
        dirsizes[dkey] += dirsizes[inp[4:]]

for dkey in dirs:
  for obj in dirs[dkey]:
    help(obj)

t=0
for item in dirsizes:
  if dirsizes[item] < 100000:
      t+=dirsizes[item]
print(t)
