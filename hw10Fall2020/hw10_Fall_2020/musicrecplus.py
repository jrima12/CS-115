'''
Jonathan Amir
I pledge my honor that I have abided by the Stevens Honor System
'''

import os.path

menu = \
'''Enter a letter to choose an option: 
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit\n'''

def LoadDict(file):
    '''Creates a dictionary from the text file storing the user profiles'''
    D = {}
    userFile = open(file, 'r')
    for user in userFile:
        if not user:
            break
        else:
            [username, artists] = user.strip().split(":")
            listartists = artists.split(",")
            listartists.sort()
            D[username] = listartists
    userFile.close()
    return D

def EnterPreferences(username, Dict):
    '''Takes the input of the artits that a user likes and adds it to the dictionary'''
    artistList = []
    while True:
        artist = input("Enter an artist that you like (Enter to finish): ").title()
        if artist == "":
            break
        artistList.append(artist)
    artistList.sort()
    Dict[username] = artistList

def findBestMatch(username, Dict):
    '''Finds which user has the most similar artists as another user (without it being a subset)'''
    users = Dict.keys()
    def matches(l1, l2):
        '''A helper function which matches how many artists are the same in 2 lists'''
        l1.sort()
        l2.sort()
        num = 0
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    num += 1
        return num
    bestMatch = 0
    for u in users:
        match = matches(Dict[u], Dict[username])
        if match > bestMatch and (match != len(Dict[username]) or match != len(Dict[u])) and u != username and u[-1] != "$":
            bestMatch = match
            bestUser = u
    return bestUser

def recommendation(l1, l2):
    '''will filter out the artists that are the same in the two list inputs and output the different artists'''
    recArtists= []
    antirecArtists= []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                antirecArtists.append(l1[i])
    for element in antirecArtists:
        l1.remove(element)
    for e in l1:
        print(e)
        
def GetRecommendations(username, Dict):
    '''calls 2 other finctions to print out recommended artists based off similar user profiles'''
    bestMatch = findBestMatch(username, Dict)
    if bestMatch:
        return recommendation(Dict[bestMatch], Dict[username])
    else:
        return "No recommendations available at this time"

def MostPopularArtist(username, Dict):
    '''determines which artist the most amount of people like'''
    artistsPop = {}
    artistlist = []
    Poplist = []
    users = Dict.keys()
    for u in users:
        for artist in Dict[u]:
            if artist not in artistlist:
                artistlist.append(artist)
    for a in artistlist:
        artistsPop[a] = 0
    for u in users:
        for a in artistlist:
            if a in Dict[u] and u[-1] != "$":
                artistsPop[a] += 1
    for i in artistsPop.values():
        Poplist.append(i)
    Poplist.sort(reverse = True)
    if not Poplist:
        return "Sorry, no artists found"
    def helper(val):
        '''A helper function to get the key pair from the value of the most liked artist'''
        for key, value in artistsPop.items():
            if val == value:
                return key
    print(helper(Poplist[0]))
    print(helper(Poplist[1]))
    print(helper(Poplist[2]))
            

def HowPopular(username, Dict):
    '''returns the number of people who follow the most liked artist'''
    def helper (username, Dict):
        '''a helper function to calculate the number of people following the most liked artist'''
        artistsPop = {}
        artistlist = []
        Poplist = []
        users = Dict.keys()
        for u in users:
            for artist in Dict[u]:
                if artist not in artistlist:
                    artistlist.append(artist)
        for a in artistlist:
            artistsPop[a] = 0
        for u in users:
            for a in artistlist:
                if a in Dict[u] and u[-1] != "$":
                    artistsPop[a] += 1
        for i in artistsPop.values():
            Poplist.append(i)
        Poplist.sort(reverse = True)
        if not Poplist:
            return "Sorry, no artists found"
        print(Poplist[0])
    return helper(username,Dict)
        

def UserLikesMost(username, Dict):
    '''returns the user that follows the most amount of artists'''
    users = Dict.keys()
    numartlist = []
    userlist = []
    for u in users:
        numart = 0
        if u[-1] != "$":
            for artist in Dict[u]:
                numart += 1
            numartlist.append(numart)
            userlist.append(u)
    usernum = numartlist.index(max(numartlist))
    print(userlist[usernum])

def saveQuit(Dict, file):
    '''updates the textfile to contain the new information from the dictionary'''
    f = open(file, "w")
    for user in Dict:
        save = str(user)+":"+",".join(Dict[user])+"\n"
        f.write(save)
    f.close()


#THE MAIN CODE STARTS HERE:
    
if not os.path.isfile('musicrecplus.txt'):
    Userfile = open('musicrecplus.txt','w')
    Userfile.close()
UserDict = LoadDict('musicrecplus.txt')
username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
if username not in UserDict:
    EnterPreferences(username, UserDict)
while True:
    option = input(menu)
    if option == "e":
        EnterPreferences(username, UserDict)
    elif option == "r":
        GetRecommendations(username, UserDict)
    elif option == "p":
        MostPopularArtist(username, UserDict)
    elif option == "h":
        HowPopular(username, UserDict)
    elif option == "m":
        UserLikesMost(username, UserDict)
    elif option == "q":
        saveQuit(UserDict, 'musicrecplus.txt')
        break
    else:
        print("try another input")
