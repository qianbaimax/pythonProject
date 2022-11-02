from urllib import request
response = request.urlopen('http://[::]:8000/')
print(response)
print(response.status)

for k, v in response.getheaders():
    print('{}: {}'.format(k, v))

