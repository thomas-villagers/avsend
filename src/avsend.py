#!/usr/bin/env python

import socket, sys, getopt

TCP_IP = '192.168.2.157'
TCP_PORT = 50000
BUFFER_SIZE = 1024

def usage():
        print "Usage: avsend.py [-h] [-v] [-u UNIT] -c COMMAND [ARGUMENTS]" 
        print "Send YNCA commands via TCP to Yamaha AV Receiver models RX-V673, RX-A720, RX-V773, RX-A820, RX-A1020 etc."
        print "" 
        print "Flags:" 
	print "-h, --help        print this help and exit" 
        print "-v, --verbose     verbose output"
        print "-u, --unit        specify a subunit: main, sys, zone2, tun, server, netradio, usb, ipodusb, airplay etc. Defaults to main"
        print "-c, --command     command to send, e. g. vol, inp, mute, enhancer, soundprg, etc."
        print "ARGUMENTS defaults to ?"
        print ""
        print "Examples:"
        print "avsend -c vol         (same as avsend -c vol ?)"
        print "avsend -c vol Up"
        print "avsend -c vol -45.0   (be CAREFUL with positive numbers here!)"
        print "avsend -c vol Up 5 dB"
        print "avsend -c mute on"
        print "avsend -c mute off"
        print "avsend -c inp HDMI1"
        print "avsend -c soundprg 7ch Stereo" 
        print "avsend -u server -c repeat All"
        print "avsend -u server -c shuffle On"
	print "avsend -u zone2 -c pwr On"
	print "avsend -u sys -c party On"
        print ""
        print "For a complete list of available commands see http://thinkflood.com/media/manuals/yamaha/Yamaha-YNCA-Receivers.pdf"
        print ""
        print "Please modify the variable TCP_IP in this script to point at your receiver's ip (eg. '192.168.0.123')"
        print "Default port is 50000 and should work out of the box."
        sys.exit(2)

def sendMessage(unit, command, arguments, verbose):
        msg = unit + ":" + command + "=" + arguments
	if verbose: 
	        print "send command " +  msg + " to " + TCP_IP + " port", TCP_PORT
        msg +=  "\r\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(msg)
        data = s.recv(BUFFER_SIZE)
        s.close
	print data.rstrip()

def main(argv):
        unit = "@MAIN"
        arguments = "?"
        command = ""
	verbose = False;
        for i,arg in enumerate(argv):
                try:
                        f = float(arg)
                        if f < 0:
                                argv.insert(i, "--")
                        break;
                except ValueError:
                        pass

        try:
                opts, args = getopt.getopt(argv,"hvu:c:",["help","verbose","unit=","command="])
        except getopt.GetoptError:
                usage()
        if len(args) > 0:
                arguments = ' '.join(args)

        for opt, arg in opts:
		if opt in ("-v", "--verbose"):
			verbose = True;
                if opt in ("-h", "--help"):
                        usage()
                if opt in ("-u", "--unit"):
                        unit = "@" + arg.upper()
                if opt in ("-c", "--command"):
                        command = arg.upper()
        if len(command) == 0:
                print "Command is missing."
                usage()

        sendMessage(unit, command, arguments, verbose)

if __name__ == "__main__":
        main(sys.argv[1:])

