import sys, time
indent = 0
indentTime  = True

try:
    while True:
        print('  ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if indentTime:
            indent = indent + 1
            if indent == 20:
                indentTime = False
            else:
                indent = indent - 1
                if indent == 0:
                    indentTime = True
except KeyboardInterrupt:
    sys.exit()
def Main(name):
    print(name)