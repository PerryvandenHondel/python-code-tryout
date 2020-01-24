#!/usr/bin/python3

##
## Working on Code - Logging
##


import logging


def main():
    print("Working on code - logging")

    logLevel = logging.DEBUG

    pathLogFile = "./codeworking.log" 

    logging.basicConfig(level=logLevel, filename=pathLogFile, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Start of script")

    logging.debug("Kind a bad thing happend!")

    logging.info("End of script")


if __name__ == "__main__":
    main()