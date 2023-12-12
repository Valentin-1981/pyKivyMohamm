from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    TextInput:
        size_hint: None, None
        size: 400, 30
        text: 'Select this text, then maximize the window.'
        use_bubble: True
"""

class test_1(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    test_1().run()