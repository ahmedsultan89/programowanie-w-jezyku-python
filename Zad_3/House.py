from Property import Property

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House at {self.address}, Area: {self.area} m², Rooms: {self.rooms}, "
            f"Price: ${self.price}, Plot size: {self.plot} m²"
        )