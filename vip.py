import requests
def Tele(ccx):
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = ccx.split("|")[2][-2:]
		cvc = ccx.split("|")[3]

		headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		data = f'billing_details[address][state]=NY&billing_details[address][postal_code]=10001&billing_details[address][country]=US&billing_details[address][city]=New+YURK&billing_details[address][line1]=New+YURK&billing_details[address][line2]=&billing_details[email]=gvvvv7277%40gmail.com&billing_details[name]=Angel+Rippin&billing_details[phone]=16462965794&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&pasted_fields=number&payment_user_agent=stripe.js%2Fd8d368f981%3B+stripe-js-v3%2Fd8d368f981%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fwww.metabee.com&time_on_page=147996&client_attribution_metadata[client_session_id]=5d7d692e-8ccb-46ba-9949-c9bcb8460938&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&guid=fb83f278-a5da-4c63-af1a-c3e75f74a5579320a4&muid=f779b2f4-fab0-4a9f-89a7-d7a7d9e44ce2038add&sid=52586367-6cc2-4bc9-aace-76a75a85f3aed0dab4&key=pk_live_51MbhFsJA4rtbodqOPW776Ncc2Nb9MX0xCqxWqWHegtdWAvbnfYBi1F3ycfnK4NgqhrAR5rBGoB4gIKexAZb9LJe100UbEJji4I&_stripe_version=2020-03-02&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZ7EvffT0yvWQqqI9btPUDmU8WiD6TiYUwCWEfCegYykpIKZjMZw7RTMuYvxyi0UzIYt02yF2t7ue-FCErdNCpskZAllG1vSSW9ccREXkTTqXSNm4mWlWOF7GSPUgZGRG8Jq6emeRaXHXDjL0hO_iL7Xumffv1FaS2GFUeMVmLCupl9eyGSlJSRYsv6Q0RDtruA0KKf-Rb3g5Ig02v4ZlwBJ7gmHI7rrKqQrwarwpU3od6Jhu7Gppb8c66etQhknFik9vl_Lur6PN1zV4rbVWSofqVVdugtb6THs5iq6-TL4o7eFkv0RGIoXELob_tu-GCBFvJu2W9kVY2Ebs5dmdciXOttJ0SRBMEu4EeuoDZibFNx-OhFrqvrdI9_RLbeC5rFepxBBjtel0xZShefy5a1ue8dGX2IOI7M9xaH516-45Sm2RtkXdXIIkj8pj_QtJwtCG1jsuWjjsvgEDD_qzrSioeh8ZLflJCyVgkL4PEuCXIUM8KE7-28JUv4krY-bdbqDSClsW-j-7KEoaytFJKBOicDA80chpmwPghw5H-ZlD-Zxswhc26rWbAKQvHchYqS2vStUkTk4_E_52Ny5hnHeto_3GDVIl14UmQ9IUEH2f_m4ivjU66MbQIQ-MBvSL3Z3kfszglapVzohBExUZr2mO6RLpDz97v9qyts9mgNqnKXaOO4EwjRgRyHC8J0KPz4m9t4sCTM02NyZrbkvbz-tujJyBRvf7PsOIFA9CYpMjkAnUA3wzZn6Cef4hcTDdSxOE8Vp5ysIBitB7tpF5XQ-9-7oNJfageE3vqtpm3J3vxbkeFXDFApmKLI6mvOe7byHVl8H48x_MLrcVm9RWkqaAEWAFmqBzMeRodK6Qlq5l__HVYwyn4bLy-IPm0DI2AX-Mnyb3F7OXNDBnbqmadHNHVBOqk_ybVLK_TtxHl7-YtBJ9L6UU7OZZ4SVZorahEsXyAdwau9lqlfYnQfYa1U0ihFnb9HhalMUVSPYMVUY42dgKCLUND2L0th6sCS0KYpJWxUBncdJLAxBgK4X2WFeqZ5LU6aBbHyljMALNPm-zKqRboIu1XuPHhR9NJNuuXa5VdPSaBLZs9_08F7mmYk31OiLVZrxQGB-lwWwaOKp-Gh-bSnaC7UskekfEd0Gn473U2n7fb3NqX0z_iQLjBcUl-uEmwxW_M3PRzwF0PiZWvjuORNXKwlsHLUxeoGP1UU3m8YghL2eoHA-lmg9-JDMLiitFepm96oy4yu-oIaP0qNG0Tq6jPu00ojLOU4nKEwJo9ASUc09PV-9objwEpCumEH01ruxwa2rnpTuWx-7noQ_VWEdKlxmV2OiFsSoRY0xdBHeM_eaZ51KVrZRuxl8SpXahthEyqVBGuybPzXNrdoPW_srrc53_Pk5-cJDZNXc09luI0qWUmX4LgmDzZa3cblsSHh6biUdvNXAoZPepWAqWpf-0ESdzRdu06RUHY274m-aPFlFyUlPh-ukDCarV1UnOWf1n0pTImpvzq6QGKtBWVZxS4B9640UCImOYC7eytktrHdOmkByLHStUi6LZSQLI8sYIdFrrkcv9yxsCbeiUq4GbzltXuVvtR_tTvjQiESXCHx7rz_9Acb6mZV1IOunp4pj7UuXhJ1_g3HA4hTftT2t2_G6mCjmHu3-x8psPVU5kkU_0UKeZGjR1bWvAltO9t_zRMi555tDIBXrFhmpp2LmtJmtDzih76j40n36g5eiPWQ7YfFggXyf3x-ZVypYOxgTLncSB9b4MJ3VuFJYZ84r3N__6gHqh3I5ceS26KM5PG8b6uUuy0yKIpshRSQPPaHt7GFQEP0_3ucFh_WcqlytfTPJjE1Wu7iH1ywyD8uESQQzOdbcBy500QHMJCU4Vf6SM8zHqd-XsGBzVqyrAUH_Dq6EM-lexFMTO5QZtyZsy3eoZOWkWAOCSCUU-5anr86BIitQ5iYhu4VtfqHubIi7N21qifErlDj7xuViVS3kbtu79I7kphmF6hZTOf7N4vg8jd4v8AIbYRqp-NdaeUXMnlNMJ8YkAlXUCVe8EuJqXsqNxVo0Sp9P6i55NJZZHyI-raEnZkusGese74QEEq8Ap1YdpQVXoX0Zmb0p7kibGsRvTW4uaLE2q66rr1f9ZUhCMr5DL4ktQyYC-V2Ffki6ynvLgcjy6toAzsHNCNVgZU06El2ahrv3j391wh5wIVFXzHbpJtHo2V4cM5mcL12qHNoYXJkX2lkzjGtTIGia3KoMzMzNjQ5MDeicGQA.sf0o_q-9v9Zy8WnUh8u7uUav_Wa3GYZjTFNj_3nm6uA'
		response = requests.post('https://api.stripe.com/v1/payment_methods',headers=headers, data=data)
		
		
		idd = (response.json())['id']
		
		
		
		cookies = {
		    'X-Magento-Vary': '9e3ffb41bfb757d6150aefc5bc0625289145ee73',
		    'cf_consent': '{"jnaU":true}',
		    'user_id': 'US-2a0d:5600:24:c3e:c6f:3c5a:efc5:2-203697.05858240827',
		    '_ga': 'GA1.1.231719587.1718664249',
		    '_fbp': 'fb.1.1718664250682.455391638245272199',
		    'form_key': 'R6Cy1zpWvf9M6RXM',
		    'mage-cache-storage': '{}',
		    'mage-cache-storage-section-invalidation': '{}',
		    '_clck': 'ch6ts0%7C2%7Cfmp%7C0%7C1629',
		    'mage-messages': '',
		    'recently_viewed_product': '{}',
		    'recently_viewed_product_previous': '{}',
		    'recently_compared_product': '{}',
		    'recently_compared_product_previous': '{}',
		    'product_data_storage': '{}',
		    'PHPSESSID': '79opfjlnqi2d19krrjg20pv69s',
		    'mage-cache-sessid': 'true',
		    'form_key': 'R6Cy1zpWvf9M6RXM',
		    'private_content_version': '6804fc8dbe8d909f69232116d827cd66',
		    '__stripe_mid': 'f779b2f4-fab0-4a9f-89a7-d7a7d9e44ce2038add',
		    '__stripe_sid': '52586367-6cc2-4bc9-aace-76a75a85f3aed0dab4',
		    '_clsk': '5bpfga%7C1718664296093%7C5%7C1%7Cz.clarity.ms%2Fcollect',
		    '_ga_KZ9K93GRS2': 'GS1.1.1718664248.1.1.1718664444.60.0.527205924',
		    'section_data_ids': '{%22cart%22:1718664378%2C%22directory-data%22:1718664286%2C%22messages%22:1718664378%2C%22gtm-checkout%22:1718664445%2C%22captcha%22:1718664378}',
		}
		
		headers = {
		    'authority': 'www.metabee.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    # 'cookie': 'X-Magento-Vary=9e3ffb41bfb757d6150aefc5bc0625289145ee73; cf_consent={"jnaU":true}; user_id=US-2a0d:5600:24:c3e:c6f:3c5a:efc5:2-203697.05858240827; _ga=GA1.1.231719587.1718664249; _fbp=fb.1.1718664250682.455391638245272199; form_key=R6Cy1zpWvf9M6RXM; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; _clck=ch6ts0%7C2%7Cfmp%7C0%7C1629; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=79opfjlnqi2d19krrjg20pv69s; mage-cache-sessid=true; form_key=R6Cy1zpWvf9M6RXM; private_content_version=6804fc8dbe8d909f69232116d827cd66; __stripe_mid=f779b2f4-fab0-4a9f-89a7-d7a7d9e44ce2038add; __stripe_sid=52586367-6cc2-4bc9-aace-76a75a85f3aed0dab4; _clsk=5bpfga%7C1718664296093%7C5%7C1%7Cz.clarity.ms%2Fcollect; _ga_KZ9K93GRS2=GS1.1.1718664248.1.1.1718664444.60.0.527205924; section_data_ids={%22cart%22:1718664378%2C%22directory-data%22:1718664286%2C%22messages%22:1718664378%2C%22gtm-checkout%22:1718664445%2C%22captcha%22:1718664378}',
		    'origin': 'https://www.metabee.com',
		    'referer': 'https://www.metabee.com/checkout/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		json_data = {
		    'cartId': 'Dj6fDiNj15aUVFC2OSNo6uPvz3d4Bf5y',
		    'billingAddress': {
		        'countryId': 'US',
		        'regionId': '43',
		        'regionCode': 'NY',
		        'region': 'New York',
		        'street': [
		            'New YURK',
		            '',
		            '',
		        ],
		        'company': '',
		        'telephone': '16462965794',
		        'postcode': '10001',
		        'city': 'New YURK',
		        'firstname': 'Angel',
		        'lastname': 'Rippin',
		        'saveInAddressBook': None,
		    },
		    'paymentMethod': {
		        'method': 'stripe_payments',
		        'additional_data': {
		            'payment_element': True,
		            'payment_method': idd,
		            'manual_authentication': 'card',
		        },
		    },
		    'email': 'gvvvv7277@gmail.com',
		}
		
		response = requests.post(
		    'https://www.metabee.com/rest/default/V1/guest-carts/Dj6fDiNj15aUVFC2OSNo6uPvz3d4Bf5y/payment-information',
		    cookies=cookies,
		    headers=headers,
		    json=json_data,
		)
		try:
			ii=(response.text)
		except:
			return 'error'
		return ii
	
