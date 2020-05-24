from selenium import webdriver
import os
import time

def check_exists_by_tag(webdriver,tag):
    try:
        webdriver.find_element_by_tag_name(tag)
    except Exception:
        return False
    return True

path = "C:\\Users\\mychu\\WorkSpace\\Selenium_crawler\\"
starting_url = "https://www.haberler.com/arsiv/"

years = []
for x in range(2006,2020):
    years.append(x)

months = ["Ocak","Subat","Mart",
            "Nisan","Mayıs","Haziran",
            "Temmuz","Agustos","Eylul",
            "Ekim","Kasım","Aralik",]

days = range(1,32)

pages = [(lambda x : "s"+str(x))(x) for x in range(1,11)]

class TooLong(Exception): pass

driver = webdriver.Firefox(path)

data = []

for year in years:
    for month in months:
        for day in days:
            for page in pages:
                    url = "https://www.haberler.com/"+str(year)+"/"+month+"/"+str(day)+"/haberler/"+page
                    print(url)
                    driver.get(url)
                    count = driver.find_elements_by_xpath("//div[@id='wrapper1']/div[@id='rightBlockMtrx']/div[@class='content-align']/div[@id='CntnrNew']/div")
                    for i in range(1,len(count)+1):
                        article_XPATH = "//div[@id='wrapper1']/div[@id='rightBlockMtrx']/div[@class='content-align']/div[@id='CntnrNew']/div["+str(i)+"]/a[@class='hbrListLink']"
                        try:
                            article = driver.find_element_by_xpath(article_XPATH)
                            driver.execute_script("arguments[0].click();", article)
                            time.sleep(1)
                            if check_exists_by_tag(driver,"h2"):
                                header = driver.find_element_by_tag_name("h2")
                                data.append(header.text)
                            if check_exists_by_tag(driver,"p"):
                                body = driver.find_element_by_tag_name("p")
                                if len(body.text) > 10:
                                    data.append(body.text)

                            print(driver.current_url)
                            print(len(data))
                            if len(data) > 30:
                                file = open("turkish_archive.txt","w+",encoding='utf-16')
                                for paragraph in data:
                                    file.write(paragraph)
                                data = []

                        except KeyboardInterrupt:
                            driver.close()
                            driver.quit()
                            exit()

                        
                        except Exception as e:
                            print(e)
                            print("Article not found")
                            exit()
                        else:
                            driver.get(url)
