import requests
from requests.auth import HTTPBasicAuth
import argparse
import getpass

#Check fw, upgrade fw(http or tftp)
#Check power , reset power
#Locator LEDs

#url_encl='https://10.50.14.159/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate/Status'
#r=requests.get(url_encl, auth=HTTPBasicAuth('admin','admin'), verify=False)
#json_data=r.json()
#print(json_data)

import http.server
import socketserver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#PORT = 8081

parser = argparse.ArgumentParser(description='This is \'Beta\' version 1.1 firmware upload server for Data60 and Data102 IOMs. This version doesn\'t verify HTTP Certificate')
parser.add_argument('-s', dest='HTTP_SERVER_IP',nargs='+', help='IP Address ',required=True)
#parser.add_argument('-u',dest='user',help='username', required=False)
#parser.add_argument('-p',dest='password',nargs='?', help='ask password', required=False)
parser.add_argument('-port',dest='port',nargs='?', help='HTTP PORT', required=False)
parser.set_defaults(port=80) #Default port=80
parser.set_defaults(u='admin') #Default user=admin
parser.set_defaults(p='admin') #Default password=admin

args = parser.parse_args()
#print('simple_value     =', args.ServerIP)
#print('simple_value     =', args.user)
#print('simple_value     =', args.password)
PORT=int(args.port)
#user=args.u
#passw=args.password

#print("HTTP server running at port: ",PORT)

#if args.password==None:
#	print("")
#	try:
#		passw= getpass.getpass()
#	except:
#		print("\nCancelled: exiting....")
#		sys.exit()

#IP=args.ip[0]
IP=args.HTTP_SERVER_IP[0]
ipaddr="https://"+IP+"/redfish/v1"

Handler = http.server.SimpleHTTPRequestHandler
headers = {'content-type': 'application/json', 'Cache-Control': "no-cache" }
httpd=socketserver.TCPServer((IP, PORT), Handler)
print("Serving at IP [PORT]:",IP,"[",PORT,"]")
print("\n**Don't close this window while firmware is being upgraded**")
httpd.serve_forever()
#url_fw_upg=ipaddr+'/UpdateService/Actions/UpdateService.SimpleUpdate'
#payload = "{\n \"ImageURI\": \"http://10.50.14.163:8081/hgst_mm_bundle_200T-073_T2.0.34.tar.gz\"\n }"

#r = requests.request("POST",url_fw_upg, data=payload, headers=headers)
#print(r.text)
print("Done")
