import pandas as pd

# Create a sample DataFrame
data = {
    "country": ["Italy", "France", "USA", "Australia", "New Zealand", "Italy", "USA", "France", "Australia", "New Zealand"],
    "province": ["Tuscany", "Bordeaux", "California", "Barossa Valley", "Marlborough", "Piedmont", "Oregon", "Champagne", "Yarra Valley", "Hawke's Bay"],
    "points": [92, 96, 88, 95, 97, 90, 85, 91, 93, 98],
    "variety": ["Sangiovese", "Merlot", "Chardonnay", "Shiraz", "Sauvignon Blanc", "Nebbiolo", "Cabernet Sauvignon", "Pinot Noir", "Cabernet Sauvignon", "Pinot Gris"],
    "description": [
        "Fruity and elegant.",
        "Rich and complex.",
        "Crisp with citrus notes.",
        "Full-bodied and spicy.",
        "Fresh and vibrant.",
        "Earthy and structured.",
        "Smooth and oaky.",
        "Light and floral.",
        "Jammy and bold.",
        "Crisp and aromatic."
    ]
}

reviews = pd.DataFrame(data)

###Selecting Columns
countries = reviews['country']
country_points = reviews[["country",'points']]

###Selecting Rows
first_row = reviews.iloc[0]
some_reviews = reviews.loc[[3,4,5]]
last_3 = reviews.iloc[-3:]

###Conditional Selection
high_points = reviews[reviews['points'] > 95]
italy_france = reviews[reviews["country"].isin(['Italy','France'])]
aus_wines = reviews.loc[(reviews["country"]== 'Australia') & (reviews['points'] <= 95)]

###Indexing with loc and iloc
desc_index2 = reviews.loc[2,'description']
province_5th = reviews.iloc[4,reviews.columns.get_loc('province')]
province_6th = reviews.loc[4,'province']

###Assigning / Adding Columns
reviews['high_score'] = reviews['points'] >= 95
reviews['points_backwards'] = range(len(reviews),0,-1)

###Advanced Slicing
first5 = reviews.loc[0:4,['country', 'variety']]
even_index_reviews = reviews.loc[[0,2,4,6,8],['country','points']]





