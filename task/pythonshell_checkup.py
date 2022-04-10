from authemail import wrapper
account = wrapper.Authemail()
first_name = 'aatif'
last_name = 'fraz'
email = 'imaatiffraz@gmail.com'
password = 'admin123'
response = account.login(email=email, password=password)
print(account.token)
token = account.token
response = account.logout(token=token)
print(response)