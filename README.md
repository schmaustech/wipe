$ ./kni-wipe.py -h
usage: kni-wipe.py [-h] -ip IP -u U -p P -t T

Python script using Redfish API which will delete any virtual drives, then
secure erase all drives on host and finally re-establish the virtual drive

optional arguments
  -h, --help  show this help message and exit
  -ip IP      iDRAC/ILOM/BMC IP address
  -u U        iDRAC/ILOM/BMC username
  -p P        iDRAC/ILOM/BMC password
  -t T        Vendor Hardware Type DELL|HP|OTHER
