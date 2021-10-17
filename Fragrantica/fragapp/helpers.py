from bulk_update_or_create import BulkUpdateOrCreateQuerySet

import bulk_update_or_create

from .models import *

from django.http import HttpResponse

from django_pandas.io import read_frame

import pandas as pd

def home(request):

	brand = [{'Brand_Name': 'April Aromatics',
	  'Brand_Official_link': 'http://aprilaromatics.com/',
	  'Brands_Activity': 'Natural Perfumery',
	  'Brands_Country': 'Germany',
	  'About_Brand': 'April Aromatics was founded in New York by Tanja Bochnig. Since 2008 the brand has been based in Berlin. The line presents a range of natural perfumes and follows a holistic approach. With April Aromatics, Tanja Bochnig lives an ideal that only a few perfumers worldwide pursue: all ingredients are certified organic or wild crafted whenever available. 100% of the ingredients are from authentic, pure and natural origin. April Aromatics does not use animal derived ingredients, that involve killing and torturing animals. The perfumes are based on organic jojoba oil or organic alcohol. All packagings are recyclable. "I strongly believe that people can feel the love and energy I give into my perfumes—may it be conscious or unconscious. Adding chemical ingredients into natural essences is like putting MSG on your organic food. Trust in the power of nature. That‘s all we need.“—Tanja Bochnig Designer April Aromatics has 35 perfumes in our fragrance base. April Aromatics is a new fragrance brand. The earliest edition was created in 2011 and the newest is from 2020. The nose who worked on the fragrances is Tanja Bochnig.',
	  'Link': 'https://www.fragrantica.com/designers/April-Aromatics.html',
	  'Image': 'https://fimgs.net/mdimg/dizajneri/o.863.jpg'},
	 {'Brand_Name': "Adopt' by Reserve Naturelle",
	  'Brand_Official_link': 'https://www.adopt.fr/',
	  'Brands_Activity': 'Cosmetics',
	  'Brands_Country': 'France',
	  'About_Brand': "Designer Adopt' by Reserve Naturelle has 126 perfumes in our fragrance base. Adopt' by Reserve Naturelle is a new fragrance brand. The earliest edition was created in 2017 and the newest is from 2021. The nose who worked on the fragrances is Dominique Monlun",
	  'Link': 'https://www.fragrantica.com/designers/Adopt-by-Reserve-Naturelle.html',
	  'Image': 'https://fimgs.net/mdimg/dizajneri/o.1852.jpg'}]

	product = [{'Brand_Name': 'April Aromatics',
	  'Product_Name': 'XXX Charcoal Ermenegildo Zegna 2021',
	  'Product_Image': 'https://pimages.parfumo.de/480/153969_img-6738-ermenegildo-zegna-xxx-charcoal_480.jpg',
	  'Sex': 'Male',
	  'Year': '2021',
	  'Description': 'XXX Charcoal is a new perfume by Ermenegildo Zegna for men and was released in 2021. It is being marketed by Estēe Laud',
	  'Reference': 'https://www.parfumo.net/Perfumes/Ermenegildo_Zegna/xxx-charcoal',
	  'Color': (83, 88, 86)},
	 {'Brand_Name': "Adopt' by Reserve Naturelle",
	  'Product_Name': "L'Anonyme ou OP-1475-A A Lab on Fire 2011",
	  'Product_Image': 'https://pimages.parfumo.de/480/12315_img-3248-a_lab_on_fire-l_anonyme_ou_op_1475_a_480.jpg',
	  'Sex': 'Unisex',
	  'Year': '2011',
	  'Description': "L'Anonyme ou OP-1475-A is a perfume by A Lab on Fire for women and men and was released in 2011. The scent is floral-fresh. It is still available to purchase.",
	  'Reference': 'https://www.parfumo.net/Perfumes/A_Lab_on_Fire/L_Anonyme_ou_OP1475A',
	  'Color': (174, 174, 173)}]

	brand_instances = [Brand(

		b_name=value['Brand_Name'],
		official_link=value['Brand_Official_link'],
		activity=value['Brands_Activity'],
		about=value['About_Brand'],
		country=value['Brands_Country'],
		reference = value['Link']

		) for value in brand]
	Brand.objects.bulk_update_or_create(brand_instances,['b_name','official_link','activity','about','country','reference','rating'],match_field=['b_name','official_link','activity','about','country','reference','rating'])

	getBrand = Brand.objects.all()
	BrandDF = read_frame(getBrand)
	getProduct = pd.DataFrame(product)
	# print(BrandDF)
	df_join = pd.merge(getProduct, BrandDF, how="left", left_on='Brand_Name',
                          right_on='b_name')
	print(df_join)
	return HttpResponse('Brand is saved !')