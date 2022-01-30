import csv
from os import name, stat
import statistics
from numpy import result_type
import pandas as pd
from pandas.core.indexes.datetimes import date_range
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('StudentsPerformance.csv')
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)

first_std_dev_start ,first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start ,second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start ,third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

fig = ff.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,1],mode="lines",name="STANDRAD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,1],mode="lines",name="STANDRAD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,1],mode="lines",name="STANDRAD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,1],mode="lines",name="STANDRAD DEVIATION 2"))
fig.show()

list_of_data_points_btw_first_std_dev = [result for result in data if result> first_std_dev_start and result<first_std_dev_end]
list_of_data_points_btw_second_std_dev = [result for result in data if result> second_std_dev_start and result<second_std_dev_end]
list_of_data_points_btw_third_std_dev = [result for result in data if result> third_std_dev_start and result<third_std_dev_end]

print("Mean of data is:- {}".format(mean))
print("Median of data is:- {}".format(median))
print("Mode of data is:- {}".format(mode))
print("Standard Deviation of data is:- {}".format(std_dev))
print("{}% of datalies within first satndard deviation".format(len(list_of_data_points_btw_first_std_dev)*100/len(data)))
print("{}% of datalies within second satndard deviation".format(len(list_of_data_points_btw_second_std_dev)*100/len(data)))
print("{}% of datalies within third satndard deviation".format(len(list_of_data_points_btw_third_std_dev)*100/len(data)))