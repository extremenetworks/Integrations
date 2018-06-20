#!/usr/bin/python
## version 2018-06-01

import requests, json, sys, logging
from requests.auth import HTTPBasicAuth

varUsername = "admin"
varPassword = "infoblox"
varInfoBloxIP = "192.168.10.10"
varInfoBloxPort = "443"
varDebug = False
varDebugFile = "XMC2IBfilter.log"
varAddFilterName = "ExtremeControlAutoUpdated"

#########################################
##### Custom tuning above not below #####
#########################################

if varDebug:
    logging.basicConfig(filename=varDebugFile,level=logging.DEBUG)

args = {}
i = 1
while i < len(sys.argv):
    args[sys.argv[i]] = sys.argv[i+1]
    i += 2
if varDebug:
    logging.debug("Attributes received:"+str(sys.argv[1:]))
    logging.debug("Loaded attributes:"+str(args))

#####################
## check arguments ##
#####################


if "Mac" in args.keys():
    varMAC = str(args["Mac"])
else:
    if varDebug:
        logging.error("Missing mandatory argument Mac followed by value.")
    print ("Missing mandatory argument Mac followed by value.")
    sys.exit(1)

if "Status" in args.keys():
    varSTATUS = str(args["Status"])
else:
    if varDebug:
        logging.error("Missing mandatory argument Status followed by value.")
    print ("Missing mandatory argument Status followed by value.")
    sys.exit(1)


#######################################
## check if the MAC is in the filter ##
#######################################

varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/macfilteraddress?_return_fields=&filter='+varAddFilterName+'&mac='+varMAC.lower()

if varDebug:
    logging.debug("requesting: "+varURL)

# call the API to know if it exists and to get the _REF identifier
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

if varSTATUS == "DISCONNECTED":
    # if the object exists and the status is DISCONNECTED then delete the object
    if myResponse.text != "[]":
        # the myResponse does contain [] what we do not like => remove first and last character
        Response = myResponse.text[1:len(myResponse.text)-1]

        jData = json.loads(Response)
        varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/'+jData["_ref"]
        if varDebug:
            logging.debug("DELETEing URL: "+varURL)

        # delete the object from the filter through the API call
        try:
            myResponse = requests.delete(varURL, auth=HTTPBasicAuth(varUsername, varPassword), verify=False)
        except requests.exceptions.RequestException as e:
            logging.error(str(e))
            sys.exit("DeleteException")

        if varDebug:
            logging.debug("response:"+myResponse.text)
    
else:
    # if the object does not exists and the status is not DISCONNECTED then add the object
    if myResponse.text == "[]":

        ################################################
        ## Add the MAC to the macfilteraddress object ##
        ################################################
  
        varURL = 'https://'+varInfoBloxIP+':'+varInfoBloxPort+'/wapi/v2.7/macfilteraddress'
        if varDebug:
            logging.debug("POSTing URL: "+varURL)

        varData = '{"filter":"'+varAddFilterName+'","mac":"'+varMAC+'"}'
        if varDebug:
            logging.debug("POSTing data: "+varData)

        varHeaders = {'Content-Type': 'application/json'}
        if varDebug:
            logging.debug("POSTing headers: "+str(varHeaders))

        # update the object through the API call
        try:
            myResponse = requests.post(varURL, auth=HTTPBasicAuth(varUsername, varPassword), verify=False, data = varData, headers = varHeaders)
        except requests.exceptions.RequestException as e:
            logging.error(str(e))
            sys.exit("RequestException")

        if varDebug:
            logging.debug("response:"+myResponse.text)
    
#################
## Be Extreme! ##
#################
