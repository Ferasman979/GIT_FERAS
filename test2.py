dict={'A': [('B', '2'),('D', '3')],'D': [('A', '5'),('G', '2')],'G':[('X','2'),('C','2')]}
source=str(input("Enter source: "))
dest= str(input("Enter destination: "))
path=[]
#path.append(source)
for x in dict:
    
    if source==dest:
        print("Destination reached!")
        break

    for source in dict:
        path.append(source)
        for i in range(0,len(dict[source])):
            max= dict[source][0][1]
            if dict[source][i][1]>max:
                max= dict[source][i][1]
                print(max+"is the longest route")
                term=dict[source][i][0]
                path.append(term)
                path.remove(term)
                source=term
                if source==dest:
                   print("Destination reached")
                   break
            else:
                continue
            if source==dest:
                print("Destination reached")
                break
    else:
        path.append(dest)
        print("Destination reached")
        break
        #continue
print(path)


