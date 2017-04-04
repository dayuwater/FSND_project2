def draw_triangle(p1x,p1y,p2x,p2y,p3x,p3y,iter):
    if iter == 0:
        return ""
    else:
        return draw_triangle((p1x+p2x)/2,(p1y+p2y)/2,p2x,p2y,(p2x+p3x)/2,(p1y+p2y)/2,iter-1)\
               +draw_triangle(p1x,p1y,(p1x+p2x)/2,(p1y+p2y)/2,p2x,p1y,iter-1)\
               +draw_triangle(p2x,p1y,(p2x+p3x)/2,(p1y+p2y)/2,p3x,p3y,iter-1)\
               + "<polygon points=\"{0},{1} {2},{3} {4},{5}\" fill=\"blue\"/>\n" \
               .format((p1x+p2x)/2,(p1y+p2y)/2,p2x,p1y,(p2x+p3x)/2,(p1y+p2y)/2)

head = "<svg version=\"1.1\" \
     baseProfile=\"full\"\
     width=\"600\" height=\"400\"\
     xmlns=\"http://www.w3.org/2000/svg\"> \n"

content = "<polygon points=\"0,400 300,0 600,400\" />\n"
content += draw_triangle(0,400,300,0,600,400,3)


tail = "</svg>"
result = head + content + tail


f = open('img/triangle.svg' , 'w')
f.write(result)