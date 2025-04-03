"""
This program wil keep track of the composition of a train and its cargo. It will compute the length
and speed of potential train configurations.

Author: Ryo Kimmick
"""
# This class stores the information about the specifications of the engines
class Locomotive:
    # This method initializes the attributes
    def __init__(self, locomovitve_length, locomovitve_max_payload, locomovitve_max_speed):
        # This is the length in meters
        self.locomovitve_length = locomovitve_length
        # This is the max payload in tons
        self.locomovitve_max_payload = locomovitve_max_payload
        # This is the max speed in miles per hour
        self.locomovitve_max_speed = locomovitve_max_speed


    # This method returns the length of the locomotive
    def get_length(self):
        return self.locomovitve_length


    # This method returns the max payload of the locomotive
    def get_maximum_payload(self):
        return self.locomovitve_max_payload


    # This method retuns the max speed of the locomotive
    def get_maximum_speed(self):
        return self.locomovitve_max_speed



# This class stores the information about the specifications of the railcars
class Railcar:
    # This method initializes the attributes
    def __init__(self, railcar_length, railcar_cargo_type, railcar_min_weight, railcar_max_weight, railcar_capacity):
        # This is the length in meters
        self.railcar_length = railcar_length
        # This is whether the cargo type is passenger or freight
        self.railcar_cargo_type = railcar_cargo_type
        # This is the minimum weight in tons
        self.railcar_min_weight = railcar_min_weight
        # This is the maximum weight in tons
        self.railcar_max_weight = railcar_max_weight
        # This is the capacity as a fraction
        self.railcar_capacity = railcar_capacity
    

    # This method returns the length of the railcar
    def get_length(self):
        return self.railcar_length
    

    # This method returns the type of cargo
    def get_cargo_type(self):
        return self.railcar_cargo_type
    

    # This method returns the weight of the railcar
    def get_weight(self):
        return self.railcar_min_weight + self.railcar_capacity * (self.railcar_max_weight - self.railcar_min_weight)



# This class stores all the information about the trains as a whole and provides the method to print it to the user
class Train:
    # This method initializes the attributes
    def __init__(self):
        self.locomotives = []
        # This is a list to hold locomotives
        self.railcars = []
        # This is a list to hold railcars
    

    # This method returns the length of the train
    def get_length(self):
        # This creates the total locomotive length variable and sets it to 0
        total_locomotive_length = 0
        # This iterates over the locomotives
        for locomotive in self.locomotives:
            # This adds the length of each locomotive to the total locomotive length
            total_locomotive_length += locomotive.get_length()
        
        # This creates the total railcar length variable and sets it to 0
        total_railcar_length = 0
        # This iterates over the railcars
        for railcar in self.railcars:
            # This adds the length of each railcar to the total railcar length
            total_railcar_length += railcar.get_length()
        
        # This adds the total railcar length and total locomotive length and returns it
        return total_railcar_length + total_locomotive_length
    

    # This method returns the weight of the cargo
    def get_payload(self):
        # This creates the total payload variable and sets it to 0
        total_payload = 0
        # This iterates over the railcars
        for railcar in self.railcars:
            # This adds the weight of each railcar to the total payload
            total_payload += railcar.get_weight()
    
        # This returns the total payload
        return total_payload
    
    
    # This method returns the speed of the train
    def get_speed(self):
        # This finds the maximum speed of the slowest locomotive
        slowest_locomotive = min(locomotive.get_maximum_speed() for locomotive in self.locomotives)
        # This adds up all the payloads for the locomotives, finding the overall max payload
        locomotive_max_payload = sum(locomotive.get_maximum_payload() for locomotive in self.locomotives)
        
        # If the max payload is 0, the maximum speed is the maximum speed of the slowest locomotive
        if locomotive_max_payload == 0:
            return slowest_locomotive
        
        # This linearly decreases the train's speed as its payload increaes
        current_speed = slowest_locomotive * (1 - self.get_payload() / locomotive_max_payload / 2)
        # This returns whichever speed is larger, the current speed or the minimum speed of the train
        return max(current_speed, 0.5 * slowest_locomotive)
    

    # This method adds the railcars to the end of the train
    def add_railcar(self, railcar):
        # If the additional railcar does not cause the train to exceed its maximum payload, the railcar will be added
        if self.get_payload() + railcar.get_weight() <= sum(locomotive.get_maximum_payload() for locomotive in self.locomotives):
            self.railcars.append(railcar)
    

    # This method removes the railcar at the end of the train
    def remove_railcar(self):
        if self.railcars:
            self.railcars.pop()
    

    # This method adds a locomotive
    def add_locomotive(self, locomotive):
        self.locomotives.append(locomotive)
    

    # This method removes a locomotive as long as it is not the only locomotive on the train
    def remove_locomotive(self):
        if len(self.locomotives) > 1:
            self.locomotives.pop()
    
    
    # This method prints the information about the train to the user
    def print_train(self):
        # This is the payload of the train
        payload = self.get_payload()
        # This is the speed of the train
        speed = self.get_speed()
        # This is the length of the train
        length = self.get_length()
        
        # This prints the payload, speed, and length for the user
        print(f"Payload: {payload} tons")
        print(f"Speed: {speed:.1f} mph")
        print(f"Length: {length} meters")
        
        # This creates the composition variable and makes it an empty string
        composition = ""

        # This iterates over all the locomotives and adds an L to the composition
        for locomotive in self.locomotives:
            composition += ". L . "
        
        # This iterates over all the railcars and adds a P for passenger or F for freight to the composition
        for railcar in self.railcars:
            if railcar.get_cargo_type() == "Passenger":
                composition += ". P . "
            else:
                composition += ". F . "
        
        print(composition)

# This is the example information for the train
if __name__ == "__main__":
    # This creates some locomotives for the train
    loco1 = Locomotive(locomovitve_length=23, locomovitve_max_payload=150, locomovitve_max_speed=100)
    loco2 = Locomotive(locomovitve_length=24, locomovitve_max_payload=160, locomovitve_max_speed=110)
    
    # This creates some railcars for the train
    railcar1 = Railcar(railcar_length=20, railcar_cargo_type="Passenger", railcar_min_weight=10, railcar_max_weight=50, railcar_capacity=0.5)
    railcar2 = Railcar(railcar_length=20, railcar_cargo_type="Freight", railcar_min_weight=15, railcar_max_weight=60, railcar_capacity=0.7)
    railcar3 = Railcar(railcar_length=20, railcar_cargo_type="Passenger", railcar_min_weight=20, railcar_max_weight=70, railcar_capacity=0.9)

    # This creates the train and adds the locomotives and railcars
    train = Train()
    train.add_locomotive(loco1)
    train.add_locomotive(loco2)
    train.add_railcar(railcar1)
    train.add_railcar(railcar2)
    train.add_railcar(railcar3)
    
    # This prints the information about the train
    train.print_train()