# ExtremeControl & EfficientIP

>Powered by S. Harrer [Bell Computer-Netzwerke GmbH](http://www.bell.de/)

_Abstract: How to integrate ExtremeManagement & ExtremeControl with EfficientIP._


## Information enhancement
With Extreme Control the customer does have visibility of each end-system attached to the network. Extreme Control does update EfficientIP Custom Classes through the API calls.
For EfficientIP objects fixed "Addresses“ and „Static DHCP Entries“ the EfficientIP operator does get information like:
*	Status = Accept / Disconnected / Quarantine / Assessing / Error / Reject
*	Authentication Type = 802.1X / MAC 
*	Switch IP = IP address of the switch
*	Switch Port = Port description and name / AP name + BSSID + SSID
*	Switch Location = SNMP location
*	Access Profile = Name of the profile used as network access authorization 
*	Username = Name of the logged in user
*	Reason = Name of the access control rule what authorized the end-system
*	Last seen time = When the information was last updated  
All those attributes can be used for search in Infoblox GUI.

[Details & How-To](ext_attributes/README.md)
Tested versions:
* Extreme Management Center: 8.1 and 8.3
* EfficientIP: 7.1.0a


# Support
_The software is provided as-is and neither [Extreme Networks](http://www.extremenetworks.com/) nor [Bell Computer-Netzwerke GmbH](http://www.bell.de/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) or [Bell Computer-Netzwerke GmbH](http://bell.de) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme
 
