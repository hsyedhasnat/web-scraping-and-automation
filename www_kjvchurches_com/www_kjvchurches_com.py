from selenium import webdriver
import time
import openpyxl


PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('start')
wb = openpyxl.open("www_kjvchurches_com.xlsx")
sheet = wb.active


driver.get('https://www.kjvchurches.com/churches/')
time.sleep(3)

while(1):
    lis=driver.find_elements_by_xpath('//*[@id="post-39505"]/div/div[4]/ul/li')

    j=1
    for li in lis:
        data=[]
        try:
            name=driver.find_element_by_xpath('//*[@id="post-39505"]/div/div[4]/ul/li['+str(j)+']/div[2]/div[1]/h2/a')
            print(name.text)
            data.append(name.text)
        except:
            data.append('N/A')
        try:

            address=driver.find_element_by_xpath('//*[@id="post-39505"]/div/div[4]/ul/li['+str(j)+']/div[2]/div[4]/div/div[1]')
            address=address.text
            address=address.replace('\n','  ')
            print(address)
            data.append(address)
        except:
            data.append('N/A')
        try:
            phone=driver.find_element_by_xpath('//*[@id="post-39505"]/div/div[4]/ul/li['+str(j)+']/div[2]/div[4]/div/div[3]/a')
            print(phone.text)
            data.append(phone.text)
        except:
            data.append('N/A')
        try:
            Detail=driver.find_element_by_xpath('//*[@id="post-39505"]/div/div[4]/ul/li['+str(j)+']/div[2]/div[5]/div/p[1]')
            print(Detail.text)
            data.append(Detail.text)
        except:
            data.append('N/A')

        sheet.append(data)
        wb.save("www_kjvchurches_com.xlsx")
        j=j+1



    try:
        driver.find_element_by_xpath('//*[@id="post-39505"]/div/div[5]/nav/ul/li[last()]/a').click()
        print('NEXT PAGE FOUND')
        time.sleep(3)
    except:
        print('NEXT PAGE NOT FOUND')
        break


Print("All Done++++++++++++++++++++++++++++++++++++")
