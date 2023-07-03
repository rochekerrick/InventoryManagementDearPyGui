import dearpygui.dearpygui as dpg
import Function as f
import DB_Main_Connection as dbmc



array_pos = []

# print(db2.supplierIdCombo())


def clearTable(table_tag):
    # delete headers
    dpg.delete_item("TAG-0")
    dpg.delete_item("TAG-1")
    dpg.delete_item("TAG-2")
    dpg.delete_item("TAG-3")
    dpg.delete_item("TAG-4")
    dpg.delete_item("TAG-5")
    dpg.delete_item("TAG-6")
    dpg.delete_item("TAG-7")

    # delete data rows
    for tag in dpg.get_item_children(table_tag)[1]:
        dpg.delete_item(tag)

def updateTable(sender, app_data, user_data):
    try:
        dbmc.a().db.recon()
        # parent is table tag
        parent = user_data
        # delete previous table data then recreate with new data
        clearTable(parent)

        dpg.add_table_column(label="ID", parent=parent, tag="TAG-0", width=20, width_fixed=True)
        dpg.add_table_column(label="Product Name", parent=parent, tag="TAG-1")
        dpg.add_table_column(label="Supplier ID", parent=parent, tag='TAG-2', width=25, width_fixed=True)
        dpg.add_table_column(label="Category ID", parent=parent, tag='TAG-3')
        dpg.add_table_column(label="Quantity", parent=parent, tag='TAG-4')
        dpg.add_table_column(label="Unit Price", parent=parent, tag='TAG-5')
        dpg.add_table_column(label="Stock", parent=parent, tag='TAG-6')
        dpg.add_table_column(label="Action", parent=parent, tag='TAG-7')

        data = dbmc.a().db.getAllRows()
        for data_key, data_value in enumerate(data):
            with dpg.table_row(parent=parent):
                dpg.add_text(data_value[0])
                dpg.add_text(data_value[1])
                dpg.add_text(data_value[2])
                dpg.add_text(data_value[3])
                dpg.add_text(data_value[4])
                dpg.add_text(data_value[5])
                dpg.add_text(data_value[6])
                with dpg.table_cell():
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="DELETE", user_data=data_value[0], callback=deleteButton)
                        dpg.add_button(label="UPDATE", user_data=data_value[0], callback=updateButton)

        update_series('', '', parent)
        dpg.set_axis_ticks("x-axis", graph())
        dpg.set_axis_limits_auto("x-axis")
        dpg.fit_axis_data("x-axis")
        update_pie()


    except Exception as e:
        print(e)

def deleteButton(sender, app_data, user_data):
    dpg.show_item("modal2")
    data = dbmc.a().db.readSingleData(user_data)
    print(data)

def delete(sender, app_data, user_data):
    # delete data from database

    print('delete function: ', dbmc.a().db.get_ID())
    dbmc.a().db.deleteData(str(dbmc.a().db.get_ID()))

    x = dbmc.a().countOfProducts()
    y = dbmc.a().allProductStock()
    z = dbmc.a().countOfSuppliers()
    f.buttonCount_Set(x, y, z)

    updateTable('', '', user_data="datatable")
    dpg.configure_item("modal2", show=False)


def updateButton(sender, app_data, user_data):
    dpg.show_item('modal3')
    data = dbmc.a().db.readSingleData2(user_data)
    print(data)
    for key_value, data_value in enumerate(data):
        dpg.set_value('id2', data_value[0])
        dpg.set_value('productName2', data_value[1])
        dpg.set_value('supplierID2', data_value[2])
        dpg.set_value('categoryID2', data_value[3])
        dpg.set_value('quantity2', data_value[4])
        dpg.set_value('unitPrice2', data_value[5])
        dpg.set_value('stock2', data_value[6])

def update_(sender, app_data, user_data):
    id = dpg.get_value('id2')
    productName = dpg.get_value('productName2')
    supplierID = dpg.get_value('supplierID2')
    categoryID = dpg.get_value('categoryID2')
    quantity = dpg.get_value('quantity2')
    unitPrice = dpg.get_value('unitPrice2')
    stock = dpg.get_value('stock2')
    print(productName)
    res = id, productName, supplierID, categoryID, quantity, unitPrice, stock
    dbmc.a().db.updateData(res)

    x = dbmc.a().countOfProducts()
    y = dbmc.a().allProductStock()
    z = dbmc.a().countOfSuppliers()
    f.buttonCount_Set(x, y, z)

    updateTable('', '', user_data="datatable")
    dpg.configure_item("modal3", show=False)

def saveData(sender, data):
    # get data from input fields

    productName = dpg.get_value('productName')
    supplierID = dpg.get_value('supplierID')
    categoryID = dpg.get_value('categoryID')
    quantity = dpg.get_value('quantity')
    unitPrice = dpg.get_value('unitPrice')
    stock = dpg.get_value('stock')
    dbmc.a().db.createRow((productName, supplierID, categoryID, quantity, unitPrice, stock))

    x = dbmc.a().countOfProducts()
    y = dbmc.a().allProductStock()
    z = dbmc.a().countOfSuppliers()
    f.buttonCount_Set(x, y, z)

    update_series('', '', str(dbmc.a().db.get_ID()))
    updateTable('', '', user_data="datatable")
    dpg.configure_item("modal", show=False)


def clearTextfields(sender, data):
    dpg.set_value('productName', '')
    dpg.set_value('supplierID', 0)
    dpg.set_value('categoryID', 0)
    dpg.set_value('quantity', 0)
    dpg.set_value('unitPrice', 0.00)
    dpg.set_value('stock', 0)

def graph():
    db = dbmc.DB('products')
    db.recon()
    rows = db.getAllProducts()

    new_value = 2
    tup_list = list(rows)

    for i in range(len(tup_list)):
        tup_list[i] += (new_value,)
        new_value += 2

    new_tup = tuple(tup_list)

    # Print the original and updated tuples
    return new_tup


def SortedProductName():

    x = dbmc.a().db.getAllStocksWithProductName()
    y = []
    for i in range(0, 5):
        y.append(x[i][1])
    return y

def SortedStock():

    x = dbmc.a().db.getAllStocksWithProductName()
    y = []
    for i in range(0, 5):
        y.append(x[i][0])
    return y


def position():
    new_tup = graph()
    second_column_values = []
    for row in new_tup:
        second_column_values.append(row[1])

    return second_column_values

def valueStocks():
    db = dbmc.DB('products')
    db.recon()
    rows = db.getAllStocks()

    # extract the values of the first column from the rows tuple
    first_column_values = []
    for row in rows:
        first_column_values.append(row[0])
    return first_column_values

def update_series(sender, app_data, user_data):
    pos = position()
    values = valueStocks()

    print(pos, values)
    dpg.set_value('chart', [pos, values])

def update_pie():
    pos = getLowestValueStocks()
    values = getLowestStocks()

    print(pos, values)
    dpg.set_value('chart2', [pos, values])

def getLowestValueStocks():
    db = dbmc.DB('products')
    db.recon()
    rows = db.getValueLowestStocks()
    first_column_values = []

    for row in rows:
        first_column_values.append(row[0])

    return first_column_values


def getLowestStocks():
    db = dbmc.DB('products')
    db.recon()
    rows = db.getLowestStocks()

    first_column_values = []
    for row in rows:
        first_column_values.append(row[0])

    return first_column_values


def struct():
    # btn
    x = 'total_Products_Products'
    y = 'total_Stocks_Products'
    z = 'total_Suppliers_Products'
    f.buttonCount(x, y, z)

    dpg.add_text(dbmc.a().db.getAllStocksWithProductName())



    with dpg.child_window(autosize_x=True, height=305):
        # dpg.add_plot(tag="graphStocks")
        # dpg.add_plot_axis(dpg.mvXAxis,tag='graphStocks')
        # updateGraph('','',user_data="graphStocks")
        with dpg.group(horizontal=True):
            with dpg.plot( height=305, width=800):
                dpg.add_plot_legend()
                # create x axis
                dpg.add_plot_axis(dpg.mvXAxis, label="Product Name", no_gridlines=True, tag="x-axis")

                # create y axis
                with dpg.plot_axis(dpg.mvYAxis, label="Stocks"):
                    dpg.set_axis_limits(dpg.last_item(), 0, 310)
                    dpg.add_bar_series(position(), valueStocks(), label="Number of Stocks", weight=1, tag="chart")

            #pie
            with dpg.plot(no_title=True, no_mouse_pos=True, height=305, width=400):
                # create legend
                dpg.add_plot_legend()

                # create x axis
                dpg.add_plot_axis(dpg.mvXAxis, label="", no_gridlines=True, no_tick_marks=True, no_tick_labels=True)
                dpg.set_axis_limits(dpg.last_item(), 0, 1)

                # create y axis
                with dpg.plot_axis(dpg.mvYAxis, label="", no_gridlines=True, no_tick_marks=True, no_tick_labels=True):
                    dpg.set_axis_limits(dpg.last_item(), 0, 1)
                    dpg.add_pie_series(0.5, 0.5, 0.3, getLowestValueStocks(), getLowestStocks(), tag="chart2")




    with dpg.child_window(autosize_x=True, height=305):
        dpg.add_table(tag="datatable")
        updateTable('', '', user_data="datatable")

        dpg.add_button(label="Create")

    # check out simple module for details
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal"):

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Product Name: ")
            dpg.add_input_text(tag='productName')

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Supplier ID: ")
            dpg.add_combo(dbmc.a().db2.supplierIdCombo(), width=50, tag='supplierID')

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Category ID: ")
            dpg.add_combo(dbmc.a().db3.categoryIdCombo(), width=50, tag='categoryID')

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Quantity: ")
            dpg.add_input_int(tag='quantity')

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Unit Price: ")
            dpg.add_input_float(tag='unitPrice')

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Stock: ")
            dpg.add_input_int(tag='stock')

        with dpg.group(horizontal=True, xoffset=50):
            dpg.add_button(label='Clear', callback=clearTextfields, pos=[170, 200])
            dpg.add_button(label='Save', callback=saveData, user_data="datatable", pos=[225, 200])

        # DELETE MODAL
        f.deleteModal('modal2', delete)

        # UPDATE MODAL
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal3"):
        dpg.add_text("UPDATE DETAILS")
        # db.deleteData()
        with dpg.group(horizontal=True):
            dpg.add_text('ID:')
            dpg.add_text(tag='id2')
        with dpg.group(horizontal=True):
            dpg.add_text('Product Name:')
            dpg.add_input_text(tag='productName2')
        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Supplier ID: ")
            dpg.add_combo(dbmc.a().db2.supplierIdCombo(), width=50, tag='supplierID2')
        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Category ID: ")
            dpg.add_combo(dbmc.a().db3.categoryIdCombo(), width=50, tag='categoryID2')
        with dpg.group(horizontal=True):
            dpg.add_text('Quantity:')
            dpg.add_input_int(tag="quantity2")
        with dpg.group(horizontal=True):
            dpg.add_text('Unit Price:')
            dpg.add_input_float(tag="unitPrice2")
        with dpg.group(horizontal=True):
            dpg.add_text('Stock:')
            dpg.add_input_int(tag="stock2")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Save", callback=update_)
            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal3", show=False))
