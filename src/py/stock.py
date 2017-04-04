import random
def draw_point(x,y,x2,y2):
    out_circle = "<circle cx=\"{0}\" cy=\"{1}\" r=\"6\" fill=\"#2d3c49\"/>".format(x,y)
    in_circle = "<circle cx=\"{0}\" cy=\"{1}\" r=\"3\" fill=\"#02b3e4\"/>".format(x,y)
    line = "<line x1=\"{0}\" y1=\"{1}\" x2=\"{2}\" y2=\"{3}\" stroke=\"#7d97ad\" stroke-width=\"5\"/>".format(x,y,x2,y2)
    return out_circle+in_circle+line

prices=[]
volumes=[]

head = "<svg version=\"1.1\" \
     baseProfile=\"full\"\
     width=\"600\" height=\"400\"\
     xmlns=\"http://www.w3.org/2000/svg\"> \n"

content = "<line x1=\"0\" y1=\"400\" x2=\"0\" y2=\"0\" stroke=\"black\" stroke-width=\"5\"/>"
content += "<line x1=\"0\" y1=\"400\" x2=\"600\" y2=\"400\" stroke=\"black\" stroke-width=\"5\"/>"

for ii, i in enumerate(range(25,575,30)):
    prices.append(random.randint(65,185))
    volumes.append(random.randint(25,85))
    if ii >= 1:
        content += draw_point(i-30,prices[ii-1], i,prices[ii])
    content+="<rect x=\"{0}\" y=\"{1}\" width=\"30\" height=\"{2}\" fill=\"#7d97ad\"/>".format(i-15,400-volumes[ii],volumes[ii])




tail = "</svg>"
result = head + content + tail


f = open('img/stock.svg' , 'w')
f.write(result)