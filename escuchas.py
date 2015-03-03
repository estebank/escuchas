import requests
import re

mp3_pattern = 'http://cdn\d*-.*-cfront.infobae.com/media/\d*/.-\d*-\d*-\d*-\d*-\d*-\d*.mp3'

urls = open('l.txt').readlines()

#urls.sort()

#bucket = 1
#buckets = 5
#length = len(urls)/buckets

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
  print idx, url,
  try:
    n = s.get(url)

    mp3 = re.findall(mp3_pattern, n.content)

    if mp3:
      r = s.get(mp3[0])
      name = re.findall('.-\d*-\d*-\d*-\d*-\d*-\d*.mp3', mp3[0])[0]
      print name
      f = open(name, 'wb')
      f.write(r.content)
      f.close()
  except Exception as e:
    print ' failed'
    print e
