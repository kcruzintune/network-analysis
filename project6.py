# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import numpy as np


############################### 1st analysis ##################################


TwitterData = pd.read_csv('C:/Users/kcruz29/.spyder-py3/twitter_cleaned(3).csv', encoding='ISO-8859-1')

TwitterData5 = TwitterData.head(5)

g = nx.Graph()

g.add_edges_from(TwitterData.values)
g.number_of_nodes()
g.number_of_edges()

degrees = nx.degree(g)
degree_sets = dict(degrees)
degree_sets = pd.Series(dict(nx.degree(g)))
degree_sets = degree_sets.sort_values(ascending=False)#.head(10)

plt.figure(1)
degree_sets.plot(kind='hist', title="Unscaled Degree Distribution by Kevin Cruz")

degree_sets_log10 = np.log10(degree_sets)

plt.figure(2)
degree_sets_log10.plot(kind='hist', title='Distribution log of degrees by Kevin Cruz')

cent = nx.degree_centrality(g)

cent10 = pd.Series(cent)

james = cent10["James"]

g_cored = nx.Graph()

g_cored = nx.k_core(g, 3)
g_cored.number_of_nodes()
g_cored.number_of_edges()

core_degrees = nx.degree(g_cored)
core_sets = dict(core_degrees)
core_pandas = pd.Series(dict(nx.degree(g_cored)))
core_pandas = core_pandas.sort_values(ascending=False)

plt.figure(3)
core_pandas.plot(kind='hist', title="3-cored graph degree distribution by Kevin Cruz")





labels = g_cored.nodes
labels = list(labels)

dict1 = {}
for i in labels:
    
    key = str(i)
    if len(key) >= 9:
        val = key[:7] + '.'
    if len(key) <= 8:
        val = key + '.'
    dict1[i] = val

# print(dict1)

plt.figure(4, [12,12])
plt.title("First Analysis Network by Kevin Cruz")

nx.draw_networkx(g_cored, with_labels=True, labels=dict1, font_size=8)



############################### 2nd analysis ##################################    


AsiaData = pd.read_csv('C:/Users/kcruz29/.spyder-py3/lab 11/project 6/lastfm_asia_edges.csv', encoding='ISO-8859-1')

Asia5 = AsiaData.head(5)

k = nx.Graph()

k.add_edges_from(AsiaData.values)
k.number_of_nodes()
k.number_of_edges()

asia_degrees = nx.degree(k)
asia_degree_sets = dict(asia_degrees)
asia_degree_sets = pd.Series(dict(nx.degree(k)))
asia_degree_sets = asia_degree_sets.sort_values(ascending=False)#.head(10)

plt.figure(5)
asia_degree_sets.plot(kind='hist', title="[Asia] Unscaled Degree Distribution by Kevin Cruz")

asia_degree_sets_log10 = np.log10(asia_degree_sets)

plt.figure(6)
asia_degree_sets_log10.plot(kind='hist', title='[Asia] Distribution log of degrees by Kevin Cruz')

asia_cent = nx.degree_centrality(k)

asia_cent10 = pd.Series(asia_cent)


asia_g_cored = nx.Graph()

asia_g_cored = nx.k_core(k, 12)
#I increased the number inside (k, #) since the number nodes exceeded 1024 
#nodes
asia_g_cored.number_of_nodes()
asia_g_cored.number_of_edges()

asia_core_degrees = nx.degree(asia_g_cored)
asia_core_sets = dict(asia_core_degrees)
asia_core_pandas = pd.Series(dict(nx.degree(asia_g_cored)))
asia_core_pandas = asia_core_pandas.sort_values(ascending=False)

plt.figure(7)
asia_core_pandas.plot(kind='hist', title="[Asia] 3-cored graph degree distribution by Kevin Cruz")

asia_labels = asia_g_cored.nodes
asia_labels = list(asia_labels)

asia_dict1 = {}
for asia_keys in asia_labels:
    
    key = str(asia_keys)
    if len(key) >= 4:
        val = key[:2] + '00.'
    if len(key) <= 3:
        val = key + '.'
    asia_dict1[asia_keys] = val


plt.figure(8, [12,12])
plt.title("Second Analysis Network by Kevin Cruz")

nx.draw_networkx(asia_g_cored, with_labels=True, labels=asia_dict1, font_size=8)

