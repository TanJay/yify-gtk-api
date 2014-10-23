import json
import requests
import ttk
from Tkinter import *
import os
dic = {}


# label.config(text = "Taus")

def main(input):
    try:
#         search = raw_input("Please Enter name of movie : ")
        url = "https://yts.re/api/list.json?keywords=" + input
        # print(url)
        request = requests.get(url)
    #     print(request.content)
        decode = json.loads(request.content)
        # print json.dumps(decode, sort_keys=True, indent=4)
        amount = decode['MovieCount']
        title = decode['MovieList']
        label.config(text = "We Found " + str(amount) + " Movies on search " + str(input))
        print("We Found " + str(amount) + " Movies on search " + str(input))
        for til in title:
            dic[str(til['MovieTitle'])] = til['TorrentMagnetUrl']
            listb.insert(END, til['MovieTitle'])
            print("Title :" + til['MovieTitle'])
    except(KeyError):
        listb.insert(END, "Found no movies")
        print("No movies found")
    except(requests.exceptions.ConnectionError):
        listb.insert(END, "Check the Internet")
        print("Check Internet Connection")

def line():
    listb.delete(0, END)
    main(str(input1.get()))

def download():
    x = listb.curselection()
    b = str(x).replace(',', "").replace('(', "")
    c = str(b).replace(')', "")
    k = listb.get(c)
#     print(k)
    mag = dic[k]
#     print(mag)
    os.startfile(mag)

root = Tk()
listb = Listbox(root, width = 50)
listb.pack()
label = ttk.Label(root, text = "Hello")
label.pack()
input1 = ttk.Entry()
input1.pack()
button = ttk.Button(root, text = "Search")
# print(str(input1.get()))
button.pack()
button.config(command = line)
button2 = ttk.Button(root, text = "Download")
button2.pack()
button2.config(command = download)
root.mainloop()
