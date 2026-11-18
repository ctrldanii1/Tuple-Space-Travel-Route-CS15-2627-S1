mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)


print("The First Destination:", mission_route[0])
print("The Final Destination:", mission_route[-1])
print("Total Number Of Destinations:", len(mission_route))

for destination in mission_route:
    print(destination)

if "Europa" in mission_route:
    print("Europa is in the mission route!!!")
else:
    print("Europa is not in the mission route.")