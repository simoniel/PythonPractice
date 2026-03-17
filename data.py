import pandas as pd
import matplotlib.pyplot as plt


def practice_series():
    a = [1, 7, 2]
    s1 = pd.Series(a, index = ["x", "y", "z"])
    print(s1)

    calories = {"day1": 420, "day2": 380, "day3": 390}
    s2 = pd.Series(calories)
    print(s2)

def practice_df():
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    ##option 1
    #labels = []
    #for i in range(len(data["calories"])):
    #    labels.append(f'day{i+1}')
    #d1 = pd.DataFrame(data, index = labels)
    #print(d1)
    
    ##option 2
    d1 = pd.DataFrame(data)
    d1.index = [f"day{i+1}" for i in range(len(d1))]
    print(d1)
    print(d1.loc['day1'])
    print(d1.loc[['day1','day2']])

def convert_csv_to_json():
    df = pd.read_csv('boardgames_ranks.csv')
    #df.to_json('file.json', orient='records', lines=True) #machine-friendly
    df.to_json('boardgames_ranks_conv.json', orient='records', indent=4)


def practice_csv():

    df = pd.read_csv('boardgames_ranks.csv')

    print(df.head(10))
    print(df.info())  

    #clean data
    # 1. replace null with 0
    df.fillna(0, inplace = True)  

    print(df.head(10))
    print(df.info())  

    print(df.shape)

    #df.plot()
    #plt.show() 


if __name__ == '__main__':
    #practice_series()
    #practice_df()
    #convert_csv_to_json()
    practice_csv()
