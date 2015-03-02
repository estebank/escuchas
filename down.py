import requests
import re

url = 'http://www.infobae.com/2014/11/26/1708428-escuchas-causa-nisman-b-1009-2014-11-26-215804-30'
url_pattern = 'http://www.infobae.com/\d*/\d*/\d*/\d*-escuchas-causa-nisman-.-\d*-\d*-\d*-\d*-\d*-\d*'

next_page_pattern = 'http://www.infobae.com/temas/escuchas-causa-nisman-...../\d*'

#n = requests.get('http://www.infobae.com/archivos-de-nisman')
# el sitemap tiene algunas de las urls y la pagina archivos-de-nisman no esta andando ahora

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

n = s.get('http://www.infobae.com/sitemap.xml')
print n


urls = list(re.findall(url_pattern, n.content))

print '\n'.join(urls)

exit()

i = 0

while urls:
  i += 1
  n = requests.get('http://www.infobae.com/archivos-de-nisman/%d' % i)
  urls = list(re.findall(url_pattern, n.content))
  print len(urls)
  exit()
  print '\n'.join(urls)
