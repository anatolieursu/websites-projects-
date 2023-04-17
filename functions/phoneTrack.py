import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

from datetime import datetime

import opencage
from opencage.geocoder import OpenCageGeocode
import folium

console = open("console", "a+")

def phone_track(number):
    ch_nmber = phonenumbers.parse(number, "CH")
    cntry = geocoder.description_for_number(ch_nmber, "en")
    service_nmber = phonenumbers.parse(number, "RO")
    service_nb = carrier.name_for_number(service_nmber, "en")
    key = "4969e77a86b940818e05379335e13a2f"

    gecoder = OpenCageGeocode(key)
    query = str(cntry)
    results = gecoder.geocode(query)

    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]

    Address = [lat, lng]

    my_map1 = folium.Map(location=Address,
                         zoom_start=12)
    folium.CircleMarker(location=Address,
                        radius=50, popup="Yorkshire").add_to(my_map1)
    folium.Marker(location=Address,
                  popup="Yorkshire").add_to(my_map1)
    my_map1.save(f"maps-phone-numbers/{number}.html")

    print("\nPHONE_NUMBER TRACKER" + "-" * 50)
    print(f"\nNumber: {number}\nCountry: {cntry}\nService Provider: {service_nb}")
    print(f"\nDate & Time: {datetime.now()}")
    print("\n" + "-" * 50)

    # console
    console.write("\nPHONE_NUMBER TRACKER" + "-" * 50)
    console.write(f"\nNumber: {number}\nCountry: {cntry}\nService Provider: {service_nb}")
    console.write(f"\nDate & Time: {datetime.now()}")
    console.write("\n" + "-" * 50)