from kivy.config import Config 
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '950')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts
from kivy.factory import Factory
from kivy.lang import Builder

class ContentNavigationDrawer(BoxLayout):
    pass

class GFS(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A700"
        return Builder.load_file('navigation.kv')
    
    def rail_open(self):
        if self.root.ids.rail.state == "open":
            self.root.ids.rail.state = "close"
        else:
            self.root.ids.rail.state = "open"
    

GFS().run()                