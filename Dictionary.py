def lyrics_to_frequencies(lyrics):
    myDict={}
    for word in lyrics:
        if word in myDict:
            myDict[word]+=1
        else:
            myDict[word]=1
    return myDict
def most_common_words(freq):
    values=freq.values()
    best=max(values)
    words=[]
    for k in freq:
        if freq[k]==best:
            words.append(k)
    return (words,best)
    
def words_often(freq,minTimes):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freq)
        if temp[1]>=minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else:
            done=True
    return result
    
john_mayer="Gravity is working against me And gravity wants to bring me down Oh I will never known what makes this man With all the love that his heart can stand Dream of ways to throw it all awayWhoa gravity is working against meAnd gravity wants to bring me down Oh twice as much ain't twice as good And can't sustain like one half could It's wanting more that's gonna send me to my knees Oh twice as much ain't twice as good And can't sustain like one half could It's wanting more that's gonna send me to my knees Whoa gravity stay the hell away from me Whoa gravity has taken better men than me Now how can that be Just keep me where the light is Just keep me where the light is Just keep me where the light is Come on keep me where the light is Come on keep me where keep me where the light is"
jm=john_mayer.lower()
lyrics=jm.split()
freq = (lyrics_to_frequencies(lyrics))
print (freq)
print ("The most commonly recurring words are: ",words_often(freq,5))