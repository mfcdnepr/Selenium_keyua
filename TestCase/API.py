
#import requests
data = {'username': 'leonid.keyua@gmail.com','password': '11111'}
res = requests.post('https://staging.completecase.com:8001/api/v1/rest-auth/login/', data=data)
res
res.__dict__
res.json()
token = res.json()['token']
token = f'JWT {token}'
headers = {
	"first_name": "TEST",
	"last_name": "TEST22222",
	"password": "TESTTTTTTTTT",
	"password_confirmation": "TESTTTTTTTTT",
	"external_site_id": 67,
	"state": "california",
	"email": "test+5684684@test.test"
}

users = requests.get('https://staging.completecase.com:8001/admin/accounts/user/add/')
