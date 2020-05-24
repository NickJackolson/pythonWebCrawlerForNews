from selenium import webdriver
import os

path = "C:\\Users\\mychu\\WorkSpace\\Selenium_crawler\\"
starting_url = "https://www.haberler.com/arsiv/"

years = []
for x in range(2005,2020):
    years.append(x)

months = ["Ocak","Subat","Mart",
            "Nisan","Mayıs","Haziran",
            "Temmuz","Agustos","Eylul",
            "Ekim","Kasım","Aralik",]

days = range(1,32)

pages = [(lambda x : "s"+str(x))(x) for x in range(1,11)]

i = 1

report_data = []

driver = webdriver.Firefox(path)
# page = driver.get("https://www.haberler.com/2017/Mayis/1/haberler/s10/")
# content = driver.find_element_by_xpath("//div[@id='wrapper1']/div[@id='rightBlockMtrx']/div[@class='content-align']/div[@id='CntnrNew']/div[1]")
# content.click()

for year in years:
    for month in months:
        for day in days:
            for page in pages:
                try:
                    url = "https://www.haberler.com/"+str(year)+"/"+month+"/"+str(day)+"/haberler/"+page
                    driver.get(url)
                except KeyboardInterrupt:
                    print("User KeyboardInterrupt!")
                    exit()
                except Exception:
                    print("Wrong Page URL")
                    continue
                else:
                    i = 0
                    while True:
                        try:
                            report = "//div[@id='wrapper1']/div[@id='rightBlockMtrx']/div[@class='content-align']/div[@id='CntnrNew']/div["+str(i)+"]"
                            instance = driver.find_element_by_xpath(report)
                            instance.click()
                        except Exception:
                            print("Can't access report")
                            i = 0
                            break
                        else:
                            try:
                                body = driver.find_element_by_tag_name('p')
                            except Exception:
                                header = driver.find_element_by_tag_name('h2')
                                report_data.append(header.text)
                                print(header.text)
                                driver.get(url)
                                i += 1
                            else:
                                print(body.text)
                                report_data.append(body.text)
                                header = driver.find_element_by_tag_name('h2')
                                report_data.append(header.text)
                                print(header.text)
                                driver.get(url)
                                i += 1




# file = open("siber_savaş.txt","w+",encoding='utf-16')
# for paragraph in page_content:
#     file.write(paragraph.text)
#

print(report_data)

driver.close()
driver.quit()
