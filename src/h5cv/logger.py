import logging
from logging import getLogger, INFO, DEBUG


def get_logger(debug=False):
    logging.basicConfig(
        level=(logging.DEBUG if debug else logging.INFO),
        format="%(asctime)s %(levelname)s - %(message)s",
    )
    return getLogger(__name__)
