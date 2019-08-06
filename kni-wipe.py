#!/usr/bin/env python
#########################################################################################################
#													                                                                              #
# This Python script will look at storage controllers delete any virtual disk and then wipe all disks	  #
#												                                                                              	# 
#########################################################################################################

import requests, json, sys, re, time, warnings, argparse

from datetime import datetime

warnings.filterwarnings("ignore")

parser=argparse.ArgumentParser(description="Python script using Redfish API which will delete any virtual drives, then secure erase all drives on host and finally re-establish the virtual drive")
parser.add_argument('-ip',help='iDRAC/ILOM/BMC IP address', required=True)
parser.add_argument('-u', help='iDRAC/ILOM/BMC username', required=True)
parser.add_argument('-p', help='iDRAC/ILOM/BMC password', required=True)
parser.add_argument('-t', help='Vendor Hardware Type DELL|HP|OTHER', required=True)
args=vars(parser.parse_args())

idrac_ip=args["ip"]
idrac_username=args["u"]
idrac_password=args["p"]
vendor_type=args["t"]

def check_supported_idrac_version():
    response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/Storage' % idrac_ip,verify=False,auth=(idrac_username, idrac_password))
    data = response.json()
    if response.status_code != 200:
        print("\n- ERROR, iDRAC version installed does not support this feature using Redfish API")
        sys.exit()
    else:
        pass

def get_storage_controllers():
    global controller
    raidpattern = re.compile("RAID")
    response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/Storage' % idrac_ip,verify=False,auth=(idrac_username, idrac_password))
    data = response.json()
    controller_list=[]
    for i in data[u'Members']:
        controller_list.append(i[u'@odata.id'].split("/")[-1])
        controller = i[u'@odata.id'].split("/")[-1]
        if raidpattern.search(controller):
            #print"Controller: ",(i[u'@odata.id'].split("/")[-1])
            get_virtual_disks()
        get_controller_disks()

def get_controller_disks():
    global secure_erase_device
    response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/Storage/%s' % (idrac_ip, controller),verify=False,auth=(idrac_username, idrac_password))
    data = response.json()
    drive_list=[]
    if response.status_code != 200:
        print("\n- FAIL, either controller not found on server or typo in controller FQDN name")
        return
    if data[u'Drives'] == []:
        print("\n- WARNING, no drives detected for %s" % controller)
        return
    else:
        print("\n- START CONTROLLER, Drive(s) detected for %s -\n" % controller)
        for i in data[u'Drives']:
            drive = i[u'@odata.id'].split("/")[-1]
            print(drive)
            secure_erase_device = drive
            secure_erase()
            if job_type == "realtime":
                loop_job_status()
            elif job_type == "staged":
                get_job_status()
                reboot_server()
                loop_job_status()
            drive_list.append(drive)

def secure_erase():
    global job_id
    global job_type
    url = 'https://%s/redfish/v1/Systems/System.Embedded.1/Storage/Drives/%s/Actions/Drive.SecureErase' % (idrac_ip, secure_erase_device)
    headers = {'content-type': 'application/json'}
    payload = {}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False,auth=(idrac_username,idrac_password))
    #response = requests.post(url, headers=headers, verify=False,auth=(idrac_username,idrac_password))
    if response.status_code == 202:
        print("\n- COMPLETE: POST command passed to secure erase device \"%s\", status code 202 returned" % secure_erase_device)
    else:
        print("\n- FAIL, POST command failed for secure erase, status code is %s" % response.status_code)
        data = response.json()
        print("\n- POST command failure is:\n %s" % data)
        sys.exit()
    x=response.headers["Location"]
    try:
        job_id=re.search("JID.+",x).group()
    except:
        print("\n- FAIL, unable to create job ID")
        sys.exit()
        
   
    req = requests.get('https://%s/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/%s' % (idrac_ip, job_id), auth=(idrac_username, idrac_password), verify=False)
    data = req.json()
    if data[u'JobType'] == "RAIDConfiguration":
        job_type="staged"
    elif data[u'JobType'] == "RealTimeNoRebootConfiguration":
        job_type="realtime"
    print("- COMPLETE, \"%s\" %s jid successfully created for secure erase drive \"%s\"" % (job_type, job_id, secure_erase_device))

start_time=datetime.now()

def get_virtual_disks():
    global virtual_disk
    response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/Storage/%s/Volumes' % (idrac_ip, controller),verify=False,auth=(idrac_username, idrac_password))
    data = response.json()
    vd_list=[]
    if data[u'Members'] == []:
        print("\n- WARNING, no volume(s) detected for %s" % controller)
        return
    else:
        for i in data[u'Members']:
            vd_list.append(i[u'@odata.id'].split("/")[-1])
    #print("\n- Supported virtual disk(s) detected to delete for controller %s -" % controller)
    #print("\n")
    supported_vds=[]
    volume_type=[]
    for ii in vd_list:
        response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/Storage/Volumes/%s' % (idrac_ip, ii),verify=False,auth=(idrac_username, idrac_password))
        data = response.json()
        for i in data.items():
            if i[0] == "VolumeType":
                if i[1] != "RawDevice":
                    supported_vds.append(ii)
                    volume_type.append(i[1])
                else:
                    pass
    if supported_vds == []:
        print("- WARNING, no virtual disk(s) detected to delete for controller %s" % controller)
    else:
        for i,ii in zip(supported_vds,volume_type):
            print("%s, Volume Type: %s" % (i, ii))
            virtual_disk = i
            delete_vd()
            if job_type == "realtime":
                loop_job_status()
            elif job_type == "staged":
                get_job_status()
                reboot_server()
                loop_job_status()

def delete_vd():
    global job_id
    global job_type
    url = 'https://%s/redfish/v1/Systems/System.Embedded.1/Storage/Volumes/%s' % (idrac_ip, virtual_disk)
    headers = {'content-type': 'application/json'}
    response = requests.delete(url, headers=headers, verify=False,auth=(idrac_username,idrac_password))
    if response.status_code == 202:
        print("\n- COMPLETE: DELETE command passed to delete \"%s\" virtual disk, status code 202 returned" % virtual_disk)
    else:
        print("\n- FAIL, DELETE command failed, status code is %s" % response.status_code)
        data = response.json()
        print("\n- DELETE command failure is:\n %s" % data)
        sys.exit()
    x=response.headers["Location"]
    try:
        job_id=re.search("JID.+",x).group()
    except:
        print("\n- FAIL, unable to create job ID")
        sys.exit()
        
    req = requests.get('https://%s/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/%s' % (idrac_ip, job_id), auth=(idrac_username, idrac_password), verify=False)
    data = req.json()
    if data[u'JobType'] == "RAIDConfiguration":
        job_type="staged"
    elif data[u'JobType'] == "RealTimeNoRebootConfiguration":
        job_type="realtime"
    print("\n- COMPLETE, \"%s\" %s jid successfully created for delete virtual disk\n" % (job_type, job_id))

start_time=datetime.now()

def loop_job_status():
    while True:
        req = requests.get('https://%s/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/%s' % (idrac_ip, job_id), auth=(idrac_username, idrac_password), verify=False)
        current_time=(datetime.now()-start_time)
        statusCode = req.status_code
        if statusCode == 200:
            pass
        else:
            print("\n- FAIL, Command failed to check job status, return code is %s" % statusCode)
            print("Extended Info Message: {0}".format(req.json()))
            sys.exit()
        data = req.json()
        if str(current_time)[0:7] >= "0:90:00":
            print("\n- FAIL: Timeout of 90 minutes has been hit, script stopped\n")
            sys.exit()
        elif "Fail" in data[u'Message'] or "fail" in data[u'Message']:
            print("- FAIL: %s failed" % job_id)
            sys.exit()
        elif data[u'Message'] == "Job completed successfully.":
            print("\n--- COMPLETE, Final Detailed Job Status Results ---\n")
            for i in data.items():
                if "odata" in i[0] or "MessageArgs" in i[0] or "TargetSettingsURI" in i[0]:
                    pass
                else:
                    print("%s: %s" % (i[0],i[1]))
            break
        else:
            #print("- PROGRESS, JobStatus not completed, current status is: \"%s\", percent completion is: \"%s\"" % (data[u'Message'],data[u'PercentComplete']))
            print("- PROGRESS - %s - Percent complete: %s" % (data[u'Message'],data[u'PercentComplete']))
            time.sleep(15)


def get_job_status():
    while True:
        req = requests.get('https://%s/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/%s' % (idrac_ip, job_id), auth=(idrac_username, idrac_password), verify=False)
        statusCode = req.status_code
        if statusCode == 200:
            pass
            time.sleep(5)
        else:
            print("\n- FAIL, Command failed to check job status, return code is %s" % statusCode)
            print("Extended Info Message: {0}".format(req.json()))
            sys.exit()
        data = req.json()
        if data[u'Message'] == "Task successfully scheduled.":
            print("\n- STATUS, staged config job marked as scheduled, power on or rebooting the system to execute config job")
            break
        else:
            print("\n- WARNING: JobStatus not scheduled, current status is: %s\n" % data[u'Message'])

                                                                          
def reboot_server():
    response = requests.get('https://%s/redfish/v1/Systems/System.Embedded.1/' % idrac_ip,verify=False,auth=(idrac_username, idrac_password))
    data = response.json()
    current_power_state = data[u'PowerState']
    if current_power_state == "On":
        url = 'https://%s/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset' % idrac_ip
        payload = {'ResetType': 'ForceOff'}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=(idrac_username,idrac_password))
        statusCode = response.status_code
        if statusCode == 204:
            print("\n- COMPLETE, Command passed to power OFF server, code return is %s\n" % statusCode)
        else:
            print("\n- FAIL, Command failed to power OFF server, status code is: %s\n" % statusCode)
            print("Extended Info Message: {0}".format(response.json()))
            sys.exit()
        time.sleep(10)
        payload = {'ResetType': 'On'}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=(idrac_username,idrac_password))
        statusCode = response.status_code
        if statusCode == 204:
            print("\n- COMPLETE, Command passed to power ON server, code return is %s\n" % statusCode)
        else:
            print("\n- FAIL, Command failed to power ON server, status code is: %s\n" % statusCode)
            print("Extended Info Message: {0}".format(response.json()))
            sys.exit()
    if current_power_state == "Off":
        url = 'https://%s/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset' % idrac_ip
        payload = {'ResetType': 'On'}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=(idrac_username,idrac_password))
        statusCode = response.status_code
        if statusCode == 204:
            print("\n- COMPLETE, Command passed to power ON server, code return is %s\n" % statusCode)
        else:
            print("\n- FAIL, Command failed to power ON server, status code is: %s\n" % statusCode)
            print("Extended Info Message: {0}".format(response.json()))
            sys.exit()

def create_raid_vd():
    global job_id
    global job_type

    controller="RAID.Integrated.1-1"
    disks="Disk.Bay.0:Enclosure.Internal.0-1:RAID.Integrated.1-1,Disk.Bay.1:Enclosure.Internal.0-1:RAID.Integrated.1-1"
    raid_levels={"0":"NonRedundant","1":"Mirrored","5":"StripedWithParity","10":"SpannedMirrors","50":"SpannedStripesWithParity"}
    volume_type=raid_levels["1"]
    
    url = 'https://%s/redfish/v1/Systems/System.Embedded.1/Storage/%s/Volumes' % (idrac_ip, controller)
    disks_list=disks.split(",")
    final_disks_list=[]
    for i in disks_list:
        s="/redfish/v1/Systems/System.Embedded.1/Storage/Drives/"+i
        d={"@odata.id":s}
        final_disks_list.append(d)
    payload = {"VolumeType":volume_type,"Drives":final_disks_list}
    try:
        payload["CapacityBytes"]=vd_size
    except:
        pass
    try:
        payload["OptimumIOSizeBytes"]=vd_stripesize
    except:
        pass
    try:
        payload["Name"]=vd_name
    except:
        pass
    
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False,auth=(idrac_username,idrac_password))
    if response.status_code == 202:
        print("\n- COMPLETE: POST command passed to create \"%s\" virtual disk, status code 202 returned" % volume_type)
    else:
        print("\n- FAIL, POST command failed, status code is %s" % response.status_code)
        data = response.json()
        print("\n- POST command failure is:\n %s" % data)
        sys.exit()
    x=response.headers["Location"]
    try:
        job_id=re.search("JID.+",x).group()
    except:
        print("\n- FAIL, unable to create job ID")
        sys.exit()
        
    req = requests.get('https://%s/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/%s' % (idrac_ip, job_id), auth=(idrac_username, idrac_password), verify=False)
    data = req.json()
    if data[u'JobType'] == "RAIDConfiguration":
        job_type="staged"
    elif data[u'JobType'] == "RealTimeNoRebootConfiguration":
        job_type="realtime"
    print("\n- COMPLETE, \"%s\" %s jid successfully created for create virtual disk" % (job_type, job_id))
    
start_time=datetime.now()

if __name__ == "__main__":
    if vendor_type == "DELL":
        check_supported_idrac_version()
        get_storage_controllers()
        create_raid_vd()
        if job_type == "realtime":
            loop_job_status()
        elif job_type == "staged":
            get_job_status()
            reboot_server()
            loop_job_status()
        sys.exit()
    elif vendor_type == "HP":
        print("\n HP Not Implemented Yet")
        sys.exit()
    else:
        print("\n Other Not Implemented Yet")
        sys.exit()
