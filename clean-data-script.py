import pandas as pd 

df = pd.read_csv('cyber-operations-incidents.csv')

#Clean data - everything in parenthesis and unwanted string
df['Sponsor']=df['Sponsor'].replace(r" \(.*\)", "", regex=True)
df['Sponsor']=df['Sponsor'].replace(r", State of", "", regex=True)

#Separate Sponsor by comma delimeter
df['Sponsor'] = df['Sponsor'].str.split(',').explode().reset_index(drop=True)

#Check data and save into new csv
df.to_csv('clean-cyber-operations-incidents.csv', index = False)



