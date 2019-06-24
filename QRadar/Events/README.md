# Sending internal Events to QRadar

_Abstract: How to integrate Extreme Management Center with IBM QRadar_

## Notification Engine
The information is sent from Extreme Management Center to QRadar by syslog messages through build in rsyslogd. Open the terminal access to the Extreme Management Center. 
1. Create file /etc/rsyslog.d/10-remote.conf
   ```Bash
   cat > /etc/rsyslog.d/10-remote.conf
   module(load="imfile" PollingInterval="1" mode="inotify") input(type="imfile" file="/usr/local/Extreme_Networks/NetSight/appdata/logs/admin.log" 
      tag="xmc-admin-log" 
      severity="info" 
      facility="local6" 
      PersistStateInterval="10" 
   ) 
   local6.info             @@<IP-of-your-QRadar>:514 
   & stop 
   ```
2. You may repeat step above for following files:  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/appid.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/console.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/fabricManager.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/Governance.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/inventory.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/nacApplianceEvent.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/nsschedule.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/Policy.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/tamAudit.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/tam.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/wireless.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/wirelessAudit.log`  
   `/usr/local/Extreme_Networks/NetSight/appdata/logs/wirelessEvent.log`
3. Restart the rsyslogd
   ```Bash
   service rsyslog restart
   ```

Tested versions:
* Extreme Management Center: 8.2.5.6
* IBM QRadar 7.3


# Support
_The software is provided as-is and [Extreme Networks](http://www.extremenetworks.com/) has no obligation to provide maintenance, support, updates, enhancements, or modifications. Any support provided by [Extreme Networks](http://www.extremenetworks.com/) is at its sole discretion._

Issues and/or bug fixes may be reported on [The Hub](https://community.extremenetworks.com/extreme).

>Be Extreme