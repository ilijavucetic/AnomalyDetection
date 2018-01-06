import PatternsMining.apriori as apriori
# http://aimotion.blogspot.com/2013/01/machine-learning-and-data-mining.html
dataset = apriori.load_dataset()

print(dataset)

C1 = apriori.createC1(dataset=dataset)

D = map(set, dataset)
print(D)