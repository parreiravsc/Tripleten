import pandas as pd


class DataFrame:
    '''Recebe o dataframe e contem as funções para  tratar os dados e realizar análises.'''

    def __init__(self, df):
        self.df = df

    def ajusta_dados(self):
        self.df['date_posted'] = pd.to_datetime(self.df['date_posted'])
        self.df['model_year'] = pd.to_datetime(
            self.df['model_year'], format='%Y').dt.year
        self.df['model_year'] = self.df['model_year'].fillna('unknown')
        self.df['cylinders'] = self.df['cylinders'].fillna(0).astype(int)
        self.df['odometer'] = self.df['odometer'].fillna(0).astype(int)
        self.df['paint_color'] = self.df['paint_color'].fillna('unknown')
        self.df['is_4wd'] = self.df['is_4wd'].fillna(0).astype(int)
        return self.df
