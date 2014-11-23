avsend
======

Sends YNCA commands via TCP to Yamaha AV Receiver models RX-V673, RX-A720, RX-V773, RX-A820, RX-A1020 etc. for Home Automation.

Usage:

    avsend.py [-h] [-v] [-u UNIT] -c COMMAND [ARGUMENTS] 

Flags:

    -h, --help        print this help and exit
    -v, --verbose     verbose output
    -a, --address     specify Receiver network name or IP (default is "RX-A820")
    -u, --unit        specify a subunit: main, sys, zone2, tun, server, netradio, usb, ipodusb, airplay etc. Defaults to main
    -c, --command     command to send, e. g. vol, inp, mute, enhancer, soundprg, etc.
    ARGUMENTS defaults to ?

Examples:

    avsend -c vol         (same as avsend -c vol ?)
    avsend -c vol Up
    avsend -c vol -45.0   (be CAREFUL with positive numbers here!)
    avsend -c vol Up 5 dB
    avsend -c mute On
    avsend -c mute Off
    avsend -c inp HDMI1
    avsend -c soundprg 7ch Stereo
    avsend -u server -c repeat All
    avsend -u server -c shuffle On
    avsend -u zone2 -c pwr On
    avsend -u sys -c party On

For a complete list of available commands see http://thinkflood.com/media/manuals/yamaha/Yamaha-YNCA-Receivers.pdf

Please modify the variable TCP_IP in this script to point at your receiver's ip (eg. '192.168.0.123').

Default port is 50000 and should work out of the box.
