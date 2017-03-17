import sys


class LoggerWriter:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        if message != '\n':
            self.level(message)

    def flush(self):
        self.level(sys.stderr)

class Counter(object):
    @staticmethod
    def progress(count, total, suffix=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        progress_bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s of total active servers...%s\r' % (progress_bar,
                                                                       percents,
                                                                       '%',
                                                                       suffix))
