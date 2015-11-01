##################################### Method 1
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('http://www.running2win.com/index.asp')

# View available forms
for f in br.forms():
    print f

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=1)

# User credentials
br.form['login'] = 'aaron_liberatore'
br.form['password'] = 'k9n21SdLz'

# Login
br.submit()

print(br.open('http://www.running2win.com/community/view-member-running-log.asp?vu=&sd=9/17/2015&ed=9/17/2015&uk=DKZEBOLWUOJPUMBS50SZRCKNOVSJGMHFSPCAGBIPOFKLJISHM62888NADHFZFGAHBNIGCX').read())
