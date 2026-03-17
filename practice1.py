import pandas as pd
import numpy as np

def ex1():

    customers = pd.read_csv('customers.csv')
    orders = pd.read_csv('orders.csv')

    print(customers.head())
    print(customers.info())
    print(orders.head())
    print(orders.info())

    dfm = pd.merge(orders, customers, on='customer_id', how='left')
    print('\n')
    print(dfm)

    result = (
         dfm.groupby('customer_id')['amount']
            .sum()
            .reset_index()
            .sort_values(by='amount', axis=0, ascending=False)
            .head(2)
    )
    print('\n')
    print(result)
    result.to_csv("result.csv", index=False)
    
def ex2():

    customers = pd.read_csv('customers2.csv')
    orders = pd.read_csv('orders2.csv')
    # get info on df and check that index and columns are unique and check for duplicates
    print('\n customers df info')
    print(customers.head(4))
    print(customers.info())
    print('index is unique ', customers.index.is_unique)
    print('columns is unique ', customers.columns.is_unique)
    print('duplicated \n', customers[customers.duplicated(subset=["customer_id"])])
    #if duplicatd drop (keep first): df = df.loc[:, ~df.columns.duplicated()]
    #if duplicatd drop (keep first): df = df[~df.index.duplicated()]
    #df = df.groupby(level=0).sum() - instead of drop to combine duplicated index
    print('\n orders df info')
    print(orders.head(4))
    print(orders.info())
    print('index is unique ', orders.index.is_unique)
    print('columns is unique ', orders.columns.is_unique)
    print('duplicated \n', orders[orders.duplicated(subset=["customer_id", "order_date"])])
    print('=====> extract row with Nan')
    print(orders.loc[orders.isna().any(axis=1),:])
    print('\n')

    orders = orders.fillna(0)

    df = pd.merge(orders, customers, on='customer_id', how='left')
    print(df.head(4))
    print(df.info())

    result = (
        df.groupby('customer_id')
        .agg(
            total_spent=('amount','sum'),
            num_orders=('order_id', 'count')            
        )
        .reset_index()
        .sort_values(by='total_spent',ascending=False)
        .head(3)
    )

    print(result)
    result.to_csv('result2a.csv',index=False)

    result2 = (
        df.groupby('country')['amount']
            .sum()
            .reset_index()
            .sort_values(by='amount', ascending=False) 
    )   
    print('\n')
    print(result2.head())
    result2.to_csv('result2b.csv',index=False)

def ex3():
    df = pd.read_csv('CricketTestMatchData.csv')
    print(df.head())
    print(df.columns)
    df = df.rename(columns= {'Mat':'Matches','NO':'Not_Outs', 'HS':'Highest_Inns_Score', 'BF':'Balls_Faced', 'SR':'Batting_Strike_Rate'})
    print(df.columns)

    # remove na
    print(df.isna().any())
    print('\n')
    print(df[df['Balls_Faced'].isna()][['Player','Balls_Faced','Batting_Strike_Rate']])
    #print(df.info())
    df['Balls_Faced'] = df['Balls_Faced'].fillna(0)
    df['Batting_Strike_Rate'] = df['Batting_Strike_Rate'].fillna(0)
    #print(df[df['Player']=='ED Weekes (WI)'])

    # check duplicates
    #print(df.columns.duplicated())
    #print('duplicates is any')
    #print(df[df.duplicated()])
    df = df[~df.duplicated()]
    #print('duplicates after correction')
    #print(df[df.duplicated()])

    #creat new columns to split span date and player name
    print('\n')
    print(df['Span'].head())
    valid = df['Span'].str.match(r"^\d{4}-\d{4}$")
    print('all rows have same format = ', valid.all())
    df['Rookie_Year'] = df['Span'].str.split('-').str[0]
    df['Final_Year'] = df['Span'].str.split('-').str[1]
    df["Rookie_Year"] = pd.to_numeric(df["Rookie_Year"])
    df["Final_Year"] = pd.to_numeric(df["Final_Year"])
    df = df.drop('Span', axis=1)
    print(df.head())
    df['Player_Name'] = df['Player'].str.split('(').str[0].str.strip()
    df['Country'] = df['Player'].str.split('(').str[1].str.replace(')','')
    df = df.drop('Player', axis=1)
    print(df.head())

    problem = df['Highest_Inns_Score'].str.contains(r"[^\d.]", na=False)
    #print(df.loc[problem,'Highest_Inns_Score'])
    df['Highest_Inns_Score'] = df['Highest_Inns_Score'].str.strip('*')
    #print(df.loc[problem,'Highest_Inns_Score'])
    df["Highest_Inns_Score"] = pd.to_numeric(df["Highest_Inns_Score"])

    problem = df['Batting_Strike_Rate'].str.contains(r"[^\d.]", na=False)
    print(df.loc[problem,'Batting_Strike_Rate'])
    df['Batting_Strike_Rate'] = df['Batting_Strike_Rate'].str.replace('-', '0')
    df['Batting_Strike_Rate'] = pd.to_numeric(df['Batting_Strike_Rate'])

    #print(problem.all())
    #print(df.loc[problem, 'Balls_Faced'])
    #df['Balls_Faced'] = pd.to_numeric(df['Balls_Faced'])

    #print('\n problematic = ', repr(df.loc[53, 'Balls_Faced']))
    df['Balls_Faced'] = df['Balls_Faced'].str.replace('15456','0')
    df['Balls_Faced'] = df['Balls_Faced'].str.replace('-','0')
    df['Balls_Faced'] = pd.to_numeric(df['Balls_Faced'])
    print(df.dtypes)
    print(df.isnull().any())
    df = df.fillna(0)
    print(df.isnull().any())

    df['Career_Length'] = df['Final_Year']-df['Rookie_Year']
    df['Rank'] = df.index + 1
    print(df.head())


    print(df.dtypes)
    df = df.sort_values(by='Career_Length', ascending=False)
    #print(df['Carrer_Length'].dtype)
    #df = df.sort_values(by='Carrer_Length' , ascending=False)
    print(df.head())

    print(df.describe())

    print('\n mean carrer length = ', df['Career_Length'].mean())
    print('\n AVG Batting_Strike_Rate for cricketers who played over 10 years = ', df[df['Career_Length']>10]['Batting_Strike_Rate'].mean())
    print('\n n player who played before 1960 = ', df[df['Final_Year']<1960]['Player_Name'].count() )
    result = df.groupby('Country').agg(
        max_strike=('Batting_Strike_Rate','max'),
        mean_100=('100','mean'),
        mean_50=('50','mean'),
        mean_0=('0','mean')
    ).reset_index().sort_values(by='max_strike', ascending=False)
        
#['Batting_Strike_Rate'].max().reset_index().sort_values(by='Batting_Strike_Rate', ascending=False)
        
    print('\n result = ')
    print(result)

def ex4():
    '''
    Find most recent golden cross: short term moving average move from below to above long term moving average:
    compute 50 days moving avr
    compute 200 days moving average
    binary flag to mark any istance of a golden cross
    '''
    df = pd.read_csv('SPY_close_price_5Y.csv')
    print(df.head())
    print(df.info())
    '''
    print('\n Any none: \n', df.isna().any())
    print('\n Any duplicated: \n', df.duplicated() )
    print('\n Is unique: \n', df.columns.is_unique )
    print('\n Is unique: \n', df.index.is_unique )
    '''
    df['Avg50'] = df['Close'].rolling(50).mean()
    df['Avg100'] = df['Close'].rolling(100).mean()

    df['Avg50>Avg100'] =  df['Avg50']>df['Avg100']

    print('\n ', df[df['Avg50>Avg100']]  )

    cross_up = (df['Avg50'] > df['Avg100']) & (df['Avg50'].shift(1) <= df['Avg100'].shift(1))
    #df['cross_up'] = (df['Avg50>Avg100']) & (~df['Avg50>Avg100'].shift(1)) 

    print(df[cross_up])
    print(df.iloc[465:467,:])


    #df['Avg50>Avg100'] = df.transform(lambda x: True if df['Avg50']>df['Avg100'] else False)
    #print(df[50:150])

def ex5():

    customers = pd.read_csv('customers3.csv')
    orders = pd.read_csv('orders3.csv')

    print(customers.head())
    print(customers.info())

    print('\n')
    print(orders.head())
    print(orders.info())

    customers['signup_date'] = pd.to_datetime(customers['signup_date'], format='mixed')
    orders['order_date'] = pd.to_datetime(orders['order_date'], format='mixed')

    valid = orders['amount'].str.contains(r'\d.', na=False)
    #print(orders[~valid])
    orders['amount'] = orders['amount'].str.replace('-','0.')
    orders['amount'] = pd.to_numeric(orders['amount'])    
    #print(orders.isna().any())

    df = pd.merge(orders, customers, on='customer_id', how='left')
    print(df.head())

    df['days_since_signup'] = df['order_date'] - df['signup_date']
    print(df.head())

    tot_per_cust = df.groupby(['customer_id','name']).agg(
        total_spent = ('amount', 'sum'),
        num_orders = ('order_id', 'count')
        ).reset_index().sort_values('total_spent', ascending=False)
    print(tot_per_cust)

    tot_rev = df.groupby('country')['amount'].sum().reset_index().sort_values('amount', ascending=False)
    tot_rev = tot_rev.rename(columns={'amount': 'total_revenue'})
    print(tot_rev)

    df['order_month'] = df['order_date'].transform(lambda x: pd.Period(x, freq='M'))
    print(df.head())

    month_rev = df.groupby('order_month')['amount'].sum().reset_index()
    print(month_rev)

def ex6():

    customers = pd.read_csv('customers4.csv')
    orders = pd.read_csv('orders4.csv')
    products = pd.read_csv('products4.csv')

    print(customers.head())
    print(customers.info())
    print(orders.head())
    print(orders.info())
    print(products.head())
    print(products.info())

    customers['signup_date'] = pd.to_datetime(customers['signup_date'], format='mixed')
    customers['name'] = customers['name'].str.strip()
    customers = customers.drop_duplicates()

    orders['order_date'] = pd.to_datetime(orders['order_date'], format='mixed')

    df = pd.merge(orders, customers, on='customer_id', how='left')
    df = pd.merge(df, products, on='product_id', how='left')
    df['total_price'] = df['quantity']*df['price']

    print('\n')
    print(df.head())
    print('\n')
    print(df[['order_id', 'customer_id', 'quantity', 'price', 'total_price']].head())
    print(df.info())

    per_customer = df.groupby('customer_id').agg(
        total_spent = ('total_price', 'sum'),
        number_of_orders = ('order_id', 'count')
    ).reset_index().sort_values('total_spent',ascending=False)

    print('\n')
    print(per_customer.head())

    per_country = df.groupby('country')['total_price'].sum().reset_index().sort_values('total_price',ascending=False)

    print('\n')
    print(per_country.head())

    per_product = df.groupby('product_name')['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
    per_product = per_product.rename(columns={'quantity': 'total_quantity'})

    print('\n')
    print(per_product)

    df['order_month'] = df['order_date'].dt.to_period(freq='M')
    #print('\n')
    #print(df[['order_date','order_month']].head())
    
    per_month = df.groupby('order_month')['total_price'].sum().reset_index().sort_values('total_price', ascending=False)
    per_month = per_month.rename(columns={'total_price': 'revenue'})
    print('\n')
    print(per_month)

    per_country_customer = df.groupby(['country','name'])['total_price'].sum().reset_index().sort_values(['country','total_price'], ascending=[False, False])
    per_country_customer = per_country_customer.rename(columns={'total_price': 'total_spent'})

    print('\n')
    print(per_country_customer)

    condition = ~per_country_customer['country'].duplicated()
    per_country_customer = per_country_customer[condition]

    print('\n')
    print(per_country_customer) 

    






    


if __name__ == '__main__':
    #ex1()
    #ex2()
    #ex3()
    #ex4()
    #ex5()
    ex6()

