# -*- coding: utf-8 -*-
import sys, time
if '--prod' in sys.argv:
    PROD = True
    sys.argv.remove('--prod')
else: PROD = None 

from models.models import Database
from models.config import CONFIG
########################################################
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
from kivy.clock import Clock

########################################################
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.spinner import MDSpinner
from kivy.metrics import dp



class CustomToolbar(ThemableBehavior, RectangularElevationBehavior, MDBoxLayout):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class GFS(MDApp):


    def __init__(self):
        super().__init__()
        self.db = None

        with open('main.kv', encoding='utf-8') as f:
            self.INTERFACE = Builder.load_string(f.read())

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
        if PROD:
            self.db = Database(CONFIG)
    
    
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
    

    def loading(self):
        self.INTERFACE.ids.button_login.text = " "
        self.INTERFACE.ids.button_login.icon = " "
        self.INTERFACE.ids.loader.color = (1,1,1,1)
        self.INTERFACE.ids.loader.active = True

        Clock.schedule_once(self.login, 3)

    def login(self, event):
        if not self.db: return 
        
        username = self.INTERFACE.ids.username.text
        password = self.INTERFACE.ids.password.text
        if not PROD or self.db.login(username,password):
            self.INTERFACE.current = "Main"
            return


        # self.INTERFACE.ids.button_login.label_change("S'identifier")
        self.INTERFACE.ids.loader.active = False
        self.INTERFACE.ids.password.text = ""
        self.INTERFACE.ids.button_login.icon = "arrow-right"
        self.INTERFACE.ids.button_login.text = "S'identifier"
        self.INTERFACE.ids.errorLogin.text = "Le mot de passe est incorrect !"

GFS().run()      