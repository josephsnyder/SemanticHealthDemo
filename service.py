import urllib2
def run(patientIEN=198):
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%209000011%20FILTER(.02=9000001-"+patientIEN+")")
  s1 = urllib2.urlopen(req).read()
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%209000010%20FILTER(.05=9000001-"+patientIEN+")")
  s2 = urllib2.urlopen(req).read()
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%20120_5%20FILTER(.02=2-"+patientIEN+")")
  s3 = urllib2.urlopen(req).read()
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%20120_8%20FILTER(.01=2-"+patientIEN+")")
  s4 = urllib2.urlopen(req).read()
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%2052%20FILTER(2=2-"+patientIEN+")")
  s5 = urllib2.urlopen(req).read()
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%209000010_11%20FILTER(.02=9000001-"+patientIEN+")")
  s6 = urllib2.urlopen(req).read()
  req = urllib2.Request(url="http://www.semantichealthcare.info/fmqlEP?fmql=DESCRIBE%209000010_18%20FILTER(.02=9000001-"+patientIEN+")")
  s7 = urllib2.urlopen(req).read()
  return "[" + s1 + "," + s2 + "," + s3 + "," + s4  + "," + s5 + "," + s6 + "," + s7 +"]"
