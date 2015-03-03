import requests
import re


mp3_pattern = 'http://cdn\d*-.*-cfront.infobae.com/media/\d*/.-\d*-\d*-\d*-\d*-\d*-\d*.mp3'

urls = open('l.txt').readlines()

if False:
  bucket = -1
  bucket_file = open('bucket.txt', 'r+')
  lines = bucket_file.readlines()
  if lines:
    bucket = int(lines[0]) + 1
  bucket_file.seek(0)
  bucket_file.write(str(bucket))
  bucket_file.close()

  length = 1000

  start = bucket * length
  end = bucket * length + length
  urls = urls[start:end]

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

for idx, url in enumerate(urls):
  #print idx, url,
  try:
    n = s.get(url)

    mp3 = re.findall(mp3_pattern, n.content)

    name = ''
    if mp3:
      r = s.get(mp3[0])
      name = re.findall('.-\d*-\d*-\d*-\d*-\d*-\d*.mp3', mp3[0])[0]

    line = re.findall('Origen:.*Destino:.*Inicio:.*Fin:.*Calle:.*', n.content)
    if line:
      html = line[0].split('<br>')
      origen = html[0].split(' ')[-1]
      destino = html[1].split(' ')[-1]
      inicio = ' '.join(html[2].split(' ')[-2:])
      fin = ' '.join(html[3].split(' ')[-2:])
      calle = ' '.join(html[5].split(' ')[1:])
      numero = ' '.join(html[6].split(' ')[1:])
      localidad = ' '.join(html[7].split(' ')[1:])
      provincia = ' '.join(html[8].split(' ')[1:])

      print '|'.join([name, origen, destino, inicio, fin, calle, numero, localidad, provincia, url[:-1]])

  except Exception as e:
    #print ' failed'
    #print e
    pass
