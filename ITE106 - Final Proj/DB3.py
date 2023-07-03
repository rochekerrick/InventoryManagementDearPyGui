import connection_DB

class DB3:
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
            return count
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def countOfStocks(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT SUM(stock) FROM products')
                count = cur.fetchone()[0]
            return count
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def createRow(self,data):
        self.recon()
        try:
            with self.cursorObject as cur:
                # data format: (Attr1, Attr2, Attr3, Attr4, Attr5, Attr6, Attr7, Attr8, Attr9, Attr10)
                cur.execute('INSERT INTO ' + self.table + ' VALUES(0, %s)',data)
                cur.close()
                print('New row inserted with data: {}'.format(data))

        except Exception as e:
            print("Exception occurred: {}".format(e))

    def readSingleData2(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute("SELECT * FROM " + self.table + " WHERE CategoryID = '" + str(data) + "'")
                rows = cur.fetchall()
                return rows

        except Exception as e:
            print("Exception occured:{}".format(e))

    def readSingleData(self, data):
        self.recon()
        with self.cursorObject as cur:
            cur.execute('SELECT * FROM ' + self.table + ' where CategoryID = ' + str(data)) # DB query
            data = cur.fetchall()  # get all data

            print(data)
            print("daf")
            arr = [data[0][0], data[0][1]]

            self.set_ID(data[0][0])
            return arr

    def readData(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table)  # DB query
                rows = cur.fetchall()  # get all data
                for data in rows:
                    print(f'{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]} {data[6]}')  # this will depend on the number of cols
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def updateData(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute("UPDATE categories SET categoryName = %s WHERE CategoryID = %s",
                            (data[1], data[0]))
                print('UPDATED {}'.format(data))

        except Exception as e:
            print("Exception occured:{}".format(e))

    def deleteData(self, data):
        self.recon()
        try:
            deletequery = "delete from " + self.table + " where CategoryID = '" + data + "'"
            self.cursorObject.execute(deletequery)
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def getAllRows(self):
        self.cursorObject.execute(f"SELECT * FROM {self.table}")
        rows = self.cursorObject.fetchall()
        return rows

    def set_Table(self, table):
        self.table = table

    def recon(self):
        self.cursorObject = connection_DB.myConnection.cursor()

    def closeConn(self):
        self.cursorObject.close()



