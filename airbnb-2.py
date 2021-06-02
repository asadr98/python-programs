"""
This script allows us to parse data and produce box plots.
Driver: Sana Hassan
Navigator: Asad Raheem
Assignment: Exercise 9
Date: 4-14-2021 
"""
import seaborn
import pandas
import matplotlib.pyplot as plt

ab_nyc_2019_filename = 'AB_NYC_2019.csv'

ab_nyc_2019 = pandas.read_csv(ab_nyc_2019_filename)

#requirement 1
less_than_400 = ab_nyc_2019['price']< 400
data_lt_400 = ab_nyc_2019[less_than_400]
plot = seaborn.boxplot(data = data_lt_400,
                       x = 'neighbourhood_group', 
                       y= 'price',
                       hue = 'room_type')
plot.get_figure().savefig('boxplot1.png')

#requirement 2
top2 = ab_nyc_2019['host_id'].value_counts()[:2].index.tolist()
top = top2[1]
penultimate = top2[0]

top_rows = ab_nyc_2019['host_id'] == top
top_data = ab_nyc_2019[top_rows]

top_plot = seaborn.boxplot(data = top_data,
                           x = 'minimum_nights',
                           y = "price",
                           hue = 'room_type')
top_plot.get_figure().savefig('boxplot2.png')
plt.clf()

penultimate_rows = ab_nyc_2019['host_id']==penultimate
penultimate_data = ab_nyc_2019[penultimate_rows]

penultimate_plot = seaborn.boxplot(data = penultimate_data,
                                   x= 'minimum_nights',
                                   y = 'price',
                                   hue = 'room_type')
penultimate_plot.get_figure().savefig('boxplot3.png')        
plt.clf()     

print(top_data['host_name'])
print(penultimate_data['host_name'])
