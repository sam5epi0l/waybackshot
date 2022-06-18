# waybackshot 🥃
Takes a list of URLs and retrieve screenshots of older versions stored on the Wayback Machine. I mainly developed this script for Bug Bounty purposes.It uses [waybackshot](https://github.com/markusbink/wayback-shot) (new) package from python library to capture screenshot of older stored version of webpage and uses selenium as web-driver.

# Install 💼
Run these commands
```
git clone https://github.com/sam5epi0l/waybackshot.git
cd waybackshot
pip3 install -r requirements.txt
python3 shot.py -h
```

# Example 🔻
```
waybackshot -u https://example.com/
waybackshot -u urls.txt
cat scope.txt | gau | waybackshot -u
```

# Uses 🚀
```
usage: wayback-shot [-h] [-d DATEFROM] [-o OUTPUTDIR] [-w WIDTH] [-r] [-i] -u URL

Get screenshot of archived urls in wayback machine by @sam5epi0l

optional arguments:
  -h, --help            show this help message and exit
  -d DATEFROM, --dateFrom DATEFROM
                        fetch archived urls after provided date (Format=YYYYMMDD)
  -o OUTPUTDIR, --outputDIR OUTPUTDIR
                        save screenshot output to directory (default="")
  -w WIDTH, --width WIDTH
                        Width of the webpage used to screenshot (default=1920)
  -r, --replace         replace existing screenshot of the URL
  -i, --includeDate     fetch Date when the URL was archived
  -u URL, --url URL     perform screenshot on the provided URL
```

# Credits 💳
👉 waybackshot: @markusbink https://github.com/markusbink/wayback-shot for providing the python library
