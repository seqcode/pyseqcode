def Request():
    def __init__(self):
        self.map = {}
        self.list = []
        self.type = None
        self.alignid = None
        self.chromid = None
        self.start = None
        self.end = None
        self.isPaired = None
        self.isLeft = True
        self.isPlusStrand = None
        self.isType2 = None
        self.minWeight = None
    
    def clear(self):
        self.type = None
        self.alignid = None
        self.chromid = None
        self.start = None
        self.end = None
        self.isPaired = None
        self.isLeft = True
        self.isPlusStrand = None
        self.isType2 = None
        self.minWeight = None
        self.map = {}
        self.list = []
    def parse(self, requests):
        '''parses from a list of strings in the same format as toString() outputs.
           returns null on success or an error message on failure.
        '''
        self.clear()
        for s in requests:
            pieces = s.split("\\s*=\\s*")
            if len(pieces) == 2:
                if pieces[0] == "alignid":
                    self.alignid = pieces[1]
                elif pieces[0] == "requesttype":
                    self.type = pieces[1]
                elif pieces[0] == "chromid":
                    try:
                        self.chromid = int(pieces[1])
                    except:
                        return("invalid number for chromid " + pieces[1])
                elif pieces[0] == "start":
                    try:
                        self.start = int(pieces[1])
                    except:
                        return("invalid number for start " + pieces[1])
                elif pieces[0] == "end":
                    try:
                        self.end = int(pieces[1])
                    except:
                        return("invalid number for end " + pieces[1])
                elif pieces[0] == "ispaired":
                    self.isPaired = bool(pieces[1])
                elif pieces[0] == "isleft":
                    self.isLeft = bool(pieces[1])
                elif pieces[0] == "isplusstrand":
                    self.isPlusStrand = bool(pieces[1])
                elif pieces[0] == "istype2":
                    self.isType2 = bool(pieces[1])
                elif pieces[0] == "minweight":
                    try:
                        self.minWeight = float(pieces[1])
                    except:
                        return("invalid minweight " + pieces[1])
                else:
                    self.map[pieces[0]] = pieces[1]
            elif len(pieces) == 1:
                self.list.append(s)
            else:
                return("invalid number of fields on line " + s)
        if self.type == None:
            return("must provide a request type")
        if self.isPaired == None:
            self.isPaired = False
        if self.isType2 == None:
            self.isType2 = False
        if self.isPaired == None and self.isLeft == None:
            return("must provide isleft when providing is paired")
        if not self.isPaired:
            self.isLeft = False
        
        return None
    def toString(self):
        out = ""
        if self.type != None:
            out += ("requesttype=" + self.type +  "\n")
        else:
            assert "no request type"
        if self.alignid != None:
            out += ("alignid=" + self.alignid + "\n")
        if self.chromid != None:
            out += ("chromid=" + self.chromid + "\n")
        if self.start != None:
            out += ("start=" + self.start + "\n")
        if self.end != None:
            out += ("end=" + self.end + "\n")
        if self.isPaired != None:
            out += ("ispaired=" + str(self.isPaired).lower() + "\n")
        if self.isLeft != None:
            out += ("isleft=" + str(self.isLeft).lower() + "\n")
        if self.isPlusStrand != None:
            out += ("isplusstrand=" + str(self.isPlusStrand).lower() + "\n")
        if self.isType2 != None:
            out += ("istype=" + str(self.isType2).lower() + "\n")
        if self.minWeight != None:
            out += ("minweight=" + self.minWeight + "\n")
        
        for key, value in self.map.iteritems():
            out += (key + "=" + value + "\n")
        for item in self.list:
            out += (item + "\n")
        out += "ENDREQUEST\n"

        return out
    

                