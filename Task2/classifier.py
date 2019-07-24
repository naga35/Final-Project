import numpy as np
import pandas as pd
import matplotlib as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
header = ['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustDir','WindGustSpeed',
          'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
          'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm',
          'RainToday', 'RISK_MM', 'RainTomorrow']
def get_score(file_path):
    df=pd.read_csv(file_path, names=header)
    data=df.drop(['Evaporation','Sunshine'], axis=1)
    le=LabelEncoder()
    data['WindDir3pm']=le.fit_transform(data['WindDir3pm'].fillna('0'))
    data['RainToday']=le.fit_transform(data['RainToday'].fillna('0'))
    data['RainTomorrow']=le.fit_transform(data['RainTomorrow'].fillna('0'))
    data['Location']=le.fit_transform(data['Location'].fillna('0'))
    data['WindGustDir']=le.fit_transform(data['WindGustDir'].fillna('0'))
    data['WindDir9am']=le.fit_transform(data['WindDir9am'].fillna('0'))
    X=data.iloc[:,1:22].values
    X = np.nan_to_num(X)
    Y=data['RainTomorrow'].values
    Y = np.nan_to_num(Y)
    X_train,X_test,y_train,y_test=train_test_split(X,Y)
    classifier=LogisticRegression(solver='lbfgs')
    classifier.fit(X_train,y_train)
    result = classifier.score(X_test,y_test)
    return result
def format_results(results):
    f = open('output\\result.txt', 'w')
    for country in results:
        output_format = "[" + country + "] : [" +  str(results[country]) + "]\n"
        f.write(output_format)
    avg = sum(results.values())/len(results)
    f.write("average_accuracy: [" + str(avg) + "]")
    f.close()
if __name__ == "__main__":
    path = "data"
    files = os.listdir(path)
    d = {}
    for file_ in files:
        file_path = os.path.join(path, file_)
        country = file_.split("_")[-1][:-4]
        d[country] = get_score(file_path)
        print("Accuracy of {} is {}".format(country, d[country]))
    format_results(d)
