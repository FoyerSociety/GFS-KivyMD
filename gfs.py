# -*- coding: utf-8 -*-
from kivy.config import Config 
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '978')
Config.set('graphics', 'height', '628')

########################################################
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.font_definitions import fonts
from kivy.factory import Factory
from kivy.lang import Builder

########################################################
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
        
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
        self.__tableau()

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

    
    def __tableau(self):
        tab = MDDataTable(
            size_hint=(0.9, 0.3),
            column_data=[
                ("Lundi", dp(24)),
                ("Mardi", dp(24)),
                ("Mercredi", dp(24)),
                ("Jeudi", dp(24)),
                ("Vendredi", dp(24)),
                ("Samedi", dp(24)),
                ("Dimanche", dp(24)),
            ],
            row_data=[
                (
                    "Trondro frite",
                    "Petsay",
                    "Akoho Sauce",
                    "Kitoza",
                    "Chou Sauce",
                    "Tsaramaso",
                    "Légumes",
                ),
                (
                    "4 500 Ar",
                    "2 500 Ar",
                    "5 000 Ar",
                    "6 000 Ar",
                    "2 000 Ar",
                    "3 500 Ar",
                    "3 000 Ar",
                )
            ],
        )

        self.INTERFACE.ids.tableau_repas.add_widget(tab)
    
GFS().run()      