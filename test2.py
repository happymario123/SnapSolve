from flask import Flask, render_template, request, flash, redirect
from flask_cors import CORS
from werkzeug import secure_filename
app = Flask(__name__)
from gettext import * #getTextFromImage
#from gettext import checkOutputExist
#from gettext import googleSearchURL
#from gettext import googSearchResults


import ssl

ssl._create_default_https_context = ssl._create_unverified_context



@app.route('/')
def upload_f():
   return render_template('index.html', message="Hello!")
    
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      getTextFromImage('suplise.txt', f.filename)

      text = "test"
      #with open('suplise.txt') as f:
#        pass
      result = checkOutputExist('suplise.txt') + 'yahoo'
      def googleSearchURL(keyword):
            search_results_list = []
            for url in search(keyword, stop=10):
                search_results_list.append(url)
            return search_results_list
      Search_list = googleSearchURL(result)
      try:
            questions_enm = [['Two long straight wires carrying the same current I and separated by a distance r exert a force F on each other. The current is increased to 4I and the separation is reduced to r/6 . What will be the force between two wires?', '96 X F_old'],
            ['Two long straight wires carrying the same current 15 A  exert a force of 0.001 N per unit length on each other. What is the distance between the wires?', '4.5cm'], ['The magnetic field strength at a distance of 5 cm from a thin, straight wire is 0.00005 T. What is the current in the wire?', '12.5A']] #Databse of questions based on concepts. Didn't have time to fully implement the website crawling for questions based on subjects
            str_question = 'Question:  ' +questions_enm[0][0] + '\n Solution:  ' + questions_enm[0][1]
            str_present_keywords = ''
            for a in list_present_keywords:
                if a in str_present_keywords:
                    pass
                else:
                    str_present_keywords += a
            #print(str_present_keywords)
            final_message = ''
            for a in range(len(Search_list)):
                if 'chegg' in Search_list[a]:
                      pass
                else:
                      #print(links[a])
                      r = requests.get(Search_list[a], verify=False)
                      soup = BeautifulSoup(r.content, 'html.parser')
                      _div = mobiles = soup.findAll("div", {"class": "AnswersList__listWrap___2D8-6"})
                      results = [[i.text for i in b.find_all('li')] for b in _div[0].find_all('ul')]
                      #print('Link', a+1, '\n')
                      a = results[0][0].split('Favorite Answer') #Removes start useless stuff
                      a = a[1].split('Login') #Removes end useless stuff
                      a = a[0].split('Report') #Removes more end useless stuff
                      a = a[0].split('These')
                      final_message += a[0]
      except Exception as a:
              print(a)
      return render_template('index.html', message1=final_message, message2=checkOutputExist('suplise.txt'), message3 = str_present_keywords, message4 = str_question)


if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug = True)


#    outfile = '/Users/evanzhang/Marihacks/out_file.txt'
#    #picName = 'download.png'
#    picName = upload_file() #'/Users/evanzhang/Marihacks/TestImagePhysics.jpg'
#    #a = getTextFromImage (outfile, picName)
#    #print(a)
#    #result = checkOutputExist(outfile)
#    result = picName
#    result += ' yahoo'
#    #print(result)
#
#    #if not result :
#    #    print ("extract nothing")
#    #else:
#    #    print ("the extract result : ", result)
#
#    Search_list = googleSearchURL(result)
#    links = Search_list
#    try:
#            for a in range(len(links)):
#                    #print(links[a])
#                    r = requests.get(links[a])
#                    soup = BeautifulSoup(r.content, 'html.parser')
#                    _div = mobiles = soup.findAll("div", {"class": "AnswersList__listWrap___2D8-6"})
#                    results = [[i.text for i in b.find_all('li')] for b in _div[0].find_all('ul')]
#                    print('Link', a+1, '\n')
#                    a = results[0][0].split('Favorite Answer') #Removes start useless stuff
#                    a = a[1].split('Login') #Removes end useless stuff
#                    a = a[0].split('Report') #Removes more end useless stuff
#                    print (a[0], '\n')
#    except Exception as a:
#            print(a)
            

    #googleSearchResults(result)
    #webbrowser.open("https://google.com/search?q=%s" % result)  
