a={}
n=int(input("Enter the number of buses:"))
for i in range(n):
    id=input("Enter the ID of the bus:")
    way=input("Enter the rout: ")
    completed=int(input("Enter the completed number of trips"))
    delay=int(input("Enter the delay :"))
    deport_station=input("Enter the deporting station:")
    a[id]={"rout":way,"Trips_Completed":completed,"avg_delay":delay,"deport":deport_station }
print(a)
bus= {
    "B201": {"route": "Route A", "Trips_Completed": 42, "delay": 3, "depot": "Central"},
    "B202": {"route": "Route B", "Trips_Completed": 35, "delay": 6, "depot": "North"},
    "B203": {"route": "Route C", "Trips_Completed": 50, "delay": 2, "depot": "Central"},
    "B204": {"route": "Route A", "Trips_Completed": 28, "delay": 8, "depot": "South"},
    "B205": {"route": "Route D", "Trips_Completed": 45, "delay": 4, "depot": "East"}
}

# def bus_id(a):
#     find_id = input("Enter the bus ID you want to find: ")

#     for i in a:
#         if i == find_id:
#             print(a[i]["route"],
#                   a[i]["Trips_Completed"],
#                   a[i]["delay"],
#                   a[i]["depot"])
# bus_id(a)

# def sort(bus):
#     a=[]
#     b=[]
#     for i in bus:
#         a.append(bus[i]["trips"])
#         b.append(i)
#     n=len(a)
#     for i in range(n):
#         for j in range(n-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#                 b[j],b[j+1]=b[j+1],b[j]
#     return b
# print(sort(bus))

def serch(bus):
    k=[]
    name=input("Enter the name:")
    for i in bus:
        if bus[i]["route"]==name:
            k.append(i)
    return(k)
print(serch(bus))


def avg(bus):
    total = {}
    count = {}
    for i in bus:
        if bus[i]["delay"]<5:
            place=bus[i]["deport"]
            trips=bus[i]["Trips_Completed"]
            if place in total:
                total[place]+=trips
                count[place]+=1
            else:
                total[place]=trips
                count[place]=1
    avg={}
    for j in total:
        avg[j]=total[j]/count[j]
    return avg
            
def high_reliability_buses(bus):
    result = []

    for i in bus:
        if bus[i]["Trips_Completed"] >= 40 and bus[i]["delay"] <= 4:
            result.append(i)

    return result