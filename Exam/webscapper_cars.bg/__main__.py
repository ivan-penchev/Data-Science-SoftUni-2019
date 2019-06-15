from http_connection import HttpConnection
from page_parser import PageParser
from link_generator import LinkGenerator
from time import sleep


'''
Generates a link links 
with possible car offer page links to parse
'''
httpCon = HttpConnection()
lg = LinkGenerator()

lg.generateLinks(httpCon, "link_generator_output.txt")


lines = [line.rstrip('\n') for line in open('link_generator_output.txt', encoding='utf-8')]

p = PageParser()

cnt = 0
ls = {}
for line in lines:
    cnt += 1
    content = line.split(',')
    if content[1].strip() in ls:
     print("id " + content[0] + "is found but with "+ls[content[1].strip()])
    else:
     ls[content[1].strip()] = line


if ls:
    cnt = 0
    for key, val in ls.items():
        cnt += 1
        sleep(1)
        c = p.parsePage(url=key)
        if c is not None:
            print("successfully parsed "+key)
            with open('page_parse_log.txt', 'a', encoding='utf-8') as f:
                f.write("{0} \n".format(val, encoding='utf-8'))
            with open('page_parse_output.txt', 'a', encoding='utf-8') as f:
                f.write("{0},\n".format(c.toJSON(), encoding='utf-8'))
        else:
            with open('page_parse_log.txt', 'a', encoding='utf-8') as f:
                f.write("{0} - FAILED PARSING\n".format(val, encoding='utf-8'))

        if  cnt % 10 == 0:
            sleep(20)


