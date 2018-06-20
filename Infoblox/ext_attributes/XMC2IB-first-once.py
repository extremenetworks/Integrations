#!/usr/bin/python
## version 2018-05-31

import requests, json, sys, argparse, logging
from requests.auth import HTTPBasicAuth

varDebug = False
varUsername = "admin"
varPassword = "infoblox"
varInfoBloxIP = "192.168.10.10"
varInfoBloxPort = "443"
varDebugFile = 'XMC2IB-once.log'

#########################################
##### Custom tuning above not below #####
#########################################

varAttrStatus = "XMC Status"
varAttrAuth = "XMC Authentication Type"
varAttrSwitchIP = "XMC Switch IP"
varAttrSwitchPort = "XMC Switch Port"
varAttrSwitchLocation = "XMC Switch Location"
varAttrProfile = "XMC Profile"
varAttrUser = "XMC User Name"
varAttrReason = "XMC Reason"
varAttrTimeStamp = "XMC Updated"

##########################################################
##### Values above must match those in XMC2IB script #####
##########################################################

if varDebug:
    logging.basicConfig(filename=varDebugFile,level=logging.DEBUG)

varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/extensibleattributedef'
if varDebug:
    logging.debug ("POSTing URL: "+varURL)

varHeaders = {'Content-Type': 'application/json'}
if varDebug:
    logging.debug ("POSTing headers: "+str(varHeaders))

for i in varAttrStatus,varAttrAuth,varAttrSwitchIP,varAttrSwitchPort,varAttrSwitchLocation,varAttrProfile,varAttrUser,varAttrReason,varAttrTimeStamp:
    varData = '{"name":"'+i+'","type":"STRING","comment":"Extreme Control","allowed_object_types":["FixedAddress","HostRecord"]}'
    if varDebug:
        logging.debug ("POSTing data: "+varData)

    # call the API to create extensible attribute
    try:
        myResponse = requests.post(varURL, auth = HTTPBasicAuth(varUsername, varPassword), verify = False, data = varData, headers = varHeaders)
    except requests.exceptions.RequestException as e:
        logging.error (e)
        sys.exit("RequestException")

    if varDebug:
        logging.debug ("response:"+myResponse.text)

    if myResponse.status_code != requests.codes.created:
        logging.warning ("ERROR communicating to InfoBlox "+str(myResponse.status_code)+myResponse.text)
        sys.exit("ERROR communicating to InfoBlox")

print ("#################")
print ("## Be Extreme! ##")
print ("#################")

#################
## Be Extreme! ##
#################
