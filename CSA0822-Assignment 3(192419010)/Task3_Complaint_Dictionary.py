# TASK 3: FARMER HELPLINE COMPLAINT ANALYSIS
import random, string, time
from collections import Counter
complaints = [
("Kisan","Rice","Seeds not received seeds delayed"),
("Kisan","Wheat","Fertiliser price high"),
("Kisan","Rice","Seeds price high subsidy not received"),
("Kisan","Wheat","Seeds delayed not received"),
("North","Rice","Water shortage in rice field"),
("North","Wheat","Wheat seeds not available"),
("South","Cotton","Cotton crop pest problem"),
("South","Rice","Rice seeds delayed")]
stop_words = {"not","the","is","at","and","in"}

def clean(text):
    return text.lower().translate(str.maketrans("","",string.punctuation)).split()

def count_words(texts):
    counts = {}
    for text in texts:
        for word in clean(text):
            if word not in stop_words:
                counts[word] = counts.get(word,0)+1
    return counts

texts = [x[2] for x in complaints]
frequencies = count_words(texts)
top_three = sorted(frequencies.items(),key=lambda x:(-x[1],x[0]))[:3]
districts, crops = {}, {}
for district,crop,text in complaints:
    districts[district] = districts.get(district,0)+1
    crops.setdefault(crop,[]).append(text)
print("Frequencies:",frequencies)
print("Top three:",top_three)
print("District complaint counts:",districts)
print("Crop-wise complaints:",crops)
words = [w for text in texts for w in clean(text) if w not in stop_words]
list_counts = {w:words.count(w) for w in set(words)}
print("Dictionary/list count agree:",frequencies==list_counts)

random.seed(42)
vocabulary = ["seeds","price","fertiliser","water","crop","subsidy","delayed","received"]
for size in (1000,10000,100000):
    data = [" ".join(random.choices(vocabulary,k=8)) for _ in range(size)]
    start=time.perf_counter()
    dictionary_result=count_words(data)
    dict_time=time.perf_counter()-start
    start=time.perf_counter()
    counter_result=Counter(w for text in data for w in clean(text) if w not in stop_words)
    counter_time=time.perf_counter()-start
    print("Complaints:",size,"Dictionary:",round(dict_time,6),"Counter:",round(counter_time,6),"Same:",dictionary_result==dict(counter_result))
print("Empty:",count_words([""]))
print("Case test:",count_words(["SEEDS seeds Seeds"]))
print("Punctuation test:",count_words(["seeds, price! seeds."]))
