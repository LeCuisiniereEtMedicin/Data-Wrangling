import pandas as pd
dic = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
       'Dimension':['Length','Width','Height','Length','Width','Height'],
       'Value':[6,4,2,5,3,4]}
df = pd.DataFrame(dic, columns=['Box','Dimension','Value'])
tidy = df.pivot(index='Box',columns='Dimension',values='Value').reset_index()
tidy['Volume'] = tidy.Length*tidy.Width*tidy.Height