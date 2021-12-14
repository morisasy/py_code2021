# customer

class Customer:
    """
     class: Customer represent an object
     attr:
            name: name of the customer
            membership_type: type of customer membership. eg. gold, silver,

     methods:
     update_membership: update status
     print_all_customers: return all customer
    """

    def __init__(self, name, membership_type):
        """
            instantiate customer object.
        """
        self.name = name
        self.membership_type = membership_type
        print("customer created ")

    def update_membership(self, new_membership_type):
        """ method to update membership status
            params:
                new_membership_typ: update membership status
        """
        self.membership_type = new_membership_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    @name.deleter
    def name(self, name):
        print("setting name")
        self._name = name
        

    def __str__(self):
        print("converting to string")
        return f"{self.name} {self.membership_type}"

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type:
            return True
        return False


customers = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze")]
c = Customer("Salome", "Gold")
print(c.name, c.membership_type)
c2 = Customer("Brand", "Pronze")
print(c2.name, c2.membership_type)
print(customers[1].membership_type)
print(customers[1].update_membership("gold"))
print(customers[0]== customers[1])
print(Customer.__doc__)
