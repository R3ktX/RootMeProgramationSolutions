import socket, math

def connect(host, port):
    try:
        with socket.create_connection((host, port)) as s:
            while True:
                data = s.recv(1024).decode().strip()
                if "flag" in data:
                    print("Flag:", data)
                    break

                if "please:" not in data:
                    continue
                polynome = data.split("please:")[1].split('?')[0].strip()
                
                lhs, rhs = polynome.split('=')
                rhs = int(rhs.strip())
                parts = lhs.strip().split()

                a = int(parts[0].split('.')[0])                      
                b = int(parts[1] + parts[2].split('.')[0])           
                c = int(parts[3] + parts[4])                         

                c = c - rhs  

                result = solve(a, b, c)
                if result == 0:
                    s.sendall("Not possible\n".encode())
                else:
                    x1, x2 = result
                    x1 = round(x1, 3)
                    x2 = round(x2, 3)
                    print(f"Sending {x1, x2} ....")
                    if abs(x1 - x2) < 1e-6:
                        s.sendall(f"x: {x1:.3f}\n".encode())
                    else:
                        s.sendall(f"x1: {x1:.3f} ; x2: {x2:.3f}\n".encode())

    except Exception as e:
        print("Error:", e)



def solve(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 0
    r = math.sqrt(delta)
    x1 = (-b - r) / (2 * a)  
    x2 = (-b + r) / (2 * a)  
    return x1, x2


def main():
    connect("challenge01.root-me.org", 52018)


if __name__ == "__main__":
    main()
