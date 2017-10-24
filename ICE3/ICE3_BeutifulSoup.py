
#1. Import these libraries
import requests
from bs4 import BeautifulSoup


#2.define a variable and put the link you are willing to extract data of that
url = 'https://en.wikipedia.org/wiki/Machine_learning'

#3. use the Request library to download the url in another variable
source = requests.get(url)

#4. parse the sourceCode using the BeautifulSoap library and save the parsed code in a variable
soup = BeautifulSoup(source.content,'lxml')

#5.use  findAll(‘div’) to find all the div in the parsed sourcecode
divResult = soup.find_all('div')

#6. use a loop by the result that you have got of the step 5 to find heading
for div in divResult:
	heads = div.find('h1')
	print(heads)
#7. print the content of the r1

# 8. do the same for printing the body
body = soup.body
for paragraph in body.find_all('p'):
	print(paragraph.text)


# print(soup.title.string)
# print(soup.p)
# print(soup.find_all("p"))

# for paragraph in soup.find_all('p'):
#     print(paragraph.string)
# print(soup.get_text())

# for url in soup.find_all('a'):
#     print(url.get('href'))







