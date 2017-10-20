f = open("running-config.cfg")
fin = f.read()
line = fin.strip(' ')
word = line.split()

print(word)



