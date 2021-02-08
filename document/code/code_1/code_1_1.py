f = open('open.mp3')
t = open('open.txt','w')
for eachline in f:
    t.write(eachline)
f.close
t.close
