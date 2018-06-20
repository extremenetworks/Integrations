# ExtremeControl & Infoblox

_Abstract: How to integrate ExtremeManagement & ExtremeControl with Infoblox._

## Monitoring by Extreme Management Center
The communication between Extreme Management Center and Infoblox is based on SNMP and API calls (https). API calls are originated from Extreme Management Center to enhance the Infoblox information (Extensible attributes, IP filters). API calls are originated from Infoblox to quarantine the attacker.  
[Details & How-To](monitoring/README.md)
### Tested versions
#### Extreme Management Center: 8.0 and 8.1.2.59
#### Infoblox: 8.2.5-369575


## Information enhancement
With Extreme Control the customer does have visibility of each end-system attached to the network = what devices are in the network and where, what is the actual status. Extreme Control does update Infoblox extensible attributes through the API calls.
For Infoblox objects „Reservation“ and „Host“ the Infoblox operator does get information like:
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
### Tested versions
#### Extreme Management Center: 8.0 and 8.1.2.59
#### Infoblox: 8.2.5-369575

## DHCP pool protection
There are attacks against the DHCP server what can dry the DHCP pool.
* The attacker can change source MAC address = Can be mitigated by authentication or mac lock.
* The attacker can create request where the source MAC not the same as „DHCP client hardware address“ = Advanced DHCP inspection is needed at the switch level or some thresholds are necessary to stop this.
Extreme Control does know what devices are in the network. Extreme Control does maintain the list of connected devices and update this list in the DHCP server.
The result is that DHCP server does not grant IP address to device what is not connected to the network => The DHCP pool is protected.  
[Details & How-To](dhcp/README.md)
### Tested versions
#### Extreme Management Center: 8.0 and 8.1.2.59
#### Infoblox: 8.2.5-369575

## Distributed IPS
DNS attacks are more and more popular. DNS tunneling is very high risk for the company.
Very advanced techniques are necessary to stop such attacks. Infoblox can detect such attack and stop it.
Extreme Control does know what devices are in the network and where those devices are connected (wired port, wireless SSID & AP, VPN, both physical and virtual).
Infoblox solution does inform Extreme Management Center through the API calls about the security incident. 
Extreme Control (part of Extreme Management Center) does quarantine the attacking device at the switch and/or AP level.
The result is that the attack is stopped and attacker is quarantined.  
[Details & How-To](dips/README.md)
### Tested versions
#### Extreme Management Center: 8.0 and 8.1.2.59
#### Infoblox: 8.2.5-369575

# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme