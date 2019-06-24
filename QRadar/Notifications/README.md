# Sending ExtremeControl End-System information to QRadar

_Abstract: How to integrate ExtremeControl with IBM QRadar_

## Notification Engine
The information is sent from Extreme Management Center to QRadar by syslog messages through Notification Engine. Open the OneView -> Control -> Access Control -> Configuration -> Notifications
Add following rules:

Rule #1:  
Rule Name: `SIEM Notification Registration Syslog`  
Type: `Registration`  
Trigger: `Any`  
Actions: `Syslog to Server(s)`  
Override Content:  
Syslog Tag: `NAC`  
Syslog Message: `RegistrationType=$type,,RegistrationTime=$time,,RegistrationMessage=$message,,RegistrationSource=$source`

Rule #2:  
Rule Name: `SIEM Notification Health Result Syslog`  
Type: `Health Result`  
Trigger: `Any`  
Actions: `Syslog to Server(s)`  
Override Content:  
Syslog Tag: `NAC`  
Syslog Message: `IP=$ipAddress,,MAC=$macAddress,,startScanDate=$startScanDate,,endScanDate=$endScanDate,,assessmentServerName=$assessmentServerName,,assessmentServerIpAddress=$assessmentServerIpAddress,,totalScore=$totalScore,,topScore=$topScore,,testSets=$testSets,,assessmentSummary=$assessmentSummary,,riskLevel=$riskLevel,,riskLevelReason=$riskLevelReason`

Rule #3:  
Rule Name: `SIEM Notification End-System Added Syslog`  
Type: `End-System`  
Trigger: `End-System Added`  
Actions: `Syslog to Server(s)`  
Override Content:  
Syslog Tag: `NAC`  
Syslog Message: `IP=$ipAddress,,MAC=$macAddress,,Username=$username,,Switch=$switchIP,,SwitchPortId=$switchPortId,,Hostname=$hostname,,OS=$operatingSystemName,,State=$state,,ExtendedState=$extendedState,,Reason=$reason,,NACAppliance=$nacApplianceIp`

Rule #4:  
Rule Name: `SIEM Notification End-System Moved Syslog`  
Type: `End-System`  
Trigger: `End-System Moved`  
Actions: `Syslog to Server(s)`  
Override Content:  
Syslog Tag: `NAC`  
Syslog Message: `IP=$ipAddress,,MAC=$macAddress,,Username=$username,,Switch=$switchIP,,SwitchPortId=$switchPortId,,Hostname=$hostname,,OS=$operatingSystemName,,State=$state,,ExtendedState=$extendedState,,Reason=$reason,,NACAppliance=$nacApplianceIp`

Rule #5:  
Rule Name: `SIEM Notification State Change Syslog`  
Type: `End-System`  
Trigger: `State Change`  
Actions: `Syslog to Server(s)`  
Override Content:  
Syslog Tag: `NAC`  
Syslog Message: `IP=$ipAddress,,MAC=$macAddress,,Username=$username,,Switch=$switchIP,,SwitchPortId=$switchPortId,,Hostname=$hostname,,OS=$operatingSystemName,,State=$state,,ExtendedState=$extendedState,,Reason=$reason,,NACAppliance=$nacApplianceIp`

Tested versions:
* Extreme Management Center: 8.2.5.6
* IBM QRadar 7.3


# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme