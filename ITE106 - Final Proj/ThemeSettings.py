from dearpygui_ext.themes import *

class strt:
    def radioButtons(self):
        def themeSettings(self, data):
            if data == "Night":
                darkTheme = create_theme_imgui_dark()
                dpg.bind_theme(darkTheme)

            elif data == "Day":
                lightTheme = create_theme_imgui_light()
                dpg.bind_theme(lightTheme)

            else:
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

        dpg.add_radio_button(["Default", "Day", "Night"], label="radio", callback=themeSettings)
