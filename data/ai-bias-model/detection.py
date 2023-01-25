totalArticles = 100
articles, neg_words, pos_words = [], [], []
names = ["South Asian", "Chinese", "Black", "Filipino", "Arab", "Latin American", "Southeast Asian", "West Asian", "Korean and Japanese", "Indigenous", "White"]
keywords = {
    'South Asian' : [[], []],
    'Chinese' : [[], []],
    'Black' : [[], []],
    'Filipino' : [[], []],
    'Arab' : [[], []],
    'Latin American' : [[], []],
    'Southeast Asian' : [[], []],
    'West Asian' : [[], []],
    'Korean and Japanese' : [[], []],
    'Indigenous': [[], []],
    'White' : [[], []],
}
words = {
    'South Asian' : [[], []],
    'Chinese' : [[], []],
    'Black' : [[], []],
    'Filipino' : [[], []],
    'Arab' : [[], []],
    'Latin American' : [[], []],
    'Southeast Asian' : [[], []],
    'West Asian' : [[], []],
    'Korean and Japanese' : [[], []],
    'Indigenous': [[], []],
    'White' : [[], []],
}

for i in range(1, totalArticles+1):
    file = "./data/ai-bias-model/articles/article" + str(i) + ".txt"
    with open(file, "r") as f:
        articles.append(list(map(str.strip, f.readlines(), )))

with open("./data/ai-bias-model/adjectives/negative_words.txt", "r") as f:
    neg_words = list(map(str.strip, f.readlines(), ))

with open("./data/ai-bias-model/adjectives/positive_words.txt", "r") as f:
    pos_words = list(map(str.strip, f.readlines(), ))

cnt = 1
for article in articles:
    for line in article:
        for keyword in keywords:
            if keyword not in line: continue
            for word in neg_words:
                if word not in line: continue
                keywords[keyword][0].append(line)
                words[keyword][0].append(word)
            for word in pos_words:
                if word not in line: continue
                keywords[keyword][1].append(line)
                words[keyword][1].append(word)
    print(cnt)
    cnt += 1

results = []

for keyword in keywords:
    print(keyword, len(keywords[keyword][0]), len(keywords[keyword][1]))

for keyword in keywords: results.append([[], []])

for i in range(len(results)):
    #print(keyword)
    for line in keywords[names[i]][0]: 
        if line in results[i][0]: continue
        results[i][0].append(line)
    for line in keywords[names[i]][1]: 
        if line in results[i][1]: continue
        results[i][1].append(line)
        #print(line)
        #print(words[keyword][0])
        #x = 1
    

with open("./data/ai-bias-model/test.txt", "w") as f:
    for i in range(len(results)):
        print(len(results[i][0]), len(results[i][1]))
        f.write(str(results[i][0]))
        f.write("\n")
        f.write(str(results[i][1]))
        f.write("\n")
        f.write(names[i])
        f.write("\n")
