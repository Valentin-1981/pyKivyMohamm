from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''
<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Hello world!!!'
    Button:
        text: 'Click me!!!'
        on_press: root.dismiss()
''')

class CustomPopup(Popup):
    pass

class TestApp(App):
    def build(self):
        b = Button(on_press=self.show_Popup)
        return b
    def show_Popup(self, b):
        p = CustomPopup()
        p.open()

TestApp().run()