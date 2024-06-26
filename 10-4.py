class ManageCustomer(Customer):
    cart=Customer
    def addbill(self):
        self.total=cart.total+50
    def payment(self):
        self.total=cart.total-100
