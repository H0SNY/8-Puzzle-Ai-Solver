
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from main import breadthFirst , depthFirst  , checkInversion





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
	    self.breadth = Button(text = "Breadth First")
	    self.breadth.bind(on_press = self.breadthPress)
	    self.depth = Button(text = "Depth First")
	    self.depth.bind(on_press = self.depthPress)
	    self.a = Button(text = "A*")
	    self.a.bind(on_press = self.aPress)
	    self.clear = Button(text = "clear")
	    self.clear.bind(on_press = self.clearPress)
	    self.add_widget(self.breadth)
	    self.add_widget(self.depth)
	    self.add_widget(self.a)
	    self.add_widget(self.clear)
	    self.initialState = []
	    self.answer = BoxLayout(orientation = "vertical")
	    self.state = Label()
	    self.explored = Label()
	    self.visited = Label()
	    self.answer.add_widget(self.state)
	    self.answer.add_widget(self.explored)
	    self.answer.add_widget(self.visited)
	    self.add_widget(self.answer)


	def breadthPress(self , instance):
		self.initialState = []
		for i in range(9):
			self.initialState.append(int(self.inputs[i].text))

		count = checkInversion(self.initialState)
		self.answer.text = str(count)
		if not count % 2 == 0:
			self.state.text =  "odd inversions : " + str(count) 
			
		else :
			finalState = breadthFirst(self.initialState)
			ans = finalState[0]
			explored = finalState[1]
			visited = finalState[2]
			answerString = ''
			for i in range(len(ans)):
				answerString = answerString + str(ans[i])
			self.state.text = "Final State : " + answerString
			self.explored.text = "Explored Nodes : " + str(explored)
			self.visited.text =  "Visited Nodes : " + str(visited) 
	def depthPress(self , instance):
		self.initialState = []
		for i in range(9):
			self.initialState.append(int(self.inputs[i].text))

		count = checkInversion(self.initialState)
		self.answer.text = str(count)
		if not count % 2 == 0:
			self.answer.text =  "odd inversions : " + str(count) 
			
		else :
			finalState = depthFirst(self.initialState)
			ans = finalState[0]
			explored = finalState[1]
			visited = finalState[2]
			answerString = ''
			for i in range(len(ans)):
				answerString = answerString + str(ans[i])
			self.state.text = "Final State : " + answerString
			self.explored.text = "Explored Nodes : " + str(explored)
			self.visited.text =  "Visited Nodes : " + str(visited) 
	def aPress(self , instance):
		self.initialState = []
		for i in range(9):
			self.initialState.append(int(self.inputs[i].text))

		count = checkInversion(self.initialState)
		self.answer.text = str(count)
		if not count % 2 == 0:
			self.answer.text =  "odd inversions : " + str(count) 
			
		else :
			finalState = breadthFirst(self.initialState)
			ans = finalState[0]
			explored = finalState[1]
			visited = finalState[2]
			answerString = ''
			for i in range(len(ans)):
				answerString = answerString + str(ans[i])
			self.state.text = "Final State : " + answerString
			self.explored.text = "Explored Nodes : " + str(explored)
			self.visited.text =  "Visited Nodes : " + str(visited) 
	def clearPress(self , instance):
		for i in range(len(self.inputs)):
			self.inputs[i].text = ''
		  	
	


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