import urllib.request
contents = urllib.request.urlopen(
    'https://stepik.org/media/attachments/lesson/209717/1.html').read().decode('utf-8')
if contents.count('Python') > contents.count('C++'):
    print('Python')
else:
    print('C++')
