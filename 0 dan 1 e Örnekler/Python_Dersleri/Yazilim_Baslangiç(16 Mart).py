import requests
from bs4 import BeautifulSoup
def get_windows(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        rows = soup.find_all('tr')
        windows_names=[]
        for row in rows:
            icon = row.find('i',class_='fab fa-windows')
            if icon:
                common_name=row.find('td',class_='common_name').text.strip()
                windows_names.append(common_name)
        return windows_names

def save_txt(names,filename):
    with open(filename,'a') as file:
        for name in names:
            file.write(name + '\n')

if __name__ =="__main__":
    base_url="https://malpedia.caad.fkie.fraunhofer.de/families/"
    total_pages = 31
    filename= "output.txt"
    for page_number in range(1,total_pages+1):
        url=base_url + str(page_number) + "/"
        print(f"sayfa işleniyor {page_number}")
        common_names=get_windows(url)
        if common_names:
            save_txt(common_names,filename)
            print(f"bu sayfa işlendi ve bitti")