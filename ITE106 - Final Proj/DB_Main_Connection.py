from DB import DB
from DB2 import DB2
from DB3 import DB3

class a:
    db = DB('products')
    db2 = DB2('suppliers')
    db3 = DB('categories')

    def countOfProducts(self):
        return self.db.countOfProducts()

    def allProductStock(self):
        count = 0
        for i in range(0, len(self.db.getAllStocks())):
            count = count + self.db.getAllStocks()[i][0]
        return count

    def supplierIdCombo(self):
        return self.db2.supplierIdCombo()

    def countOfSuppliers(self):
        return self.db.countOfSuppliers()