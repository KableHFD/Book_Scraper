import requests
from bs4 import BeautifulSoup


def SciFi():

	headers = {
		'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	response = requests.get('https://www.barnesandnoble.com/b/books/science-fiction-fantasy/_/N-1fZ29Z8q8Z180l?Ns=P_Sales_Rank', headers=headers)

	bsr = BeautifulSoup(response.text, 'html.parser')

	#this is the class that contains author and book info, and href, pulls only the first book at index 0
	book = bsr.select('.product-info-title')[0]

	author_on_site = bsr.select('.product-shelf-author')[0]

	# link = f'https://www.barnesandnoble.com/{burl}'
	author = author_on_site.getText()
	title = author_on_site.getText()
	book_name = book.getText()
	return f'The Number 1 best selling SciFi book is {book_name}{title}'

#this function returns url for SciFi
def scurl():
	headers = {
		'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	response = requests.get('https://www.barnesandnoble.com/b/books/science-fiction-fantasy/_/N-1fZ29Z8q8Z180l?Ns=P_Sales_Rank', headers=headers)

	bsr = BeautifulSoup(response.text, 'html.parser')
	#grabs html class that contains href for book
	book = bsr.select('.product-info-title')[0]
	#seperates href from class information
	burl = book.a.get('href')
	scurl = f'https://www.barnesandnoble.com/{burl}'
	return scurl


def Thrillers():

	headers = {
		'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	response = requests.get('https://www.barnesandnoble.com/b/books/fiction/thrillers/_/N-1fZ29Z8q8Z1d3u?Ns=P_Sales_Rank', headers=headers)

	bsr = BeautifulSoup(response.text, 'html.parser')

	#this finds the the number at which the book sits on best seller list
	# count = bsr.select('.count')

	#this is the class that contains author and book info, and href, pulls only the first book at index 0
	book = bsr.select('.product-info-title')[0]

	author_on_site = bsr.select('.product-shelf-author')[0]

	# link = f'https://www.barnesandnoble.com/{burl}'
	author = author_on_site.getText()
	title = author_on_site.getText()
	book_name = book.getText()
	return f'The Number 1 best selling Thriller book is {book_name}{title}'


#this function returns url for thriller
def turl():
	headers = {
	'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	response = requests.get('https://www.barnesandnoble.com/b/books/fiction/thrillers/_/N-1fZ29Z8q8Z1d3u?Ns=P_Sales_Rank', headers=headers)

	bsr = BeautifulSoup(response.text, 'html.parser')
	book = bsr.select('.product-info-title')[0]
	burl = book.a.get('href')
	turl = f'https://www.barnesandnoble.com/{burl}'
	return turl


def History():

	headers = {
		'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	response = requests.get('https://www.barnesandnoble.com/b/books/history/_/N-1fZ29Z8q8Z11km?Ns=P_Sales_Rank', headers=headers)

	bsr = BeautifulSoup(response.text, 'html.parser')


	#this is the class that contains author and book info, and href, pulls only the first book at index 0
	book = bsr.select('.product-info-title')[0]

	author_on_site = bsr.select('.product-shelf-author')[0]

	# link = f'https://www.barnesandnoble.com/{burl}'
	author = author_on_site.getText()
	title = author_on_site.getText()
	book_name = book.getText()
	return f'The Number 1 best selling History book is {book_name}{title}'

#this function returns the url for History
def hurl():

	headers = {
		'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	}

	response = requests.get('https://www.barnesandnoble.com/b/books/history/_/N-1fZ29Z8q8Z11km?Ns=P_Sales_Rank', headers=headers)

	bsr = BeautifulSoup(response.text, 'html.parser')

	book = bsr.select('.product-info-title')[0]
	burl = book.a.get('href')

	hurl = f'https://www.barnesandnoble.com/{burl}'

	return hurl

