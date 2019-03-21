import subprocess
import requests

retcodeSite=subprocess.call(r'"C:\Program Files (x86)\WinSCP\winscp.com" /ini=nul /console /command "option batch on" "option confirm off" "open sftp://root@host -hostkey=""ssh-rsa 2048 TESTaJzqFfGNiNPX9vOwVz7Di1mgJzxAeW/Sx37gsV2="" -privatekey=C:\Script\backup.ppk" "synchronize -criteria=time -transfer=binary remote D:\path\ /path/to/remote/" "exit" ', shell=True)

if retcodeSite == 0:
	url = "https://api.telegram.org/botid:AAHZL-ZwKxrkHnz1HFwwas4O2vn-8yiFqb8/"
	def get_updates_json(request):  
		response = requests.get(request + 'getUpdates')
        	return response.json()

	def last_update(data):  
		results = data['result']
		total_updates = len(results) - 1
		return results[total_updates]

	def send_mess(chat, text):  
		params = {'chat_id': chat, 'text': text}
		response = requests.post(url + 'sendMessage', data=params)
		return response

	send_mess(348144968, 'OK: S-grain Site + Mail')
	send_mess(201837960, 'OK: S-grain Site + Mail')

else:
        url = "https://api.telegram.org/botid:AAHZL-ZwKxrkHnz2dswwhp4O2vn-8yiFqb8/"
        def send_mess(chat, text):  
                params = {'chat_id': chat, 'text': text}
                response = requests.post(url + 'sendMessage', data=params)
                return response
        def get_updates_json(request):  
                response = requests.get(request + 'getUpdates')
                return response.json()

        def last_update(data):  
                results = data['result']
                total_updates = len(results) - 1
                return results[total_updates]

        send_mess(348144968, 'FAIL: S-grain Site + Mail')
        send_mess(201837960, 'FAIL: S-grain Site + Mail')
