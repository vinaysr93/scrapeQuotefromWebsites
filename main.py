import requests,bs4

url='http://quotes.toscrape.com/'
response= requests.get(url)
soup=bs4.BeautifulSoup(response.text,'html5lib')

quotes=soup.find_all('span',class_='text')
authors=soup.find_all('small',class_='author')
ta=soup.find_all('div',class_='tags')
for i in range(len(quotes)):
  print(quotes[i].text)
  print(authors[i].text)
  individual_tags=ta[i].find_all('a',class_='tag')
  for j in individual_tags:
    print(j.text)
