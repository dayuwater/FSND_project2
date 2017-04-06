
head = "<svg version=\"1.1\" \
     baseProfile=\"full\"\
     width=\"600\" height=\"400\"\
     xmlns=\"http://www.w3.org/2000/svg\"> \n"

content = "<rect fill=\"#2d3c49\" width=\"600\" height =\"400\"/>"
#content += "<rect fill=\"none\" width=\"100\" height =\"100\" x=\"300\" y=\"200\" stroke=\"#02b3e4\" stroke-width=\"2px\"/>"
for i in range(55,415,10):
    content += "<rect transform=\"rotate({3} 300 200)\" fill=\"none\" width=\"100\" height =\"100\" x=\"300\" y=\"200\" \
    stroke=\"rgb({0},{1},{2})\" stroke-width=\"2px\"/>".format(abs(180-i+55),255-abs(180-i+55),128+abs(180-i+55),i)
    



tail = "</svg>"
result = head + content + tail


f = open('img/flower.svg' , 'w')
f.write(result)

print("a")
