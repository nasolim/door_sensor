#http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup as BS

#########################################
#Status = 0 - Open | Status = 1 - In Use#
#########################################

def unit_Status(Room, Status):

Room_directory={
'War_Room': 0,
'Conference_Room':1,
'Video_Conference_Room':2,
'Creative_Room':3,
'Class_Room':4,
'Library':5,
'Sams_Office':6,
'Interview_Room':7
}

Status=int(Status)

path='/var/www/index.html'

with open(path) as r:
html=r.read()
soup = BS(html)

tag=soup.find_all('div',{"class": Room})


#how to determine index
#how to determine New_Text

styleOpen="Vacant"
styleClosed="Occupied"

if Status==0:
tag[0]['id']=styleOpen
pass

if Status==1:
tag[0]['id']=styleClosed
pass


# Source of info: https://mail.python.org/pipermail/python-list/2011-November/627698.html for converting soup to html
new_html=str(soup)

with open (path,'w') as f:
f.write(new_html)


#########################################
########### function test###############
#########################################