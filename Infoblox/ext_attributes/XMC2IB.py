#!/usr/bin/python
## version 2018-05-31

import requests, json, sys, logging
from requests.auth import HTTPBasicAuth

varUsername = "admin"
varPassword = "infoblox"
varInfoBloxIP = "192.168.10.10"
varInfoBloxPort = "443"
varDebug = False
varDebugFile = "XMC2IB.log"

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

#####################################################
##### Values above must match those in InfoBlox #####
#####################################################

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
## check arguments and prepare Extensible Attributes Structure ##
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

###########################################
## test if the MAC is in the HOST object ##
###########################################

varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/record:host?_return_fields=&mac='+varMAC.lower()
if varDebug:
    logging.debug("requesting: "+varURL)

# call the API to get the _REF identifier
try:
    myResponse = requests.get(varURL, auth=HTTPBasicAuth(varUsername, varPassword), verify=False)
except requests.exceptions.RequestException as e:
    logging.error(str(e))
    sys.exit("RequestException")

if varDebug:
    logging.debug("response:"+myResponse.text)

if myResponse.status_code != requests.codes.ok:
    logging.error("ERROR communicating to InfoBlox "+str(myResponse.status_code)+myResponse.text)
    sys.exit("ERROR communicating to InfoBlox")

if myResponse.text != "[]":
    # the myResponse does contain [] what we do not like => remove first and last character
    Response = myResponse.text[1:len(myResponse.text)-1]

    jData = json.loads(Response)
    varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/'+jData["_ref"]
    if varDebug:
        logging.debug ("PUTing URL: "+varURL)

    varData = '{"extattrs+":'+str(varExtensibleAttr).replace("'",'"')+',"comment":"XMC updated"}'
    if varDebug:
        logging.debug ("PUTing data: "+varData)

    varHeaders = {'Content-Type': 'application/json'}
    if varDebug:
        logging.debug ("PUTing headers: "+str(varHeaders))

    # update the object through the API call
    try:
        myResponse = requests.put(varURL, auth=HTTPBasicAuth(varUsername, varPassword), verify=False, data = varData, headers = varHeaders)
    except requests.exceptions.RequestException as e:
        logging.error(str(e))
        sys.exit("RequestException")

    if varDebug:
        logging.debug ("response:"+myResponse.text)

###################################################
## test if the MAC is in the FIXEDADDRESS object ##
###################################################

varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/fixedaddress?_return_fields=&mac='+varMAC.lower()
if varDebug:
    logging.debug ("requesting: "+varURL)

# call the API to get the _REF identifier
try:
    myResponse = requests.get(varURL, auth=HTTPBasicAuth(varUsername, varPassword), verify=False)
except requests.exceptions.RequestException as e:
    logging.error(str(e))
    sys.exit("RequestException")

if varDebug:
    logging.debug ("response:"+myResponse.text)

if myResponse.status_code != requests.codes.ok:
    logging.error ("ERROR communicating to InfoBlox "+str(myResponse.status_code)+myResponse.text)
    sys.exit("ERROR communicating to InfoBlox")

if myResponse.text != "[]":
    # the myResponse does contain [] what we do not like => remove first and last character
    Response = myResponse.text[1:len(myResponse.text)-1]

    jData = json.loads(Response)
    varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/'+jData["_ref"]
    if varDebug:
        logging.debug ("PUTing URL: "+varURL)

    varData = '{"extattrs+":'+str(varExtensibleAttr).replace("'",'"')+',"comment":"XMC updated"}'
    if varDebug:
        logging.debug ("PUTing data: "+varData)

    varHeaders = {'Content-Type': 'application/json'}
    if varDebug:
        logging.debug ("PUTing headers: "+str(varHeaders))

    # update the object through the API call
    try:
        myResponse = requests.put(varURL, auth=HTTPBasicAuth(varUsername, varPassword), verify=False, data = varData, headers = varHeaders)
    except requests.exceptions.RequestException as e:
        logging.error(str(e))
        sys.exit("RequestException")

    if varDebug:
        logging.debug ("response:"+myResponse.text)

#################
## Be Extreme! ##
#################
