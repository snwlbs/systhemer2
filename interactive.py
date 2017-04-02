import logging
import cmd
import Progs


class iconsole(cmd.Cmd):
    def __init__(self, Settings, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.Settings = Settings
        self.logger = logging.getLogger('Systhemer.interactive')

    intro = 'Welcome to the Systhemer console!'
    prompt = '> '
    file = None

    def do_quit(self, args):
        print('exiting interactive mode...')
        exit(0)

    def do_exec(self, args):
        print(args)
        exec(args[0])

    def do_reload(self, args):
        args = args.split()
        sub_cmd = args.pop(0)
        if sub_cmd == 'prog-defs':
            Progs.setup(self.Settings)
        else:
            print('Error: subcommand not found \'%s\'' % sub_cmd)

    def do_tree(self, args):
        args = args.split()
        target = args.pop(0)
        for pd in Progs.prog_defs:
            if target == pd.get_name():
                print(target)
                print('├')
