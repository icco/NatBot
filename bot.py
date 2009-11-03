#!/usr/bin/env python

import sys
import socket
import string

HOST="irc.freenode.net"
PORT=6667
NICK="icco-server"
IDENT="Byahh"
REALNAME="Nat"
CHAN="#cpglug"

# This is where we will come up with responses
def parseLine(msg, s):
   msg = string.rstrip(msg)
   msg = string.split(msg)

   if(msg[0] == "PING"):
      s.send("PONG %s\r\n" % msg[1])

# this is where we will log messages
def logLine(line):
   print line

# The main block of the script.
readbuffer = ""
s = socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello There!"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "I am a bot"))

while 1:
    readbuffer = readbuffer+s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop( )

    for line in temp:
       parseLine(line, s)
       logLine(line)

