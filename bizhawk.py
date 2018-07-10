import subprocess
from matplotlib.pyplot import imread

class BizHawk(object):
    def __init__(self, rom_path, bizhawk_path, lua_path='', movie_path=''):
        proc_options = [bizhawk_path + 'EmuHawk.exe', rom_path]
        if lua_path != '':
            proc_options.append('--lua=' + lua_path)
        if movie_path != '':
            proc_options.append('--movie=' + movie_path)
        self.proc = subprocess.Popen(proc_options,
                                     stdout=subprocess.PIPE,
                                     stdin=subprocess.PIPE,)

    #Loop until 'start'
    def __enter__(self):
        while True:
            out_line = self.proc.stdout.readline()
            if out_line[:5] == b'start':
                break
        return self

    #Terminate BizHawk
    def __exit__(self, *args):
        self.proc.terminate()

    #Send lua code
    def send(self, msg):
        self.proc.stdin.write(msg)
        self.proc.stdin.flush()

    #Wait for confirmation
    def wait_until(self, msg):
        while self.proc.stdout.readline() != msg:
            pass

    #Save and read screenshot
    def read_img(self, img_path):
        code = b''
        code += b'client.screenshot("' + bytes(img_path, 'utf-8') + b'");'
        code += b'io.stdout:write("continue");'
        self.send(code)
        self.wait_until(b'continue\n')

        temp_img = imread(img_path)
        return temp_img
