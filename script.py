import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content, "html.parser")


ratings = []
class_rating = soup.find_all(attrs = {"class": "Rating"})
class_rating.pop(0)
for i in range(len(class_rating)):
  ratings.append(float(class_rating[i].get_text()))
#print(ratings)

plt.hist(ratings)
plt.show()
