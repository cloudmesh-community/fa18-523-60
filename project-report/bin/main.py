''' This file is mainly used for performance benchmarking '''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from datetime import datetime
import pymongo
from pymongo import MongoClient
from wordcloud import WordCloud
import time
import numpy as np
import time 

def show_wordcloud(data, title = None):
    '''Split names by space and generate word counts.'''
    wordcloud = WordCloud(
        background_color='white',
        max_words=100,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin it was heads
    ).generate(str(data))

    fig = plt.figure(figsize =(10,10))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    return plt.imshow(wordcloud)

''' Build DataFrame from MongoDB data '''

def load_data_mongo():
   
       ''' Read the Credentials '''

       config_file = open('config.txt','r')
       connect_str = config_file.read()

       ''' Connect using PyMongo Driver and load Data '''
       client = pymongo.MongoClient(connect_str)
       db = client.kick
       collection = db.project
       df = pd.DataFrame(list(collection.find()))
       config_file.close()
       return df

def load_data():    
    
    ''' If want to use DigitalOcean please use below connection string '''
    # client = pymongo.MongoClient("mongodb://nishad:Tesla18$@159.203.170.43/kick")

    df = load_data_mongo()
    #df.drop(['usd pledged'], axis=1, inplace=True)

    df.replace('N,0"','NO',inplace=True)

    ''' Launched date conversion to day,year,month,time'''
    df['year'] = df['launched'].apply(lambda x:x[0:4])                                                                                                                                                                                                                                          
    df['month'] = df['launched'].apply(lambda x:x[5:7])
    df['day'] = df['launched'].apply(lambda x:x[8:10])
    df['time'] = df['launched'].apply(lambda x:x[11:])

    ''' Deadline date conversion to day,year,month,time'''
    df['year_d'] = df['deadline'].apply(lambda x:x[0:4])                                                                                                                                                                                                                                          
    df['month_d'] = df['deadline'].apply(lambda x:x[5:7])
    df['day_d'] = df['deadline'].apply(lambda x:x[8:10])
    df['time_d'] = df['deadline'].apply(lambda x:x[11:])

    df['A'] = pd.to_datetime(df['deadline'])
    df['B'] = pd.to_datetime(df['launched'])
    df['duration'] = df['A'] - df['B']
    df.duration = df.duration.dt.days
    return df


def main():
    start = time.time()
    ''' Projects statuses '''
    df = load_data()
    plt.style.use('ggplot')
    fig1 = plt.figure(figsize=(12,8))
    df['state'].value_counts().plot(kind='bar')
    plt.title('project_count_by_status')
    fig1.savefig('project_states_count.png')


    sns.set_style('white')
    fig2 = plt.figure(figsize=(10,6))
    df3 = df[(df['state']=='successful')| (df['state']=='failed')].sort_values(by='pledged',ascending=True)
    sns.countplot(x='year',hue='state',data=df3)
    plt.title('project_count_by_year')
    fig2.savefig('project_count_by_year.png')


    sns.set_style('white')
    fig3 = plt.figure(figsize=(10,6))
    df[['main_category', 'state']].pivot_table(columns='state', index='main_category', aggfunc=np.size).plot(kind='bar', figsize=(12, 8), stacked=True)
    plt.title('project_states_over_main_category')
    fig3.savefig('project_states_by_category.png')


    fig4 = plt.figure(figsize=(10,6))
    df_s = df[(df['state']=='successful')| (df['state']=='failed')]
    df_c = df_s[['usd pledged','state','country']]
    df_cp = df_c.groupby(['country','state'],as_index=False).mean().sort_values(by='usd pledged',ascending=False)
    sns.barplot(x='country',y='usd pledged',data=df_cp,hue='state',palette='muted')
    plt.title('top_global_markets_for_pledged')
    fig4.savefig('top_markes_for_pledged.png')

    fig5 = plt.figure(figsize=(10,6))
    df_gn = df[['usd_pledged_real','state','main_category']]
    df_gn_g = df_gn.groupby(['main_category','state'],as_index=False).mean()
    df_pivot = df_gn_g.pivot(index='state',columns='main_category')
    df_pivot.dropna(inplace=True)
    labels = ['art','comics','crafts','dance','design','fashion','film & video','food','games','journalism','music','photography','publishing','technology','theater']
    g = sns.heatmap(df_pivot,cmap='viridis',xticklabels=labels)
    #plt.xticks(np.arange(0, 1, step=0.5))
    plt.xticks(rotation=45)
    plt.title('heatmap:main_category,state & plegded_amount')
    fig5.savefig('heatmap.png')

   
    dims = (10,6)
    fig6, (ax1, ax2) = plt.subplots(ncols=2, sharey=False, figsize=dims)
    sns.distplot(df.goal, ax=ax1)
    sns.distplot(np.log1p(df.goal), ax=ax2)
    plt.title('distplot_goal')
    fig6.savefig('distplot_goal.png')


    fig7 = plt.figure(figsize=(10,6))
    df_r = df[df['state'] == 'failed'] 
    df_r['remain'] = df_r['goal']- df_r['pledged']
    df8 = (df_r.groupby(['main_category']).agg({'goal':'sum', 'pledged':'sum', 'remain':'sum'}).reset_index())
    #print(df8)
    ax = plt.axes()
    ax.bar(df8.main_category, df8['remain'], width=0.4, color='r',label = 'remaining')
    ax.bar(df8.main_category, df8['pledged'], width=0.4, color='g', label = 'pledged')
    plt.xticks(rotation=45)
    ax.legend(fontsize = 10)
    plt.title('failure_categories_pledged_remaining_fund.png')
    fig7.savefig('failure_categories_pledged_remaining_fund.jpg')

    fig8 = plt.figure(figsize=(10,6))
    df4  = df.groupby('state').duration.mean().sort_index()
    df4.plot(kind='box')
    plt.title('duration_box_plot')
    fig8.savefig('duration_box_plot.png')
    
    show_wordcloud(df[df.state == 'successful']['category'])
    end = time.time()
    elapsed_time = end - start
    print("Program RunTime On Mongo Atlas cloud in seconds:", elapsed_time)
main()
