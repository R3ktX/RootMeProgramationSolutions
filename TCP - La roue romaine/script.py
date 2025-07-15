import socket


def ROT13(ch):
    result = ''
    for char in ch:
        if char.isalpha():  
            offset = 65 if char.isupper() else 97  
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result

def connect(host,port):
    try:
        with socket.create_connection((host,port)) as s :
            data = s.recv(1024).decode().strip()
            encoded_string = str(data.split("'")[1])
            print(f"Received string: {encoded_string}")
            data_to_send = (ROT13(encoded_string)+'\n').encode()
            s.sendall(data_to_send)
            flag = s.recv(1024).decode().strip()
            print(flag)
    except Exception as e:
        print(e)
    
    
    
    
def main():
    connect("challenge01.root-me.org",52021)
    
    
if __name__ =="__main__":
    main()