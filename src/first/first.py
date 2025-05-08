import kivy
from kivy.uix.label import Label
from kivy.app import App


class Fapp(App):
    def build(self):
        return Label(text="Whoa !!!")


if __name__ == "__main__":
    Fapp().run()
