from Property import Property


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat at {self.address}, Area: {self.area} m², "
            f"Rooms: {self.rooms}, "
            f"Price: ${self.price}, Floor: {self.floor}"
        )
