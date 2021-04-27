import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',float_precision = 'legacy')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (12,8))
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    df_add = pd.concat([pd.DataFrame([i], columns=['Year']) for i in range(2014,2050,1)],ignore_index=True)
    df_future = df.append(df_add)
    
    res_1 = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    bestfit_x1 = df_future['Year'].tolist()
    bestfit_y1 = []

    for i in bestfit_x1:
      bestfit_y1.append(res_1.intercept + res_1.slope*i) 
    
    plt.plot(bestfit_x1, bestfit_y1,'r')

    # Create second line of best fit
    df_aught = df_future[df_future['Year'] >= 2000]

    res_2 = linregress(x = df[df['Year'] >= 2000]['Year'], y = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])#second res line
    
    bestfit_x2 = df_aught['Year'].tolist()
    bestfit_y2 = []
    
    for i in bestfit_x2:
      bestfit_y2.append(res_2.intercept + res_2.slope*i) 
    
    plt.plot(bestfit_x2, bestfit_y2,'b')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()