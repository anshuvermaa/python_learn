import requests

url='https://api.pwnedpasswords.com/range/'+'_CBFDAC6008F9CAB4083784CBD1874F76618D2A97_'
res=requests.get(url)
print(res)