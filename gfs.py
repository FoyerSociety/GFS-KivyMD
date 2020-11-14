from kivy.config import Config 
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '978')
Config.set('graphics', 'height', '628')

########################################################
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.font_definitions import fonts
from kivy.factory import Factory
from kivy.lang import Builder

########################################################
from kivymd.theming import ThemableBehavior
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
        
class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GFS(MDApp):
    def __init__(self):
        super().__init__()
        self.INTERFACE = Builder.load_file('main.kv')
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A700"

    def build(self):
        
        menu_items = [
            {"icon": "account", "text": "Profil"},
            {"icon": "logout", "text": "Déconnexion"}
        ]
        self.menu = MDDropdownMenu(
            caller=self.INTERFACE.ids.button_2,
            items=menu_items,
            width_mult=5,
            )

        self.menu.bind(on_release=self.set_item)

        return self.INTERFACE
    
    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.field.text = instance_menu_item.text
            instance_menu.dismiss()
        Clock.schedule_once(set_item, 0.5)    

    def on_start(self):
        pass
    
GFS().run()      
