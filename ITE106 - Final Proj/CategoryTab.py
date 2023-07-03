import dearpygui.dearpygui as dpg
import DB_Main_Connection as dbmc
import Function as f


categoryDB = dbmc.DB3('categories')


def clearTable(table_tag):
    # delete headers
    dpg.delete_item("TAGS0")
    dpg.delete_item("TAGS1")
    dpg.delete_item("TAGS2")

    # delete data rows
    for tag in dpg.get_item_children(table_tag)[1]:
        dpg.delete_item(tag)


def updateTable(sender, app_data, user_data):
    try:
        categoryDB.recon()
        # parent is table tag
        parent = user_data
        # delete previous table data then recreate with new data

        clearTable(parent)

        dpg.add_table_column(label="Category ID", parent=parent, tag="TAGS0", width=20, width_fixed=True)
        dpg.add_table_column(label="Category Name", parent=parent, tag="TAGS1")
        dpg.add_table_column(label="Action", parent=parent, tag='TAGS2')

        data = categoryDB.getAllRows()

        for data_key, data_value in enumerate(data):
            with dpg.table_row(parent=parent):
                dpg.add_text(data_value[0])
                dpg.add_text(data_value[1])

                with dpg.table_cell():
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="DELETE", user_data=data_value[0], callback=deleteButton)
                        dpg.add_button(label="UPDATE", user_data=data_value[0], callback=updateButton)

    except Exception as e:
        print(e)


def deleteButton(sender, app_data, user_data):
    dpg.show_item("modalCategory2")
    data = categoryDB.readSingleData(user_data)
    print(data)



def delete(sender, app_data, user_data):
    # delete data from database

    print('delete function: ', categoryDB.get_ID())
    categoryDB.deleteData(str(categoryDB.get_ID()))

    updateTable('', '', user_data="datatable3")
    dpg.configure_item("modalCategory2", show=False)

def updateButton(sender, app_data, user_data):
    dpg.show_item('modalCategory3')
    data = categoryDB.readSingleData2(user_data)
    print(data)
    for key_value, data_value in enumerate(data):
        dpg.set_value('category', data_value[0])
        dpg.set_value('categoryName2', data_value[1])


def update_(sender, app_data, user_data):
    categoryID = dpg.get_value('category')
    categoryName = dpg.get_value('categoryName2')
    print(categoryName)
    res = (categoryID, categoryName)
    categoryDB.updateData(res)
    updateTable('', '', user_data="datatable3")
    dpg.configure_item("modalCategory3", show=False)


def saveData(sender, data):
    # get data from input fields
    categoryName = dpg.get_value('categoryName')

    categoryDB.createRow(categoryName)
    updateTable('', '', user_data="datatable3")
    dpg.configure_item("modalCategory", show=False)


def clearTextfields(sender, data):
    dpg.set_value('categoryName', '')


# with dpg.window(label="Inventory System", width=885, height=600, no_close=True, no_title_bar=False, no_move=True,
#                 pos=[0, 18]):
def strt():
    x = 'total_Products_Category'
    y = 'total_Stocks_Category'
    z = 'total_Suppliers_Category'
    f.buttonCount(x, y, z)

    dpg.add_table(tag="datatable3")
    updateTable('', '', user_data="datatable3")

    dpg.add_button(label="Create")
    # check out simple module for details
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modalCategory"):
        with dpg.group(horizontal=True, xoffset=120):
            dpg.add_text("Category Name: ")
            dpg.add_input_text(tag="categoryName")

        with dpg.group(horizontal=True, xoffset=50):
            dpg.add_button(label='Clear', callback=clearTextfields, pos=[180, 70])
            dpg.add_button(label='Save', callback=saveData, user_data="datatable3", pos=[225, 70])

        # DELETE MODAL
        f.deleteModal('modalCategory2', delete)

        # UPDATE MODAL
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modalCategory3"):
        dpg.add_text("UPDATE DETAILS")
        # db.deleteData()
        with dpg.group(horizontal=True):
            dpg.add_text('Category ID:')
            dpg.add_text(tag="category")
        with dpg.group(horizontal=True):
            dpg.add_text('Category Name:')
            dpg.add_input_text(tag='categoryName2')

        with dpg.group(horizontal=True):
            dpg.add_button(label="Save", callback=update_)
            dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modalCategory3", show=False))


