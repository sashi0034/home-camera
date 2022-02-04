from ast import arg
from asyncio import constants
from multiprocessing.dummy import Array
import re
import string
from xmlrpc.client import boolean
from main import post_mes

class Arg:
    def __init__(self, words) -> None:
        self.value = words
    
    def get_len(self) -> int:
        return len(self.value)
        
    def take_value(self) -> str:
        return self.value.pop(0)
    
    def check_next(self, str: str) -> bool:
        return self.value[0] == str


class ExeCmd:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def input_command(mes: str):
        #print("mes = "+mes)
        has_process: bool = False
        has_invalid_cmd: bool = False
        
        words = re.compile(r"\s+").split(mes)
        if words==[]:
            return
        
        print(words)
        
        argv = Arg(words)

        if (argv.take_value()=="$"):
            while argv.get_len()>0:

                cmd = argv.take_value()

                def fn(a): return len(a)
                funcs = {
                    "ping": ExeCmd.Command.ping,
                    "plus": ExeCmd.Command.plus,
                }
                if (cmd in funcs):
                    fn = funcs[cmd]
                    try:
                        fn(argv)
                        has_process = True
                    except Exception as e:
                        print(e)
                        post_mes("無効な引数があります")
                        has_process = True
                        break
                else:
                    has_invalid_cmd = True

        if (has_invalid_cmd):
            post_mes("無効なコマンドが存在しました")

        return has_process
    
    

    class Command:
        @staticmethod
        def ping(argv: Arg):
            # print(argv)
            post_mes("生きてるー!")
            return 1

        @staticmethod
        def plus(argv: Arg):
            # print(argv)
            a = int(argv.take_value())
            b = int(argv.take_value())
            
            post_mes(f"{a}+{b}={str(a+b)}です")
            return 1


