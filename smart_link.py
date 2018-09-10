# Copyright by Chenguang Ru

import os
import sys


def main():
    url = os.environ['POPCLIP_TEXT']
    title = os.environ['POPCLIP_SPECIAL_BROWSER_TITLE']
    mdurl = title + ': ' + url
    sys.stdout.write(mdurl)


if __name__ == '__main__':
    main()
