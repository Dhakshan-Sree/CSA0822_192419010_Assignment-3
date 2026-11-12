# TASK 6: RAILWAY TIMETABLE
import random, time
trains={
"T101":{"stations":[("Central","08:00","08:10"),("Egmore","08:25","08:30"),("Tambaram","09:00","09:05")],"days":{"Mon","Tue","Wed","Thu","Fri"}},
"T102":{"stations":[("Central","07:30","07:40"),("Guindy","08:00","08:05"),("Tambaram","08:35","08:40")],"days":{"Mon","Wed","Fri"}},
"T103":{"stations":[("Beach","09:00","09:05"),("Park","09:20","09:25"),("Egmore","09:40","09:45")],"days":{"Sat","Sun"}},
"T104":{"stations":[("Central","10:00","10:10"),("Egmore","10:25","10:30"),("Villupuram","12:00","12:05")],"days":{"Mon","Tue","Wed","Thu","Fri","Sat"}},
"T105":{"stations":[("Central","06:45","06:50"),("Guindy","07:15","07:20"),("Tambaram","07:50","07:55")],"days":{"Tue","Thu","Sat"}}}
station,day="Central","Mon"
matches=sorted([(t,s,a,d) for t,info in trains.items() if day in info["days"]
                for s,a,d in info["stations"] if s==station],key=lambda x:x[3])
print("Trains:",len(trains),"Query:",station,day)
print("Matches:",matches)
print("Unknown station:",[t for t,info in trains.items()
      if any(s=="Unknown" for s,a,d in info["stations"])])
index={}
for train,info in trains.items():
    for s,a,d in info["stations"]:
        index.setdefault(s,[]).append((train,a,d,info["days"]))
indexed=sorted([(t,station,a,d) for t,a,d,days in index.get(station,[]) if day in days],key=lambda x:x[3])
print("Index agrees:",matches==indexed,"Stations:",sorted(index))

random.seed(42)
names=["Central","Egmore","Guindy","Tambaram","Beach","Park","T Nagar"]
for size in (100,1000,10000):
    data={f"X{i:05d}":{"stations":[(s,"08:00","08:05") for s in random.sample(names,4)],
          "days":{"Mon","Wed","Fri"}} for i in range(size)}
    start=time.perf_counter()
    scan=[(t,s,a,d) for t,info in data.items() if "Mon" in info["days"]
          for s,a,d in info["stations"] if s==station]
    scan_time=time.perf_counter()-start
    start=time.perf_counter()
    lookup={}
    for t,info in data.items():
        for s,a,d in info["stations"]:
            lookup.setdefault(s,[]).append((t,a,d,info["days"]))
    build_time=time.perf_counter()-start
    start=time.perf_counter()
    fast=[(t,station,a,d) for t,a,d,days in lookup.get(station,[]) if "Mon" in days]
    query_time=time.perf_counter()-start
    print("Trains:",size,"Scan:",round(scan_time,6),"Index build:",round(build_time,6),
          "Index query:",round(query_time,6),"Same:",sorted(scan)==sorted(fast))
