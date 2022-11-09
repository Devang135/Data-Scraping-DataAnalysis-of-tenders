
import pandas as pd
import requests
from bs4 import BeautifulSoup


list_=[]
class Scrape:
    def ukcabinet(self):
        url = "https://www.contractsfinder.service.gov.uk/Search/Results?&page="

        
        for page in range(1,25): # stop parameter defines the page scrape length
            link_ = requests.get(url + str(page))
      
            soup = BeautifulSoup(link_.content, "lxml")
            all_data = soup.find_all("div", {"class": "search-result"})

            for idx in all_data:

                data={}
                data["Tender"] = idx.find("a", {"class": ["govuk-link", "search-result-rwh", "break-word"]}).text
                data["Company"] = idx.find("div", {"class": ["search-result-sub-header", "wrap-test"]}).text
                data["Procurement"] = idx.find_all("div", {"class": "search-result-entry"})[0].text.replace("Procurement stage", " ")
                data["Notice"] = idx.find_all("div", {"class": "search-result-entry"})[1].text.replace("Notice status",  " ")
                data["Location"] = idx.find_all("div", {"class": "search-result-entry"})[3].text.replace("Contract location"," ")
                data["Closing"] = idx.find_all("div", {"class": "search-result-entry"})[2].text.replace("Closing"," ")
                try:
                    data["Closing"] = idx.find_all("div", {"class": "search-result-entry"})[2].text.replace("Closing"," ")
                except:
                    data["Closing"] = "None"
                try:
                    data["Value"] = idx.find_all("div", {"class": "search-result-entry"})[4].text.replace("Contract value", " ")
                except:
                    data["Value"] = "None"
                try:
                    data["Date"] = idx.find_all("div", {"class": "search-result-entry"})[5].text.replace("Publication date", " ")
                except:
                     data["Date"] = "None"
                list_.append(data)

        df=pd.DataFrame(list_)
        df.to_csv("tenderdata.csv",index=False)


obj=Scrape()
obj.ukcabinet()



 
 
