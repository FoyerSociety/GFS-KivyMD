from kivy.config import Config 
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '950')
Config.set('graphics', 'height', '580')

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts
from kivy.lang import Builder


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class ContentNavigationDrawer(BoxLayout):
    pass

class GFS(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A700"
        return Builder.load_file('navigation.kv')

    def on_start(self):
        nom_icons = ('home', 'food', 'broom', 'cash', 'flash', 'backup-restore' )
        nom_tabs = ('Générale', 'Cuisine', 'Ménage', 'Cotisation', 'Jirama', 'Trosa')
        i = 0
        while (i < 6):
            self.root.ids.tabs.add_widget(
                Tab(
                    text = f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[nom_icons[i]]}[/size][/font] {nom_tabs[i]}"
                )
            )
            i += 1
        
           
        

      


GFS().run()                