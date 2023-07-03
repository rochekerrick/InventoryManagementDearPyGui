import dearpygui.dearpygui as dpg
import DB_Main_Connection as dbmc
import Function as f



supplierDB = dbmc.DB2('suppliers')

# array_pos = []


def clearTable(table_tag):
    # delete headers
    dpg.delete_item("TAG0")
    dpg.delete_item("TAG1")
    dpg.delete_item("TAG2")
    dpg.delete_item("TAG3")
    dpg.delete_item("TAG4")
    dpg.delete_item("TAG5")
    dpg.delete_item("TAG6")
    dpg.delete_item("TAG7")
    dpg.delete_item("TAG8")

    # delete data rows
    for tag in dpg.get_item_children(table_tag)[1]:
        dpg.delete_item(tag)


def updateTable(sender, app_data, user_data):
    try:
        supplierDB.recon()
        # parent is table tag
        parent = user_data
        # delete previous table data then recreate with new data
        clearTable(parent)

        dpg.add_table_column(label="Supplier ID", parent=parent, tag="TAG0", width=20, width_fixed=True)
        dpg.add_table_column(label="Company Name", parent=parent, tag="TAG1")
        dpg.add_table_column(label="Contact Employee", parent=parent, tag='TAG2', width=25, width_fixed=True)
        dpg.add_table_column(label="Contact Title", parent=parent, tag='TAG3')
        dpg.add_table_column(label="Address", parent=parent, tag='TAG4')
        dpg.add_table_column(label="City", parent=parent, tag='TAG5')
        dpg.add_table_column(label="Country", parent=parent, tag='TAG6')
        dpg.add_table_column(label="Phone", parent=parent, tag='TAG7')
        dpg.add_table_column(label="Action", parent=parent, tag='TAG8')

        data = supplierDB.getAllRows()
        for data_key, data_value in enumerate(data):
            with dpg.table_row(parent=parent):
                dpg.add_text(data_value[0])
                dpg.add_text(data_value[1])
                dpg.add_text(data_value[2])
                dpg.add_text(data_value[3])
                dpg.add_text(data_value[4])
                dpg.add_text(data_value[5])
                dpg.add_text(data_value[6])
                dpg.add_text(data_value[7])
                with dpg.table_cell():
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="DELETE", user_data=data_value[0], callback=deleteButton)
                        dpg.add_button(label="UPDATE", user_data=data_value[0], callback=updateButton)


    except Exception as e:
        print(e)


def deleteButton(sender, app_data, user_data):
    dpg.show_item("modalSupplier2")
    data = supplierDB.readSingleData(user_data)
    print(data)

def delete(sender, app_data, user_data):
    # delete data from database
    print('delete function: ', supplierDB.get_ID())
    supplierDB.deleteData(supplierDB.get_ID())

    x = dbmc.a().countOfProducts()
    y = dbmc.a().allProductStock()
    z = dbmc.a().countOfSuppliers()
    f.buttonCount_Set(x, y, z)

    updateTable('', '', user_data="datatable2")
    dpg.configure_item("modalSupplier2", show=False)

def updateButton(sender, app_data, user_data):
    dpg.show_item('modalSupplier3')
    data = supplierDB.readSingleData2(user_data)
    print(data)
    for key_value, data_value in enumerate(data):
        dpg.set_value('supplier', data_value[0])
        dpg.set_value('companyName2', data_value[1])
        dpg.set_value('contactEmployee2', data_value[2])
        dpg.set_value('contactTitle2', data_value[3])
        dpg.set_value('address2', data_value[4])
        dpg.set_value('city2', data_value[5])
        dpg.set_value('country2', data_value[6])
        dpg.set_value('phone2', data_value[7])


def update_(sender, app_data, user_data):
    supplierID = dpg.get_value('supplier')
    companyName = dpg.get_value('companyName2')
    contactEmployee = dpg.get_value('contactEmployee2')
    contactTitle = dpg.get_value('contactTitle2')
    address = dpg.get_value('address2')
    city = dpg.get_value('city2')
    country = dpg.get_value('country2')
    phone = dpg.get_value('phone2')

    print(companyName)
    res = supplierID, companyName, contactEmployee, contactTitle, address, city, country, phone
    supplierDB.updateData(res)
    updateTable('', '', user_data="datatable2")
    dpg.configure_item("modalSupplier3", show=False)


def saveData(sender, data):
    # get data from input fields
    companyName = dpg.get_value('companyName')
    contactEmployee = dpg.get_value('contactEmployee')
    contactTitle = dpg.get_value('contactTitle')
    address = dpg.get_value('address')
    city = dpg.get_value('city')
    country = dpg.get_value('country')
    phone = dpg.get_value('phone')
    supplierDB.createRow((companyName, contactEmployee, contactTitle, address, city, country, phone))

    x = dbmc.a().countOfProducts()
    y = dbmc.a().allProductStock()
    z = dbmc.a().countOfSuppliers()
    f.buttonCount_Set(x, y, z)

    updateTable('', '', user_data="datatable2")
    dpg.configure_item("modalSupplier", show=False)


def clearTextfields(sender, data):
    dpg.set_value('companyName', '')
    dpg.set_value('contactEmployee', '')
    dpg.set_value('contactTitle', '')
    dpg.set_value('address', '')
    dpg.set_value('city', '')
    dpg.set_value('country', '')
    dpg.set_value('phone', '')


# with dpg.window(label="Inventory System", width=885, height=600, no_close=True, no_title_bar=False, no_move=True,
#                 pos=[0, 18]):

def str():
    x = 'total_Products_Suppliers'
    y = 'total_Stocks_Suppliers'
    z = 'total_Suppliers_Suppliers'
    f.buttonCount(x, y, z)

    dpg.add_table(tag="datatable2")
    updateTable('', '', user_data="datatable2")

    dpg.add_button(label="Create")
    # check out simple module for details
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modalSupplier"):
        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Company Name: ")
            dpg.add_input_text(tag="companyName")

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Contact Employee: ")
            dpg.add_input_text(tag="contactEmployee")

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Contact Title: ")
            dpg.add_input_text(tag="contactTitle")

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Address: ")
            dpg.add_input_text(tag="address")

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("City: ")
            dpg.add_input_text(tag="city")

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Country: ")
            dpg.add_input_text(tag="country")

        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Phone: ")
            dpg.add_input_text(tag="phone")

        with dpg.group(horizontal=True, xoffset=50):
            dpg.add_button(label='Clear', callback=clearTextfields)
            dpg.add_button(label='Save', callback=saveData, user_data="datatable2")

        # DELETE MODAL
        f.deleteModal('modalSupplier2', delete)

        # UPDATE MODAL
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modalSupplier3"):
        dpg.add_text("UPDATE DETAILS")
        # db.deleteData()
        with dpg.group(horizontal=True):
            dpg.add_text('Supplier ID:')
            dpg.add_text(tag="supplier")
        with dpg.group(horizontal=True):
            dpg.add_text('Company Name:')
            dpg.add_input_text(tag='companyName2')
        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Contact Employee: ")
            dpg.add_input_text(tag="contactEmployee2")
        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Contact Title: ")
            dpg.add_input_text(tag="contactTitle2")
        with dpg.group(horizontal=True):
            dpg.add_text('Address:')
            dpg.add_input_text(tag="address2")
        with dpg.group(horizontal=True):
            dpg.add_text('City:')
            dpg.add_input_text(tag="city2")
        with dpg.group(horizontal=True):
            dpg.add_text('Country:')
            dpg.add_input_text(tag="country2")
        with dpg.group(horizontal=True):
            dpg.add_text('Phone:')
            dpg.add_input_text(tag="phone2")

        with dpg.group(horizontal=True):
            dpg.add_button(label="Save", callback=update_)
            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modalSupplier3", show=False))

