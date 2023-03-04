# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:25:44 2023

@author: devendra
"""

import matplotlib.pyplot as plt
'''
This module provide tools to  represent the data in different types
of plots for example pie plot, lineplot.
'''
import pandas as pd
'''
This python module consist of multiple tools useful for data handelling 
and manuplation
'''

# Reading the source file by using pandas
gas = pd.read_csv('C:/Users/shrav/OneDrive/Desktop/sai/gas_prices2.csv') 
expo = pd.read_csv('C:/Users/shrav/OneDrive/Desktop/sai/Extracted_data.csv')
fifa22 = pd.read_csv('C:/Users/shrav/OneDrive/Desktop/sai/players_22.csv', low_memory = (False)) # When reding large data sets

def lineplot(gas):
    '''
    Plots  a line graph for gas prices over the period in different countries

    Parameters
    ----------
    gas : A pandas dataframe contains gas prices of different countries(in USD) and years

    Returns
    -------
    None.

    '''
    # create a Plot
    plt.figure(figsize = (15, 8))
    
    # Set the title to Plot
    plt.title('Gas Prices Over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize':22})
    
    # way one of doing line plot   
    # Plot the data for different countreies
    plt.plot(gas.Year, gas.Australia, label='Australia', marker='o')
    plt.plot(gas.Year, gas.Germany, label='Germany', marker='o')
    plt.plot(gas.Year, gas.Canada, label='Canada', marker='o')
    plt.plot(gas.Year, gas.France, label='France', marker='o')
    plt.plot(gas.Year, gas.Mexico, label='mexico', marker='o')
    plt.plot(gas.Year, gas.SouthKorea, label='Sou_Korea', marker='o')
    plt.plot(gas.Year, gas.UK, label='UK', marker='o')
    plt.plot(gas.Year, gas.USA, label='USA', marker='o')
    
    # Set the x-axis tick marks
    plt.xticks(gas.Year[::2])
    
    # Set labels for x- axis and y- axis
    plt.xlabel('Year', fontdict={'fontweight':'bold', 'fontsize':18})
    plt.ylabel('Price in USD',fontdict={'fontweight':'bold', 'fontsize':18})
    
    
    # save the plot as png file
    plt.savefig('Line_Plot.png', dpi=600)
    # Set legend of the plot
    plt.legend()
    
    # Show the plot
    plt.show()
    
def lineplot2(expo):
    '''
    Plots the line graph of exporting gas prices for different countries over the time

    Parameters
    ----------
    expo : A pandas dataframe containing gas exporting prices through vessel of different countries 
        
    Returns
    -------
    None.

    '''
    # Create figure with size (x,y)
    fig, ax = plt.subplots(figsize=(12, 6)) 
    
    # way two of doing line plot
    # plot the data for different countries
    for country in expo.drop('Year', axis=1):
        ax.plot(expo.Year, expo[country], marker='o', label=country)
    # Plot the legend to graph    
    ax.legend()
    
    #labelling
    ax.set_xlabel('Year')
    ax.set_ylabel('Prices in USD')
    
    # title to the graph
    ax.set_title('Exporting Prices of Gas through Vessel')
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    plt.show()
    
    
# set bins for histograms        
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
def histogram(fifa22):
    '''
    Plots the four different histograms for player skills in the dataset FIFA22
    It Compares the data of different plyers and plots the vizulized data

    Parameters
    ----------
    fifa22 : A pandas dataframe containing the data of every player in FIFA22 
    sample data 
    Name, Id,  Height, Weight, Skills, Club name, etc
    Bins: int, optional
    The number of bins to use in thr histogram
    Returns
    -------
    None.

    '''
    # plots  Dribling skill histogram of different players
    plt.hist(fifa22.dribbling, bins=bins)
    
    #sets the bin values
    plt.xticks(bins)
    
    # labelling
    plt.title('Distribution of Player Skills in FIFA 2022 ', fontdict={'fontweight':'bold', 'fontsize':12})
    plt.xlabel('Dribbling skill level', fontdict={'fontweight':'bold', 'fontsize':8})
    plt.ylabel('Number Of Players',fontdict={'fontweight':'bold', 'fontsize':8})
    
    #create fig and show
    plt.figure(figsize = (9, 9))
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    
    plt.show()
    
    # Plots Movement acceleration Histogram of different players
    plt.hist(fifa22.movement_acceleration, bins=bins, color='g')
    
    # create ticks in x-axis
    plt.xticks(bins)
    
    # labelling and title
    plt.title('Distribution of Player Skills in FIFA 2022 ', fontdict={'fontweight':'bold', 'fontsize':12})
    plt.xlabel('Momentum_Acceleration', fontdict={'fontweight':'bold', 'fontsize':8})
    plt.ylabel('Number Of Players',fontdict={'fontweight':'bold', 'fontsize':8})
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    plt.figure(figsize = (8, 8))
    plt.show()

    # plots Mentality histogram of different players
    plt.hist(fifa22.mentality_aggression, bins=bins, color='r')
    
    # create ticks in x-axis
    plt.xticks(bins)
    
    #title and labelling
    plt.title('Distribution of Player Skills in FIFA 2022 ', fontdict={'fontweight':'bold', 'fontsize':12})
    plt.xlabel('Mentality Aggression', fontdict={'fontweight':'bold', 'fontsize':8})
    plt.ylabel('Number Of Players',fontdict={'fontweight':'bold', 'fontsize':8})
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    plt.figure(figsize = (8, 8))
    plt.show()
    
    # plots goalkeepin histogram of different players
    plt.hist(fifa22.goalkeeping_speed, bins=bins, color='y')
    
    # create ticks in x-axis
    plt.xticks(bins)
    
    # title and labelling
    plt.title('Distribution of Player Skills in FIFA 2022 ', fontdict={'fontweight':'bold', 'fontsize':12})
    plt.xlabel('Goalkeeping Speed', fontdict={'fontweight':'bold', 'fontsize':8})
    plt.ylabel('Number Of Players',fontdict={'fontweight':'bold', 'fontsize':8})
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    plt.figure(figsize = (8, 8))
    plt.show()
    
    return

def pieplot(fifa22):
    '''
    creates a pie chart to display the foot preference of FIFA players in 2022
    vizualize the data and reprents in a pie chart 

    Parameters
    ----------
    fifa22 : A Pandas dataframe containing the information of fifa players 2022
        
    Returns
    -------
    None.

    '''
    left = fifa22.loc[fifa22['preferred_foot'] == 'Left'].count()[0]
    right = fifa22.loc[fifa22['preferred_foot'] == 'Right'].count()[0]
    
    #labelling
    labels = ['Left-Foot', 'Right-Foot']
    
    
    plt.pie([left, right], labels = labels, autopct = '%.2f')
    plt.title('Foot Preference Of  FIFA players In 2022',fontdict={'fontweight':'bold', 'fontsize':12})
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    plt.figure(figsize = (8, 8))
    plt.show()
    
    return

def pieplot2(fifa22):
    '''
    creates a pie chat to disply the different weight groups of FIFA22 players
    vizualize the data and reprents in a pie chart

    Parameters
    ----------
    fifa22 : A Pandas dataframe containing the information of fifa players 2022 

    Returns
    -------
    None.

    '''
    light_weight = fifa22.loc[fifa22.weight_kg <= 60].count()[0]
    middle_weight = fifa22.loc[(fifa22.weight_kg >= 65) & (fifa22.weight_kg <75)].count()[0]
    heavy_weight = fifa22.loc[(fifa22.weight_kg >= 75) & (fifa22.weight_kg <110)].count()[0]
    
    # labelling
    labels=['Light Weight', 'Middle Weight', 'Heavy weight']
    plt.pie([light_weight, middle_weight, heavy_weight], labels=labels, autopct='%.2f')
    plt.title('Weight Divisions Of FIFA players In 2022', fontdict={'fontweight':'bold', 'fontsize':12})
    
    
    plt.figure(figsize = (8, 8))
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600)
    plt.style.use('ggplot')
    plt.show()
    
    return

def boxplot(fifa22):
    '''
    creates a box plot representing football clubs and theri overall performance
    vizualizes the data and represents the data in box and whisker

    Parameters
    ----------
    fifa22 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # plots the data of different clubs and their overall performance
    barcelona = fifa22.loc[fifa22.club_name == 'FC Barcelona']['overall']
    man_city = fifa22.loc[fifa22.club_name == 'Manchester City']['overall']
    liverpool = fifa22.loc[fifa22.club_name == 'Liverpool']['overall']
    arsenal = fifa22.loc[fifa22.club_name == 'Arsenal']['overall']
    
    #defualt settings of plt style
    plt.rcdefaults()
    
    # labelling
    labels=['FC Barcelona', 'Man_City', 'Liverpool', 'Arsenal']
    plt.title('Football clubs Stats Comprasion FIFA22 ', fontdict={'fontweight':'bold', 'fontsize':12})
    plt.ylabel('Overall Reading Of the Team')
    plt.boxplot([barcelona, man_city, liverpool, arsenal], labels=labels)
    
    plt.figure(figsize=(10, 8))
    
    # save the plot as png and show
    plt.savefig('Line_Plot2', dpi=600) 
    plt.show()
    
    return

lineplot(gas)
lineplot2(expo)
histogram(fifa22)
pieplot(fifa22)
pieplot2(fifa22)
boxplot(fifa22)



