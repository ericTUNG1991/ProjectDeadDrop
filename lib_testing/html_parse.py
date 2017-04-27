from bs4 import BeautifulSoup

file = open('testDigiDrop.php', 'r')
html = file.read()
file.close()

soup = BeautifulSoup(html, 'html.parser')
list_items = soup.find(id="DigiDropMessageList").children

for item in list_items:
	print item.string
