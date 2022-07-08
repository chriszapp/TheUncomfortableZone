from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):  #define the class 
    def build(self):  #define the function/method
    
        self.window = GridLayout()  #define the parameter window
        self.window.cols=1          #i only want one column in my gridlayout
        self.window.add_widget(Image(source="penguin.png"))
        self.greeting=Label(text="Thank you for your visiti! What is your name?")

if __name__ == "__main__":
    SayHello().run()
