import http.client
import mimetypes
conn = http.client.HTTPSConnection("rd-mantis.aoc.com.br", 8080)
payload = ''
headers = {
  'Authorization': 'XFmGfULe09wRwQnfziVd-xq9tZm0WH9Y',
  'Cookie': 'PHPSESSID=notllhqjp9mevigj7c52bfhqo7'
}
conn.request("GET", "/api/rest/issues?project_id71&page_size500&page", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
