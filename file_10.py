from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    # size_hint: .5, .5
    TextInput:        
        size_hint: None, None
        size: 600, 200
        text: "MAHMOUD RAOUF\\nMAHMOUD RAOUF\\nMAHMOUD RAOUF\\n"
        font_size: 50
        focus: True
        on_scroll_y: print(self.focus)
"""

class TextInput(App):
    def build(self):
        from kivy.config import Config
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '800')
        return Builder.load_string(kv)

if __name__ == "__main__":
    TextInput().run()