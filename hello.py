def serv(environ, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  start_response(status, headers)
  print(environ)
  #body = str
  return body
