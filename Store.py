# Author: Rebecca Starr
# Date: 1/15/2020
# Description: Creates 4 classes for an exception, a Product, Customer, and Store.


class InvalidCheckoutError(Exception):
    pass


class Product:
    """
    Creates a Product object with an ID code, title, description, price, and
    quantity available
    """

    def __init__(self, id_code, title, description, price, quantity_available):
        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_id_code(self):
        """Returns the ID code of the item"""
        return self._id_code

    def get_title(self):
        """Returns the title of the item"""
        return self._title

    def get_description(self):
        """Returns the description of the item"""
        return self._description

    def get_price(self):
        """Returns the price of the item"""
        return self._price

    def get_quantity_available(self):
        """Returns the I# of items available"""
        return self._quantity_available

    def decrease_quantity(self):
        """Decreases the quantity by one"""
        self._quantity_available -= 1


class Customer:
    """
    Creates a Customer object with a name and account ID. The customer can be a premium
    member and has a cart.
    """

    def __init__(self, name, account_id, premium_member):
        self._name = name
        self._account_id = account_id
        self._premium_member = premium_member
        self._cart = []

    def get_name(self):
        """Returns the customer's name"""
        return self._name

    def get_account_ID(self):
        """Returns the customer's account ID"""
        return self._account_id

    def get_cart(self):
        """Returns the customer's cart"""
        return self._cart

    def is_premium_member(self):
        """Returns whether the customer is a premium member"""
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """Adds the product id to the customer's cart"""
        self._cart.append(product_id)

    def empty_cart(self):
        """Empties the customer's cart"""
        self._cart = []


class Store:
    """
    Creates a Store object with an inventory and customer list.
    """

    def __init__(self):
        self._inventory = []
        self._customer_list = []

    def add_product(self, product):
        """Adds product to inventory list"""
        self._inventory.append(product)

    def add_customer(self, customer):
        """Adds product to inventory list"""
        self._customer_list.append(customer)

    def get_product_from_ID(self, product_id):
        """Returns the product with the given product id. If the product ID is
        not in the inventory, returns None."""
        for product in self._inventory:
            if product.get_id_code() == product_id:
                return product

    def get_member_from_ID(self, customer_id):
        """Returns the customer with the given customer id. If the customer ID is
        not in the  customer list, returns None."""
        for customer in self._customer_list:
            if customer.get_account_ID() == customer_id:
                return customer

    def product_search(self, search_word):
        """Returns a sorted list of the ID codes of all the products in the store inventory
        that match the search word."""

        search_list = []

        for product in self._inventory:
            if (search_word.lower() in product.get_title().lower()) or \
                    (search_word.lower() in product.get_description().lower()):
                search_list.append(product.get_id_code())

        search_list.sort()

        return search_list

    def add_product_to_member_cart(self, product_id, customer_id):
        """Adds the product to the customer's cart if they are a member and if the product
        is in inventory."""

        product = self.get_product_from_ID(product_id)
        customer = self.get_member_from_ID(customer_id)

        if product in self._inventory:
            if customer in self._customer_list:
                if product.get_quantity_available() > 0:
                    customer.add_product_to_cart(product_id)
                    return "product added to cart"
                else:
                    return "product out of stock"
            else:
                return "member ID not found"
        else:
            return "product ID not found"

    def check_out_member(self, customer_id):
        """Checks out the member by removing items from the store inventory that
        the customer is buying, return the price of the items, and emptying the customer's
        cart."""

        customer = self.get_member_from_ID(customer_id)

        # checking customer is in store member list
        if customer in self._customer_list:
            final_cart_price = 0

            # looping though items in cart
            for product_id in customer.get_cart():
                product = self.get_product_from_ID(product_id)

                # checking if product is in store inventory
                if product in self._inventory:

                    # checking 1+ items in inventory
                    if product.get_quantity_available() > 0:
                        final_cart_price += product.get_price()
                        product.decrease_quantity()

            # checking if customer is a premium member
            # if they are, price is final
            if customer.is_premium_member():
                customer.empty_cart()
                return final_cart_price

            # if they aren't a member, add 7% shipping fee to total price
            else:
                final_cart_price *= 1.07
                customer.empty_cart()
                return final_cart_price

        else:
            raise InvalidCheckoutError


def main():
    try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("890", "Kitten", "when a cat won't do", 200.50, 1)
        c1 = Customer("Yinsheng", "QWF", True)
        c2 = Customer("Matt", "QWG", False)
        myStore = Store()
        myStore.add_customer(c1)
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product_to_member_cart("889", "QWF")
        myStore.add_product_to_member_cart("890", "QWF")
        result = myStore.check_out_member("QWG")
    except InvalidCheckoutError:
        print("Customer is not in member list.")
    else:
        print("Total price is",  result)


if __name__ == '__main__':
    main()
