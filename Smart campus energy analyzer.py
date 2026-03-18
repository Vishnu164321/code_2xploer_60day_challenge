User=input("enter Values:")

items=User.split()
numbers=[]
for i in items:
    numbers=numbers+[int(i)]

data={
    "Efficient":[],
    "Moderate":[],
    "High":[],
    "Invalid":[]
}
for val in numbers:
    if val<0:
        data["Invalid"]=data["Invalid"]+[val]
    elif val<=50:
        data["Efficient"]=data["Efficient"]+[val]
    elif val<=150:
        data["Moderate"]=data["Moderate"]+[val]
    else:
        data["High"]=data["High"]+[val]

    Valid_val=[x for x in numbers if x>=0]
    total=0
    for x in Valid_val:
        total=total+x

    count=len(Valid_val)

    Info=(total,count)
    High=len(data["High"])
    Efficient=len(data["Efficient"])
    Moderate=len(data["Moderate"])

    d=Efficient-Moderate
    if d<0:
        d=d*-1

    if High>3:
        res="OverConsumption"

    elif d<=1:
        res="Balanced usage"
    elif total>600:
        res="Energy Waste detected"
    else:
        res="Moderate usage"

print("/n----Report-----")
print("Efficient:",data["Efficient"])
print("Moderate:",data["Moderate"])
print("High:",data["High"])
print("Invalid:",data["Invalid"])
print("Total:",Info[0])
print("Buildings:",Info[1])
print("Result:",res)