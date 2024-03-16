import pandas as pd

df2 = pd.read_csv("pokemon.csv") #loads in the csv file as a dataframe
df = pd.read_excel("pokemon_data.xlsx") #loads in the excel file as a dataframe
'''
print(df.head(5)) #prints the first 5 rows of the dataframe
print(df.tail(5)) #prints the last 5 rows of the dataframe

print(df.columns) #prints the headers of each column

print(df['Name'][0:5]) #prints out every name from the first five records
print(df.Name) #does similar to above

print(df[['Name','HP']]) #prints two columns

print(df.iloc[10]) #prints out the info for row 10
print(df.iloc[0:4]) #prints out multiple rows

print(df.iloc[2,1]) #prints out the attribute at Row, Column

#goes through the whole frame, and prints out every index and the name value from the row
for index, row in df.iterrows(): 
    print(index, row['Name'])

print(df.loc[df['Type 1'] == 'Fire']) #prints all rows with fire types

df.describe() #gives tons of data about the frame

print(df.sort_values(['Name'], ascending = False)) #sorts the data by descending name
print(df.sort_values(['Sp. Atk', 'Sp. Def'], ascending = [1,0])) #sorts the data by ascending Sp Atk, then descending Sp. Def

#adds another column to the dataframe then prints out the new stat for each name
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df[['Name','Total']])

df = df.drop(columns=['Total']) #gets rid of the "total" column

#for each row makes a new column by adding the 4th to 9th column
df['Total'] = df.iloc[:,4:10].sum(axis=1)

cols = list(df.columns) #gets the columns
df = df[cols[0:4] + [cols[-1]] + cols[4:12]] #rearranges the columns in the dataframe

#prints the dataframe to a csv file, does not have a column of indexes
df.to_csv("modified.csv", index=False)

df.to_excel("modified.xslx") #prints out to an excel file

#makes a separate dataframe only containing fire pokemon with a speed stat of 100
df2 = df[(df['Speed'] == 100) & (df['Type 1'] == 'Fire')]
df2 = df2.reset_index(drop = True) #resets the indexes so we don't keep the ones from the first df, drops that column
df2 = df2.drop(columns = 'index') #another way to drop that column
print(df2)

print(df.loc[df['Name'].str.contains("ch")]) #gets every row where the name contains ch
print(df.loc[~df['Name'].str.contains("ch")]) #gets every row where the name does NOT contains ch

import re #imports regex

#using regex, gets every pokemon that 'type' contains fire or grass
print(df.loc[df['Type 1'].str.contains('fire|grass', flags = re.I, regex = True)]) #flags = re.I means don't care about caps

#updates all 'Fire" type 1's to be 'Flamer'
df.loc[df['Type 1'] == "Fire", 'Type 1'] = 'Flamer' 

#can update multiple columns at a time
df.loc[df['HP'] > 50, ['#', 'Legendary']] = ['999', True]

#groups the data by type 1, and gets the mean of the atk and sp. atk
df2 = df.groupby('Type 1')[['Attack', 'Sp. Atk']].mean()

df2 = df.groupby('Type 1')[['Defense', 'Sp. Def']].sum()

df2 = df.groupby('Type 1').count()
print(df2)
'''
df2 = df.drop(columns = ['Name', 'Type 1', 'Type 2', 'Legendary'])

#the corr method tracks correlation between columns
print(df2.corr())

