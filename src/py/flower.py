head = "<svg version=\"1.1\" \
     baseProfile=\"full\"\
     width=\"600\" height=\"400\"\
     xmlns=\"http://www.w3.org/2000/svg\"> \n"

content = "<rect fill=\"#2d3c49\" width=\"600\" height =\"400\"/>"
content += "<rect fill=\"none\" width=\"100\" height =\"100\" x=\"300\" y=\"200\" stroke=\"#02b3e4\" stroke-width=\"2px\"/>"
for i in range(10,360,10):
    content += "<rect transform=\"rotate({0} 300 200)\" fill=\"none\" width=\"100\" height =\"100\" x=\"300\" y=\"200\" \
    stroke=\"rgb({0},{1},{2})\" stroke-width=\"2px\"/>".format(i,255-i,128+i)
    



tail = "</svg>"
result = head + content + tail


f = open('img/flower.svg' , 'w')
f.write(result)