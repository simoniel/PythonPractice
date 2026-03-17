

f = open("boardgames_ranks.csv")
count = 0
for l in f:
    print(l)
    count += 1
    if count > 10:
        break

#out_file = open("out_test.txt",'w')
#out_file.write("ciao")

