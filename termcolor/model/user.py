import pandas as pd

pd.set_option('display.max_columns', None)


def get_user():
    df = pd.read_csv('./data/user.csv')
    return df

def save_user(data):
    df = get_user()
    df.loc[len(df)] = data

    df.to_csv('./data/user.csv', index=False)

        