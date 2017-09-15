from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "html.parser" )

soup = BeautifulSoup(open('index.html'), "html.parser" )

#print soup.prettify()
#Tag
print soup.title
#<title>The Dormouse's story</title>


print soup.head
#<head><title>The Dormouse's story</title></head>
print soup.a
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print type(soup.a)
#<class 'bs4.element.Tag'>

print

print soup.name
print soup.head.name
#[document]
#head
print soup.p.attrs
#{'class': ['title'], 'name': 'dromouse'}
print soup.p['class']
#['title']
print soup.p.get('class')
#['title']
soup.p['class']="newClass"
print soup.p
#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

print

#NavigableString
print soup.p.string
#The Dormouse's story
print type(soup.p.string)
#<class 'bs4.element.NavigableString'>

print

#BeautifulSoup
print type(soup.name)
#<type 'unicode'>
print soup.name
# [document]
print soup.attrs
#{} 空字典

print

