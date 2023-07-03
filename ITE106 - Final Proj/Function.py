import dearpygui.dearpygui as dpg
import DB_Main_Connection as dbmc


def buttonCount(x, y, z):
    a = dbmc.a().db.countOfProducts()
    b = dbmc.a().db.countOfStocks()
    c = dbmc.a().db.countOfSuppliers()
    result = "Total Products {res}".format(res=a)
    result2 = "Total Stocks {res}".format(res=b)
    result3 = "Total Suppliers {res}".format(res=c)

        # KAYA BUTTON NILAGAY KO KASI WALANG PADDING AND BORDER DESIGN PAG TEXT PERO PAG NAGAWAN NIYO NG PARAAN MAG TEXT TAYO
    with dpg.child_window(autosize_x=True, height=95):
        with dpg.group(horizontal=True):
            dpg.add_button(label=result, width=398, height=85, tag=x)
            dpg.add_button(label=result2, width=398, height=85, tag = y)
            dpg.add_button(label=result3, width=398, height=85, tag = z)
            # dpg.add_button(label="Header 3", width=205, height=75)

            # # KAYA BUTTON NILAGAY KO KASI WALANG PADDING AND BORDER DESIGN PAG TEXT PERO PAG NAGAWAN NIYO NG PARAAN MAG TEXT TAYO
            # with dpg.child_window(autosize_x=True, height=100):
            #     with dpg.group(horizontal=True):
            #         dpg.add_button(label=result, width=398, height=85, tag='btn2')
            #         dpg.add_button(label=result2, width=398, height=85)
            #         dpg.add_button(label="Header 3", width=398, height=85)
            #         # dpg.add_button(label="Header 3", width=205, height=75)

def buttonCount_Set(x, y, z):

        dpg.set_item_label('total_Products_Products', "Total Products " + str(x))
        dpg.set_item_label('total_Products_Suppliers', "Total Products " + str(x))
        dpg.set_item_label('total_Products_Category', "Total Products " + str(x))

        dpg.set_item_label('total_Stocks_Products', "Total Products " + str(y))
        dpg.set_item_label('total_Stocks_Suppliers', "Total Products " + str(y))
        dpg.set_item_label('total_Stocks_Category', "Total Products " + str(y))

        dpg.set_item_label('total_Suppliers_Products', "Total Suppliers " + str(z))
        dpg.set_item_label('total_Suppliers_Suppliers', "Total Suppliers " + str(z))
        dpg.set_item_label('total_Suppliers_Category', "Total Suppliers " + str(z))

def deleteModal(x, y):

    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag=x):
        dpg.add_text("Are you sure you want to delete?")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Yes", callback=y)
            dpg.add_button(label="No", callback=lambda: dpg.configure_item(x, show=False))
