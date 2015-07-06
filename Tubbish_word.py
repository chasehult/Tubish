# -*- coding: utf-8 -*-
import sys
import warnings
import random
import urllib2
import urllib
import update
try:
    alert=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Alert.txt")
    print alert.read()
except:
    pass
print "Loading..."
try:
    import Numbers
except:
    urllib.urlretrieve("https://raw.githubusercontent.com/chasehult/Translation/master/Numbers.py", "Numbers.py")
    import Numbers

import datetime
tubbishbirthday=datetime.date(2015, 7, 5)
present="\x68\x74\x74\x70\x3A\x2F\x2F\x75\x6E\x69\x63\x6F\x64\x65\x73\x6E\x6F\x77\x6D\x61\x6E\x66\x6F\x72\x79\x6F\x75\x2E\x63\x6F\x6D"


PROUNOUNCIATION={u"ā":"ay",u"â":"a",u"b":"b",u"d":"d",u"ē":"ee",u"ê":"e",
                 u"ə":"u",u"f":"f",u"g":"g",u"h":"h",u"ī":"ie",u"î":"i",
                 u"j":"j",u"ʒ":"zh",u"k":"k",u"l":"l",u"m":"m",u"n":"n",
                 u"ñ":"ny",u"ō":"oh",u"ô":"o",u"ó":"oo",u"p":"p",u"r":"r",
                 u"ᵲ":"rr",u"s":"s",u"t":"t",u"ū":"oo",u"û":"u",u"v":"v",
                 u"w":"w",u"y":"y",u"z":"z",u"ʧ":"ch",u"ʃ":"sh",u"θ":"th",
                 u"ᵲ":"rr",u"s":"s",u"t":"t",u"ū":"oo",u"û":"u",u"v":"v",
                 u"ð":"vth",u"ʊ":"uh"}
MIDDLESUBS={u"":u"bl",u"▀":u"fl",u"▁":u"dl",u"▂":u"gl",u"▃":u"pl",u"▄":u"ʃl",
         u"▅":u"sl",u"▇":u"kl",u"█":u"br",u"▉":u"fr",u"▊":u"θr",u"▋":u"gr",
          u"▌":u"pr",u"▍":u"tr",u"▎":"dw",u"▏":"gw",u"▐":"tw",u"▓":u"ʃw",
          u"▔":u"θw", u"▕":"sw"}
VCSUBS={u"▙":u"ûrp", u"▛":u"ûrb",u"⛄":u"ûmp", u"〶":u"ód☃l"}
ENDSUBS={u"▗":u"☃rt", u"▘":u"☃r",u"⛄":u"ûmp", u"〶":u"ód☃l"}

VOWELS=u"óûôēō"
CONS=u"bmfdgwptʃθshrjklnz"  # 26


def to_tubbish(asdf="asd"):
    global VOWELS
    global CONS
    global SUBS
    vcount=random.randint(1,25)
    if vcount<=7:
        word=random.choice(u"〶⛄▗▘▛óēō")
        vcount=True
    else:
        word=random.choice(CONS)
        vcount=False
    length=random.randint(1,100)
    p=[5, 30, 50, 80, 90, 100]
    for x in range(6):
        if length<=p[x]:
            length=x+1
            break
    vcsub=False
    for x in range(length):
        if vcsub:
            vcsub=False
            vcount=not vcount
            continue
        if vcount:
            nl=random.randint(1,42)
            if nl<=4:
                vcsub=True
                word+=random.choice(VCSUBS.keys())
            else:
                word+=random.choice("".join(map(unicode, MIDDLESUBS))+CONS)
        else:

            word+=random.choice(VOWELS)
        vcount=not vcount
    word=word[::-1]
    part=""
    if random.randint(1, 100)<=15 and len(word)<=4:
        if word[0] in u"óûôēō":
            part=random.choice("".join(map(unicode, MIDDLESUBS))+CONS)+word
        else:
            part=random.choice("".join(map(unicode, MIDDLESUBS))+CONS)+word[1:]
    total=word+part
    output=""
    for let in total:
        if let in MIDDLESUBS:
            output+=MIDDLESUBS[let]
        elif let in VCSUBS:
            output+=VCSUBS[let]
        elif let in ENDSUBS:
            output+=ENDSUBS[let]
        else:
            output+=let
    return output
    


class Translation:
    def __init__(self):
        self.dictionary={}
        self.trans=open("Translation.txt", "r+")
        self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")
        self.readfromfile()



    
    def printword(self,word):
        """Exactly the same as getword, but prints the word instead of returning it."""
        print self.getword(word)
        
    def getword(self, word):
        """Translates one word into Galbraithanese."""
        if all(map(lambda x: x.isdigit(), list(word))) and word:
            return Numbers.galbraithanese_number(int(word))
        elif set(list(word))==set(['\x98', '\x83', '\xe2']):
            return word
        elif word=="love":
            return random.choice(["óstīðōyó", "ᵲōsnôfôbr", "lēvēy", "jūkwôbr"])
        elif word=="loved":
            return random.choice(["óstīðōyóēnē", "ᵲōsnôfôbrēnē", "lēvēyēnē", "jūkwôbrēnē"])
        elif word=="loving":
            return random.choice(["óstīðōyóîgē", "ᵲōsnôfôbrîgē", "lēvēyîgē", "jūkwôbrîgē"])
        elif word in self.dictionary:
            return self.dictionary[word]
        elif word[:-2] in self.dictionary and word[-2:]=="ly":
            return self.dictionary[word[:-2]]+"əʃ"
        elif word[:-3]+"y" in self.dictionary and word[-2:]=="ily":
            return self.dictionary[word[:-3]+y]+"əʃ"
        elif word[:-3] in self.dictionary and word[-3:]=="ing":
            return self.dictionary[word[:-3]]+"îgē"
        elif word[:-3]+"e" in self.dictionary and word[-3:]=="ing":
            return self.dictionary[word[:-3]+"e"]+"îgē"
        elif word[:-2] in self.dictionary and word[-2:]=="ed":
            return self.dictionary[word[:-2]]+"ēnē"
        elif word[:-1] in self.dictionary and word[-1]=="d":
            return self.dictionary[word[:-1]]+"ēnē"
        elif word[:-1] in self.dictionary and word[-1]=="s":
            return self.dictionary[word[:-1]]+"glôb"
        elif word[:-2] in self.dictionary and word[-2:]=="es":
            return self.dictionary[word[:-2]]+"glôb"
        else:
            return "?"*len(word)

    def readfromdoc(self):
        """Forces the program to read off of the online translation."""
        self.dictionary={}
        for word in self.trans2.read().split():
            try:
                self.dictionary[word.split("-")[0]]=word.split("-")[1]
            except:
                pass
        self.trans2.close()
        self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")

    def readfromfile(self):
        """Forces the program to read off of your translation file."""
        self.dictionary={}
        for word in self.trans.read().split():
            try:
                self.dictionary[word.split("-")[0]]=word.split("-")[1]
            except:
                pass
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
    
    def addword(self,word):
        """Adds a single english word to the dictionary and its translation is randomly chosen through to_tubbish."""
        self.dictionary[word]=to_tubbish(word)

    def removeword(self,word):
        """Removes a single word from the dictionary, the input word must be in english."""
        self.dictionary.pop(word)

    def restart(self):
        """Completely restarts and saves the translation file.  Every thing will be changed.  Also makes sure there are no homonyms.  ASK CHASE BEFORE USING!!"""
        self.trans.truncate(0)
        self.dictionary={}
        words=open("/usr/share/dict/words")
        for word in list(set(words.read().lower().split("\n"))):
            translation=to_tubbish()
            while translation in self.dictionary.values():
                translation=to_tubbish()
            self.trans.write((word+"-"+translation+"\n").encode('utf8'))
            self.dictionary[word]=translation
            if len(list(self.dictionary))%1000==0:
                print str(len(list(self.dictionary)))+"/"+str(len(open("/usr/share/dict/words").readlines()))
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
        self.words=open("/usr/share/dict/words")

    def save(self):
        """Saves the current dictionary to the translation file."""
        self.trans=open("Translation.txt", "r+")
        self.trans.truncate(0)
        for word in self.dictionary:
            written=word+u"-"+self.dictionary[word.encode('utf-8')]+u"\n"
            self.trans.write(written.encode('utf-8'))
        self.trans.write(text)
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
        
    def gettranslation(self, word):
        """Translates a single galbraithanese word into english."""
        try:
            return str(Numbers.from_galbraithanese(word))
        except:
            pass
        if word in ["óstīðōyó", "ᵲōsnôfôbr", "lēvēy", "jūkwôbr"]:
            return "love"
        elif word in ["óstīðōyóēnē", "ᵲōsnôfôbrēnē", "lēvēyēnē", "jūkwôbrēnē"]:
            return "loved"
        elif word in ["óstīðōyóîgē", "ᵲōsnôfôbrîgē", "lēvēyîgē", "jūkwôbrîgē"]:
            return "loving"
        else:
            for eng in self.dictionary:
                if self.dictionary[eng]==word:
                    return eng
                elif self.dictionary[eng]==word[:-5] and word[-5:]=="ēnē":
                    if eng[-1]=="e":
                        return eng+"d"
                    return eng+"ed"
                elif self.dictionary[eng]==word[:-5] and word[-5:]=="îgē":
                    if eng[-1]=="e":
                        return eng[:-1]+"ing"
                    return eng+"ing"
                elif self.dictionary[eng]==word[:-4] and word[-4:]=="əʃ":
                    if eng[-1]=="y":
                        return eng[:-1]+"ily"
                    return eng+"ly"
                elif self.dictionary[eng]==word[:-5] and word[-5:]=="glôb":
                    if eng[-1]=="s":
                        return eng[:-1]+"es"
                    return eng+"s"
            return "?"*len(word)


    def fulltranslate(self, sentence):
        """Fully and correctly translates an english word into galbraithanese.  Warning:  Incomplete."""
        def trymost(word):
            try:
                return gettranslation(word)
            except:
                return False
        def trynoun(word):
            if word[-3:]=="ób":
                case="nom"
                word=word[:-3]
            elif word[-5:]=="îgē":
                case="gen"
                word=word[:-5]
            elif word[-5:]=="ûbē":
                case="dat"
                word=word[:-5]
            elif word[-5:]=="ōbō":
                case="acc"
                word=word[:-5]
            elif word[-5:]=="óló":
                case="abl"
                word=word[:-5]
            else:
                return False
            if word[-4:]=="nôb":
                num="non"
                word=word[:-4]
            elif word[-5:]=="trôb":
                num="sin"
                word=word[:-5]
            elif word[-5:]=="flôb":
                num="bil"
                word=word[:-5]
            elif word[-5:]=="glôb":
                num="plu"
                word=word[:-5]
            else:
                return False
            prefix=""
            suffix=""
            try:
                if case=="gen":
                    prefix="of the "
                if num in ["non", "bil", "plu"]:
                    suffix="s"
                return prefix+self.gettranslation(word)+suffix
            except:
                return False
        def tryadjective(word):
            if word[-4:]=="əʃ":
                return tryadjective(word[:-4])+"ly"
            try:
                return self.gettranslation(word)
            except:
                return False
        def tryadverb(word):
            if word[-4:]=="óθ":
                return trynoun(word[:-4])+"ful"
            try:
                return self.gettranslation(word)
            except:
                return False
        def tryverb(word):
            if word[-3:]=="ôk":
                try:
                    return "y'all need to "+self.gettranslation(word) if word[-6:]=="īpôk" else "you need to "+self.gettranslation(word)
                except:
                    return False
            if word[-2:]=="ó":
                try:
                    return "to "+self.gettranslation(word)
                except:
                    return False
            pro=False
            if word[-5:]=="îgē":
                pro=True
                word=word[:-5]
            if word[-5:]=="ēnē":
                tense="pas"
                word=word[:-5]
            elif word[-3:]=="ûb":
                tense="pre"
                word=word[:-3]
            elif word[-4:]=="ûgl":
                tense="fut"
                word=word[:-4]
            else:
                return False
            plu=False
            if word[-3:]=="īp":
                plu=True
                word=word[:-3]
            if word[-6:]=="ópóp":
                person=1
                word=word[:-6]
            elif word[-6:]=="ôbēb":
                person=2
                word=word[:-6]
            elif word[-3:]=="óf":
                person=3
                word=word[:-3]
            else:
                person=4
            perstr=[None, "we", "y'all", "they", "everyone"][person] if plu else [None, "I", "you", "they", "anyone"][person]
            try:
                ver=self.gettranslation(word)
            except:
                pass
            
                
            
            
    
    def custom_trans(self, word, trans):
        """Adds one english word to the dictionary with its specific galbraithanese translation."""
        self.dictionary[word]=trans

    def getsentencetranslation(self,sentence):
        """Translates a large chunk of galbraithanese into english."""
        newsentence=""
        for letter in sentence.lower():
            if letter not in ",?.!:;":
                newsentence+=letter
        output=[]
        for word in newsentence.split():
            output.append(self.gettranslation(word))
        return self.keeppunct(sentence, " ".join(output))

    def printsentence(self,sentence):
        """Exactly the same as getsentence but prints the output."""
        print self.getsentence(sentence)

    def getsentence(self,sentence):
        """Translates a large chunk of english into galbraithanese."""
        newsentence=""
        sentence=sentence.replace("unicode snowman", "☃")
        sentence=sentence.replace("unicode snowmen", "☃☃☃")
        for letter in sentence.lower():
            if letter not in ",?.!:;":
                newsentence+=letter
        output=[]
        for word in newsentence.split():
            output.append(self.getword(word))
        try:
            return self.keeppunct(sentence, " ".join(output))
        except:
            return " ".join(output)

    def keeppunct(self, old, new):
        """Keeps puncutation of a translated string.  Not really useful to use alone.  Is used in code."""
        punctdictionary={}
        oldspl=old.split()
        for x in range(len(oldspl)):
            if oldspl[x][-1] in ",?.!:;":
                punctdictionary[x]=oldspl[x][-1]
        newspl=new.split()
        for index in punctdictionary:
            newspl[index]+=punctdictionary[index]
        return " ".join(newspl)

    def getpronounciation(self, word):
        """Gives you the pronouciation of a sentence."""
        global VOWELS
        global CONS
        global PROUNOUNCIATION
        global SUBS
        try:
            if not any(map(lambda x: x=="?", list(self.getsentence(word)))):
                word=self.getsentence(word)
        except:
            pass
        word=unicode(word, 'utf-8')
        for item in SUBS:
            word=word.replace(SUBS[item], item)
        newword=u""
        for char in word:
            if char in VOWELS:
                newword+=PROUNOUNCIATION[char]+"-"
            elif char in CONS:
                newword+=PROUNOUNCIATION[char]
            else:
                newword+=char
        for item in SUBS:
            newword=newword.replace(item, SUBS[item])
        for char in " !?-.,\n\t\"\'(){}[]/":
            newword=newword.replace("-"+char, char)
        if newword[-1]==u"-":
            newword=newword[:-1]
        newword=" ".join(map(lambda x: x[::-1].replace("-", "", 1)[::-1],newword.split()))
        return newword

    def fullsentence(self, sentence):
        """Fully translates a sentence by asking a lot of questions.  Warning:  Not thoroughly tested."""
        def askquestion(question, answers):
            newanswers=""
            for x in range(len(answers)):
                newanswers+="\t"+str(x+1)+". "+answers[x]+"\n"
            x="asdf"
            while x not in map(lambda x: str(x+1), range(len(answers))):
                if x!="asdf":
                    print "Invalid answer"
                x=raw_input(question+"\n"+newanswers)
            return int(x)
            
        newsentence=""
        for letter in sentence.lower():
            if letter not in ",?.!:;":
                newsentence+=letter
        output=[]
        pro=""
        lastisto=False
        for word in newsentence.split():
            if word=="to":
                lastisto=True
                continue
            x=askquestion("The word \""+word+"\" is:", ["An article", "A noun", "An adjective", "A verb", "An adverb", "A conjunction", "A preposition", "An interjection", "A pronoun"])
            if x==1:  #Article
                pass   #Do nothing
            elif x==2:  #Noun
                x=askquestion("There are/is ___ of this noun (\""+word+"\"):", ["None", "One", "Two", "None of the above"])
                if x==1:  #Nonullar
                    number="nôb"
                elif x==2:  #Singular
                    number="trôb"
                elif x==3:  #Bilar
                    number="flôb"
                elif x==4:  #Plural
                    number="glôb"
                x=askquestion("The noun (\""+word+"\") is in the ___ case:", ["Nominative", "Genitive", "Dative", "Accusitive", "Ablative"])
                if x==1:  #Nom
                    case="ób"
                elif x==2:  #Gen
                    case="îgē"
                elif x==3:  #Dat
                    case="ûbē"
                elif x==4:  #Acc
                    case="ōbō"
                elif x==5:  #Abl
                    case="óló"
                works=False
                while not works:
                    x=raw_input("Please enter a simple form of the noun \""+word+"\" (ex. of the cats -> cat)")
                    try:
                        output.append(self.getword(x)+number+case)
                        works=True
                    except:
                        print "Even simpler"
            elif x==3:  #Adjective
                x=askquestion("Is the adjective \""+word+"\" formed from a noun?", ["Yes", "No"])
                if x==1:
                    works=False
                    while not works:
                        x=raw_input("Please enter a simple form of the noun that makes up the adjective \""+word+"\" (ex. windy -> wind)")
                        try:
                            output.append(self.getword(x)+"óθ")
                            works=True
                        except:
                            print "Even simpler"
                else:
                    output.append(self.getword(x))
            elif x==4:  #Verb
                isinf=False
                if lastisto:
                    x=askquestion("Is \"to "+word+"\" a full infinitive/to-infinitive?", ["Yes", "No"])
                    if x==1:
                        works=False
                        while not works:
                            x=raw_input("Please enter a simple form of the infinitive \""+word+"\" (ex. to run -> run)")
                            try:
                                isinf=True
                                output.append(self.getword(x)+"ó")
                                works=True
                            except:
                                print "Even simpler"
                    elif x==2:
                        output.append("to")
                isimp=True
                if not isinf:
                    x=askquestion("Is the verb \""+pro+word+"\" imperative?", ["Yes", "No"])
                    if x==1:
                        plural=["","","īp"][askquestion("Is the imperative verb \""+pro+word+"\" plural?", ["Yes", "No"])]
                        works=False
                        while not works:
                            x=raw_input("Please enter a simple form of the imperative \""+pro+word+"\" (ex. All of you, run! -> run)")
                            try:
                                output.append(self.getword(x)+plural+"ôk")
                                works=True
                            except:
                                print "Even simpler"
                    elif x==2:
                        isimp=False
                if not isimp and not isinf:
                    person=["","ópóp","ôbēb","óf"][askquestion("What person is the verb \""+pro+word+"\" in?", ["1st", "2nd", "3rd"])]
                    plural=["","īp",""][askquestion("Is the verb \""+pro+word+"\" plural?", ["Yes", "No"])]
                    tense=["","ēnē","ûb","ûgl"][askquestion("What tense is the verb \""+pro+word+"\" in?", ["Past", "Present", "Future"])]
                    progress=["","îgē",""][askquestion("Is the verb \""+pro+word+"\" progressive?", ["Yes", "No"])]
                    works=False
                    while not works:
                        x=raw_input("Please enter a simple form of the verb \""+pro+word+"\" (ex. I was running -> run)")
                        try:
                            output.append(self.getword(x)+person+plural+tense+progress)
                            works=True
                        except:
                            print "Even simpler"
                pro=""
            elif x==5:  #Adverb
                x=askquestion("Is the adverb \""+word+"\" an adjective with -ly or something added at the end?", ["Yes", "No"])
                if x==1:
                    works=False
                    while not works:
                        x=raw_input("Please enter a simple form of the adjective that makes up the adverb \""+word+"\" (ex. quickly -> quick)")
                        try:
                            output.append(self.getword(x)+"əʃ")
                            works=True
                        except:
                            print "Even simpler"
                else:
                    output.append(self.getword(word))
            elif x==6: #Conjunction
                output.append(self.getword(word))
            elif x==7: #Preposition
                output.append(self.getword(word))
            elif x==8: #Interjection
                output.append(self.getword(word))
            elif x==9: #Pronoun
                pro=word+" "
                continue
            if pro:
                output.insert(len(output)-1, pro[:-1])
                pro=""
            if lastisto:
                output.insert(len(output)-1, self.getword("to"))
        return " ".join(output)

    def rhyme(self, word, upto=3):
        """Gets all rhymes of a word.  Warning:  Each word has a lot of rhymes so this code might overload your idle interpreter."""
        if word in self.dictionary: word=self.getword(word)
        upto=min(len(word.decode('utf-8', 'ignore')), upto)
        return filter(lambda x: x.decode('utf-8', 'ignore')[-upto:]==word.decode('utf-8', 'ignore')[-upto:] and x!=word, self.dictionary.values())

    def printrhyme(self, word, upto=3):
        """Exactly the same as rhyme, but prints the words."""
        y=self.getword(word) if word in self.dictionary else word
        print y+"\n------------\n"+"\n".join(self.rhyme(word, upto))

    def pronouncerhymes(self, word, upto=3):
        """Exactly the same as printrhyme, but prints pronounciation of the rhyme."""
        y=self.getword(word) if word in self.dictionary else word
        print self.getpronounciation(y)+"\n------------\n"+"\n".join(map(self.getpronounciation, self.rhyme(word, upto)))              

    def englishrhyme(self, word, upto=3):
        """Same as rhyme, except translates to english"""
        return map(self.gettranslation, self.rhyme(word, upto))

    def printenglishrhyme(self, word, upto=3):
        """Exactly the same as englishrhyme, but prints the words."""
        y=word if word in self.dictionary else self.gettranslation(word)
        print y+"\n------------\n"+"\n".join(self.englishrhyme(word, upto))
    


r="gâlbrāθənēz"
x=Translation()
tr="dətês vîᵲâr, jôʒóñ dûzūm prīfrēg ēgʊkʊ? sótəy ðūplēpr tēwōsm tôpləbr ksūʒūsl wêplîd lūzôgāg. grēskōt ʊdîkrū trôhîθōsnîh hāslākw bróʃîzīkl ksūʒūsl hāslākw yʊglūgēʃîgē klāʃódâʃūr. tûñâfr âwâzōbī, grēskōt ʊdîkrū kwəsnīblîr hêyôklāy ñīnâg Gâlbrāθənēz."
print "Done"

