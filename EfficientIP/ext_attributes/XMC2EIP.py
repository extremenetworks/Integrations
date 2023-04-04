#!/usr/bin/python
##############################################################################
#
# Creator: Stephan Harrer - Bell Computer Netzwerke GmbH
# Softwarename : XMC2EIP.py
# Last Updated : April, 2022
#
# Purpose:  Send XMC data to EfficientIP IPAM
#
# Changes:  2018 Mai 31:  Created
#	    2022 April 4: Json added for response
#
##############################################################################

#############
## IMPORTS ##
#############

import requests
import re
import sys
import logging
import base64
import json

###############
## User data ##
###############

varUser = "ipmadmin"
varPassword = "admin"
varEipIP = '1.1.1.1'
#Set varDebug to "True" if you need more debug information
varDebug = False
varDebugFile = "XMC2EIP.log"

###################################
## Custom tuning above not below ##
###################################

varAttrStatus = "xmcstatus"
varAttrAuth = "xmcauthtype"
varAttrSwitchIP = "xmcswitchip"
varAttrSwitchPort = "xmcswitchport"
varAttrSwitchLocation = "xmcswitchlocation"
varAttrProfile = "xmcprofile"
varAttrUser = "xmcuser"
varAttrReason = "xmcreason"
varAttrTimeStamp = "xmcupdate"

##################################################
## Values above must match those in EfficientIP ##
##################################################

if varDebug:
    logging.basicConfig(filename=varDebugFile,level=logging.DEBUG)

varMakeUpdate = False

args = {}
i = 1
while i < len(sys.argv):
    args[sys.argv[i]] = sys.argv[i+1]
    i += 2
if varDebug:
    logging.debug("Attributes received:"+str(sys.argv[1:]))
    logging.debug("Loaded attributes:"+str(args))

#################################################################
## Check arguments and prepare Extensible Attributes Structure ##
#################################################################

varExtensibleAttr = {}

if "Mac" in args.keys():
    varMAC = str(args["Mac"])
else:
    if varDebug:
        logging.error("Missing mandatory argument Mac followed by value.")
    print ("Missing mandatory argument Mac followed by value.")
    sys.exit(1)

if "Status" in args.keys():
    varExtensibleAttr.update({varAttrStatus:{"value":args["Status"]}})
    varMakeUpdate = True

if "Auth" in args.keys():
    varExtensibleAttr.update({varAttrAuth:{"value":args["Auth"]}})
    varMakeUpdate = True
    
if "SwitchIP" in args.keys():
    varExtensibleAttr.update({varAttrSwitchIP:{"value":args["SwitchIP"]}})
    varMakeUpdate = True

if "SwitchPort" in args.keys():
    varExtensibleAttr.update({varAttrSwitchPort:{"value":args["SwitchPort"].replace('"',"")}})
    varMakeUpdate = True

if "SwitchLocation" in args.keys():
    if args["SwitchLocation"].replace('"',"") == ' ':
        varExtensibleAttr.update({varAttrSwitchLocation:{"value":'-'}})
    else:
        varExtensibleAttr.update({varAttrSwitchLocation:{"value":args["SwitchLocation"].replace('"',"")}})
    varMakeUpdate = True
    
if "Profile" in args.keys():
    varExtensibleAttr.update({varAttrProfile:{"value":args["Profile"].replace('"',"")}})
    varMakeUpdate = True

if "User" in args.keys():
    if args["User"].replace('"',"") == ' ':
        varExtensibleAttr.update({varAttrUser:{"value":str(args["Mac"])}})
    else:
        varExtensibleAttr.update({varAttrUser:{"value":args["User"].replace('"',"")}})
    varMakeUpdate = True

if "Reason" in args.keys():
    varExtensibleAttr.update({varAttrReason:{"value":args["Reason"].replace('"',"")}})
    varMakeUpdate = True

if "Time" in args.keys():
    varExtensibleAttr.update({varAttrTimeStamp:{"value":args["Time"]}})
    varMakeUpdate = True

if varDebug:
    logging.debug("Attributes in the structure: "+str(varExtensibleAttr))
    logging.debug("End-System:"+str(args["Mac"]))

if varMakeUpdate == False:
    logging.error("At least one argument followed by value is needed: Status, Auth, SwitchIP, SwitchPort, SwitchLocation, Profile, User, Reason, Time")
    print ("At least one argument followed by value is needed: Status, Auth, SwitchIP, SwitchPort, SwitchLocation, Profile, User, Reason, Time")
    sys.exit(1)

########################
## Test if MAC exists ##
########################

headers = {
	'X-IPM-Username': base64.standard_b64encode(varUser),
	'X-IPM-Password': base64.standard_b64encode(varPassword),
	'cache-control': 'no cache'}
	
url = "https://" + varEipIP + "/rest/ip_address_list"
querystring = {"WHERE":"mac_addr like '" + varMAC + "'"}

if varDebug:
    logging.debug("requesting: " + url + " with querysting: " + str(querystring))

try:
	varResponse = requests.request("GET", url, headers=headers, params=querystring, verify=False)
except requests.exceptions.RequestException as e:
    logging.error(str(e))
    sys.exit("RequestException")

varResponseJson = json.loads(varResponse.text)
varIpInfo = varResponseJson[0]['ip_class_parameters']

if varDebug:
    logging.debug("response: " + varResponse.text)
    logging.debug("response json: " + varIpInfo)
	
if varResponse.raise_for_status():
	logging.error("ERROR communicating to EIP " + str(varResponse.status_code) + varResponse.text)
	sys.exit("ERROR communicating to EIP")
		
varSearchResult = re.search(r"ip_id\":\"(\d*)", varResponse.text)

if varSearchResult:
	varIpId = varSearchResult.group(1)
	print("IP_ID: " + varIpId)
else:
	logging.error("Can't find MAC-Address " + varMAC)
	sys.exit("UnknownMAC")
    
varIsStatic = False

if (re.search(r"dhcpstatic=0", varIpInfo)):
    logging.error("DynamicAddress")
    sys.exit("DynamicAddress")
else:
	varIsStatic = True

varSearchResult = re.search(r"site_id\":\"(\d*)", varResponse.text)

if varSearchResult:
	varSiteId = varSearchResult.group(1)
	print("Site_ID: " + varSiteId)
else:
	logging.error("Can't find Site_ID")
	sys.exit("WrongSiteID")

class_param = ""
varParamCounter = 0

for key in varExtensibleAttr:
	if varParamCounter == 0:
		class_param = class_param + key + "=" + varExtensibleAttr[key]['value']
	else:
		class_param = class_param + "&" + key + "=" + varExtensibleAttr[key]['value']
	varParamCounter = 1

if varIsStatic:
	class_param = class_param + "&dhcpstatic=1"
	querystring = {"ip_id":varIpId,"site_id":varSiteId,"mac_addr":varMAC,"ip_class_parameters":class_param}
else:
	querystring = {"ip_id":varIpId,"site_id":varSiteId,"ip_class_parameters":class_param}
	
url = "https://" + varEipIP + "/rest/ip_add"

if varDebug:
    logging.debug("requesting: " + url)
	
try:
	varResponse = requests.request("PUT", url, headers=headers, params = querystring, verify=False)
except requests.exceptions.RequestException as e:
    logging.error(str(e))
    sys.exit("RequestException")

if varDebug:
	logging.debug ("response:" + varResponse.text)

if varResponse.raise_for_status():
	logging.error("ERROR communicating to EIP "+str(varResponse.status_code) + varResponse.text)
	sys.exit("ERROR communicating to EIP")

#################
## Be Extreme! ##
#################
