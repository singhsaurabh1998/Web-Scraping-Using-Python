import urllib.request
from bs4 import BeautifulSoup
import ssl


class Insta_Info_Scraper:

    def getinfo(self, url):
        html = urllib.request.urlopen(url) # getting the link
        soup = BeautifulSoup(html, 'html.parser')

        data = soup.find_all('meta', {'property': 'og:description'})
        text = data[0].get('content').split()

        username = text[-1] # last item is the username
        ind = text.index('from') # after 'from' name occurs
        name = text[ind+1: :] # but it also contains the username
        name.pop() # avoiding the username

        followers = text[0]  # first item is followers
        following = text[2]  # second item is following
        posts = text[4]

        print("*********** Info ***********\n")
        print('Username :', username)
        print('Name :', *name, sep=' ')
        print('Followers : ', followers)
        print('Following : ', following)
        print('Posts :', posts)
        print('---------------------------')

    def main(self):
        # these three lines just for establishing the secure connection
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        url = input("Enter The link  ")
        self.getinfo(url)


obj = Insta_Info_Scraper()
obj.main()
