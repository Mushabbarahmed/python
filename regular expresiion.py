
import re
mystr = '''Tata Limited ai
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281,+91 2072358281,+81 6789054321,+91 8765432192
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Faxan: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiaiinai fax'''
#path=re.compile(r'fass')
#path=re.compile(r'.')                   #(.)prints or finds any character
#path=re.compile(r'adm.')
# path=re.compile(r'^Tata')#(^)find whether its astarts from string(note:string should be same)
# path=re.compile(r'ai$')#($) ends with
#path=re.compile(r'ai*')#(*)zero or more occurense
path=re.compile(r'ai+i')#(+)one or more
# path1=re.compile(r'ai|fax1')
#
# #special sequences
# # path=re.compile(r'\Afax')
# path=re.compile(r'fax\Z')
#path=re.compile(r'\bFax')
path=re.compile(r'\d{4}-\d{4}')
matches=path.finditer(mystr)
for match in matches:
    print(match)
# matches1=path.finditer(mystr)
# for match in matches1:
#      print(match)


# #print(mystr[412, 414])
# numbers='''hi +91-9731597812
# +81-7654321890
# +91-8553883914
# guy humaid and hashim are brother '''
# # pp= re.compile(r'ai{1}')
# # #pp= re.compile(r'\W{1}(91 )\d{10}')
# # matches=pp.finditer(mystr)
# # for match  in matches:
# #     print(match)
# # print(mystr[189: 191])
# p1=re.compile(r'91')
# matches=p1.finditer(numbers)
# for match in matches:
#     print(match)
# re.match