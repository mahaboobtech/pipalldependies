import re

f = open("/home/$username/anyfolder/file.txt",'r+')
pata = f.read()
comp = []
comp.append(re.findall(r"^.[^-]{22}",pata,flags=re.MULTILINE))
f.close()
print(len(comp[0]))
print(comp[0])
g = open("/home/$username/Desktop/pipdep.txt","w+")
for l in range (len(comp[0])):
    g.writelines(str(comp[0][l]))
    g.write("\n")
g.seekable()
g.close()
