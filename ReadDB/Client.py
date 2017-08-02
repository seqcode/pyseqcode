'''
<p>Python API for remote access to the readdb server.

<p>Calls throw IOException on network errors.
   Calls throw ClientException on other errors (authentication, authorization, invalid request ,etc.

<p>Client generally assumes that the hit positions are the 5' end of the hit. 

<p>Client IS NOT REENTRANT.  Do not overlap calls to a single Client object.

<p>The current version of Client keeps a separate thread that would close the connection if it is idle too long. 
 
<p>Most method parameters that are object types (eg Integer, Boolean) are optional.  If a null value
   is passed then no filtering is done based on that parameter.  

<p>Standard parameters shared across methods:
 <ul>
 <li> alignid is the name of the alignment.
 <li> isType2 specifies whether to work on ordinary single-ended reads (false) or the "type 2" reads (true). 
 		An example of type 2 reads are the R2 reads in paired-end ChIP-exo. 
 <li> isPaired specifies whether to work on single-ended reads (false) or paired-end reads (true)
 <li> isLeft if isPaired is true, then isLeft specifies whether to work on the left read (true)
     or right read (false) of the pair
 <li> plusStrand specifies whether to return only reads on the plus strand (true) or minus strand (false). null
     means that reads on both strands should be returned.
 <li> minWeight specifies the minimum weight of reads (or read pairs) to be returned or included in 
     the histogram
 <li> start, stop specify the lowest (inclusive) and highest (exclusive) coordinates of reads
     that should be included in the results
 </ul>

 
'''
import socket
import struct

class Client():
    def __init__(self,hostname=None, portnum=None, username=None, passwd=None, persistent=False):
        '''Connects to a ReadDB server on the specified host and port using the specified 
           username and password. Or creates the default connection
           as specified by ~/.readdb_passwd or a readdb_passwd found in the classpath
           Must have keys hostname, port, username, and passwd in the format shown in the HOWTO file'''
        _init(hostname, portnum, username, passwd, persistent)
    

    def _init(hostname, portnum, username, passwd, persistent):
        return NotImplemented


    def setPersistentConnection(persistent):
        return NotImplemented
    

    def _openConnection():
        s = socket.socket((hostname,portnum))
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        s.setsockopt(SOL_SOCKET., SO_SNDBUF, 8192*20)
        s.setsockopt(SOL_SOCKET., SO_RCVBUF, 8192*20)
        s.settimeout(6000)
    
    def connectionAlive(self):
        '''Pings the ReadDB server,
        returns ture if the server pongs'''
        return NotImplemented
    

    def getServerInfo(self):
        '''Return some basic information about the server'''
        return NotImplemented
    

    def _authenticate(self,hostname, username, password):
        '''Performs the SASL authentication exchange with the server.'''
        return NotImplemented
    

    def _sendString(self,s):
        '''Sends a string to the server and flushes the socket'''
        return NotImplemented
    

    def _readLine(self):
        '''Reads one line from the server'''
        return NotImplemented
    

    def shutdown(self):
        '''Tells the server to shut itself down.  Use this to stop the server process.'''
        return NotImplemented
    

    def storeSingle(alignid, allhits, isType2):
        '''Stores a set of SingleHit objects (representing an un-paired or single-ended read
           aligned to a genome) in the specified alignment. The hits are appended
           to any hits that have already been stored in the alignment.'''
        return NotImplemented
    

    def storePaired(alignid, allhits):
        '''Stores a set of PairedHit objects (representing an paired-ended read
           aligned to a genome) in the specified alignment.  The hits are appended
            to any hits that have already been stored in the alignment'''
        return NotImplemented
    
    
    def exists(alignid):
        '''Returns true if the alignment and chromosome exist and are accessible
           to the user.  Returns false if they don't exist or if they aren't accessible'''
        return NotImplemented
    

    def deleteAlignment(aligned, isPaired):
        ''' Deletes an alignment (all chromosomes).  isPaired specifies whether to delete
            the paired or single ended reads.'''
        return NotImplemented
    

    def getChroms(alignid, isType2, isPaired, isLeft):
        '''Returns the set of chromosomes that exist for this alignment.'''
        return NotImplemented
    

    def getCount(alignid, isType2, isPaired, isLeft, plusStrand):
        '''Returns the total number of hits in this alignment.'''
        return NotImplemented
    

    def getWeight(alignid, chromid, isType2, plusStrand):
        '''Returns the sum of the weights of all hits in this alignment'''
        return NotImplemented
    

    def getNumPositions(alignid, isType2, isPaired, isLeft, plusStrand):
        '''Returns the total number of unique positions in this alignment.'''
        return NotImplemented
    
    
    def getNumPairedPositions(alignid, isType2, isLeft):
        '''Returns the total number of unique paired positions in this alignment.'''
        return NotImplemented
    

    def getCount(alignid, chromid, isType2, paired, start, stop, minWeight, isLeft, plusStrand):
        '''returns the total number of hits on the specified chromosome in the alignment.
           Any of the object parameters can be set to null to specify "no value"'''
        return NotImplemented
    

    def getWeight(alignid, chromid, isType2, paired, start, stop, minWeight, isLeft, plusStrand):
        '''returns the total weight on the specified chromosome in this alignment'''
        return NotImplemented
    

    def getNumPositions(alignid, chromid, isType2, paired, start, stop, minWeight, isLeft, plusStrand):
        '''returns the total number of unique positions on the specified chromosome in the alignment.
           Any of the object parameters can be set to null to specify "no value"'''
        return NotImplemented
    

    def getNumPairedPositions(alignid, chromid, isType2, start, stop, minWeight, isLeft):
        '''returns the total number of unique paired positions on the specified chromosome in the alignment.
           Note that total number of unique paired positions will depend on the setting of "isLeft",
           e.g. will count pair positions with left read in specified chromosome.
           Any of the object parameters can be set to null to specify "no value"'''
        return NotImplemented
    

    def getPositions(alignid, chromid, isType2, paired, start, stop, minWeight, isLeft, plusStrand):
        '''returns the sorted (ascending order) hit positions in the specified range of a chromosome,alignment pair.'''
        return NotImplemented
    

    def getWeightsRange(alignid, chromid, isType2, paired, start, stop, minWeight, isLeft, plusStrand):
        '''returns the hit weights in the specified range of a chromosome,alignment pair.  The weights
           will be in the same order as the sorted positions returned by getPositions'''
        return NotImplemented
    

    def getSingleHits(alignid, chromid, isType2, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getPairedHits(alignid, chromid, isType2, start, stop, minWeight, plusStrand):
        return NotImplemented
    
    '''
    returns a TreeMap from positions to counts representing a histogram
    of the hits in a range with the specified binsize.  Bins with a count
    of zero are not included in the output.
    minweight is the minimum weight for reads to be included in the histogram.

    dedup is the limit on how many times reads with any given 5' position will be counted.
    A value of zero means no limit.  A limit of, eg, 2, means that at most two reads at
    any 5' position will be included in the output.  For weighted histograms, the choice of reads
    included is unspecified.  For methods that operate on a set of alignments, this many
    reads from each alignment will be included.
    
    Normally, a read is only counted in a single bin as defined by its position (generally
    the 5 end of the read).  A non-zero read-Extension counts the read in any
    bin that you cross within that many bases of the reads position.  A negative value
    goes backwards (smaller coordinates) and a larger value goes forward.  You need
    to get the sign right depending on the strandedness of the chromosome that you're
    working with.
    '''
    def getHistogram(alignid, chromid, isType2, paired, extension, binsize, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getHistogram(alignid, chromid, isType2, paired, extension, binsize, dedup, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getWeightHistogram(alignid, chromid, isType2, paired, extension, binsize, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getWeightHistogram(alignid, chromid, isType2, paired, extension, binsize, dedup, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getHistogram(alignids, chromid, isType2, paired, extension, binsize, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getHistogram(alignids, chromid, isType2, paired, extension, binsize, dedup, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getWeightHistogram(alignids, chromid, isType2, paired, extension, binsize, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getWeightHistogram(alignids, chromid, isType2, paired, extension, binsize, dedup, start, stop, minWeight, plusStrand):
        return NotImplemented
    

    def getACL(alignid):
        '''Returns a Map from READ, WRITE, and ADMIN to lists of principals that have those privileges on the specified alignment.'''
        return NotImplemented
    

    def _fillPartACL(output):
        '''fills one section of the acl output data structure.  A section
           is either read, write, or admin.'''
        return NotImplemented
    

    def setACL(alignid, changes):
        '''Applies the specified ACLChangeEntry objects to the acl for this experiment/chromosome.'''
        return NotImplemented
    
    
    def addToGroup(princ, group):
        '''Adds the specified user (princ) to a group.'''
        return NotImplemented
    

    def close():
        '''Closes this connection to the server.'''
        return NotImplemented
    

    def closeConnection():
        '''Closes this connection to the server.'''
        return NotImplemented
    
