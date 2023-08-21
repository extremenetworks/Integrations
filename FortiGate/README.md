# ExtremeControl & FortiGate Firewall

_Abstract: How to integrate ExtremeCloud IQ - Site Engine & ExtremeControl with FortiGate Firewall._

## Monitoring by ExtremeCloud IQ - Site Engine
The communication between Site Engine and FortiGate is based on SNMP.

[Details & How-To](monitoring/README.md).

Tested versions:
* Site Engine: 23.7.11
* FortiGate: v5.6.2, 7.2.3

## User ID to IP mapping through RSSO
The communication between Site Engine and FortiGate is based on Radius Accounting. Radius Accounting messages are originated from Site Engine to enhance the FortiGate user identity information.

[Details & How-To](idtoip/README.md)

[Video how does it work](https://extr.co/2PLpro2)

Tested versions:
* Site Engine: 23.7.11
* FortiGate: v5.6.2, 7.2.3

## Distributed IPS solutions
FortiGate does inform Extreme Control (part of Site Engine) and the threat is quarantined. Syslog message is used for this communication.

[Details & How-To](dips/README.md)

[Video how does it work](https://extr.co/2LFRMsx)

Tested versions:
* Site Engine: 23.7.11
* FortiGate: v5.6.2, v6.0.4,  7.2.3

# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme