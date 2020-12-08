########################################################
# -*- coding: utf-8 -*-
import sys, time,datetime
from datetime import timedelta
if '--prod' in sys.argv:
    PROD = True
    sys.argv.remove('--prod')
else: PROD = None 
########################################################

from models.models import Database, _SESSION
from models.config import CONFIG
########################################################
from kivy.config import Config 
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '978')
Config.set('graphics', 'height', '628')

########################################################
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivymd.font_definitions import fonts
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.clock import Clock

########################################################
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton, MDRoundFlatIconButton,MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.behaviors import RectangularElevationBehavior



class CustomToolbar(ThemableBehavior, RectangularElevationBehavior, MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class GFS(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if PROD:
            self.db = Database(CONFIG)
        
        ###Load the kv file with the encoding utf8 [!important in winidows]
        with open('main.kv', encoding='utf-8') as f:
            self.INTERFACE = Builder.load_string(f.read())

        ###Application color_theme parameter in general
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style= "Light"

        self.quit_dialog = None
        self.dialog = None
        self.db = None
        self.__tableau()
        self.__tableau_status()
        self.__tableau_status_facture()
        self.transact = []
        self.__tableau_transaction(self.transact)

        ###For the MDRaisedButton in Grand-menage
        for i in range(10): self.INTERFACE.ids[f'raisedBtn{i+1}'].md_bg_color = get_color_from_hex("#2763e1")

        ###The dropdown menu in the profile button in the top-right
        menu_items = [
            {"icon": "account", "text": "Profil"},
            {"icon": "logout", "text": "Déconnexion"},
            {"icon": "exit-run", "text": "Quit"}
        ]
        self.menu = MDDropdownMenu(
            caller=self.INTERFACE.ids.button_2,
            items=menu_items,
            width_mult=5,
        )
        self.menu.bind(on_release=self.logout)


        self.date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2010,
            month=2,
            day=12,
        )

    ###Instance of the Database class
    def on_start(self):
        if PROD:
            self.db = Database(CONFIG)


    def build(self):
        return self.INTERFACE


####################################################
##          About login                            #
####################################################

    def loadConnection(self):
        if not self.db and PROD: 
            self.INTERFACE.ids.errorLogin.text = "Vérifier votre connexion Internet"
            return

        self.INTERFACE.ids.button_login.text = " "
        self.INTERFACE.ids.button_login.icon = " "
        self.INTERFACE.ids.loader.color = (1,1,1,1)
        self.INTERFACE.ids.loader.active = True

        Clock.schedule_once(self.login, 1)


    def initialisaion(self):
        self.INTERFACE.ids.loader.active = False
        self.INTERFACE.ids.password.text = ""
        self.INTERFACE.ids.button_login.icon = "arrow-right"
        self.INTERFACE.ids.button_login.text = "S'identifier"


    def login(self, event):
        username = self.INTERFACE.ids.username.text
        password = self.INTERFACE.ids.password.text
        if not PROD or self.db.login(username,password):
            self.INTERFACE.current = "Main"
            self.INTERFACE.ids.username.text = ""
            self.INTERFACE.ids.errorLogin.text
            self.initialisaion()

            return
        self.initialisaion()
        self.INTERFACE.ids.errorLogin.text = "Le mot de passe est incorrect !"

####################################################
##             Logout || Quit the app              #
####################################################

    def logout(self, menu, item):
        if item.text == "Déconnexion":
            _SESSION = None
            self.INTERFACE.current = "Login"
            self.menu.dismiss()
        if item.text == "Quit":
            self.show_quit_dialog()
        
    def show_quit_dialog(self):
        if not self.quit_dialog:
            self.quit_dialog = MDDialog(
                text="Etes vous sur de quittez ?",
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color,on_press=self.close_quit_Dialog
                    ),
                    MDFlatButton(
                        text="CONFIRMER", text_color=self.theme_cls.primary_color,on_press=self.close_quit_Dialog
                    ),
                ],
            )
            self.quit_dialog.bind(on_release=self.close_quit_Dialog)
        self.quit_dialog.open()

    def close_quit_Dialog(self,btn):
        if btn.text == "ANNULER":
            self.quit_dialog.dismiss()
        else:
            self.stop()
####################################################
##                    Tour de tâche                #
####################################################
    def tour_de_tache(self,jour,tache,slide):
        date_tache = datetime.date.today()
        if jour == "hier":
            if slide == 1 : date_tache = datetime.date.today() - timedelta(1)
            elif slide == 2 : date_tache = datetime.date.today() + timedelta(2)
        elif jour == "aujourdhui":
            if slide == 1 : date_tache = datetime.date.today()
            elif slide == 2 : 
                date_tache = datetime.date.today() + timedelta(3)
        elif jour == "demain": 
            if slide == 1 : date_tache = datetime.date.today() + timedelta(1)
            elif slide == 2 : date_tache = datetime.date.today() + timedelta(4)

        date_tache = date_tache.strftime("%Y-%m-%d")
        return self.db.tour_tache(date_tache,tache)

    def jour_de_tache(self,jour,slide):
        date_tache = datetime.date.today()
        if jour == "hier": 
            if slide == 1 : date_tache = datetime.date.today() - timedelta(1)
            elif slide == 2 : date_tache = datetime.date.today() + timedelta(2)
        elif jour == "aujourdhui": 
            if slide == 1 : date_tache = datetime.date.today()
            elif slide == 2 : date_tache = datetime.date.today() + timedelta(3)
        elif jour == "demain": 
            if slide == 1 : date_tache = datetime.date.today() + timedelta(1)
            elif slide == 2 : date_tache = datetime.date.today() + timedelta(4)

        return date_tache.strftime("%d-%m-%y")


####################################################
##             Tableau in the cook menu            #
####################################################

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
                    "Oeuf sauce",
                    "Kitoza",
                    "Voanjobory",
                    "Soupe Légume",
                    "Poulet frite",
                    "Tsaramaso",
                    "Brède",
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


####################################################
##           Tableau de status de cotisation       #
####################################################

    def __tableau_status(self):
        tab = MDDataTable(
            size_hint=(0.815, 0.45),
            column_data=[
                ("Membres", dp(50)),
                ("Cotisations", dp(50)),
                ("Status", dp(50)),
            ],
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                (
                    "Landry",
                    "Bazar",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "En attente"),
                ),
                (
                    "Gaetan",
                    "Tee-shirt",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "En attente"),
                ),
                (
                    "Haja",
                    "Tee-shirt",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Payé",
                    ),
                ),
                (
                    "Fabien",
                    "Bazar",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "En attente"),
                ),
                (
                    "Casmir",
                    "Tee-shirt",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Payé",
                    ),
                ),
            ],
        )
        self.INTERFACE.ids.tableau_status_cotisation.add_widget(tab)



####################################################
##           Tableau de status de cotisation       #
####################################################

    def __tableau_status_facture(self):
        tab = MDDataTable(
            size_hint=(0.815, 0.45),
            column_data=[
                ("Membres", dp(50)),
                ("Factures", dp(50)),
                ("Status", dp(50)),
            ],
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                (
                    "Landry",
                    "Septembre",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "En attente"),
                ),
                (
                    "Gaetan",
                    "Février",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "En attente"),
                ),
                (
                    "Haja",
                    "Novembre",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Payé",
                    ),
                ),
                (
                    "Fabien",
                    "Janvier",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "En attente"),
                ),
                (
                    "Casmir",
                    "Décembre",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Payé",
                    ),
                ),
            ],
        )
        self.INTERFACE.ids.tableau_status_facture.add_widget(tab)


####################################################
##           Tableau de transaction                #
####################################################

    def __tableau_transaction(self,transact):
        self.tab = MDDataTable(
            size_hint=(0.813, 0.45),
            column_data=[
                ("Dates de transaction", dp(35)),
                ("Dates d'insertion", dp(30)),
                ("Membres", dp(25)),
                ("Montants", dp(25)),
                ("Raisons", dp(40)),
            ],
            row_data=transact,
        )
        self.INTERFACE.ids.tableau_transaction.clear_widgets()
        self.INTERFACE.ids.tableau_transaction.add_widget(self.tab)


####################################################
##               Grand  Menage                     #
####################################################

###Reinitialiser les tâches
    def show_init_dialog(self,num):
        self.num = num
        self.dialog = None

        if not self.dialog:
            self.dialog = MDDialog(
                title="Réinitialisation ?",
                text="Voulez-vous vraiment réinitialiser cette tâche ?",
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color, on_press=self.close_init_Dialog
                    ),
                    MDFlatButton(
                        text="VALIDER", text_color=self.theme_cls.primary_color, on_press=self.close_init_Dialog
                    ),
                ],
            )
        self.dialog.open()
    
    def close_init_Dialog(self,btn):
        if btn.text == "ANNULER":
            self.dialog.dismiss()
        if btn.text == "VALIDER":
            self.INTERFACE.ids[f'raisedBtn{self.num}'].text = ""
            self.dialog.dismiss()

###Modifier les tâches
    def show_edit_dialog(self,num):
        self.num = num
        self.dialog = None

        if not self.dialog:
            cls = BoxLayout(
                orientation= "vertical",
                spacing= "12dp",
                size_hint_y= None,
                height= "120dp"
            )
            cls.add_widget(
                MDLabel(
                    text = self.INTERFACE.ids[f'raisedBtn{self.num-1}'].text
                )
            )

            self.personne = MDTextField(
                text = self.INTERFACE.ids[f'raisedBtn{self.num}'].text,
                
            )

            self.dialog = MDDialog(
                title="Grand Menage:",
                type="custom",
                content_cls = cls,
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color, on_press=self.close_edit_Dialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_press=self.close_edit_Dialog
                    ),
                ],
            )
            cls.add_widget(self.personne)

        self.dialog.open()


    def close_edit_Dialog(self,btn):
        if btn.text == "ANNULER":
            self.dialog.dismiss()
        if btn.text == "OK":
            self.INTERFACE.ids[f'raisedBtn{self.num}'].text = self.personne.text
            self.dialog.dismiss()

####################################################
##               Cotisation                        #
####################################################

###Add cotisation
    def add_cotis_dialog(self):
        self.dialog = None

        if not self.dialog:
            cls = BoxLayout(
                orientation= "vertical",
                spacing= "12dp",
                size_hint_y= None,
                height= "210dp"
            )

            ###Reason of the cotisation
            cls.add_widget(
                MDLabel(
                    text = "Motifs"
                )
            )
            self.motifs_cotis = MDTextField()
            cls.add_widget(self.motifs_cotis)

            ###Amount of the cotisation
            cls.add_widget(
                MDLabel(
                    text = "Montant"
                )
            )
            self.argent_cotis = MDTextField()
            cls.add_widget(self.argent_cotis)

            ###The date of the transaction
            cls.add_widget(
                MDLabel(
                    text = "Date"
                )
            )
            self.date_cotis = MDTextField(on_release= self.show_date_picker)
            cls.add_widget(self.date_cotis)

            self.dialog = MDDialog(
                title="Ajouter cotisation:",
                type="custom",
                content_cls = cls,
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color, on_press=self.close_cotis_Dialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_press=self.close_cotis_Dialog
                    ),
                ],
            )

        self.dialog.open()
        self.date_cotis.bind(
            focus= lambda *args: self.show_date_picker()
        )
    def close_cotis_Dialog(self,btn):
        if btn.text == "OK":
            new_card = MDCard(
                orientation = "vertical",
                padding = "15dp",
                size_hint = (None, None),
                size = ("180dp", "220dp"),
                pos_hint = {"center_x": 0.80, "center_y": 0.31}
            )

            new_card.add_widget(
                MDFloatingActionButton(
                    icon = "alert",
                    user_font_size = "14sp",
                    theme_text_color = "Custom",
                    text_color = get_color_from_hex("#ffffff"),
                    md_bg_color = get_color_from_hex("#faaf00"),
                    elevation_normal = 0
                )
            )
            new_card.add_widget(
                MDLabel(
                    text = self.motifs_cotis.text,
                    pos_hint = {"x":0.30, "y":0.75},
                    font_size = '18sp'
                )
            )
            new_card.add_widget(
                MDRoundFlatIconButton(
                    icon = "currency-eur",
                    text = self.argent_cotis.text,
                    pos_hint = {"center_x":0.5, "center_y":0.5},
                    font_size = '17sp',
                    margin = "30dp"
                )
            )
            new_card.add_widget(
                MDIconButton(
                    icon=  "trash-can",
                    theme_text_color = "Custom",
                    font_size = "18sp",
                    text_color = get_color_from_hex("#071f38"),
                    pos_hint= {"center_x":0.5, "center_y":0.3}
                )
            )
            self.INTERFACE.ids.Cotisation.add_widget(new_card)
        self.dialog.dismiss()

###Payer cotisation
    def paye_cotisation(self):
        self.dialog = None

        if not self.dialog:
            cls = BoxLayout(
                orientation= "vertical",
                spacing= "12dp",
                size_hint_y= None,
                height= "300dp"
            )

            ###Reason of the payement
            cls.add_widget(
                MDLabel(
                    text = "Motifs"
                )
            )
            self.motifs_paye = MDTextField()
            cls.add_widget(self.motifs_paye)

            ###Who did the payement
            cls.add_widget(
                MDLabel(
                    text = "Prenom"
                )
            )
            self.who_paye = MDTextField()
            cls.add_widget(self.who_paye)

            ###Amount of the payement
            cls.add_widget(
                MDLabel(
                    text = "Montant"
                )
            )
            self.argent_paye = MDTextField()
            cls.add_widget(self.argent_paye)

            ###The date of the transaction
            cls.add_widget(
                MDLabel(
                    text = "Date de payement"
                )
            )
            self.date_paye = MDTextField()
            cls.add_widget(self.date_paye)

            self.dialog = MDDialog(
                title="Payement de cotisation:",
                type="custom",
                content_cls = cls,
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color, on_press=self.close_paye_Dialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_press=self.close_paye_Dialog
                    ),
                ],
            )

        self.dialog.open()

    def close_paye_Dialog(self,btn):
        if btn.text == "OK":
            self.transact.append((
                self.date_paye.text,
                datetime.date.today().strftime("%d-%m-%Y"),
                self.who_paye.text,
                self.argent_paye.text,
                self.motifs_paye.text
            ))

            self.__tableau_transaction(self.transact)

        self.dialog.dismiss()

###Show DatePicker
    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>

        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

GFS().run()