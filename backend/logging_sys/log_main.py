import datetime
import inspect
from .ansi import ansi
from global_varibles import Globals as G


class log:
    def _str_time(self):
        now = datetime.datetime.now()
        return now.strftime("%d.%m.%Y %H:%M")

    def _get_module_name(self):
        frame = inspect.stack()[3]
        module = inspect.getmodule(frame[0])
        if module and module.__name__:
            return module.__name__
        return inspect.getmodulename(frame.filename) or frame.filename

    def log(self, level: str, lvl_color, text):
        time_str = self._str_time()
        module_name = self._get_module_name()

        level_str = level.upper().ljust(8)
        module_str = module_name.ljust(14)
        if G.ansi_text:
            print((f"{ansi.LIGHT_PURPLE}{time_str}  "
                   f"{lvl_color}{level_str}  "
                   f"{ansi.STR}{module_str}{ansi.RESET}  "
                   f"{ansi.BOLD}{ansi.LIGHT_WHITE}||{ansi.RESET}  {text}"))
        else:
            print((f"{time_str}  "
                   f"{level_str}  "
                   f"{module_str}  "
                   f"||  {text}"))

    def info(self, text):
        self.log("INFO", ansi.BLUE, text)

    def success(self, text):
        self.log("SUCCESS", ansi.GREEN, text)

    def error(self, text):
        self.log("ERROR", ansi.RED, text)

    def debug(self, text):
        self.log("DEBUG", ansi.BG_LIME, text)
