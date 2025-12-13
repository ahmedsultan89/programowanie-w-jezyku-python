import magazine.utils as utils  # absolute import


def show_product_info(name, price):
    print(f"Product: {name}")
    print(f"Price after discount: {utils.calculate_discount(price, 10)}")
