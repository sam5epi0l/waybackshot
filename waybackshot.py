import argparse
from waybackshot import WaybackShot

wayback_shot = WaybackShot()
parser = argparse.ArgumentParser(prog='wayback-shot', description='Get screenshot of archived urls in wayback machine by @sam5epi0l')

parser.add_argument("-d", "--dateFrom", required=False, default=None, help='fetch archived urls after provided date (Format=YYYYMMDD)')
parser.add_argument("-o", "--outputDIR", required=False, default="", help='save screenshot output to directory (default="")')
parser.add_argument("-w", "--width", required=False, default=1920, help='Width of the webpage used to screenshot (default=1920)')
parser.add_argument("-r", "--replace", required=False, default=False, help='replace existing screenshot of the URL', action='store_true')
parser.add_argument("-i", "--includeDate", required=False, default=False, help='fetch Date when the URL was archived', action='store_true')
parser.add_argument("-u", "--url", required=True, help='perform screenshot on the provided URL')

args = parser.parse_args()

wayback_shot.screenshot(url=args.url, date=args.dateFrom, dir=args.outputDIR, width=args.width, overwrite=args.replace, include_date=args.includeDate)
