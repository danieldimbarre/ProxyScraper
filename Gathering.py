import asyncio, os, colorama, re, time
from proxybroker import Broker
from colorama import *

os.system("rm -rf proxies.txt")
os.system("cat proxies.txt >> proxies.txt")

def delay():
	os.system("sh blacklist.sh")
	print(">> Waiting 10 minutes to renew proxies")
	time.sleep(600)
	Scraper()

async def save(proxies, filename):
    with open(filename, 'w+') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            proto = 'https' if 'HTTPS' in proxy.types else 'http'
            row = '%s:%d\n' % (proxy.host, proxy.port)
            f.write(row)
            print(Fore.WHITE + "Proxy Found - " + Fore.GREEN + str(proxy))

		
def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5'], limit= 5),
                           save(proxies, filename='proxy.txt'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    delay()
	
def Scraper():
	os.system("wget -O PShttp.txt https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=10000&country=all&anonymity=all&ssl=all")
	os.system("wget -O PSsocks4.txt https://api.proxyscrape.com?request=getproxies&proxytype=socks4&timeout=10000&country=all")
	os.system("wget -O PSsocks5.txt https://api.proxyscrape.com?request=getproxies&proxytype=socks4&timeout=10000&country=all")
	os.system("wget -O githubList.txt https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/nixspam.ipset")
	try:
		os.system("wget -O tor.txt https://check.torproject.org/torbulkexitlist")
	try:
		os.system("wget -O proxyS4.txt https://www.proxy-list.download/api/v1/get?type=socks4")
		os.system("wget -O proxyS5.txt https://www.proxy-list.download/api/v1/get?type=socks5")
	except:
		print("A")
		pass
	try:
		os.system("wget -O psS4.txt https://www.proxyscan.io/download?type=socks4")
		os.system("wget -O psS5.txt https://www.proxyscan.io/download?type=socks5")
	except:
		print("B")
		pass
	try:
		os.system("wget -O SpeedS4.txt https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
		os.system("wget -O Speed5.txt https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
	except:
		print("C")
		pass

	os.system("cat githubList.txt >> proxies.txt && cat proxyS4.txt >> proxies.txt && cat proxyS5.txt >> proxies.txt && cat psS4.txt >> proxies.txt && cat SpeedS4.txt >> proxies.txt && cat Speed5.txt >> proxies.txt && cat tor.txt && proxies.txt")
	with open("proxies.txt") as O, open("proxy.txt","w+") as B:
        	for line in O:
                	word = ':'
                	replace_with = ''
                	occurrance  = 1
                	B.write(word.join(line.split(word)[:occurrance]) + "\n")
	main()

Scraper()



