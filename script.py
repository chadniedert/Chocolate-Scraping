import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)
