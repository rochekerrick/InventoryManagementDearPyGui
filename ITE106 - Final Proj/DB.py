import connection_DB


class DB:
    id = 0

    def __init__(self, table):
        self.cursorObject = connection_DB.myConnection.cursor()
        self.table = table

    def get_ID(self):
        return self.id

    def set_ID(self, id):
        self.id = id

    def countOfProducts(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT COUNT(id) FROM products')
                count = cur.fetchone()[0]
                self.closeConn()
            return count
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def countOfStocks(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT SUM(stock) FROM products')
                count = cur.fetchone()[0]
                self.closeConn()

            return count
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def createRow(self,data):
        self.recon()
        try:
            with self.cursorObject as cur:
                # data format: (Attr1, Attr2, Attr3, Attr4, Attr5, Attr6, Attr7, Attr8, Attr9, Attr10)
                cur.execute('INSERT INTO ' + self.table + ' VALUES(0, %s, %s, %s, %s, %s, %s)',
                            (data[0], int(data[1]), int(data[2]), int(data[3]), float(data[4]), int(data[5]) ))
                self.closeConn()
                print('New row inserted with data: {}'.format(data))

        except Exception as e:
            print("Exception occurred: {}".format(e))

    def supplierIdCombo(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute("SELECT DISTINCT supplierID FROM "+ self.table)
                rows = cur.fetchall()
                id = [row[0] for row in rows]
                self.closeConn()
                return id

        except Exception as e:
            print("Exception occurred: {}".format(e))

    def categoryIdCombo(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute("SELECT DISTINCT categoryID FROM "+ self.table )
                rows = cur.fetchall()
                id = [row[0] for row in rows]
                self.closeConn()

                return id

        except Exception as e:
            print("Exception occurred: {}".format(e))

    def readSingleData2(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute("SELECT * FROM " + self.table + " WHERE id = '" + str(data) + "'")
                rows = cur.fetchall()
                self.closeConn()

                return rows

        except Exception as e:
            print("Exception occured:{}".format(e))

    def readSingleData(self, data):
        self.recon()
        with self.cursorObject as cur:
            cur.execute('SELECT * FROM ' + self.table + ' where id = ' + str(data)) # DB query
            data = cur.fetchall()  # get all data

            print(data)
            print("daf")
            arr = [data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6]]

            self.set_ID(data[0][0])
            self.closeConn()

            return arr

    def readData(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table)  # DB query
                rows = cur.fetchall()  # get all data
                self.closeConn()

                for data in rows:
                    print(f'{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]} {data[6]}')  # this will depend on the number of cols
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def updateData(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute("UPDATE products SET productName = %s, supplierID = %s, categoryID = %s, quantity = %s, unitPrice = %s, stock = %s WHERE id = %s",
                            (data[1], data[2], data[3], data[4], data[5], data[6], data[0]))
                print('UPDATED {}'.format(data))
                self.closeConn()

        except Exception as e:
            print("Exception occured:{}".format(e))

    def deleteData(self, data):
        self.recon()
        try:
            deletequery = "delete from " + self.table + " where id = '" + data + "'"
            self.cursorObject.execute(deletequery)
            self.closeConn()

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def getAllRows(self):
        self.cursorObject.execute(f"SELECT * FROM {self.table}")
        rows = self.cursorObject.fetchall()
        self.closeConn()
        return rows

    def getAllProducts(self):
        self.cursorObject.execute(f"SELECT productName FROM {self.table}")
        rows = self.cursorObject.fetchall()
        self.closeConn()
        return rows

        # dinagdag ko
    def countOfSuppliers(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT COUNT(SupplierID) FROM suppliers')
                count = cur.fetchone()[0]
            return count
        except Exception as e:
            print("Exception occurred: {}".format(e))

    # may ginalaw ako
    def getAllStocks(self):
        self.recon()
        try:
            self.cursorObject.execute(f"SELECT stock FROM {self.table}")
            rows = self.cursorObject.fetchall()
            self.closeConn()
            return rows

        except Exception as e:
            print("Exeception occured:{}".format(e))

        # may ginalaw ako

    def getAllStocksWithProductName(self):
        self.recon()
        try:
            self.cursorObject.execute(f"SELECT stock, ProductName FROM {self.table} ORDER BY stock ASC")
            rows = self.cursorObject.fetchall()
            self.closeConn()
            return rows

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def set_Table(self, table):
        self.table = table

    def recon(self):
        self.cursorObject = connection_DB.myConnection.cursor()

    def closeConn(self):
        self.cursorObject.close()

    def getLowestStocks(self):
        self.cursorObject.execute("SELECT productName FROM products ORDER BY stock ASC  LIMIT 5")
        rows = self.cursorObject.fetchall()
        self.closeConn()
        return rows

    def getValueLowestStocks(self):
        self.recon()
        try:
            self.cursorObject.execute(f"SELECT stock FROM products ORDER BY stock ASC  LIMIT 5")
            rows = self.cursorObject.fetchall()
            self.closeConn()
            return rows

        except Exception as e:
            print("Exeception occured:{}".format(e))

