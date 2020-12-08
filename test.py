from bs4 import BeautifulSoup
import urllib.request
import requests
import time

name = input("Enter name :: ")
def getting_post_urls():
    #url = 'https://www.pornpics.com/search/srch.php?q=lisa+ann&limit=695&offset='
    url = 'https://www.pornpics.com/search/srch.php?q=' + str(name) + '&limit=100000&offset='
    headers = {"Connection": "close", "DNT": "1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflatre", "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"}
    cookies = {"cookie" : "__ae_uid_sess_id=b162cbb3-9e86-4a55-ac81-f1b1cccdd6e0; PP_UVM=1; _stat=2598133695.1528214785.23479322.3739817806; _ga=GA1.2.1272764643.1603974465; _gid=GA1.2.1206331922.1605948774"}
    req = requests.get(url, headers=headers, cookies=cookies)
    json_data = req.json()
    for linkss in json_data:
        links = linkss['g_url']
        link = []
        link.append(links)
        with open(name + "'s post_links.txt", "a") as file:
            for urls in link:
                file.write(str(urls) + "\n")
    print("Got all post's urls.")

def getting_image_urls():
    with open(name + "'s post_links.txt", 'r') as f:
        for line in f:
            payload = urllib.request.urlopen(line)
            time.sleep(2)
            soup = BeautifulSoup(payload.read(),'html.parser')
            for images in soup.find_all("a", attrs = {'class' : 'rel-link'}):
                imgg = images.get("href")
                img = []
                img.append(imgg)
                #print(img)
                with open(name + "'s image_links.txt", "a") as file:
                    for img_urls in img:
                        file.write(str(img_urls) + "\n")
    print("Got all image's urls.")
    #counting images
    with open(name + "'s image_links.txt", 'r') as f:
        data = f.read()
        line = data.splitlines()
        print('Total images are ::', len(line))


def downloading_images():
    count = len(open(name + "'s image_links.txt").readlines())
    for i in range(0, count):
        with open(name + "'s image_links.txt",'r') as f:
            url = f.read().split('\n')[i]
            url1 = url.rsplit('/',1)[-1]
            r = requests.get(url)
            time.sleep(10)
            with open(url1,'wb') as f:
                f.write(r.content)
    print("Images Downloaded.")

getting_post_urls()
getting_image_urls()
downloading_images()
