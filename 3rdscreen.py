from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class SeatsDetailsApp(App):
    def build(self):
        self.root = root = GridLayout (rows = 3,cols = 2)
        self.lbl11 = Label(text='Chair A:')
        self.lbl12 = Label(text='Unoccupied for 0h:0m:20s, person could be taking a short break.',color = (1,1,0,1))
        self.lbl21 = Label(text='Chair B:')
        self.lbl22 = Label(text='Occupied for 1h:0m:14s',color = (1,0,0,1))
        self.lbl31 = Label(text='Chair C:')
        self.lbl32 = Label(text='Unoccupied for 2h:21m:10s',color = (0,1,0,1))
        root.add_widget(self.lbl11)
        root.add_widget(self.lbl12)
        root.add_widget(self.lbl21)
        root.add_widget(self.lbl22)
        root.add_widget(self.lbl31)
        root.add_widget(self.lbl32)
        return root
    
if __name__ == "__main__":
    SeatsDetailsApp().run()