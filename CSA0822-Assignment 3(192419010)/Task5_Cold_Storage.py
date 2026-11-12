# TASK 5: COLD STORAGE TEMPERATURE MONITORING
import time, sys
readings=[((i*37)%701)/10-60 for i in range(10000)]
valid=[x for x in readings if -50<=x<=0]
fahrenheit=[round(x*9/5+32,2) for x in valid]
alarms=[(i+1,x) for i,x in enumerate(readings) if x < -50 or x > 0]
print("Total readings:",len(readings))
print("Valid readings:",len(valid))
print("Alarm readings:",len(alarms))
print("First 5 valid:",[round(x,2) for x in valid[:5]])
print("First 5 Fahrenheit:",fahrenheit[:5])
print("First 5 alarms:",alarms[:5])
filtered=list(filter(lambda x:-50<=x<=0,readings))
print("Comprehension/filter agree:",valid==filtered)
mapped=list(map(lambda x:round(x*9/5+32,2),valid))
print("Comprehension/map agree:",fahrenheit==mapped)
list_data=[x for x in readings if -50<=x<=0]
generator_data=(x for x in readings if -50<=x<=0)
print("List memory:",sys.getsizeof(list_data),"bytes")
print("Generator memory:",sys.getsizeof(generator_data),"bytes")

for size in (10000,100000,1000000):
    data=[((i*37)%701)/10-60 for i in range(size)]
    start=time.perf_counter()
    result_list=[x for x in data if -50<=x<=0]
    list_time=time.perf_counter()-start
    start=time.perf_counter()
    result_generator=(x for x in data if -50<=x<=0)
    generator_create=time.perf_counter()-start
    start=time.perf_counter()
    generator_values=list(result_generator)
    generator_consume=time.perf_counter()-start
    print("\nInput size:",size)
    print("Valid readings:",len(result_list),"Generator readings:",len(generator_values))
    print("Results match:",result_list==generator_values)
    print("List time:",round(list_time,6),"Generator creation:",round(generator_create,6),
          "Generator consumption:",round(generator_consume,6))
    print("List memory:",sys.getsizeof(result_list),"Generator memory:",
          sys.getsizeof(x for x in data if -50<=x<=0))
