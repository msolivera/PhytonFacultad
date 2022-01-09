import cgi, cgitb
cgitb.enable()

print ("Content-Type: text/html")
print ("")

params = cgi.FieldStorage()
for paramName in params:
    print (paramName,":",params[paramName].value, "<br/>")
