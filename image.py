import argparse
from PIL import Image



def extract_location(path):
    with open(path, "rb") as src:
        img = Image.open(src)

    exif_data = img._getexif()
    if exif_data is not None:
        for tag, value in exif_data.items():
            # Check if the tag corresponds to GPSInfo (tag number 34853)
            if tag == 34853 and isinstance(value, dict):
                gps_info = value
                latitude_ref = gps_info.get(1)
                latitude = gps_info.get(2)
                longitude_ref = gps_info.get(3)
                longitude = gps_info.get(4)

                if latitude and longitude:
                    lat_degrees = latitude[0]
                    lat_minutes = latitude[1]
                    lat_seconds = latitude[2]
                    lat = lat_degrees + (lat_minutes / 60) + (lat_seconds / 3600)
                    lat = float(lat)
                    lon_degrees = longitude[0]
                    lon_minutes = longitude[1]
                    lon_seconds = longitude[2]
                    lon = lon_degrees + (lon_minutes / 60) + (lon_seconds / 3600)
                    lon = float(lon)
                    # Appliquer le référentiel (N/S pour la latitude et E/O pour la longitude)
                    if latitude_ref == 'S':
                        lat = -lat
                    if longitude_ref == 'W':
                        lon = -lon

                    print(f"Lat/lon: {lat}/{lon}")
                   
                    return

    print("Location data not found in the image's EXIF.")

        

def extract_pgp(path):
    with open(path, "rb") as file:
        data = file.read()

    start = b"-----BEGIN PGP PUBLIC KEY BLOCK-----"
    end = b"-----END PGP PUBLIC KEY BLOCK-----"
    start_index = data.find(start)
    end_index = data.find(end)

    if start_index == -1 or end_index == -1:
        print("PGP public key could not be retrieved")
    else:
        pgp_key = data[start_index:end_index + len(end)].decode("utf-8").strip()
        print(pgp_key)


def main():
    parser = argparse.ArgumentParser(description="inspector-image")
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-steg", required=False, type=str, help="Extract PGP key")
    g.add_argument("-map", required=False, type=str, help="Extract location")
    args = parser.parse_args()

    if args.steg:
        extract_pgp(args.steg)
    elif args.map:
        extract_location(args.map)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

