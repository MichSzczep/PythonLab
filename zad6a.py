import xml.dom.minidom as xdm

# Open XML document using minidom parser
doc = xdm.parse("file.xml")
collection = doc.documentElement

players = collection.getElementsByTagName("player")

for player in players:
    print("\n\nScanning player: %s \n" %player.getAttribute("name"))
    
    ptype = player.getElementsByTagName("type")[0].childNodes[0].data
    pyear = player.getElementsByTagName("year")[0].childNodes[0].data
    prate = player.getElementsByTagName("rating")[0].childNodes[0].data
    pstars = player.getElementsByTagName("stars")[0].childNodes[0].data
    pdesc = player.getElementsByTagName("description")[0].childNodes[0].data
    
    print("Changing %s's description\n" %player.getAttribute("name"))
    
    player.getElementsByTagName("description")[0].childNodes[0].nodeValue = "Exceptional Player he is!"
    
    print("Desc before changes: ", pdesc)
    print("Desc after changes: ", player.getElementsByTagName("description")[0].childNodes[0].data)

print("\nWriting changes to a separate file...")

with open('players.xml','w') as f:
    f.write(doc.toxml())
    
print("\nWriting changes finished successfully")