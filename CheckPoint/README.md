# ExtremeControl & Check Point Firewall

_Abstract: How to integrate ExtremeManagement & ExtremeControl with Check Point Firewall._

## Monitoring by Extreme Management Center
The communication between Extreme Management Center and Check Point is based on SNMP.
[Details & How-To](monitoring/README.md).
Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* Check Point: GAIA R80.10

## User ID to IP mapping through RSSO
The communication between Extreme Management Center and Check Point is based on Radius Accounting. Radius Accounting messages are originated from Extreme Management Center to enhance the Check Point user identity information.
[Details & How-To](idtoip/README.md).
Tested versions
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* Check Point: GAIA R80.10

## User ID to IP mapping through API
The communication between Extreme Management Center and Check Point is based on API calls (https). API calls are originated from Extreme Management Center to enhance the Check Point user identity information.
[Documentation](https://emc.extremenetworks.com/content/oneview/docs/connect/docs/l_ov_connect_security.htm#Check)
[WebAPI settings](idtoip/WebAPI.png?raw=true)

# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme