from vector import Vector

v = Vector(3)
v2 = Vector(3)

v.change_elem(1, 9)
v.change_elem(2, 7)

v2.change_elem(1, 9)
v2.change_elem(2, 7)

mul = v*v2
# print(mul)

w = Vector(3)

w.read_from_file('file.json')
v2.write_to_file('file.json')