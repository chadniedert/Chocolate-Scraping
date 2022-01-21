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

plt.hist(ratings)
#plt.show()

companies = []
company_soup = soup.find_all(attrs = {"class": "Company"})
company_soup.pop(0)
for i in range(len(company_soup)):
  companies.append(company_soup[i].get_text())

company_rating_dict = {"Company": companies, "Ratings": ratings}
company_rating_df = pd.DataFrame.from_dict(company_rating_dict)

mean_ratings = company_rating_df.groupby("Company").Ratings.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)
