
import json

with open('convertcsv-7.json') as json_data:
    j = json.load(json_data)

print "["

for k in j:
    language = k['Languages']
    location = k['Location']
    speakers = "\"speakers\":[[2007,"+k['Speakers 2007']+"],[2008,"+k['Speakers 2008']+"],[2009,"+k['Speakers 2009']+"],[2010,"+k['Speakers 2010']+"],[2011,"+k['Speakers 2011']+"],[2012,"+k['Speakers 2012']+"],[2013,"+k['Speakers 2013']+"],[2014,"+k['Speakers 2014']+"],[2015,"+k['Speakers 2015']+"]],"
    articles = "\"articles\":[[2007,"+k['Articles 2007']+"],[2008,"+k['Articles 2008']+"],[2009,"+k['Articles 2009']+"],[2010,"+k['Articles 2010']+"],[2011,"+k['Articles 2011']+"],[2012,"+k['Articles 2012']+"],[2013,"+k['Articles 2013']+"],[2014,"+k['Articles 2014']+"],[2015,"+k['Articles 2015']+"]],"
    users = "\"users\":[[2007,"+k['Users 2007']+"],[2008,"+k['Users 2008']+"],[2009,"+k['Users 2009']+"],[2010,"+k['Users 2010']+"],[2011,"+k['Users 2011']+"],[2012,"+k['Users 2012']+"],[2013,"+k['Users 2013']+"],[2014,"+k['Users 2014']+"],[2015,"+k['Users 2015']+"]]},"
    print "{\"language\":\""+language+"\","
    print "\"location\":\""+location+"\","
    print speakers
    print articles
    print users
    
print "]"
