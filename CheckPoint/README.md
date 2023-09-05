# ExtremeControl & Check Point Firewall

_Abstract: How to integrate ExtremeCloud IQ - Site Engine & ExtremeControl with Check Point Firewall._

## Monitoring by ExtremeCloud IQ - Site Engine
The communication between ExtremeCloud IQ - Site Engine and Check Point is based on SNMP.

[Details & How-To](monitoring/README.md).

Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* Check Point: GAIA R80.10

## Username to IP mapping through RSSO = Identity Awareness
The communication between ExtremeCloud IQ - Site Engine and Check Point is based on Radius Accounting. Radius Accounting messages are originated from Extreme Management Center to enhance the Check Point user identity information.

[Details & How-To](idtoip/README.md)

[Video how does it work](https://extr.co/2vPQ6rv)

Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* Check Point: GAIA R80.10

## Distributed IPS solutions
Check Point does inform Extreme Control (part of ExtremeCloud IQ - Site Engine) and the threat is quarantined. Syslog message is used for this communication.

[Details & How-To](dips/README.md)

[Video how does it work](https://extr.co/2PbNQlv)

Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* Check Point: GAIA R80.10

## Username to IP mapping through API = Identity Awareness
The communication between ExtremeCloud IQ - Site Engine and Check Point is based on API calls (https). API calls are originated from ExtremeCloud IQ - Site Engine to enhance the Check Point user identity information.

[Documentation](https://emc.extremenetworks.com/content/oneview/docs/connect/docs/l_ov_connect_security.htm#Check)

[WebAPI settings](idtoip/WebAPI.png?raw=true)

# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme