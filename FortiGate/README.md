# ExtremeControl & FortiGate Firewall

_Abstract: How to integrate ExtremeManagement & ExtremeControl with FortiGate Firewall._

## Monitoring by Extreme Management Center
The communication between Extreme Management Center and FortiGate is based on SNMP.

[Details & How-To](monitoring/README.md).

Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* FortiGate: v5.6.2 build1486 (GA)

## User ID to IP mapping through RSSO
The communication between Extreme Management Center and FortiGate is based on Radius Accounting. Radius Accounting messages are originated from Extreme Management Center to enhance the FortiGate user identity information.

[Details & How-To](idtoip/README.md)

[Video how does it work](https://extr.co/2PLpro2)

Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* FortiGate: v5.6.2 build1486 (GA)

## Distributed IPS solutions
FortiGate does inform Extreme Control (part of Management Center) and the threat is quarantined. Syslog message is used for this communication.

[Details & How-To](dips/README.md)

[Video how does it work](https://extr.co/2LFRMsx)

Tested versions:
* Extreme Management Center: 8.0 and 8.1.2.59 and 8.1.3.65
* FortiGate: v5.6.2 build1486 (GA)

# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme