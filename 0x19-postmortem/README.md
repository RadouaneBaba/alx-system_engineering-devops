## Postmortem: Web stack debugging #3

### Issue Summary:
- **Duration:**
  - Start time: 2024-02-13 11:00 GMT+1
  - End time: 2024-02-13 16:00 GMT+1
- **Impact:**
  - Apache returning 500 error code
- **root cause:**
  - typo importing "phpp" file instead of "php"

### Timeline:
The issue was detected in the morning when we tried to curl the server and got back 500 server error, at first it was natural to check first if the server is running and that was the case then check if the necessary files exist I have also tried to restart the server to see if I can catch the error but finally using strace I was able to find the issue that was a wrong import specifically wrong file extension.

### Root cause and resolution:
Scanning "strace" on Apache server PID and curl output I found the line (lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffe2351d3d0) = -1 ENOENT (No such file or direct$ry) ) which was repeated multiple times to finally fail and from there it was straight forward I checked if the existing file had a typo but it seemd like it was an import inside wp-settings file with the typo (Error line 137: require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );)
and just by fixing the typo the server was up and running again.

### Corrective and preventative measures:
- To avoid such problems continuous testing is the solution so for every little block of work added a test is required.
- as for tools strace is such great tool to debug such problems.
