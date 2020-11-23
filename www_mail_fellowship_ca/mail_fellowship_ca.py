from selenium import webdriver
import time
import openpyxl

#name     adreess    p-hone    e-- mail    fax      cell
PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('start')
wb = openpyxl.open("mail_fellowship_ca.xlsx")
sheet = wb.active

driver.get('https://mail.fellowship.ca/churchdirectory/churchdirectory.aspx?provbox=%25&citybox=&namebox=&search=Search&__VIEWSTATEGENERATOR=3198D962&__VIEWSTATE=%2FwEPDwUKMTMyMzI1ODY0NmRkFAPG3DiRRELpM4tflb23qByaqus%3D&__EVENTVALIDATION=%2FwEWEwKexZ2BBAL9opi9DwKWo5i9DwKyopCjDwKzoqyjDwKOopCjDwKPopCjDwKPoqCjDwKPouijDwKPouyjDwKPouCjDwKMooCjDwKdoqSjDwKCoqyjDwKAooyjDwKaouijDwLN8s7JDQKVooa%2BCQLH0pL8CYPGGQwD93r6c6TpCOpAtWpTpR5s')
time.sleep(3)
Links=[]

val=5
for i in range(500):
    try:
        tLink=driver.find_element_by_xpath('//*[@id="outlist"]/div/table/tbody/tr['+str(val)+']/td[1]/a').get_attribute("href")
        print(tLink)
        Links.append(tLink)
        val=val+3
    except:
        break
    
for link in Links:
    driver.get(link)
    time.sleep(3)

    name=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/table/tbody/tr[1]/td')
    print(1,name.text)
    d=name.text
    data=d.split('\n')

    sheet.append(data)
    wb.save("mail_fellowship_ca.xlsx")

print('All Done')
