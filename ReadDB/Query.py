'''
<p>Query hits from the database.  Reads chrom:start-stop:strand values from
stdin.  Repeats them on stdout along with the hit positions.

u
<p>Usage:
<pre>
 echo "1:100-6000" | python Query.py [--hostname nanog.csail.mit.edu --port 52000 --user foo --passwd bar] [--quiet] --align 100
 </pre>
<ul>
<li>--quiet means don't print any output.  This is useful for testing the query performance
without worrying about the time it takes to print the output.
<li>--wiggle means output in wiggle format
<li>--bed means output in BED format
<li>--type2 means to query the type2 single reads.
<li>--paired means to query the paired reads.
<li>--noheader means to skip printing the input region in the outpu
<li>--right means to query the right side reads rather than left.
</ul>
'''

import argparse

class Query():

    def __init__(self):
        self.alignname = ""
        self.hostname = ""
        self.username = ""
        self.password = ""
        self.portnum = -1
        self.histogram = -1
        self.quiet, self.weights, self.isType2, self.paired, self.isleft, self.noheader, self.bed, self.wiggle = [False]*8

    def parseArgs(self):
        parser = argparse.ArgumentParser(description="Query ReadDB.  Regions are read on STDIN and output is printed on STDOUT.", usage="usage: Query.py --align alignmentname < regions.txt")
        parser.add_argument('-H','--hostname', help='server to connect to', required=True,metavar='')
        parser.add_argument('-P','--port',help='port to connect to',required=True,metavar='')
        parser.add_argument('-a','--align',help='alignment name',required=True,metavar='')
        parser.add_argument('-u','--user',help='username',required=True,metavar='')
        parser.add_argument('-p','--passwd',help='password',required=True,metavar='')
        parser.add_argument('-q','--quiet',help="don't print output",required=False,metavar='')
        parser.add_argument("-w","--weights",required=False,help="get and print weights in addition to positions",metavar='')
        parser.add_argument("-g","--histogram",required=True,help="produce a histogram with this binsize instead of printing all read positions",metavar='')
        parser.add_argument("-t2","--type2",required=False,help="work on type2 single-end alignment?",metavar='')
        parser.add_argument("-d","--paired",required=False,help="work on paired alignment?",metavar='')
        parser.add_argument("-r","--right",required=False,help="query right side reads when querying paired alignments",metavar='')
        parser.add_argument("-N","--noheader",required=False,help="skip printing the query header",metavar='')
        parser.add_argument("-W","--wiggle",required=True,help="output in wiggle format with the specified bin format",metavar='')
        parser.add_argument("-B","--bed",required=False,help="output in BED format",metavar='')
        args = parser.parse_args()

    def printHelp(self):
        print " [--quiet]  don't print any output.  Useful for performance testing without worrying about output IO time"
        print " [--weights] include weights in output or use weights for histogram"
        print " [--type2] query type2 single-end reads"
        print " [--paired] query paired reads"
        print " [--right] when querying paired reads for histograms, use right read rather than left"
        print " [--histogram 10] output a histogram of read counts or weights using a 10bp bin size"
        print " [--noheader] don't output query regions in the output"
        print " [--bed] output hit positions in BED format (doesn't work with paired reads)"
        print " [--wiggle 10] output a histogram in wiggle format with 10bp bin size"
        print ""
        print "Lines in the input should be of them form"
        print "3:1000-2000"
    def run(self):
        return NotImplemented

if __name__=='__main__':
    test = Query()
    test.parseArgs()