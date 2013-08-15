import urllib2
def run():
	req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%209000011%20FILTER(.02=9000001-198)")
	s1 = urllib2.urlopen(req).read()
	req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%209000010%20FILTER(.05=9000001-198)")
	s2 = urllib2.urlopen(req).read()
	return "[" + s1 + "," + s2 + "]"
