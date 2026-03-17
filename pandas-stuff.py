import numpy as np
import pandas as pd

def create_objects():

    # Series
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)

    #Dataframe
    dates = pd.date_range('20130101', periods=6)
    print(dates)

    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
    print(df)

    df2 = pd.DataFrame(
        {
            'A': 1.0,
            'B': pd.Timestamp('20130102'),
            'C': np.array([3]*4, dtype='int32'),
            'D': pd.Series(1, index=list(range(4)), dtype='float32'),
            'E': pd.Categorical(['test','train','test','train']),
            'F': 'foo'
        }
    )

    # view options
    print(df2.head(2))
    print(df2.tail(2))
    print('datatypes = ', df2.dtypes)
    print('index list = ', df2.index)
    print('column names = ', df2.columns)

    # view w/o labels - transform to numpy
    wo_labels = df.to_numpy()
    print(type(wo_labels))
    print(wo_labels.dtype)
    print(wo_labels)

    wo_labels2 = df2.to_numpy()
    print(type(wo_labels2))
    print(wo_labels2.dtype)
    print(wo_labels2)

    #get stats
    print('\n stats \n', df.describe())

    #transport a matrix
    t_df = df.T
    print('\n t_df \n ', t_df)

    #sort
    sorted_df = df.sort_index(axis=1, ascending=False)
    print('\n sorted df on axis 1 \n', sorted_df)
    print('\n sorted df on axis 0 \n', df.sort_index(axis=0, ascending=False))
 
def do_selections():

    s1 = pd.Series(range(5), index=list('abcde'))
    print('\n s1')
    print(s1)

    # indexing
    # loc[] label based, iloc[] position based 0:len-1, 
    print('\n s1.loc')
    print(s1.loc[['a','c','e']])

    dates = pd.date_range('1/1/2000', periods=8)
    df = pd.DataFrame(np.random.randn(8,4), index=dates, columns=list('ABCD'))

    print('\n df \n', df)

    print(f"\n Column A \n{df['A'][3]}")
    print('\n Columns A and B: \n'+df[['A','B']].to_string())

    #swapping column A and B
    df[['A','B']] = df[['B','A']]
    print('\n df with swapped columns \n', df.head(3))

    #s2 = pd.Series([chr(i) for i in range(ord('a'),ord('z'),2)])
    #print(f'\n s2 \n{s2}')

    #swap all columns:
    list_labels = df.columns
    reverted_list_labels = list_labels[::-1]
    print ('\n list labels     = ', list_labels)
    print ('\n list labels rev = ', reverted_list_labels)
    df[list_labels] = df[reverted_list_labels]
    print('\n df with ALL swapped columns \n', df.head(3))

    #just reordered columns and not label to value association
    print('\n df with resorted columns \n', df.sort_index(axis=1,ascending=False).head(3))

    # selection by label
    dfl = pd.DataFrame(
        np.random.randn(5,4),
        index=pd.date_range('20130101', periods=5),
        columns=list('ABCD')
    )

    print('\n dfl \n', dfl)
    print('\n dfl slice \n', dfl.loc['2013-01-02':'2013-01-04'])
    dfl.loc['2013-01-04':] = 0
    print('\n new dfl \n', dfl.tail(4))
    print('\n dfl another slice \n', dfl.loc['2013-01-02':'2013-01-04','A':'B'])
    print('\n dfl another slice \n', dfl.loc['2013-01-02':'2013-01-04',['A','C']])
    print('\n dfl column A \n', dfl.loc[:,'A'])
    print(f'\n dfl of a row (xs) \n{dfl.loc['2013-01-02']}') #20130101 also works
    print('\n dfl of a slice \n', dfl.loc[:,dfl.loc['20130101']>0]) 
    print('\n dfl of a slice \n', dfl.loc[:, lambda df: ['A','B'] ]) 
   

    #index intersection
    #ex 1
    s = pd.Series([10,20,30], index=list('abc'))
    t = pd.Series([1,2,3], index=list('bcd'))

    common = s.index.intersection(t.index)
    print(f'\n Result of operation s[common]+t[common]\n{s[common]+t[common]}')

    #ex2
    dates1 = pd.date_range('20000101', periods=3)   
    dates2 = pd.date_range('20000102', periods=3)
    common_dates = dates1.intersection(dates2)
    print('\n common dates \n', common_dates)

    #enlarge series/dataframe
    s = pd.Series([1,2,3], index=list('abc'))
    s['d'] = 7
    s.loc[5] = 8
    print('\n s series \n', s)

    dfi = pd.DataFrame(np.arange(6).reshape(3,2), 
                       columns=list('AB'))
    
    print('\n dfi \n', dfi)

    #add a column
    dfi.loc[3]=5
    dfi.loc[:,'sum'] = dfi.loc[:,'A']+dfi.loc[:,'B']
    print('\n dfi \n', dfi)

    print(dfi.describe())

    #filter the data with boolean vectors/indexing use: &, |, ~ (and, or, not)
    s = pd.Series(np.arange(-3,4))
    print('\n s \n', s)
    print('\n s \n', s[s>0])
    print('\n s \n', s[ (s<0) | (s>1.5)])
    print('\n s \n', s[ ~(s<0)])

    df2 = pd.DataFrame(
        {   
            'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
            'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
            'c': np.random.randn(7)
        }
    )

    print('\n df2')
    print(df2)

    criteria = df2['a'].map(lambda x: x.startswith('t'))
    criteria2 = df2['a'].str.startswith('t')
    criteria3 = df2['a'].map(lambda x: len(x)>3)

    print('\n')
    print(df2[criteria])
    print('\n')
    print(df2[criteria3])
    print('\n')
    print(df2.loc[criteria & (df2['b']=='x'), 'b':'c' ])
    print('\n')
    print(df2[df2['b'].isin(['y','z'])])
    mask = ~df2['a'].duplicated()
    print('\n mask\n', mask)
    print(df2.loc[mask, ['a','b']])

    #multiIndex
    smi = pd.Series(np.arange(6), index=pd.MultiIndex.from_product([[0,1], ['a','b','c']])) 
    print('\n') 
    print(smi)

    #Where method: to not filter but adding Nan for row/values not passing conditions 
    # for a series 
    # for df is automatocally done 
    print('\n') 
    print (s.where(s>0))

    print('\n') 
    print(dfl)
    print(dfl[dfl>0])
    print(dfl.where(dfl>0),-df) #replace value failing the condition with -df value

    #duplicates
    print('\n')
    print(df2)
    df2.loc[7] = ['one' , 'x', df2['c'][0]]
    print('\n')
    print(df2)    
    print(df2.duplicated())
    print(df2.duplicated('a'))
    print(df2.drop_duplicates('a',keep=False))

    print('\n original dfl') 
    print(dfl)   

    # user define function + agg (summary) and transform (same size as original columns)
    print('\n Columns summary mean * 100')    
    print(dfl.agg(lambda x: np.mean(x)*100))

    print('\n Columns * 100')    
    result = dfl.transform(lambda x: x*100)
    print(result)

    print('\n Only positive')    
    result = dfl.where(dfl>0, 0).where(dfl<=0, 1)
    print(result)
    print('\n Count unique rows')   
    print(result.value_counts())
    print('\n Count values for columns')
    print(result.apply(pd.Series.value_counts))
    

def merge_union():

    df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
    print('\n')
    print(df)
    # split the rows
    pieces = [df[:3], df[3:7], df[7:]]
    print('\n')
    print(pieces[0])
    #recombine the rows
    print('\n')
    print(pd.concat(pieces))

    # merge equivalent of SQL JOIN
    left = pd.DataFrame(
        {
            'key': ['foo','foo'],
            'lval': [1,2]
        }
    )

    right = pd.DataFrame(
        {   
            'key': ['foo','bar'],
            'rval': [4,5]
        }
    )
    print('\n')
    print(left)
    print('\n')
    print(right)

    print('\n')
    print(pd.merge(left, right, on='key'))

    #groupby
    df = pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
        }
    )

    print('\n')
    print(df)  

    print('\n')
    print(df.groupby('A')[["C","D"]].mean())

    print('\n')
    print(df.groupby('A')[["C","D"]].aggregate(lambda x: np.mean(x)*100))





if __name__ == '__main__':
    #create_objects()
    #do_selections()
    merge_union()

