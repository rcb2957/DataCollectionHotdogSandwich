import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def main():
    df = load_data()
    print(df)

    display_visual(df)

def display_visual(df):
    # look at examples from https://matplotlib.org/
    intern = [i for i in df if i['cohort'] == '2022 Intern' and i['hotdog'] == 1];
    tdp2021 = [t for t in df if t['cohort'] == '2021 TDP' and t['hotdog'] == 1];
    tdp2020 = [t for t in df if t['cohort'] == '2020 TDP' and t['hotdog'] == 1];
    x = ['2022 Intern', '2021 TDP', '2020 TDP'];
    y = [len(intern), len(tdp2021), len(tdp2020)];
    plt.bar(x, y);
    plt.title('Does Year Started at M&T Affect a Person\'s Views on a Hotdog Being a Sandwich?')
    plt.xlabel('Year Started at M&T')
    plt.ylabel('Number of People Thinking Hotdogs are Sandwiches')
    plt.show()

def load_data():
    df = pd.read_csv("./data.csv")

    # remove unused columns
    for label in ['#' , 'Start Date (UTC)', 'Submit Date (UTC)', 'Network ID']:
        df = df.drop(label, axis=1)

    # replace questions with more convenient, one word keys
    column_names = {'What\'s your office location': 'location', 
                    'Are you an Intern or a TDP?': 'cohort', 
                    'What year are you in school?': 'school_year', 
                    'Is the grass really greener on the other side?': 'greener', 
                    'Is a hotdog really a sandwich?': 'hotdog', 
                    'Backend or Frontend?': 'end', 
                    'Is water wet?': 'water', 
                    'Do straws have two holes or one?': 'straw', 
                    'Is it Gif or Jif?': 'moving_image', 
                    'Is cereal soup?': 'soup', 
                    'If you are at a restaurant and your waiter doesn\'t come back, are you the waiter?': 'self_service',
                    'Since tomatoes are technically fruits, does that make ketchup jam?': 'ketchup', 
                    'Does pineapple belong on pizza?': 'pineapple', 
                    'If you put one lasagna on top of another lasagna is it two lasagnas or just one big one?': 'lasagna',
                    'Does Mike Wazowski wink or blink?': 'monsters_inc', 
                    'If you fold pizza and eat it, are you eating a sandwich?': 'pizza_fold'}
    df.rename(columns = column_names, inplace=True)

    # replace some of the data values with more convenient ones
    df['end'] = df.apply(lambda x: 'front' if x['end'] == '&lt;title&gt;Frontend&lt;/title&gt;' else 'back', axis=1)
    df['straw'] = df.apply(lambda x: 1 if x['straw'] == 'One Hole' else 2, axis=1)
    df['lasagna'] = df.apply(lambda x: 1 if x['lasagna'] == 'One Lasagna' else 2, axis=1)
    
    return df

if __name__ == '__main__':
    main()