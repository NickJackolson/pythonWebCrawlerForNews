from selenium import webdriver
import os

path = "C:\\Users\\mychu\\WorkSpace\\source\\"
starting_url = "https://tr.wikipedia.org"

driver = webdriver.Firefox(path)
# driver.get(starting_url)
page = driver.get("https://tr.wikipedia.org/wiki/Siber_savaş")
page_content = driver.find_elements_by_tag_name("p")

file = open("siber_savaş.txt","w+",encoding='utf-16')
for paragraph in page_content:
    file.write(paragraph.text)
    # print(paragraph.text)

# random_page_expression = "/html/body/div[@id='mw-navigation']/div[@id='mw-pane1']/div[@id='p-navigation']/div[@class='body']/ul/li[4]"
# random_page_expression = "//div[@id='p-navigation']/div[@class='body']/ul/li[4]/a"
# next_page = driver.find_element_by_xpath(random_page_expression)

# for i in range(5):
#     rastgele = driver.find_element_by_link_text('Rastgele madde')
#     rastgele.click()
#     page_content = driver.find_elements_by_tag_name("p")
#
#     for instance in page_content:
#         print(instance.text)


driver.close()
driver.quit()
