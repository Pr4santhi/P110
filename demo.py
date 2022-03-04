import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data=df["temp"].tolist()

#Mean and standard deviation for the whole file
#store the mean value of the data
# population_mean=statistics.mean(data)

std=statistics.stdev(data)
# print("population mean=",population_mean)
print(std)

# fig=ff.create_distplot([data],["temp"],show_hist=False)
# fig.show()

#Mean and standard deviation of 100 random points in the csv file(sample data)
# dataset=[]
# for i in range (0,100):
#     random_index=random.randint(0,len(data))
#     value=data[random_index]
#     dataset.append(value)

# mean=statistics.mean(dataset)
# std=statistics.stdev(dataset)
# print(mean)
# print(std)

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print("mean of sampling distribution=",mean)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()