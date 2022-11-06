import logging
import sys


def set_logger(name=None):
    fmt = logging.Formatter("%(name)s [%(levelname)s] %(message)s")
    # INFO以下のログを標準出力する
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(fmt)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)

    # WARNING以上のログを標準エラー出力する
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(fmt)

    # ロガーにハンドラを設定する
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
