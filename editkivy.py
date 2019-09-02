

import predictseat as pred
class PredictionScreen(Screen):
    
    def predict(self):
        # More detailed explanations of each functions can be found in the module: predictseat.py
        
        time_list,seat_list,day_list = pred.read_data('Seats_occupancies.csv')       #retrieving data from database
        data = pred.compile_to_week(time_list,seat_list,day_list)                    #Compiling data
        x = pred.seats_prediction(self.ids.Day.text,self.ids.Time.text,data) 
        print("PREDICTED")
        self.lbl_w.text='{} seat(s) are likely to be occupied'.format(round(x))

kv=Builder.load_string('''
ScreenManager:
    id: screen_manager
    #transition: 
    MainScreen:
        id: main_screen
        name: 'Check/Predict'
        manager: 'screen_manager'
    Lvl2Screen:
        id: lvl2screen
        name: 'Level 2 Study Room'
        manager: 'screen_manager'
    Lvl4Screen:
        id: lvl4screen
        name: 'Level 4 Study Room'
        manager: 'screen_manager'
    Lvl6Screen:
        id: lvl6screen
        name: 'Level 6 Study Room'
        manager: 'screen_manager'
    Lvl9Screen:
        id: lvl9screen
        name: 'Level 9 Study Room'
        manager: 'screen_manager'
    Lvl10Screen:
        id: lvl10screen
        name: 'Level 2 Study Room'
        manager: 'screen_manager'
    Lvl11Screen:
        id: lvl11screen
        name: 'Level 11 Study Room'
        manager: 'screen_manager'
    PredictionScreen:
        id: predict_screen
        name: 'Prediction Screen'
        manager: 'screen_manager'
    CurrentScreen:
        id: check_current_screen
        name: 'Current Screen'
        manager: 'screen_manager'
    RoomSelectionScreen:
        id: room_selection_screen
        name: 'Room Selection'
        manager: 'screen_manager'
    PREDICTEDScreen:
        id: predicted_lvl6
        name: 'PREDICTED Screen'
        manager: 'screen_manager'
    Level6Details:
        id: lvl6details
        name: 'Level 6 details'
        manager: 'screen_manager'
        
<MainScreen>:
    BoxLayout:
        orientation: 'horizontal'
        Button:
            id: makeprediction
            text: 'Make A Prediction!'
            font_size: 20
            on_press: app.root.current= 'Room Selection'
            
        Button:
            id: checkcurrent
            text: 'Check Current Vacancy!'
            font_size: 20
            on_press: app.root.current= 'Current Screen'

<CurrentScreen>:
    GridLayout:
        rows:2
        cols:3
        Button:
            id: btn1
            text: 'Study Room lvl2'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn2
            text: 'Study Room lvl4'
            font_size: 20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn3
            text: 'Study Room lvl6'
            font_size:20
            color: (1,0,1,1)
            on_press: app.root.current= 'Level 6 Study Room'
        Button:
            id: btn4
            text: 'Study Room lvl9'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn5
            text: 'Study Room lvl10'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn6
            text: 'Study Room lvl11'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
            
    FloatLayout:
        Button:
            size_hint_x: None
            size_hint_y: None
            height: 40 
            text: 'Back'
            font_size: 20
            on_press: app.root.current= 'Check/Predict'
            
<RoomSelectionScreen>:
    GridLayout:
        rows:2
        cols:3
        Button:
            id: btn1
            text: 'Study Room lvl2'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn2
            text: 'Study Room lvl4'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn3
            text: 'Study Room lvl6'
            font_size:20
            color: (1,0,1,1)
            on_press: app.root.current= 'Prediction Screen'
        Button:
            id: btn4
            text: 'Study Room lvl8'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn5
            text: 'Study Room lvl10'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
        Button:
            id: btn6
            text: 'Study Room lvl11'
            font_size:20
            color: (1,0,1,1)
            on_press: pass
    FloatLayout:
        Button:
            size_hint_x: None
            size_hint_y: None
            height: 40 
            text: 'Back'
            font_size: 20
            on_press: app.root.current= 'Check/Predict'

<PredictionScreen>:
    lbl_w: lbl
    BoxLayout:
        orientation: 'vertical'
        GridLayout:
            rows:2
            cols:2
            
            Label:
                text: 'Which Day of the Week?'
                font_size:20
                color: 1,1,1,1
                canvas.before:
                    Color:
                        rgba: 0,0.52,0.52,1
                    Rectangle: 
                        pos: self.pos
                        size:self.size
            Label:
                text: 'Time? (in Hr)'
                font_size:20
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0.67,0.9,0,1
                    Rectangle: 
                        pos: self.pos
                        size:self.size
                        
            BoxLayout:
                Button:
                    id: Day
                    text: 'Pick a Day'
                    font_size:20
                    background_normal: ''
                    background_color: 0,0.52,0.52,1                    
                    on_release: days_dropdown.open(self)
                       
                DropDown:
                    id: days_dropdown
                    on_select: Day.text = '{}'.format(args[1])
                    Button:
                        text: 'Monday'
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0,0.52,0.52,1                    
                        on_release: days_dropdown.select(self.text)
                    Button:
                        text: 'Tuesday'
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0,0.52,0.52,1                    
                        on_release: days_dropdown.select(self.text)
                    Button:
                        text: 'Wednesday'
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0,0.52,0.52,1                    
                        on_release: days_dropdown.select(self.text)
                    Button:
                        text: 'Thursday'
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0,0.52,0.52,1                    
                        on_release: days_dropdown.select(self.text)
                    Button:
                        text: 'Friday'
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0,0.52,0.52,1                    
                        on_release: days_dropdown.select(self.text)
                    
            BoxLayout:
                Button:
                    id:Time
                    text: 'Pick A Time'
                    color: 0,0,0,1
                    font_size:20
                    background_normal: ''
                    background_color: 0.67,0.9,0,1                    
                    on_release: time_dropdown.open(self)
                DropDown:
                    id: time_dropdown
                    on_select: Time.text = '{}'.format(args[1])
                    Button:
                        text: '0'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '1'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '2'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '3'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '4'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '5'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '6'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '7'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '8'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '9'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                        
                    Button:
                        text: '10'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '11'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '12'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '13'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '14'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '15'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '16'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '17'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '18'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '19'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '20'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '21'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '22'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
                    Button:
                        text: '23'
                        color: 0,0,0,1
                        font_size:20
                        size_hint_y: None
                        height: 44
                        background_normal: ''
                        background_color: 0.67,0.9,0,1                    
                        on_release: time_dropdown.select(self.text)
        Button:
            text: 'Predict'
            font_size:20
            on_press: root.predict()
        
        Label:
            id: lbl
            text: '0'
            font_size:20

            
        

    FloatLayout:
        Button:
            size_hint_x: None
            size_hint_y: None
            height: 40 
            text: 'Back'
            font_size: 20
            on_press: app.root.current= 'Room Selection'

