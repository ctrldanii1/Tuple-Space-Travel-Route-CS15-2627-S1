mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

search_destination = input("Enter a destination: ")
if search_destination in mission_route:
    print("Destination is in the mission route")

    stops_from_start = mission_route.index(search_destination)
    print("Stops away from the start:", stops_from_start)

    stops_from_end = len(mission_route) - 1 - stops_from_start
    print("Stops away from the end:", stops_from_end)

    next_stop = mission_route[stops_from_start + 1]
    print("Next stop:", next_stop)
else:
    print("Destination is not in the mission route")




