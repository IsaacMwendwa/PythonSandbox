import facebook
import json

# A helper function to pretty-print Python objects as JSON
def pp(o):
    print json.dumps(o,indent=1)

# Create a connection to the Graph API with your access token

ACCESS_TOKEN = 'CAACEdEose0cBALtboCin4KD7UoO9W42BJTJxqmdIWmtZBrRAdoK3V9tY5G7khtqP7VGdDJ4BWWuzTQGU2CdBPLBjjuxoF0uHnitl2RvkZBrL6QyCeLvRYwNeZBJjyzczVlsjQIZA94vTtoOUkYERW8l2xh7s5LTuIa81vcHHQxmmJSAxxKs5nATimWdaXc5GDm064F3HpSUtPKQmbLkpwAGLjUNugXUZD'

g = facebook.GraphAPI(ACCESS_TOKEN)

# Execute queries
print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me','friends'))
print
print '---------------'
print 'Social Web'
print '---------------'
pp(g.request("search",{'q' : 'social web', 'type':'page'}))
_id = '106176762746631'
#pp(g.get_object(_id))
# MTSW catalog link
pp(g.get_object('http://shop.oreilly.com/product/0636920030195.do'))
# PCI catalog link
pp(g.get_object('http://shop.oreilly.com/product/9780596529321.do'))
