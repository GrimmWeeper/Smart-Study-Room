import predictseat as pred
import datetime

# More detailed explanations of each functions can be found in the module: predictseat.py

time_list,seat_list,day_list = pred.read_data('Seats_occupancies.csv')       #retrieving data from database
data = pred.compile_to_week(time_list,seat_list,day_list)                    #Compiling data
x = pred.seats_prediction('Wednesday','3',data)                              #Predicting seats
print(x)


'''At every 1 hour interval, when the current minute is 0, it will update the current day of the 
week, current hour and number of seats occupied at that instance into the existing database
'''
while True:
    currentDT = datetime.datetime.now()
    day = datetime.datetime.today().strftime('%A')
    if currentDT.minute != 10:
        count = 0
    if currentDT.minute == 10 and count == 0:
        pred.write_data(str(currentDT.hour),'4',day,'Seats_occupancies.csv')
        count += 1

