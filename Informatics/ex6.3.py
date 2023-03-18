def find_route(airports):
    routes = {k: v for k, v in airports.items()}
    start = set(routes.keys()) - set(routes.values())
    current = start.pop()
    route = [current]
    while current in routes:
        current = routes[current]
        route.append(current)
    return route

airports = {'HKG': 'DXB', 'FRA': 'HKG', 'DEL': 'FRA'}
airports = eval(input())
route = find_route(airports)
print(route)