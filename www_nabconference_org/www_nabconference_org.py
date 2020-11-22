from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import openpyxl


PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('start')
wb = openpyxl.open("www_nabconference_org.xlsx")
sheet = wb.active


driver.get('https://nabconference.org/church-locator/')

time.sleep(5)
Links=[]


states=['','Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

for s in states:
    #driver.find_element_by_xpath('//*[@id="wpsl-wrap"]')
    driver.find_element_by_xpath('//*[@id="wpsl-search-input"]').clear()
    driver.find_element_by_xpath('//*[@id="wpsl-search-input"]').send_keys(s)
    
    
    #driver.find_element_by_xpath('//*[@id="wpsl-radius-dropdown"]').click()
    #select = Select( driver.find_element_by_id('wpsl-radius-dropdown') )
    #select.select_by_visible_text('500 mi')

    driver.find_element_by_xpath('//*[@id="wpsl-search-btn"]').click()

    time.sleep(10)

    di=driver.find_element_by_xpath('//*[@id="wpsl-stores"]')
    ul=di.find_element_by_tag_name('ul')
    lis=ul.find_elements_by_tag_name('li')
    try:
        lis=driver.find_elements_by_xpath('//*[@id="wpsl-stores"]/ul/li')
    except:
        lis=driver.find_elements_by_xpath('//*[@id="wpsl-stores"]/ul/li')

    for li in lis:
        data=[]
        try:
            div=li.find_element_by_class_name('wpsl-store-location')
            p=div.find_element_by_tag_name('p')
            st=p.find_element_by_tag_name('strong')
            name=st.find_element_by_tag_name('a').text
            print(name)
            data.append(name)
        except:
            data.append('N/A')
        try:
            web=st.find_element_by_tag_name('a').get_attribute("href")
            print(web)
            data.append(web)
        except:
            data.append('N/A')
        try:
            add=p.find_elements_by_tag_name('span')
            print(add[0].text)
            print(add[1].text)
            data.append(add[0].text)
            data.append(add[1].text)
        except:
            data.append('N/A')
            data.append('N/A')
            
        data.append(s)
        sheet.append(data)
        wb.save("www_nabconference_org.xlsx")
     


print('++++++++++++++++++++++++++++++++All Done+++++++++++++++++++++++++++++')



