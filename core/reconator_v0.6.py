#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nmap
import sys
import multiprocessing
import subprocess
import re
import csv
import os

<<<<<<< HEAD
<<<<<<< HEAD
#do http enumeration
def httpenum(targets):
#    NIKTOSCAN =  "nikto --host %s -p %s |tee  %s.nikto  " % (targets, ports,targets)
    NIKTOSCAN =  "nikto --host %s  |tee  %s.nikto  " % (targets, targets)
    WHATWEB = "whatweb http://%s" %(targets,targets)
    SSLSCAN = "sslscan %s |tee %s.sslscan" %(targets,targets)


=======
def multproc(targetin, scanip , port):
=======
def multproc:
>>>>>>> dev
    jobs = []
    p =multiprocessing.Proces(target=)

def httpenum(targets):
<<<<<<< HEAD
    NIKTOSCAN =
>>>>>>> dev

=======
    print("2DO NIKTOSCAN" )
    subprocess.call("'/home/toxic/workspace/reconator/core/proof.sh' %s" % str(host))
>>>>>>> dev


# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = nmap.PortScanner()
    nm.scan(hosts=targets, arguments='-sV -sT -T5 -vvv -Pn -oN "/tmp/reconator_%s"' % targets)
    ip  = str(nm.all_hosts())
    print(ip)
#   subprocess.process()
    print('----------------------------------------------------')
    print("CSV")
    print('----------------------------------------------------')
    print(nm.csv())
    print('----------------------------------------------------')
    ncsv = nm.csv()
    r = csv.reader(ncsv)
    nmenm = '/tmp/nm_reco_%s' % targets
    f = open(nmenm, 'w')
    f.write(ncsv)
    f.close()
    print('----------------------------------------------------')
    print("write nm_reco_*")
    print('----------------------------------------------------')
#    subprocess.call("/home/toxic/workspace/reconator/core/format_nm.sh")

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Hostname')
        print('----------------------------------------------------')
        print('Host : {0} ({1})'.format(host, nm[host].hostname()))
        print('----------------------------------------------------')
        print("nm[host][proto].keys() lport sort")
        print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
        print('----------------------------------------------------')


#TODO fix lauch script write file

#    fncsv = ncsv.split("\n", 1)[1:]
    fncsv = ncsv.split("\n",1)
    print('----------------------------------------------------')
    print('csv')
    print('----------------------------------------------------')
    print(ncsv)
    print('----------------------------------------------------')

    for row in fncsv :
        if "http" in row:
            print(row)
            print("GOTCHA HTTP !!!!!")
#            print("launch nikto...")
            for host in nm.all_hosts():
<<<<<<< HEAD
                    print("launch  proof %s " % str(host))
                    subprocess.call("/home/toxic/workspace/reconator/core/proof.sh %s" % host)


           # try:
            #subprocess.call('/usr/bin/nikto %s ' % host)
            #subprocess.call('echo zob > "/tmp/recotouch" ')
#            subprocess.call("/home/toxic/workspace/reconator/core/proof.sh %s" % host)
=======
                print("launch  proof %s " % str(host))
                multproc(httpenum, host)
                # try:
            #subprocess.call('/usr/bin/nikto %s ' % host)
            #subprocess.call('echo zob > "/tmp/recotouch" ')
<<<<<<< HEAD
            fproof = "/home/toxic/workspace/reconator/core/proof.sh  %s" % str(host)
            subprocess.check_output(fproof, Shell= True)
>>>>>>> dev
=======
>>>>>>> dev

            #except:
             #   print('vnikto failed')
        else:
            print("pas de http")
            print('----------------------------------------------------')

       # matchttp = re.search(r'http', str(row))
    print('###########################################################')



    return parsed


if __name__ == "__main__":
#    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    f =open(sys.argv[1],   'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
    f.close()
