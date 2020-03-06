import os
import subprocess
import webbrowser
from googlesearch import search
#from googlesearch.googlesearch import GoogleSearch
import requests
from bs4 import BeautifulSoup
#from test2 import upload_file
from Levenshtein import distance


import ssl

ssl._create_default_https_context = ssl._create_unverified_context


#cmd = "tesseract download.png stdout > out_file.txt"

def getTextFromImage (output, picName):
        cmd = 'tesseract ' + picName + ' stdout > ' + output # the sign > is to
                                                    #create and write a file
        os.system(cmd) #use operating system of the file
    
list_present_keywords = []
def checkOutputExist (outfile) :
    newStr = ''
    try:
        f = open(outfile, "r")
                # Do something with the file
#        print(f.readlines())
                
#               print("second test : ", f.read())
        for line in f:
            newStr = newStr + line.replace('\n',' ')
#            print("--- ", line)

    except IOError:
        print("File not accessible") # errors where the file is not
                                            #accessible because we want to
                                            #know it
    finally:
        f.close()
#        cmd = 'rm -f ' + outfile  #force to remove a file
#        os.system(cmd)

    listofwords = newStr.split()
#    print("NEWSTRING", newStr)
    count = 0
    keywords = enm = ['alternating current', 'battery', 'cell', 'circuit', 'circuit board', 'conduction', 'conductor', 'current', 'diode', 'direct current', 'electric discharge', 'direct current', 'electric discharge', 'electric force', 'electric', 'electric power', 'electrode', 'electrolyte', 'electromagnet', 'electromagnetic induction', 'electromagnetic wave', 'electromagnetism', 'generator', 'induction', 'insulator', 'integrated circuit', 'law of electric charges', 'load', 'magnet', 'magnetic field', 'magnetic force', "ohm's law", 'parallel circuit', 'poles', 'potential difference', 'resistance', 'semiconductor', 'series circuit', 'solenoid', 'static electricity', 'thermocouple', 'transformer', 'transistor', 'voltage', 'watt', 'electric potential', 'charge'] #Database of keywords. Would be interesting to implement through machine learning
    for a in listofwords: #listofwords needs to be a list
        lowest = 1000000 #Distance will always be smaller than this
        for item in keywords:
            d = distance(a, item) #Calculates distance from keyword and other thing
            if d < lowest:
                lowest_distance_word = item
                lowest = d
        if lowest < 3: #Only want to change if its very similar
            listofwords[count] = lowest_distance_word #replaces word
            lowest_distance_word = item #Starts implementing search in dictionary
            merriam_webster ='https://www.merriam-webster.com/dictionary/' + item
            mw = requests.get(merriam_webster)
            soup = BeautifulSoup(mw.content, 'html.parser')
            _div = mobiles = soup.findAll("div", {"class": "sense no-subnum"})
            results = [[i.text for i in a.find_all('span')] for a in _div[0].find_all('span')]
            global list_present_keywords
            list_present_keywords.append(item + results[0][0])
            newStr = ' '.join(listofwords)
            count +=1
    return newStr #Need to implement ways to make things not repeat, make words more oriented towards physics, etc.

def googleSearchURL(keyword):
    search_results_list = []
    for url in search(keyword, stop=10):
        #print(url)
        search_results_list.append(url)
    return search_results_list



def googSearchResults(query):
    response = GoogleSearch().search(query)
    for result in response.results:
        pass
#        #print("Title: " + result.title)
        #print("Content: " + result.getText())


outfile = '/Users/evanzhang/Marihacks/out_file.txt'
#picName = 'download.png'
picName = '/Users/evanzhang/Marihacks/TestImagePhysics.jpg'
a = getTextFromImage (outfile, picName)
#print(a)
result = checkOutputExist(outfile)
result += 'yahoo'
#print(result)

#if not result :
#    print ("extract nothing")
#else:
#    print ("the extract result : ", result)
    
Search_list = googleSearchURL(result)
#googleSearchResults(result)
#webbrowser.open("https://google.com/search?q=%s" % result)



links = Search_list
try:
        for a in range(len(links)):
                #print(links[a])
                r = requests.get(links[a])
                soup = BeautifulSoup(r.content, 'html.parser')
                _div = mobiles = soup.findAll("div", {"class": "AnswersList__listWrap___2D8-6"})
                results = [[i.text for i in b.find_all('li')] for b in _div[0].find_all('ul')]
#                print('Link', a+1, '\n')
                a = results[0][0].split('Favorite Answer') #Removes start useless stuff
                a = a[1].split('Login') #Removes end useless stuff
                a = a[0].split('Report') #Removes more end useless stuff
#                print (a[0], '\n')
except Exception as a:
        print(a)
        

