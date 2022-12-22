filereader = open('fruits.txt','r')
filewriter = open('vegitable.txt','w')

for line in filereader:
    filewriter.write(line)

filereader.close()
filewriter.close()