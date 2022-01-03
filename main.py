#Imports
import os
from geopy import Nominatim
from geopy.distance import geodesic as Distance
import xml.etree.ElementTree as ET
import wget
import zipfile

#Initialize Stations and Geopy
app = Nominatim(user_agent="openWeather")
tree = ET.parse("stations.xml")
root = tree.getroot()

#Get Location
location = input("Wo wohnen Sie? \n")
location = app.geocode(location).raw

lat = location['lat']
lon = location['lon']
location_coords = (lat, lon)

#Get nearest Station
current_distance = Distance(location_coords, (53.10, 12.13)).km
current_id = "EW002"

print(current_distance)
print(Distance(location_coords, (53.27, 7.28)))

for child in root:
    child_lat = child.get('lat')
    child_lon = child.get('long')
    compare_coords = (child_lat, child_lon)
    compare_distance = Distance(location_coords, compare_coords)

    if compare_distance < current_distance:
        current_id = child.get('id')
        current_distance = compare_distance
        print(current_distance)
        print(current_id)

#Download Station-Data
file_name = "MOSMIX_L_LATEST_" + current_id.strip() + ".kmz"
link = "https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_L/single_stations/" + current_id.strip() + "/kml/" + file_name
print(link)

if not os.path.exists("data/"):
    print("Created Data-Folder")
    os.mkdir("data/")
else:
    for file in os.listdir("data/"):
        os.remove("data/" + file)

wget.download(link, "data/" + file_name)
print("Downloaded Data")

file_to_extract = "data/data.xml"

try:
    with zipfile.ZipFile("data/" + file_name) as z:
        z.extractall("data")
        print("Extracted all")
except:
    print("Invalid file")

#Read Data
for file in os.listdir("data/"):
    if file.endswith(".kml"):
        data_file = file

data_file = os.rename("data/" + data_file, "data/data.xml")

tree = ET.parse("data/data.xml")
root = tree.getroot()

print(root)

for child in root:
    print(child)
