import socket
import base64
def solution(host,port):
    try:
        with socket.create_connection((host,port)) as s:
            data = s.recv(1024).decode().strip()
            encoded_string = data.split(" ")[14].strip('.').strip("'")
            print(f"This is your encoded string: {encoded_string}")
            decoded_data = base64.b64decode(str(encoded_string))
            print (f"This is the decoded string: {decoded_data}")
            s.sendall((decoded_data.decode()+'\n').encode())
            flag = s.recv(1024).decode().strip()
            print(flag)
    except Exception as e:
        print(e)
        
        

def main():
    solution("challenge01.root-me.org",52023)
    
    
if __name__ =="__main__":
    main()