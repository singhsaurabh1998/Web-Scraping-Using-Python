from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm  # Matplotlib Font Manager

def generate_pic(text_color=(30, 55, 153), background_color=(130, 204, 221)):

    # 1024x1160 is the image resolution
    img = Image.new('RGB', (1024, 1160), color=background_color)
    draw_image = ImageDraw.Draw(img)
    selected_font = ImageFont.truetype(fm.findfont(fm.FontProperties(family='cinzel.otf')), 50)

    # all the reviews of the product will be contained in it
    fresh_sentence = ''
    for sentence in reviews:
        fresh_sentence += sentence.text +"\n\n"

    print("\n*Wait !! Image Is Loading... \n")

    dim = draw_image.textsize(fresh_sentence, font=selected_font)
    x_2 = dim[0]
    y_2 = dim[1]
    draw_image.text(((1024 / 2 - x_2 / 2), (1160 / 2 - y_2 / 2)), fresh_sentence, align="center",
                    font = selected_font, fill = text_color)
    img.save("quote.png")
    img.show()

# function for getting !!TOP!! the comments
def getComments(URL):
    obj = requests.get(URL)
    soup = BeautifulSoup(obj.text, 'html.parser')
    comments = soup.find_all('p', {"class": "_2xg6Ul"})
    if len(comments) == 0:
        print("**SORRY**\nThis Product Does'nt Have Any Reviews")
    elif len(comments) < 10:
        print("TOP COMMENTS OF THE PRODUCT :")
        for i in comments:
            print(i.text)
    else:
        print("TOP 10 REVIEWS OF THE PRODUCT :")
        for i in range(0,10):
            print(comments[i].text)
    return comments

URL = input("Enter The URL Of The Product : ")
reviews = getComments(URL)
generate_pic()