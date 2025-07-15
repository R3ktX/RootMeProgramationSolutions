import socket 
import base64
import zlib
def connect(host,port):
    try:
        with socket.create_connection((host,port)) as s :
            b=True
            while b:
                data = s.recv(1024).decode().strip()
                if "flag" in data:
                    b=False
                    print(data)
                    break
                encoded_string = data.split("'")[1]
                decoded = zlib.decompress((base64.b64decode(str(encoded_string)))).decode()
                print(f"This is the decoded string: {decoded}")
                s.sendall((decoded+'\n').encode())
                
    except Exception as e:
        print(e)
    
def main():
    connect("challenge01.root-me.org",	52022)
    
if __name__ == "__main__":
    main()
    
    