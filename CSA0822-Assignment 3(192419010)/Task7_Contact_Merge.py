# TASK 7: CONTACT MERGING FROM TWO PHONES AND A SIM CARD
phone_a=[
 {"name":"Ravi","phone":"+91 98400 12345","email":"ravi@gmail.com"},
 {"name":"Meena","phone":"9000011111","email":""}]
phone_b=[
 {"name":"Ravi","phone":"98400-12345","email":""},
 {"name":"Meena","phone":"+91 90000 11111","email":"meena@gmail.com"},
 {"name":"Kavi","phone":"","email":"kavi@gmail.com"}]
sim=[
 {"name":"Arun","phone":"09888822222","email":"arun@gmail.com"},
 {"name":"Kavi","phone":"","email":"KAVI@gmail.com"},
 {"name":"Unknown","phone":"","email":""}]

def normalise(phone):
    n="".join(c for c in phone if c.isdigit())
    if len(n)==12 and n.startswith("91"): n=n[2:]
    elif len(n)==11 and n.startswith("0"): n=n[1:]
    return n if len(n)==10 else ""

def merge(*sources):
    index,people,unmatched={},{},[]
    people=[]
    for source in sources:
        for c in source:
            p=normalise(c.get("phone",""))
            e=c.get("email","").strip().lower()
            keys=(["P"+p] if p else [])+(["E"+e] if "@" in e else [])
            matches=[]
            for k in keys:
                if k in index and index[k] not in matches: matches.append(index[k])
            if not keys:
                unmatched.append(c); continue
            person=matches[0] if matches else {"name":"","phones":set(),"emails":set()}
            for other in matches[1:]:
                person["phones"].update(other["phones"])
                person["emails"].update(other["emails"])
                if not person["name"]: person["name"]=other["name"]
                people.remove(other)
                for k in index:
                    if index[k] is other: index[k]=person
            person["name"]=person["name"] or c.get("name","").strip()
            if p: person["phones"].add(p)
            if "@" in e: person["emails"].add(e)
            if not matches: people.append(person)
            for k in keys: index[k]=person
    return people,unmatched

merged,unmatched=merge(phone_a,phone_b,sim)
print("Merged contacts:")
for p in merged: print(p)
print("Total contacts:",len(phone_a)+len(phone_b)+len(sim))
print("Unique contacts:",len(merged))
print("Unmatched contacts:",len(unmatched))
print("Phone formats match:",normalise("+91 98400 12345")==normalise("09840012345"))
print("Email preserved:",any("meena@gmail.com" in p["emails"] for p in merged))
print("Kavi matched:",any("kavi@gmail.com" in p["emails"] for p in merged))

def generate(n,offset=0):
    return [{"name":str(i),"phone":str(9000000000+i+offset),
             "email":str(i+offset)+"@gmail.com"} for i in range(n)]
for size in (1000,100000):
    result,missing=merge(generate(size),generate(size,size//2))
    print("Size:",size,"Unique:",len(result),"Unmatched:",len(missing))
