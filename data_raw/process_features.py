import sys
import csv
import requests
import reverse_geocoder as rg
import pprint

def main():

    # print(rg.search(()))

    coordinates = (40.73971301,-73.99456405)
    pprint.pprint(rg.search(coordinates))
    

    """
    features_filenames = ["nyc_laundry.csv"]

    manhattan_regions_csv = "manhattan_localities.csv"
    bing_maps_key = "AlFWHSKTFraKZV1I9nTjz1I2XRWGpfa6SCaudPsYVVPEXb_T2yJA6VjStLb-WcT7"

    bing_maps_params = {"key":bing_maps_key}
    bing_maps_url = "http://dev.virtualearth.net/REST/v1/Locations/"

    manhattan_regions = define_manhattan_neighborhoods(manhattan_regions_csv)
    stations_by_region = {"Lower Manhattan":[], "Midtown":[], "Upper Manhattan":[], "New York":[]}
    
    features_data = {"Laundry": {"Lower Manhattan":[], "Midtown":[], "Upper Manhattan":[]}}
    for filename in features_filenames:

        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)

            for line in csv_reader:

                industry = line[0]
                business = line[1]
                latitude = line[3]
                longitude = line[2]

                bing_maps_url = f"http://dev.virtualearth.net/REST/v1/Locations/{latitude},{longitude}"
                response = requests.get(bing_maps_url, params=bing_maps_params).json()

                try:
                    locality = response["resourceSets"][0]["resources"][0]["address"]["locality"].lower()
                except IndexError:
                    print(latitude, longitude, "Not found - skipped")
                    continue

            
                if locality in manhattan_regions["Lower Manhattan"]:
                    features_data[industry]["Lower Manhattan"].append((business, latitude, longitude))
                elif locality in manhattan_regions["Upper Manhattan"]:
                    features_data[industry]["Upper Manhattan"].append((business, latitude, longitude))
                elif locality in manhattan_regions["Midtown"]:
                    features_data[industry]["Midtown"].append((business, latitude, longitude))

    for industry in features_data:
        filename = industry + ".csv"

        with open(filename, "w") as output_csv:
            csv_writer = csv.writer(output_csv)
            csv_writer.writerow(["business", "latitude", "longitude", "region"])

            for region in features_data[industry]:
                # print(region)
                for region_data in features_data[industry][region]:
                    if region == "Upper Manhattan":
                        csv_writer.writerow([region_data[0], region_data[1], region_data[2], "Upper Manhattan"])
                    elif region == "Lower Manhattan":
                        csv_writer.writerow([region_data[0], region_data[1], region_data[2], "Lower Manhattan"])
                    elif region == "Midtown":
                        csv_writer.writerow([region_data[0], region_data[1], region_data[2], "Midtown Manhattan"])
"""
main()
