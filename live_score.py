from bs4 import BeautifulSoup
import urllib3
import sys

http=urllib3.PoolManager()
url='http://www.espncricinfo.com/ci/engine/match/index.html?view=live'
def crickinfo():
    cricfile=http.request('GET',url)
    crichtm=cricfile.data
    cricfile.close()
    soup=BeautifulSoup(crichtm,'html.parser')
    a=soup.find_all('div',attrs={'class':'innings-info-1'})
    b=soup.find_all('div',attrs={'class':'innings-info-2'})
    m=[]
    for result in a:
        m.append(result.text)
    n=[]
    for res in b:
        n.append(res.text)
    matches=dict(zip(m,n))
    print("{" + "\n".join("{} {}".format(k.strip(), v.strip()) for k, v in matches.items()) + "}")
    return "{" + "\n".join("{} {}".format(k.strip(), v.strip()) for k, v in matches.items()) + "}"

crickinfo()
