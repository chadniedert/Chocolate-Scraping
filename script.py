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

#plt.hist(ratings)
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
#print(ten_best)

cocoa_percentages = []
cocoa_soup = soup.find_all(attrs = {"class": "CocoaPercent"})

cocoa_soup.pop(0)
for i in range(len(cocoa_soup)):
  cocoa_percentages.append(float(cocoa_soup[i].get_text().strip("%")))
#print(cocoa_percentages)

company_rating_percent_dict = {"Company": companies, "Ratings": ratings, "CocoaPercent" : cocoa_percentages}
cocoa_df = pd.DataFrame.from_dict(company_rating_percent_dict) 
#print(cocoa_df)

plt.scatter(cocoa_df.CocoaPercent, cocoa_df.Ratings)
z = np.polyfit(cocoa_df.CocoaPercent, cocoa_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(cocoa_df.CocoaPercent, line_function(cocoa_df.CocoaPercent), "r--")
plt.show()

