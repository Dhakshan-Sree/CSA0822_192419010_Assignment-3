# TASK 4: ELECTIVE REGISTRATION USING SETS
import random, time
a={"192311001","192311004","192311007","192311009"}
b={"192311002","192311004","192311009","192311010"}
universe={f"192311{i:03d}" for i in range(1,11)}
print("Class A:",sorted(a))
print("Class B:",sorted(b))
print("Both:",sorted(a&b))
print("Exactly one:",sorted(a^b))
print("Neither:",sorted(universe-(a|b)))
print("Union:",sorted(a|b))
print("A minus B:",sorted(a-b))
print("Venn counts:",len(a-b),len(a&b),len(b-a),len(universe-(a|b)))

random.seed(42)
for size in (10000,100000,1000000):
    first=[random.randrange(size*2) for _ in range(size)]
    second=[random.randrange(size*2) for _ in range(size)]
    values=set(first)
    target=first[-1]
    start=time.perf_counter(); list_found=target in first; list_time=time.perf_counter()-start
    start=time.perf_counter(); set_found=target in values; set_time=time.perf_counter()-start
    start=time.perf_counter(); common=values&set(second); intersection_time=time.perf_counter()-start
    print("Size:",size,"List lookup:",round(list_time,6),"Set lookup:",round(set_time,6),
          "Same:",list_found==set_found,"Intersection:",round(intersection_time,6),"Common:",len(common))
    if size==10000:
        x,y=first[:1000],second[:1000]
        start=time.perf_counter(); nested={i for i in x for j in y if i==j}; nested_time=time.perf_counter()-start
        start=time.perf_counter(); set_result=set(x)&set(y); set_time=time.perf_counter()-start
        print("Nested/set intersection:",round(nested_time,6),round(set_time,6),"Same:",nested==set_result)
print("Duplicates:",len([1,1,2,2,3]),"to",len(set([1,1,2,2,3])))
