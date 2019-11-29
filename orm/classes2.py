class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print("Flight origin:", self.origin)
        print("Flight destination:", self.destination)
        print("Flight duration:", self.duration)

def main():
    f1 = Flight("New York", "Paris", 540)
    f1.print_info()

    f2 = Flight("Tokyo", "Shanghai", 185)
    f2.print_info()

if __name__ == "__main__":
    main()