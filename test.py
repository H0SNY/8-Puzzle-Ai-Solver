
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from main import breadthFirst , goalStates , checkInversion
import random
import numpy as np


goalState = [[ 0 , 1 , 2 ], [3 , 4 ,5] , [6 , 7 , 8]]	
initState = goalState.copy()
imgs = [[] , [] , []]



class MainLayout(BoxLayout):
	def __init__(self , **kwargs):
	    super().__init__(**kwargs)

class MainApp(BoxLayout):
	def __init__(self , **kwargs):
	    super().__init__(**kwargs)

class Board(GridLayout):
	def __init__(self , **kwargs):
	    super().__init__(**kwargs)
	    self.cols = 3
	    self.inputs = []
	    for i in range(9):
		    self.inputs.append(TextInput(multiline = False , size = [.1 , .1]))
		    self.add_widget(self.inputs[i])
	    self.submit = Button(text = "submit")
	    self.submit.bind(on_press = self.press)
	    self.add_widget(self.submit)
	    self.initialState = []
	    self.answer = Label()

	def press(self , instance):
		self.initialState = []
		for i in range(9):
			self.initialState.append(int(self.inputs[i].text))

		print("initial state : " , self.initialState , "initialState === goalState" , initState in goalStates)
		count = checkInversion(self.initialState)
		if not count % 2 == 0:
			self.answer.text =  str("odd inversions : " + count)
			
		else :
			answer = breadthFirst(self.initialState)
			answerString = ''
			for i in range(len(answer)):
				answerString = answerString + str(answer[i]) + " "
			self.answer.text = answerString
		
		self.add_widget(self.answer)
		    	
	


class Navbar(BoxLayout):
	def __init__(self , **kwargs):
	    super().__init__(**kwargs)
	def on_click(self) :
		print("Button Clicked")


 
class PuzzleApp(App):
	def build(self):
		Window.clearcolor = (.25 , .25, .25 , 1)
		return MainLayout()




PuzzleApp().run()