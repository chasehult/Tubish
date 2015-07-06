trans=open("Translation.txt", "r+")
tubbish=open("Tubbish_word.py", "r+")
update=open("update.py", "r+")
import urllib, urllib2
print "Updating"
def update():
    global tubbish, trans
    
    try:
        x=open("ignore.txt")
        print "Hello, Chase"
        return False
    except:
        pass
    try:
        tubbish2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/Tubbish_word.py")
        trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/Translation.txt")
        update2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/update.py")
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
            tubbish.write(tubbish2.read().encode('utf-8'))
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
            trans.write(trans2.read().encode('utf-8'))
            trans.close()
            trans2.close()
    if update.read()!=trans2.read():
        x=raw_input("Your update.py is not up to date!\nWould you like to update? (y/n)\n")
        if x=="y":
            update.close()
            update2.close()
            trans=open("update.py", "r+")
            update2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Tubish/master/update.py")
            update.truncate(0)
            update.write(update2.read().encode('utf-8'))
            update.close()
            update2.close()
    return True
update()
print "Done"

        
