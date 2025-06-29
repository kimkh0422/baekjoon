count = int(input())
points = []

for i in range(count):
    a,b = map(int,input().split())
    points.append((a,b))

sorted_points = sorted(points,key= lambda x: (x[1],x[0]))

for x,y in sorted_points:
    print(x,y)