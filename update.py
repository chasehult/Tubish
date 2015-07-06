try:
    trans=open("Translation.txt", "r+")
except:
    trans=open("Translation.txt", "w+")
try:
    tubbish=open("Tubbish_word.py", "r+")
except:
    tubbish=open("Tubbish_word.py", "w+")
try:
    this=open("update.py", "r+")
except:
    this=open("update.py", "w+")
import urllib, urllib2
print "Updating"
def update():
    global tubbish, trans, this
    
    
    try:
        x=open("ignore.txt")
        print "Hello, Chase"
    except:
        pass
    try:
        tubbish2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/Tubbish_word.py")
        trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/Translation.txt")
        this2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/update.py")
    except:
        print "Can not connect to internet."
        return False
    if tubbish.read()!=tubbish2.read():
        x=raw_input("Your Tubbish_word.py is not up to date!\nWould you like to update? (y/n)\n")
        if x=="y":
            tubbish.close()
            tubbish2.close()
            tubbish=open("Tubbish_word.py", "r+")
            tubbish2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/Tubbish_word.py")
            tubbish.truncate(0)
            text=tubbish2.read().decode('utf-8')
            tubbish.write(text.encode('utf-8'))
            tubbish.close()
            tubbish2.close()
    if trans.read()!=trans2.read():
        x=raw_input("Your Translation.txt is not up to date!\nWould you like to update? (y/n)\n")
        if x=="y":
            trans.close()
            trans2.close()
            trans=open("Translation.txt", "r+")
            trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/Translation.txt")
            trans.truncate(0)
            text=trans2.read().decode('utf-8')
            trans.write(text.encode('utf-8'))
            trans.close()
            trans2.close()
    if this.read()!=this2.read():
        x=raw_input("Your update.py is not up to date!\nWould you like to update? (y/n)\n")
        if x=="y":
            this.close()
            this2.close()
            this=open("update.py", "r+")
            this2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/update.py")
            this.truncate(0)
            text=this2.read().decode('utf-8')
            this.write(text.encode('utf-8'))
            this.close()
            this2.close()
    return True
print update()
print "Done updating"

        
