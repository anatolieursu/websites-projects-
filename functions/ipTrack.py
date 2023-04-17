import geocoder
from datetime import datetime
import folium

console = open("../console", "a+")

def ip_track(ip):
    g = geocoder.ip(ip)
    Address = g.latlng

    print("\nIP TRACKER" + "-" * 50)
    print(f"\nIp: {ip} \nLocation: {Address}\nDate & Time: {datetime.now()}\n")
    print("-" * 50 + "\n")

    my_map1 = folium.Map(location=Address,
                         zoom_start=20)
    folium.CircleMarker(location=Address,
                        radius=50, popup="Yorkshire").add_to(my_map1)
    folium.Marker(Address,
                  popup="Yorkshire").add_to(my_map1)

    my_map1.save(f"maps-ip/{ip}.html")

    console.write("\nIP TRACKER " + "-" * 50)
    console.write(f"\nIp: {ip} \nLocation: {Address}\nDate & Time: {datetime.now()}\n")
    console.write("-" * 50 + "\n")