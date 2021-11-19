import os
import webbrowser
import random
import time

def intro():
    print "welcome!"
    name = raw_input('what is your name ')
    print 'hello', name, "how are you doing today"
    answer = raw_input ('')
    print 'i hope the rest of your day will be amazing'
    return(name)

def security(choice,name):
    if choice.lower() == 'y':
        answer = raw_input("please enter your password ")
        check = open(name + '.txt',"r")
        if check.mode == "r":
            contents = check.read()
            if contents == answer:
                access = True
            else:
                access = False
    else:
        answer = raw_input("please create a password ")
        password = open(name + '.txt', "w")
        password.write(answer)
        access = True

    return (access)

def menu(num):
    print 'press the number of the option that you want to use'
    print
    print"what would you like to do today"
    print '1.work on files'
    print '2 play games'

    if num == '0':
        choice = raw_input('')
    else:
        choice = num
    if choice =='1':
        files()
    if choice == '2':
        game()

def files():
    print 'type the path to the folder that you would like to work on'
    path = raw_input('')
    path1 = path
    files = Files(path)
    menus = files.menu()
    if menus == '1':
        print 'what would you like to name your file'
        name = raw_input('')
        path = path1 + '/' + name +'.txt'
        files.create(path)
        print 'do you still want to work on files(y/n)'
        end = raw_input ('')
        if end.lower() == 'y':
            menu('1')
        else:
            print 'do you want to go to the main menu(y/n)'
            main = raw_input ('')
            if main.lower() =='y':
                menu('0')
            else:
                return()

    elif menus == '2':
        print 'what is the name of the file you would like to delete'
        name = raw_input('')
        path = path1 + '/' + name
        files.delete(path)
        print 'do you still want to work on files(y/n)'
        end = raw_input ('')
        if end.lower() == 'y':
            menu('1')
        else:
            print 'do you want to go to the main menu(y/n)'
            main = raw_input ('')
            if main.lower() =='y':
                menu('0')
            else:
                return()


    elif menus =='3':
        print 'what is the name of the file you would like to read'
        name = raw_input('')
        path = path1 + '/' + name
        files.read(path)
        print 'do you still want to work on files(y/n)'
        end = raw_input ('')
        if end.lower() == 'y':
            menu('1')
        else:
            print 'do you want to go to the main menu(y/n)'
            main = raw_input ('')
            if main.lower() =='y':
                menu('0')
            elif main.lower() =='n':
                return()


class Files:
    def __init__(self, path):
        self.path = path

    def menu(self):
        print 'press the number of the option that you want to use'
        print
        print"what would you like to do today"
        print '1.create a text file'
        print '2.delete a file'
        print '3.read a file'
        choice = raw_input('')
        return(choice)

    def create(self, path):
        print 'what would you like to write in the file'
        content = raw_input('')
        f = open(path, 'w')
        f.write(content)

    def delete(self, path):
        os.remove(path)

    def read(self, path):
        f = open(path, 'r')
        copy = f.read()
        print copy

def game():
    if gamemenu() == '1':
        word = raw_input('please enter a word ')
        game = hangman(word)
        gamenum = 0
        wordnum = 1
        while game.terminate(word):
            game.display(gamenum)
            game.worddisplay(wordnum,word)
            game.guess(word)
            game.terminate(word)
            if game.guess(word)[0] == 0:
                gamenum += 1
            else:
                if wordnum <= 2:
                    wordnum +=1
        return()



def gamemenu():
        print 'press the number of the option you wuld like to choose'
        print
        print 'what would you like to play today'
        print '1.hangman'
        choice = raw_input ('')
        return (choice)

class hangman:
    def __init__(self, word):
        lists = []
        self.lists = lists

    def display(self,number):
        if number == 0:
            print
            print '   ___  '
            print '  |   | '
            print '  |   o '
            print '  |  /|\ '
            print '  |  / \ '
            print '__|__    '

        elif number == 1:
            print
            print '   ___  '
            print '  |   | '
            print '  |   o '
            print '  |  /|\ '
            print '  |    \ '
            print '__|__    '

        elif number == 2:
            print
            print '   ___  '
            print '  |   | '
            print '  |   o '
            print '  |  /|\ '
            print '  |     '
            print '__|__   '

        elif number == 3:
            print
            print '   ___  '
            print '  |   | '
            print '  |   o '
            print '  |   |\ '
            print '  |      '
            print '__|__   '

        elif number == 4:
            print
            print '   ___ '
            print '  |   |'
            print '  |   o '
            print '  |   | '
            print '  |    '
            print '__|__  '

        elif number == 5:
            print
            print '   ___ '
            print '  |   |'
            print '  |   o'
            print '  |    '
            print '  |    '
            print '__|__  '

    def worddisplay(self, number, word):
        if number == 1:
            for x in range (len(word)):
                self.lists.append('_')
                print self.lists[x],
        else:
            for x in range (len(self.lists)):
                print self.lists[x],

    def guess(self, word):
        answer = raw_input('please enter your guess')
        for x in range (len(word)):
            if answer == word[x]:
                self.lists[x] = answer
        return (self.lists)

    def terminate(self,word):
        count = 0
        for x in range (len(self.lists)):
            if self.lists[x] == word[x]:
                count = count + 1
        if count == len(word):
            print 'you win'
            return (False)
        else:
            return (True)










def main():
    count = 0
    name = intro()
    print 'do you have an existing account (y/n)'
    log = security(raw_input (''),name)
    if log == True:
        print "Congratulations", name, "you have successfully entered!"
        print "you are now a part of the secret society"
        menu('0')

    else:
        if count <= 5:
            security('y',name)
        else:
            print 'you have proved that you are not a member of the society'
            print 'this program must now self destruct in'
            i = 5
            while i >0:
                print i
                i = i - 1
            print 'now'
            replace = open("password.txt", "w")
            og = open("password program.py", "r")
            data = og.read()
            placement = replace.write(data)
            os.remove('/Users/humzahokadia/Documents/personalprograms/game.py')




main()
