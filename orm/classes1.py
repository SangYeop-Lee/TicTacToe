from classes0 import Flight

def main():

    # Create flight.
    f = Flight(origin="New York", destination="Paris", duration=540)

    # Change the value of a variable
    f.duration += 10

    # Print details about flight
    print(f.origin, f.destination, f.duration)

if __name__ == "__main__":
    main()