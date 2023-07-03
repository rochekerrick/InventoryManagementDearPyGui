import dearpygui.dearpygui as dpg
import ProductsTab
import supplierTab
import ThemeSettings
from DB import DB
import CategoryTab

db = DB('products')
db.recon()
rows = db.getAllStocks()

# extract the values of the first column from the rows tuple
first_column_values = []
for row in rows:
    first_column_values.append(row[0])

print("Values of the first column:", first_column_values)


# extract the second column from the rows tuple

dpg.create_context()
dpg.create_viewport(title='Inventory System', width=1265, height=1000, resizable=False)

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (43, 48, 58))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (199, 164, 101))
        dpg.add_theme_color(dpg.mvThemeCol_Tab, (125, 101, 49))
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (82, 66, 32))
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (159, 124, 47))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (116, 83, 62))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (199, 164, 101))
        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (74, 84, 102))
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (43, 48, 58))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (125, 101, 49))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (199, 164, 101))

dpg.bind_theme(global_theme)

with dpg.font_registry():
    default_font = dpg.add_font("Bebas.otf", 18)

    dpg.bind_font(default_font)

with dpg.window(width=1250, height=800, no_close=True, no_title_bar=True, no_move=True, pos=[0, 18], no_resize=True):
    width, height, channels, data = dpg.load_image("defaultLogo.png")

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

    with dpg.group(horizontal=True):
        dpg.add_image("texture_tag", width=int(dpg.get_item_width("texture_tag") * 0.3),
                        height=int(dpg.get_item_height("texture_tag") * 0.3), pos=[560, 10])

        # dpg.add_text("Gadgets Inventory", pos=[560, 55])

    with dpg.tab_bar():
        with dpg.tab(label="Products"):
            ProductsTab.struct()

        with dpg.tab(label="Suppliers", user_data="update"):
            supplierTab.str()

        with dpg.tab(label="Categories"):
            CategoryTab.strt()

        with dpg.tab(label="Settings"):
            ThemeSettings.strt().radioButtons()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()