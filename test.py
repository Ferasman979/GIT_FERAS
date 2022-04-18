"""a="2"
print(a.isdigit())
print(a.isalpha())

a="A1"
print(a.isalpha())
print(a.isalnum())"""

lst=[[('B', '2'), ('D', '3')],[('G','3'),('F','5')]]
dest='D' 
for x in lst:
    if dest not in lst[x]:
      print("lol")
