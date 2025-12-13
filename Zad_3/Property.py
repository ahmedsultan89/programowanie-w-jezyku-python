class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property at {self.address}, Area: {self.area} m², Rooms: {self.rooms}, Price: ${self.price}"