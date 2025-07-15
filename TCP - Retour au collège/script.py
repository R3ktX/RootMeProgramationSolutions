import socket 
import math
def connect(host,port):
    try:
        with socket.create_connection((host,port)) as s:
            data = s.recv(1024).decode()
            print(f"[Received]: {data.strip()}")
            nums=[int(data.split(" ")[24]),int(data.split(" ")[28])]
            result = round(math.sqrt(nums[0])*nums[1],2)
            print(f"[Resul]: {result}")
            # sending result 
            s.sendall((str(result)+'\n').encode())
            try:
                flag = s.recv(1024).decode().strip()
                print(flag)
            except Exception as e:
                print(f"Error while receiving data {e}")
    except Exception as e :
        print(f"Error: {e}")
    
    
def main():
    connect("challenge01.root-me.org",52002)
    
    
if __name__ == "__main__":
    main()