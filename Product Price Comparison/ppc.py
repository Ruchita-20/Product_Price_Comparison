
from tkinter import *
from PIL import ImageTk
from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
import webbrowser
from collections import defaultdict
import random

from matplotlib import pyplot as plt
import numpy as np

root = Tk()
root.geometry("1152x660")
root.resizable(0, 0)
root.title('Product Price Comparison')
bgImage = ImageTk.PhotoImage(file='bgf.png')

bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)
heading = Label(root, text='PRODUCT PRICE COMPARISON', font=('Georgia', 26, 'bold'), bg='#1d273b', fg='white')
heading.place(x=530, y=180)

srchimg = ImageTk.PhotoImage(file='srchf.png')
srchlabel = Label(root, image=srchimg, bg='#1d273b')
srchlabel.place(x=550, y=300)

sbtn = ImageTk.PhotoImage(file='sbf.png')
sbtnlabel = Label(root, image=sbtn, bg='#1d273b')
sbtnlabel.place(x=710, y=400)



class Price_compare:

    def __init__(self, master):
        super()
        self.var = StringVar()
        self.var_ebay = StringVar()
        self.var_flipkart = StringVar()
        self.var_amzn = StringVar()



        def user_enter(event):
            if entry.get()=='Search Product...':
                entry.delete(0,END)

        entry = Entry(master, textvariable=self.var,font=('Century',14),bg='white',fg='black',width=40,bd=0)
        entry.place(x=618,y=317)
        entry.insert(0,'Search Product...')
        entry.bind('<FocusIn>',user_enter)


        button_find = Button(master, text='Search',font=('Constantia',15,'bold'), bd=0,fg='black',bg='#f2f2f2'
                             ,activeforeground='black',activebackground='#f2f2f2',cursor='hand2', command=self.find)
        button_find.place(x=770,y=410)


    def find(self):

        self.x1 = float()
        self.x2 = float()
        self.product = self.var.get()
        self.product_arr = self.product.split()
        self.n = 1
        self.key = ""
        self.title_flip_var = StringVar()
        self.title_amzn_var = StringVar()
        self.variable_amzn = StringVar()
        self.variable_flip = StringVar()

        for word in self.product_arr:
            if self.n == 1:
                self.key = self.key + str(word)
                self.n += 1

            else:
                self.key = self.key + '+' + str(word)

        self.window = Toplevel(root)
        self.window.geometry('1150x720')
        self.window.resizable(0, 0)



        Bk = ImageTk.PhotoImage(file='2.jpg')
        Bklabel = Label(self.window, image=Bk)
        Bklabel.place(x=0, y=0)

        flpimg = ImageTk.PhotoImage(file='flipkartlogo.png')
        flplabel = Label(self.window, image=flpimg, bg='white')
        flplabel.place(x=40, y=160)

        amzimg = ImageTk.PhotoImage(file='amazonlogo.png')
        amzlabel = Label(self.window, image=amzimg, bg='white')
        amzlabel.place(x=420, y=170)

        sb1btn = ImageTk.PhotoImage(file='sh2.png')
        sb1label = Label(self.window, image=sb1btn, bg='white')
        sb1label.place(x=70, y=450)

        sb2btn = ImageTk.PhotoImage(file='sh2.png')
        sb2label = Label(self.window, image=sb2btn, bg='white')
        sb2label.place(x=480, y=450)

        srbtn = ImageTk.PhotoImage(file='sh1.png')
        srlabel = Label(self.window, image=srbtn, bg='white')
        srlabel.place(x=200, y=560)

        chartimg = ImageTk.PhotoImage(file='sh1.png')
        chartlabel = Label(self.window, image=chartimg, bg='white')
        chartlabel.place(x=400, y=560)

        Frame(self.window, width=4, height=400, bg='black').place(x=390, y=180)

        label_title_flip = Label(self.window, text='Product Name:',font=('Cambria',16,'bold'),bg='white',fg='black',bd=0)
        label_title_flip.place(x=100,y=250)

        label_flipkart = Label(self.window, text='Price (Rs):',font=('Cambria',16,'bold'),bg='white',fg='black',bd=0)
        label_flipkart.place(x=120,y=360)

        entry_flipkart = Entry(self.window, textvariable=self.var_flipkart,bg='white',fg='black',highlightthickness=0,font=('Cambria',12,'bold'))
        entry_flipkart.place(x=80,y=410)

        label_title_amzn = Label(self.window, text='Product Name:',font=('Cambria',16,'bold'),bg='white',fg='black',bd=0)
        label_title_amzn.place(x=500,y=250)

        label_amzn = Label(self.window, text='Price (Rs):',font=('Cambria',16,'bold'),bg='white',fg='black',bd=0)
        label_amzn.place(x=520,y=360)

        entry_amzn = Entry(self.window, textvariable=self.var_amzn,bg='white',fg='black',highlightthickness=0,font=('Cambria',12,'bold'))
        entry_amzn.place(x=480,y=410)

        self.price_flipkart(self.key)
        self.price_amzn(self.key)

        try:
            self.variable_amzn.set(self.matches_amzn[0])
        except:
            self.variable_amzn.set('Product not available')
        try:
            self.variable_flip.set(self.matches_flip[0])
        except:
            self.variable_flip.set('Product not available')

        option_amzn = OptionMenu(self.window, self.variable_amzn, *self.matches_amzn)
        option_amzn.config(bg='white',fg='black',highlightthickness=0,font=('Cambria',12,'bold'),activeforeground='black',activebackground='white')
        option_amzn.place(x=450,y=300)


        option_flip = OptionMenu(self.window, self.variable_flip, *self.matches_flip)
        option_flip.config(bg='white',fg='black',highlightthickness=0,font=('Cambria',12,'bold'),activeforeground='black',activebackground='white')
        option_flip.place(x=50,y=300)


        button_search = Button(self.window, text='Search', command=self.search,font=('Constantia',13,'bold'), bd=0,fg='black',bg='#65afb8'
                             ,activeforeground='black',activebackground='#65afb8',cursor='hand2')
        button_search.place(x=267, y=620)

        button_chart = Button(self.window, text='Ratings Chart', command=self.create_chart, font=('Constantia', 13, 'bold'), bd=0,
                               fg='black', bg='#65afb8'
                               , activeforeground='black', activebackground='#65afb8', cursor='hand2')
        button_chart.place(x=445, y=620)

        button_amzn_visit = Button(self.window, text='Visit Site', command=self.visit_amzn,font=('Constantia',10,'bold'), bd=0,fg='black',bg='#80b2b1'
                             ,activeforeground='black',activebackground='#80b2b1',cursor='hand2')
        button_amzn_visit.place(x=532, y=505)

        button_flip_visit = Button(self.window, text='Visit Site', command=self.visit_flip,font=('Constantia',10,'bold'), bd=0,fg='black',bg='#80b2b1'
                             ,activeforeground='black',activebackground='#80b2b1',cursor='hand2')
        button_flip_visit.place(x=123, y=505)

        self.window.mainloop()



    def price_flipkart(self, key):
        url_flip = 'https://www.flipkart.com/search?q=' + str(
            key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
        map = defaultdict(list)

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        source_code = requests.get(url_flip, headers=self.headers)
        soup = BeautifulSoup(source_code.text, "html.parser")
        self.opt_title_flip = StringVar()
        home = 'https://www.flipkart.com'
        for block in soup.find_all('div', {'class': '_2kHMtA'}):
            title, price, link, ratings = None, 'Currently Unavailable', None, None
            for heading in block.find_all('div', {'class': '_4rR01T'}):
                title = heading.text
            for p in block.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
                price = p.text[1:]
            for l in block.find_all('a', {'class': '_1fQZEK'}):
                link = home + l.get('href')
            for r in block.find_all('div', {'class': '_3LWZlK'}):
                ratings = r.text
            map[title] = [price, link,ratings]

        user_input = self.var.get().title()
        self.matches_flip = get_close_matches(user_input, map.keys(), 20, 0.1)
        self.looktable_flip = {}
        for title in self.matches_flip:
            self.looktable_flip[title] = map[title]

        try:
            self.opt_title_flip.set(self.matches_flip[0])
            self.var_flipkart.set(self.looktable_flip[self.matches_flip[0]][0] + '.00')
            self.link_flip = self.looktable_flip[self.matches_flip[0]][1]
            self.r_flip = self.looktable_flip[self.matches_flip[0]][2]
            self.x1 = self.looktable_flip[self.matches_flip[0]][2]
        except IndexError:
            self.opt_title_flip.set('Product not found')

    def price_amzn(self, key):
        url_amzn = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + str(key)

        # Faking the visit from a browser
        headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        map = defaultdict(list)
        home = 'https://www.amazon.in'
        proxies_list = ["128.199.109.241:8080", "113.53.230.195:3128", "125.141.200.53:80", "125.141.200.14:80",
                        "128.199.200.112:138", "149.56.123.99:3128", "128.199.200.112:80", "125.141.200.39:80",
                        "134.213.29.202:4444"]
        proxies = {'https': random.choice(proxies_list)}
        source_code = requests.get(url_amzn, headers=headers)
        plain_text = source_code.text
        self.opt_title = StringVar()
        self.soup = BeautifulSoup(plain_text, "html.parser")
        # print(self.soup)
        # print(self.soup.find_all('div', {'class': 'sg-col-inner'}))
        for html in self.soup.find_all('div', {'class': 'sg-col-inner'}):
            title, link,price,ratings = None, None,None,None
            for heading in html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}):
                title = heading.text
            for p in html.find_all('span', {'class': 'a-price-whole'}):
                price = p.text
            for l in html.find_all('a',
                {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}):
                link = home + l.get('href')
            for s in html.find_all('div', {'class': 'a-row a-size-small'}):
                for r in html.find_all('span', {'class': "a-size-base"}):
                    ratings = s.text[:3]
            if title and link:
                map[title] = [price, link,ratings]
        user_input = self.var.get().title()
        self.matches_amzn = get_close_matches(user_input, list(map.keys()), 20, 0.01)
        self.looktable = {}
        for title in self.matches_amzn:
            self.looktable[title] = map[title]
        self.opt_title.set(self.matches_amzn[0])
        self.var_amzn.set(self.looktable[self.matches_amzn[0]][0] + '.00')
        self.product_link = self.looktable[self.matches_amzn[0]][1]
        self.r_amaz = self.looktable[self.matches_amzn[0]][2]
        self.x2 = self.looktable[self.matches_amzn[0]][2]

    def search(self):
        amzn_get = self.variable_amzn.get()
        self.opt_title.set(amzn_get)
        product = self.opt_title.get()
        price, self.product_link, self.r_amaz = self.looktable[product][0], self.looktable[product][1], self.looktable[product][2]
        self.var_amzn.set(price + '.00')
        self.x2=self.looktable[product][2]
        flip_get = self.variable_flip.get()
        flip_price, self.link_flip, self.r_flip = self.looktable_flip[flip_get][0], self.looktable_flip[flip_get][1], self.looktable_flip[flip_get][2]
        self.var_flipkart.set(flip_price + '.00')
        self.x1=self.looktable_flip[flip_get][2]

    def visit_amzn(self):
        webbrowser.open(self.product_link)

    def visit_flip(self):
        webbrowser.open(self.link_flip)

    def create_chart(self):
        y1=float(self.x1)
        y2=float(self.x2)
        x = np.array(["", "Flipkart", "Amazon"])
        y = np.array([0.0,float(y1),float(y2)])
        plt.bar(x,y,color='#54847c')
        plt.show()

if __name__ == "ppc":
    c = Price_compare(root)
    root.title('Price Comparison Engine')
    root.mainloop()


