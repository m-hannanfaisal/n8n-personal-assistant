import requests


user_message = "Send a mail to hannanfaisal0507@gmail.com with subject 'Test Mail' and body 'This is a test mail from n8n webhook.'"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/a4fe0402-0021-4b14-9d14-412e5073dcf9"

response = requests.post(url, json=request_message)

print(response.status_code)
print(response.json())

# print(response.json()[0]["output"])