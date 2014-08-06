import requests
import time

site_details={
"BCBSAL":[{"NP":"https://bcbsal.zeomega.org/"},{"PP":"https://bcbsalpp.zeomega.org/"},{"MP":" https://bcbsalmp.zeomega.org/"},{"IP":"https://bcbsalint.zeomega.org/"},{"SIS":"http://192.168.15.172:9080/cms/ZeUI"}],
"BCBSAL_puppet":[{"NP":" https://bcbsal2.zeomega.org/"},{"PP":"https://bcbsal2pp.zeomega.org/"},{"MP":"https://bcbsal2mp.zeomega.org/"}],
"BCBSLA":[{"NP":"https://bcbsla.zeomega.org/"},{"PP":"https://bcbslapp.zeomega.org/"},{"SIS":"http://192.168.15.174:9080/cms/ZeUI"}],
"BCI":[{"NP":"https://bci.zeomega.org/"},{"PP":"https://bcipp.zeomega.org/"},{"MP":"https://bcimp.zeomega.org/"},{"SIS":" http://192.168.15.175:9080/cms/ZeUI"}]}

username='zeadmin'
password='Jiva@123'
import pdb;pdb.set_trace()

for client in site_details.iterkeys():
    length=len(site_details[client])
    for i in range(0,length):
        for module in site_details[client][i].iterkeys():
            for site_values in site_details[client][i].itervalues():
                try:
                    r=requests.get("%s" % site_values,auth=(username,password),verify=False,timeout=5)
                    time.sleep(2)
                    if r.status_code == 200:
                        print "The %s portal is Up and working fine for client %s URL: %s" % (module,client,site_values)
                    else:
                        print "The %s portal is down for client %s URL:%s " % (module,client,site_values)
                except Exception:
                    print "Cannot find URL for %s portal for client %s URL:%s " % (module,client,site_values)

