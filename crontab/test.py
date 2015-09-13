#coding=utf-8
import sys
import os
import datetime
import time

class ArgsDealwith:

    def arg_environment(self, args):
        filepath = ('PYTHON_PATH', 'path')
        for i in filepath:
            filename = os.environ.get(i,"%s is null." % i)
            print '%s:' % i,' ', filename

    def arg_en(self, args):
        filepath = ('PYTHON_PATH', 'path')
        for i in filepath:
            filename = os.environ.get(i,"%s is null." % i)
            print '%s:' % i, ' ', ' '.join(filename.split(';'))

    def arg_file(self, args):
        if not args:
            print 'Error: file name is null.'
        else:
            if len(args) == 1 and args[0].lower() == 'python_path':
                filename = os.environ.get(args[0], None)
                if filename:
                    args = filename.split(';')
                else:
                    print 'Error: "%s" is null' % args[0]
                    exit()

            for i in args:
                if os.path.isfile(i):
                    try:
                        execfile(i)
                    except:
                        print 'Error: "%s" run failed.' % i
                else:
                    print 'Error: Not found "%s" file.' % i

    def arg_filetime(self, args):
        if not args:
            print 'Error: file name is null.'
        elif len(args) % 2 != 0:
            print "Error: args isn't validate"
        else:
            fileTimes = [i for i in args if args.index(i) % 2 != 0 ]
            for i in fileTimes:
                try:
                    fileTimes[fileTimes.index(i)] = int(i)
                except Exception:
                    print "Error: time args isn't validate"
                    exit()
                if i <= 0:
                    print 'Error: time<=0'
                    exit()

            minTime = fileTimes[0]
            for i in fileTimes:
                if i < minTime:
                    minTime = i

            strTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
            tupleTime = tuple([int(i) for i in strTime.split('-')])
            begin = datetime.datetime(tupleTime[0], tupleTime[1], tupleTime[2], tupleTime[3], tupleTime[4], tupleTime[5])


            fileTimes = [[i, 0] for i in fileTimes]
            seconds = 0
            while True:
                strTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
                tupleTime = tuple([int(i) for i in strTime.split('-')])
                end = datetime.datetime(tupleTime[0], tupleTime[1],tupleTime[2], tupleTime[3], tupleTime[4], tupleTime[5])

                time_sub = end - begin
                seconds = time_sub.seconds
                begin = end
                for i in fileTimes:
                    i[1] += seconds

                for i in fileTimes:
                    if i[1] == 0:
                        self.arg_file( [args[args.index(str(i[0])) - 1] ] )
                    elif i[1] >= i[0]:
                        i[1] %= i[0]
                        self.arg_file( [args[args.index(str(i[0])) - 1] ] )
                        if i[0] - i[1] < minTime:
                            minTime = i[0] - i[1]

                time.sleep(minTime)

    def arg_help(self, args):
        strHelp = "Usage: ps [-options] [args...] where option include:"
        strHelp += """
        -? -help            print this help message
        -e -environment     print environment path
        -en                 print envrionment path per row
        -f -file:<file> [file2 file3...]
                            execute file(.py)
        -ft -filetime:<file time> [file2 time2 file3 time3...]
                            execute file(.py) per time,
                            this run not stop,
                            but this command hasn't validate.
                            time(seconds) must is interger and
                            not less than zero"""
        print strHelp

def arg_args():
    args_dic = {'arg_help' : ['-?', '-help'], 'arg_environment' : ['-e', '-environment'],
                'arg_en' : ['-en'], 'arg_file' : ['-f', '-file'], 'arg_filetime' : ['-ft', 'filetime']}
    argsCls = ArgsDealwith()
    if len(sys.argv) <= 1:
        argsCls.arg_help(sys.argv)
    else:
        argsFun = ''
        for i in sys.argv[1:]:
            bMath = False
            for j in args_dic.items():
                if i in j[1]:
                    argsFun = j[0]
                    bMath = True
                    break
            if bMath:
                break
        if argsFun:
            try:
                getattr(argsCls, argsFun)(sys.argv[2:])
            except Exception, error:
                print error
                exit()
        else:
            print "Error: '%s' isn't validate arg." % ' '.join(sys.argv[1:])
            del argsCls

if __name__ == '__main__':
    arg_args()

