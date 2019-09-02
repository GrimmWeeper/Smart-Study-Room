import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split


def write_data(time,seat,day,file_name):
    '''
    This function takes in the time(in hours), seats occupancies and the day of the week in strings format
    and update to the existing .csv database at every hourly interval.
    '''    
    with open(file_name,'a') as f:
        df = pd.DataFrame(np.array([[time,seat,day]]))
        df.to_csv(f,mode = 'a', index=False,header=False)
        print("Updated the record: '{}, {}:00h, {} seats occupied' onto the database".format(day,time,seat))



def read_data(file_name):
    '''
    This function reads the .csv file and convert into a list format. The list format is then sorted according
    to the day of the week. After sorting, the function will split the list into a list of time;seat;day and 
    return them accordingly.
    ''' 
    data = pd.read_csv(file_name)
    data_array = np.array(data).tolist()
    mon_list = []
    tues_list = []
    wed_list = []
    thurs_list = []
    fri_list = []
    for i in range(len(data_array)):
        if data_array[i][2] == 'Monday':
            mon_list.append(data_array[i])
        elif data_array[i][2] == 'Tuesday':
            tues_list.append(data_array[i])
        elif data_array[i][2] == 'Wednesday':
            wed_list.append(data_array[i])
        elif data_array[i][2] == 'Thursday':
            thurs_list.append(data_array[i])
        elif data_array[i][2] == 'Friday':
            fri_list.append(data_array[i])   
    week_list = mon_list + tues_list + wed_list + thurs_list + fri_list    
    time = []
    seat = []
    day = []
    for i in range(len(week_list)):
        time.append(week_list[i][0])
        seat.append(week_list[i][1])
        day.append(week_list[i][2])
    return time,seat,day


def compile_to_week(time,seat,day):
    '''
    This function takes in the list of time;seat;day and group them according to the day of the week
    eg. Monday: compiled[0], Tuesday: compiled[1], ... etc.
    ''' 
    compiled = []
    for i in range(len(day)):
        if day[i] != day[i-1]:
            compiled.append([])
            compiled[-1].append([])
            compiled[-1].append([])
        compiled[-1][0].append(time[i])
        compiled[-1][1].append(seat[i])          #Mon: compiled[0], Tues: compiled[1], Wed: compiled[2], Thurs: compiled[3], Fri: compiled[4]
    return compiled

def plot_graphs(compiled):
    '''
    This function takes in the compiled data and plot the graphs of seats occupied against
    time (24h format) for each day of the week.
    ''' 
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    for i in range(len(compiled)):
        seats = compiled[i][0]
        time = compiled[i][1]
        plt.scatter(seats,time)
        plt.xlabel('Time/(24h)')
        plt.ylabel('Seats Occupied')
        plt.title("{}".format(week[i]))
        plt.show()


def best_kvalue(x_data, y_data, size, seed):
    '''
    This function will split the data into train and test sets, run k-NN classifier for N number of times and return the k value that gives
    the highest correct predictions rate
    ''' 
    
    xx_data = np.reshape(x_data, (-1,1))
    yy_data = np.reshape(y_data, (-1,1))    
    
    x_train, x_test, y_train, y_test = train_test_split(xx_data, yy_data, test_size = size, random_state=seed)
    
    acc = []
    for k in range(2,len(x_train)):
        clf = neighbors.KNeighborsClassifier(n_neighbors=k)
        clf.fit(x_train,np.ravel(y_train))
        y_predicted = clf.predict(x_test)
        count = 0
        
        for i in range(len(y_predicted)):
            if y_predicted[i] == y_test[i][0]:
                count += 1
        acc.append(count)

    
    max_acc = max(acc)
    value = acc.index(max_acc) + 2
    return value



def knn_classifier(train_data, feature_data,to_predict,k):
    '''
    This function will take in the time, in string. It will then run the k-NN classifier with the 
    best k-value obtained and predict the amount of seats occupied.
    ''' 
    train_list = np.reshape(train_data, (-1,1))
    feature_list = np.reshape(feature_data, (-1,1))

    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(train_list, np.ravel(feature_list))
    target_predicted = clf.predict([[to_predict]])
    
    return target_predicted


def weighted_average(main,sub1,sub2,sub3,sub4):
    '''
    This function takes in the amount of seats occupied at the enquired time for each day and return
    the weighted average of seats occupied in integer. The actual day has a weightage of 80% while
    the other days' weightage add up to 20%.
    ''' 
    final_val = (main*0.8)+((sub1+sub2+sub3+sub4)*0.05)
    return round(final_val)

def seats_prediction(day,time,data):
    '''
    This function runs the above functions and return the predicted seats' occupancies for the
    enquired time and day.
    ''' 
    week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4}
    key_val = week[day]
    bestmain_kvalue = best_kvalue(data[key_val][0],data[key_val][1],0.2,2727)
    main_val = knn_classifier(data[key_val][0],data[key_val][1],int(time),bestmain_kvalue)[0]
    sub_val_list = []
    for i in range(5):
        if i != key_val:
            bestsub_kvalue = best_kvalue(data[i][0],data[i][1],0.2,2727)
            sub_val_list.append(knn_classifier(data[i][0],data[i][1],int(time),bestsub_kvalue)[0])
    weighted_val = weighted_average(main_val,sub_val_list[0],sub_val_list[1],sub_val_list[2],sub_val_list[3])
    return weighted_val



