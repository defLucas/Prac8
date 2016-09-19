from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1",100, 1.2)

    my_taxi.drive(40)
    print(my_taxi)
    print("Current Fare ${:.2f}".format(my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print("Current Fare ${:.2f}".format(my_taxi.get_fare()))
main()
