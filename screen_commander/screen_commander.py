import os
import subprocess
import yaml
from time import sleep

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader as SafeLoader

class ScreenCommander:
    def __init__(self):
        self.screen_status = '%{= .} %-Lw%{= .}%> %n%f %t*%{= .}%+Lw%< %-=%{g}(%{d}%H/%l%{g})'

    def run(self, filename):
        conf = self._check_file(filename)
        if not conf:
            return

        for sock in conf:
            proc = subprocess.Popen('screen -S %s -d -m' % sock, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            sleep(0.02)
            for tab in conf[sock]:
                proc = subprocess.Popen('screen -S %s -X screen -t %s' % (sock, tab), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                sleep(0.02)
                cmds = conf[sock][tab]
                for cmd in cmds:
                    proc = subprocess.Popen("screen -S %s -p %s -X eval 'stuff \"%s\"\\015'" % (sock, tab, cmd), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                    sleep(0.02)
            proc = subprocess.Popen('screen -r %s -X hardstatus alwayslastline \"%s\"' % (sock, self.screen_status), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    def execute(self, filename):
        conf = self._check_file(filename)
        if not conf:
            return

        for sock in conf:
            for tab in conf[sock]:
                cmds = conf[sock][tab]
                for cmd in cmds:
                    proc = subprocess.Popen("screen -S %s -p %s -X eval 'stuff \"%s\"\\015'" % (sock, tab, cmd), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                    sleep(0.02)


    def kill(self, filename):
        conf = self._check_file(filename)
        if not conf:
            return

        proc_to_kill = []
        statusProc = subprocess.run('screen -ls', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        statusString = statusProc.stdout.decode('ascii')
        for sock in conf:
            for line in statusString.split('\n'):
                if sock in line:
                    proc_id = line.split('\t')[1].split('.')[0]
                    proc_to_kill.append(proc_id)
        proc = subprocess.Popen('kill %s' % " ".join(proc_to_kill), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    def _check_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return yaml.load(f.read(), SafeLoader)
        else:
            print("invalid filename %s\n" % filename)
            return None
