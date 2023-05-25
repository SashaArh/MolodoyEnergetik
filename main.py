from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MolodoyEnergetikApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, MolodoyEnergetik", halign="center")


MolodoyEnergetikApp().run()