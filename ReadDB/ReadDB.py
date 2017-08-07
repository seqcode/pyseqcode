from Client import Client
import sys
import argparse

def ReadDB():
	def __init__(self):
		self.client = Client()
		self.otherargs = ""
		self.isType2, self.paired, self.isleft, self.noclose = False, False, False, False

	def parseArgs(self):
		parser = argparse.ArgumentParser(description="ReadDB")
        parser.add_argument('-H','--hostname', help='server to connect to', required=True,metavar='')
        parser.add_argument('-P','--port',help='port to connect to',required=True,metavar='')
        parser.add_argument('-a','--align',help='alignment name',required=True,metavar='')
        parser.add_argument('-u','--user',help='username',required=True,metavar='')
        parser.add_argument('-p','--passwd',help='password',required=True,metavar='')
        parser.add_argument("-t2","--type2",required=False,help="work on type2 single-end alignment?",metavar='', default=False)
        parser.add_argument("-d","--paired",required=False,help="work on paired alignment?",metavar='', default=False)
        parser.add_argument("-r","--right",required=False,help="query right side reads when querying paired alignments",metavar='',default=False)
        args, self.otherargs = parser.parse_known_args()
        hostname, portnum, username, passwd = args['hostname'], args['port'], args['user'], args['passwd']
        if hostname is not None and portnum is not None and username is not None and passwd is not None:
			self.client = Client(hostname=hostname, portnum=portnum, username=username, passwd=passwd)
        self.type2, self.paired, self.isleft = False, False, True
        if args["type2"]:
			type2 = True
        if args["paired"]:
			paired = True
        if args["right"]:
			self.isleft = False
        print self.otherargs

	def run():
		return NotImplemented

if __name__ == "__main__":
	readdb = ReadDB()
	readdb.parseArgs()