# CPE 202 Lab 0

# represents a location using name, latitude and longitude


class Location:
    def __init__(self, name, lat, lon):
        self.name = name    # string for name of location
        self.lat = lat      # latitude in degrees (-90 to 90)
        self.lon = lon      # longitude in degrees (-180 to 180)

    def __repr__(self):
        return "Location(" + '\'' + str(self.name) + '\'' + ', ' + str(self.lat) + ', ' + str(self.lon) + ")"

    def __eq__(self, other):
        return type(other) == Location and self.name == other.name and self.lat == other.lat and self.lon == other.lon


# ADD BOILERPLATE HERE
# (__eq__ and __repr__ functions)
def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:", loc1.__repr__())
    print("Location 2:", loc2.__repr__())
    print("Location 3:", loc3.__repr__())
    print("Location 4:", loc4.__repr__())

    print("\nLocation 1 equals Location 2:", loc1.__eq__(loc2))
    print("Location 1 equals Location 3:",loc1.__eq__(loc3))
    print("Location 1 equals Location 4:",loc1.__eq__(loc4))

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)


if __name__ == "__main__":
    main()