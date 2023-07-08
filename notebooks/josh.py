def calc_year_over_avg(df, state, quarter):
    if len(df.loc[:quarter].index.values[-4:])==4:
        return df[state].loc[df.loc[:quarter].index.values[-4:]].mean()
    print("Not enough information to get year-over-year average")
