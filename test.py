from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainLayout(BoxLayout):
	def __init__(self , **kwargs):
	    super().__init__(**kwargs)
	    #adding elements prom py file
	#     b1 = Button(text="Start Game")
	#     l1 = Label(text="Start Game")
	#     self.add_widget(b1)
	#     self.add_widget(l1)

class MainWidget(Widget):
	pass
 
class PuzzleApp(App):
	pass

PuzzleApp().run()