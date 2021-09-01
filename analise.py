from leia import SentimentIntensityAnalyzer 

sa = SentimentIntensityAnalyzer()

corpus = input('\nFrase: ')

scores = sa.polarity_scores(corpus)

compound = scores['compound']

if compound > 0.75: print ('Sentença muito positiva')
elif compound > 0.2: print ('Sentença positiva')
elif compound > -0.2: print ('Sentença neutra')
elif compound > -0.75: print ('Sentença negativa')
else: print ('Sentença muito negativa')     

print (str(compound) + '\n')