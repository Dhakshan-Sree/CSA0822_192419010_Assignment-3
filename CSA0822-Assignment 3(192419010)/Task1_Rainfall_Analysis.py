# TASK 1: RAINFALL ANALYSIS
import random, time, math
random.seed(1)
rainfall = [0 if random.random() < 0.4 else round(random.uniform(0.5, 60), 1) for _ in range(365)]
weeks = [round(sum(rainfall[i:i+7]), 1) for i in range(0, 359, 7)]
averages = [round(sum(rainfall[i:i+7])/7, 2) for i in range(359)]
dry_days = [i+1 for i, x in enumerate(rainfall) if x == 0]

def running(values):
    if len(values) < 7: return []
    total = sum(values[:7])
    result = [total/7]
    for i in range(7, len(values)):
        total += values[i] - values[i-7]
        result.append(total/7)
    return result

print("Readings:", len(rainfall), "Complete weeks:", len(weeks), "Remaining:", len(rainfall)%7)
print("First 5 weekly totals:", weeks[:5])
print("Wettest week:", weeks.index(max(weeks))+1, max(weeks))
print("Driest week:", weeks.index(min(weeks))+1, min(weeks))
print("Maximum:", max(rainfall), "Day:", rainfall.index(max(rainfall))+1)
print("Minimum:", min(rainfall), "Day:", rainfall.index(min(rainfall))+1)
print("First 10 moving averages:", averages[:10])
print("Dry days:", len(dry_days), "First 10:", dry_days[:10])
print("Methods agree:", all(math.isclose(a, round(b, 2), abs_tol=1e-9) for a,b in zip(averages,running(rainfall))))

for size in (365, 36500, 365000):
    data = [random.randint(0,30) for _ in range(size)]
    start = time.perf_counter()
    direct = [sum(data[i:i+7])/7 for i in range(len(data)-6)]
    direct_time = time.perf_counter()-start
    start = time.perf_counter()
    fast = running(data)
    running_time = time.perf_counter()-start
    same = all(math.isclose(a,b,abs_tol=1e-9) for a,b in zip(direct,fast))
    print("Size:",size,"Same:",same,"Direct:",round(direct_time,6),"Running:",round(running_time,6))
