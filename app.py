#import BaseHTTPServer
#import SimpleHTTPServer
#import SocketServer

#PORT = 80

#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#httpd = SocketServer.TCPServer(("", PORT), Handler)
fprint ("WElcome to My Udacity FInal Project..")
#print ("serving at port", PORT)
#httpd.serve_forever()






#import BaseHTTPServer, SimpleHTTPServer
#import http.server
#import socketserver

#PORT = 80
#Handler = http.server.SimpleHTTPRequestHandler

#with socketserver.TCPServer(("", PORT), Handler) as httpd:
#        print("serving at port", PORT)
#        httpd.serve_forever()



#if __name__ == "__main__":
        # load pretrained model as clf
#                app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
