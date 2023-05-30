import math



locations = [

    {'id': 1, 'latitude': 23.8728568, 'longitude': 90.3984184, 'address': 'Uttara Branch'},

    {'id': 2, 'latitude': 23.8513998, 'longitude': 90.3944536, 'address': 'City Bank Airport'},

    {'id': 3, 'latitude': 23.8330429, 'longitude': 90.4092871, 'address': 'City Bank Nikunja'},

    {'id': 4, 'latitude': 23.8679743, 'longitude': 90.3840879, 'address': 'City Ban Beside Uttara Diagnostic'},

    {'id': 5, 'latitude': 23.8248293, 'longitude': 90.3551134, 'address': 'City Bank Mirpur 12'},

    {'id': 6, 'latitude': 23.827149, 'longitude': 90.4106238, 'address': 'City Bank Le Meridien'},

    {'id': 7, 'latitude': 23.8629078, 'longitude': 90.3816318, 'address': 'City Bank Shaheed Sarani'},

    {'id': 8, 'latitude': 23.8673789, 'longitude': 90.429412, 'address': 'City Bank Narayanganj'},

    {'id': 9, 'latitude': 23.8248938, 'longitude': 90.3549467, 'address': 'City Bank Pallabi'},

    {'id': 10, 'latitude': 23.813316, 'longitude': 90.4147498, 'address': 'City Bank JFP'}

]




def calculate_distance(lat1, lon1, lat2, lon2):

    lat1_rad = math.radians(lat1)

    lon1_rad = math.radians(lon1)

    lat2_rad = math.radians(lat2)

    lon2_rad = math.radians(lon2)


    dlon = lon2_rad - lon1_rad

    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = 6371 * c   

    return distance


def find_nearest_location(current_location, unvisited_locations):

    nearest_location = None

    nearest_distance = float('inf')

   

    for location in unvisited_locations:

        distance = calculate_distance(

            current_location['latitude'], current_location['longitude'],

            location['latitude'], location['longitude']

        )

        if distance < nearest_distance:

            nearest_distance = distance

            nearest_location = location

   

    return nearest_location




def find_best_route(locations):


    current_location = locations[0]

    unvisited_locations = locations[1:]
  

    best_route = [current_location]
  

    while unvisited_locations:

        nearest_location = find_nearest_location(current_location, unvisited_locations)

        best_route.append(nearest_location)

        unvisited_locations.remove(nearest_location)

        current_location = nearest_location

   
    return best_route


best_route = find_best_route(locations)



print("Best Route", end=": ")

for index, loc in enumerate(best_route):

    if index < len(best_route) - 1:

        print(loc['address'], end=" >> ")

    else:

        print(loc['address'])