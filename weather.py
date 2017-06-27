#  Graphics
from Tkinter import *
#  Import urllib2 for get file from "openweathermap.org"
import urllib2
import json
#  Parsing file "user.txt". File has 2 lines: city_id and api_key
user = open("user.txt", "r").read().split('\n')
city_id = user[0]
api_key = user[1]

#  Open url and download as json
url = "http://openweathermap.org/data/2.5/weather?id=" + city_id + "&appid=" + api_key
responce = urllib2.urlopen(url)
data = responce.read()

with open("data.json", "w") as f:
    f.seek(0)
    f.write(data)
    f.truncate()

#  Open Json file and get information from him
with open("data.json") as data_file:
    jdata = json.load(data_file)

#  Printing information about Weather
# print("Country: %s" % jdata["sys"]["country"])
# print("City: %s" % jdata["name"])
# print("t: %s" % jdata["main"]["temp"])
# print("\t%s\n\t%s" % (jdata["weather"][0]["main"],jdata["weather"][0]["description"]))

class Application(Frame):
    def createContent(self):
        self.country = Label(self)
        self.country["text"] = "Country: " + jdata["sys"]["country"]

        self.country.pack()

        self.city = Label(self)
        self.city["text"] = "City: " + jdata["name"]

        self.city.pack()


        self.temperature = Label(self)
        self.temperature["text"] = "Temperature: " + str(jdata["main"]["temp"])
        self.temperature["foreground"] = "blue"

        self.temperature.pack()


        self.info = Label(self)
        self.info["text"] = "Info: \n" + jdata["weather"][0]["main"] + "\n" + jdata["weather"][0]["description"]

        self.info.pack()


        self.CLOSE = Button(self)
        self.CLOSE["text"] = "Close"
        self.CLOSE["fg"] = "red"
        self.CLOSE["command"] = self.quit

        self.CLOSE.pack()







    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createContent()


if (__name__ == "__main__"):
    root = Tk()
    app = Application(master = root)
    app.mainloop()
    root.destroy()
