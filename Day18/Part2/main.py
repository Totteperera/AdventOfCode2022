from collections import deque
import sys
filename = sys.argv[1]

lines = [tuple(map(int, x.split(","))) for x in open(filename).read().split("\n")]

offsets = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]
faces = {}

for x,y,z in lines:
    for dx,dy,dz in offsets:
        k = (x + dx, y + dy, z + dz)

        if k not in faces:
            faces[k] = 0
        faces[k] += 1

max_x = max([x[0] for x in lines]) + 1
min_x = min([x[0] for x in lines]) - 1
max_y = max([x[1] for x in lines]) + 1
min_y = min([x[1] for x in lines]) - 1
max_z = max([x[2] for x in lines]) + 1
min_z = min([x[2] for x in lines]) - 1

going_next = [(1,0,0), (0,1,0), (0,0,1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
air = set()
q = deque([(min_x, min_y, min_z)])
air.add((min_x, min_y, min_z))

while q:
    x,y,z = q.popleft()

    for dx,dy,dz in going_next:
        nx,ny,nz = key = (x + dx, y + dy, z + dz)

        if not (min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z):
            continue
        
        if key in lines:
            continue

        if key in air:
            continue

        air.add(key)
        q.append(key)

air_faces = set()

for x,y,z in air:
    for dx,dy,dz in offsets:
        air_faces.add((x + dx, y + dy, z + dz))

print(len(air_faces))
print(len(faces))
print(len(set(faces) & air_faces))