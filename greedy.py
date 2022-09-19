import random
# set covering solution
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = dict()
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)


# TSP solution
cities_to_visit = set([3, 2])
cities_visited = set()
cities_map = dict()
cities_map[1] = dict()
cities_map[1][2] = 7
cities_map[1][3] = 4
cities_map[2] = dict()
cities_map[2][3] = 8
cities_map[2][1] = 7
cities_map[3] = dict()
cities_map[3][1] = 4
cities_map[3][2] = 8

# choose random city as starting point
start_city = 1
path_cost = 0

while cities_to_visit:
    best_city = 0
    cities_map[start_city][best_city] = float("inf")
    # choose city with the lowest cost to travel
    for city in cities_to_visit:
        if cities_map[start_city][city] < cities_map[start_city][best_city]:
            best_city = city

    # add it to visited
    cities_visited.add(best_city)
    path_cost += cities_map[start_city][best_city]
    start_city = best_city
    cities_to_visit -= cities_visited


print(path_cost)