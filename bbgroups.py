f = open("groups.csv")
br=[]
sl=[]
gl=[]
ky=[]
for line in f:
    line = line.split(",")
    if line[0]:
        br.append(line[0])
    if line[1]:
        sl.append(line[1])
    if line[2]:
        gl.append(line[2])
    if line[3] and line[3]!="\r\n":
        ky.append(line[3][:-2])

print len(br),len(sl),len(gl)

for b in br:
    for s in sl:
        if b == s:
            br.remove(b)
            break

    
for s in sl:
    print s
    for g in gl:
        if s==g:
           # print s, g
            sl.remove(s)
            break

print "bronze users: ", len(br)," | silver users: ", len(sl)," | gold users: ", len(gl), " | keyholders: ", len(ky)
                
