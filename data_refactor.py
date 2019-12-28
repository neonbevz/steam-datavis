import requests'
import pandas as pd
import numpy as np


cg_df = pd.read_csv('original/craigkelly.csv')
steamspy_df = pd.read_json('original/steamspy.json', orient='index').reset_index()

# Drop unnecessary columns

cg_df.drop(['DemoCount', 'DeveloperCount', 'MovieCount', 'PackageCount',
    'PublisherCount', 'ScreenshotCount', 'SteamSpyOwnersVariance',
    'SteamSpyPlayersVariance', 'AchievementCount', 'AchievementHighlightedCount',
    'ControllerSupport', 'FreeVerAvail', 'PurchaseAvail', 'SubscriptionAvail',
    'PCReqsHaveMin', 'PCReqsHaveRec', 'LinuxReqsHaveMin', 'LinuxReqsHaveRec',
    'MacReqsHaveMin', 'MacReqsHaveRec', 'SupportEmail', 'SupportURL', 'AboutText',
    'Background', 'ShortDescrip', 'DetailedDescrip', 'DRMNotice',
    'ExtUserAcctNotice', 'HeaderImage', 'LegalNotice', 'Website', 'PCMinReqsText',
    'PCRecReqsText', 'LinuxMinReqsText', 'LinuxRecReqsText', 'MacMinReqsText',
    'MacRecReqsText'
    ], axis=1, inplace=True)

# Refactor categories

category_names = cg_df.filter(regex='^Category')'
print(category_names)
categories_col = []
for r in range(len(cg_df.index)):
    categories = [category.replace('Category', '') for category in category_names if cg_df[category][r]]
    categories_col.append(','.join(categories) if len(categories) > 0 else None)
cg_df['Categories'] = categories_col

cg_df.drop(category_names, axis=1, inplace=True)

# Refactor genres

genre_names = cg_df.filter(regex='^GenreIs')
genres_col = []
for r in range(len(cg_df.index)):
    genres = [genre.replace('GenreIs', '') for genre in genre_names if cg_df[genre][r]]
    genres_col.append(','.join(genres) if len(genres) > 0 else None)
cg_df['Genres'] = genres_col

cg_df.drop(genre_names, axis=1, inplace=True)

cg_df.to_csv(r'refactored.csv')
