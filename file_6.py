from kivy.app import App
from kivy.base import  runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
RelativeLayout:
    padding: 10
    Button:
        text: 'R1'
        size_hint: x=.3, y=.3
        pos: 50, 100
    Button:
        text: 'R2'
        size_hint: .2, .2
        pos: 100, 0
    
'''))