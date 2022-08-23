from turtle import pos
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# BASE_FLIPKART_URL = 'https://www.flipkart.com/search?q={}'
BASE_FLIPKART_URL = 'https://www.daraz.com.np/catalog/?q={}&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.287d2d2bFiSGuF'
# BASE_AMAZON_URL = 'https://www.amazon.in/s?k={}'
BASE_AMAZON_URL = 'https://www.amazon.com/s?k={}&crid=24PXRMHNAJAJE&sprefix=nik%2Caps%2C323&ref=nb_sb_noss_2'
def home(request):
	return render(request, 'base.html')

def new_search(request):
	search = request.POST.get('search')
	print(search)
	if search == '':
		final_postings=[]
		final_postingstwo=[]
	elif search == 'nike shoes':
		final_postings = [
			['Nike Airforce','https://www.gyapu.com/detail/nike-air-force-1-low-sneakers','Rs.45000','https://m.media-amazon.com/images/I/6125yAfsJKL._AC_UL320_.jpg'],
			['Nike Shoes','https://www.gyapu.com/detail/nike-men-air-jordan-retro-black-white-shoes','Rs.2000','https://m.media-amazon.com/images/I/71G-jdjT8ZL._AC_UL320_.jpg'],
		]
		
		final_postingstwo = [
			['Nike Airforce','https://www.gyapu.com/detail/nike-air-force-1-low-sneakers','Rs.2300','https://www.gyapu.com/public/510-432//files/E561C309F945C22-Nike%20Air%20Force%201%20Low%20Sneakers_Gyapu.jpg'],
			['Nike Airforce', 'https://www.gyapu.com/detail/nike-men-air-jordan-retro-black-white-shoes','Rs. 4300', 'https://www.gyapu.com/public/510-432//files/C5EBB64B59BF321-Nike%20Men%20Air%20Jordan%20Retro%20Black%20White%20Shoes.jpg']		
		]

	elif search == 'samsung a23':
		final_postings=[
			["Samsung a23",'https://www.gyapu.com/detail/samsung-galaxy-a235f-4gb64gb-ii-battery-5000-mah-ii-66-inches-pls-lcd','Rs.23,000','https://www.gyapu.com/public/510-432//files/16E8346274C5679-e0cc525bbe8785705699f6b9a2082fc6.png' ],
			["Samsung a23",'https://www.gyapu.com/detail/silicone-samsung-galaxy-phone-cases-s20fe','Rs.22,500','https://www.gyapu.com/public/510-432//files/BA4B752B29E7FE6-837daa630d71d6512d5bedb8c4331c7b.jpg_1200x1200q80.jpg' ],
		
		]
		final_postingstwo = [
			["Samsung a23",'https://www.daraz.com.np/products/samsung-galaxy-a23-6128-blue-i114784014-s1031187622.html?spm=a2a0e.searchlist.list.15.5b1823bdHyvLz6&search=1','Rs.21,000', 'https://static-01.daraz.com.np/p/a6cc431c79d8f199a292a01c94f8d82b.png'],
			["Samsung a23",'https://www.daraz.com.np/products/samsung-a23-4gb64gb-i117554381-s1032228168.html?spm=a2a0e.searchlist.list.9.5b1823bdHyvLz6&search=1','Rs.23,999', 'https://static-01.daraz.com.np/p/08e0177b6327fd89908dcbc0075a555f.jpg'],
		]

	elif search == 'polo tshirt':
		final_postings=[
			['Polo tshirt','https://www.daraz.com.np/products/grey-solid-polo-neck-100-cotton-t-shirt-for-men-i101168602-s1021888977.html?spm=a2a0e.searchlist.list.7.2f66520fIHSkXH&search=1','Rs. 500','https://static-01.daraz.com.np/p/d73db6dab8eb17d5fe21df3283d3b4cf.jpg'],
			['x men Polo tshirt','https://www.daraz.com.np/products/dark-maroon-solid-polo-neck-100-cotton-t-shirt-for-men-i101166612-s1021894638.html?spm=a2a0e.searchlist.list.17.2f66520fIHSkXH&search=1','Rs. 700','https://static-01.daraz.com.np/p/687f9aaed08183b640ae2b9291287c75.jpg']
		]
		final_postingstwo = [
			['Polo tshirt original','https://www.gyapu.com/detail/kilometer-polo-neck-t-shirt-kmp1010','Rs. 900','https://www.gyapu.com/public/510-432//files/6A703635D639446-IMG_6588-min.jpg'],
			['Kilometer polo ','https://www.gyapu.com/detail/kilometer-polo-neck-t-shirt-2023','Rs. 900','https://www.gyapu.com/public/510-432//files/700E8E2BB0A8CCA-IMG_6572.jpg']

		]
		

	


	stuff_for_frontend = {
	'search': search,
	'final_postings': final_postings,
	'final_postingstwo': final_postingstwo
	}
	return render(request, 'myapp/new_search.html', stuff_for_frontend)
	