# TASK 2: TUPLES AND BUS-STOP DATA
import time
stops = {
 (13.0827,80.2707): {"name":"Central","routes":[21,24]},
 (13.0418,80.2341): {"name":"T. Nagar","routes":[5,12]},
 (13.0067,80.2206): {"name":"Guindy","routes":[18,27]},
 (13.0358,80.2440): {"name":"Nandanam","routes":[5,18]}
}
bad = [[0]*4]*3
bad[0][1] = 7
good = [[0]*4 for _ in range(3)]
good[0][1] = 7
grid = [["Central","T. Nagar",None,None],["Guindy","Nandanam",None,None],[None]*4]
print("Bad grid:",bad)
print("Good grid:",good)
print("Stop lookup:",stops[(13.0827,80.2707)]["name"])
print("Grid:",grid)

original = {"stop":"Central","routes":[21,24]}
shallow = original.copy()
deep = {"stop":original["stop"],"routes":original["routes"][:]}
shallow["routes"].append(30)
print("Original after shallow change:",original)
print("Shallow copy:",shallow)
print("Deep copy:",deep)

name, route1, route2 = ("Central",21,24)
print("Unpacked:",name,route1,route2)
inside = ("Central",[21,24])
inside[1].append(30)
print("Tuple with list:",inside)

values = list(range(1000000))
tuple_values, list_values = tuple(values), values[:]
index, repeats = 750000, 100000
print("One million values")
print("Tuple/list shallow bytes:",tuple_values.__sizeof__(),list_values.__sizeof__())
print("Index values:",tuple_values[index],list_values[index],"Same:",tuple_values[index]==list_values[index])
start=time.perf_counter()
tuple_total=sum(tuple_values[index] for _ in range(repeats))
tuple_time=time.perf_counter()-start
start=time.perf_counter()
list_total=sum(list_values[index] for _ in range(repeats))
list_time=time.perf_counter()-start
print("Repeated indexing results:",tuple_total,list_total)
print("Indexing time - tuple:",round(tuple_time,6),"list:",round(list_time,6))
