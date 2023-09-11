import flet
from flet import *
from appmenu import jumbotron
from cardsection import sectioncard
from tabsmenu import tabs_menu
from navigationbar import navigationbar
def main(page:Page):
    page.title = "KFC"
    page.padding=0
    page.spacing=0

    page.add(
        # Appbar
        jumbotron,
        # cardsection
        sectioncard,
        # tabs
        tabs_menu,
        # navigationbar
        navigationbar,
         


    )

flet.app(target=main, assets_dir="assets")