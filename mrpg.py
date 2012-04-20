#!/usr/bin/env python

# IdleRPG 2.0
# https://github.com/mozor/idlerpg
#
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

import socket
import sys
import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('idlerpg.cfg')

server = config.get('IRC', 'server')
port = config.getint('IRC', 'port')
channel = config.get('IRC', 'channel')
botnick = config.get('IRC', 'nickname')
host = config.get('Network', 'local_ip')

def ping():
  ircsock.send("PONG :Pong\n")

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

ircsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
ircsock.bind((host, 0))
ircsock.connect((server, port))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Mega Python IdleRPG Master\n")
ircsock.send("NICK "+ botnick +"\n")
time.sleep(5)

joinchan(channel)

while 1:
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r')
  print(ircmsg)

  if ircmsg.find("PING :") != -1:
    ping()
