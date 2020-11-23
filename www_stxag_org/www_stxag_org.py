from selenium import webdriver
import time
import openpyxl


PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('start')
wb = openpyxl.open("www_stxag_org.xlsx")
sheet = wb.active


driver.get('http://www.stxag.org/find-a-church/what-section-am-i-in')
time.sleep(3)
Links=[]


driver.find_element_by_xpath('//*[@id="ewsmenu_main"]/li[3]/a').click()

j=7
for i in range(10):
    link=driver.find_element_by_xpath('//*[@id="ctl00_contentarea_main_ctl00_ctl00_ctl01_ctl01_wContent"]/div['+str(j)+']/a').get_attribute("href")
    j=j+2
    print(link)
    Links.append(link)


for link in Links:
    driver.get(link)
    time.sleep(3)

    rows=driver.find_elements_by_xpath('/html/body/form/div[4]/div[3]/div/div/div/div/table/tbody/tr')
    print(len(rows),"+++++++++++++++++++++++++++++++")

    for row in rows:
        col=row.find_elements_by_tag_name('td')
        data=[]
        name=col[1].text
        N=name.split('\n')
        name=N[0]
        data.append(name) 
        N=N[1:]
        address=''
        for nn in N:
            address=address+nn
        data.append(address) 
        past=col[2].text
        past=past.replace('Pastor',' ')
        data.append(past) 
        data.append(col[3].text)

           

        print(data)
        sheet.append(data)
        wb.save("www_stxag_org.xlsx")


print('All Done ####################')
