from selenium import webdriver
import time
import openpyxl

"DOEN"
PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('++++++start+++++++')
wb = openpyxl.open("leadingedgecarnarvon.xlsx")
sheet = wb.active


driver.get('https://www.leadingedgecarnarvon.com.au/')
time.sleep(3)
Links=[]


lis=driver.find_elements_by_xpath('//*[@id="main-menu"]/ul/li')
i=1
for ll in lis:
    
    print(i,'+_+_+_+_+_+_+_+_+_+_+_++_+_+_+_+_+_+_+_+_+_+_++_+_+_+_+_+_+_+_+_+_+_++_+_+_+_+_+_+_+_+_+_+_++_+_+_+_+_+_+_+_+_+_+_+')
    llis=driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li['+str(i)+']')
    i=i+1
    link=llis.find_element_by_tag_name('a')
    print(link.get_attribute("href"))
    Cata=link.get_attribute("href")
    proLink=[]
    try:
        subCat=llis.find_element_by_tag_name('ul')
        li=subCat.find_elements_by_tag_name('li')
        proLink=[]
        for l in li:
            sl=l.find_element_by_tag_name('a')
            print(sl.get_attribute("href"))
            proLink.append(sl.get_attribute("href")) 
    except:
        pass

    for p in proLink:
        driver.get(p)
        time.sleep(3)
        subCat=p
        PerPro=[]
        print('PRODUCTS++++++++++++++++++++++++++++++++++++++++++')
        while(1):
            Plinks=driver.find_elements_by_xpath('//*[@id="category-products"]/div')
        
            for link in Plinks:
                try:
                    div=link.find_element_by_class_name('product')
                    href=div.find_element_by_class_name('product-tile')
                    h=href.find_element_by_tag_name('a').get_attribute("href")
                    print(h)
                    PerPro.append(h)
                except:
                    pass

            try:
                driver.find_element_by_xpath('//*[@id="category-products"]/div[13]/ul/li[last()]/a').click()
                print('NEXT PAGE___________________')
                time.sleep(2)
            except:
                print('NO MORE PAGE=================')
                break
        
        for pr in PerPro:
            driver.get(pr)
            time.sleep(3)
            data=[]
            data.append(pr)
            try:
                name=driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div/div[3]/div/div[1]').text
                print(name)
                data.append(name)
            except:
                data.append('N/A')
            
            Cata=Cata.replace('https://www.lectoronto.com.au/',' ')
            Cata=Cata.replace('.html',' ')
            print(Cata)
            data.append(Cata)
            subCat=subCat.replace('https://www.lectoronto.com.au/',' ')
            subCat=subCat.replace('.html',' ')
            print(subCat)
            data.append(subCat)
            
            try:
                arNu=driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div/div[3]/div/span').text
                print(arNu)
                data.append(arNu)
            except:
                data.append('N/A')            

            try:
                price=driver.find_element_by_xpath('/html/body/div/section/div[2]/div[1]/div/div[3]/div[1]/div[2]/span').text
                print(price)
                data.append(price)
            except:
                data.append('N/A')

            try:
                img=driver.find_element_by_xpath('//*[@id="lightSlider"]/li/a/img').get_attribute("src")
                print(img)
                data.append(img)
            except:
                data.append('N/A')                

            try:
                detail=driver.find_element_by_xpath('//*[@id="dot5"]').text
                print(detail)
                data.append(detail)
            except:
                data.append('N/A')

              
            ext=driver.find_elements_by_xpath('//*[@id="descChangeContent"]/table/tbody/tr')
            print('Extra Info $$$$$$$$$$$$$$$$$$$$$$')
            for t in ext:
                 td=t.find_element_by_tag_name('td')
                 print(td.text)
                 data.append(td.text)
            print('$$$$$$$$$$$$$$$$$$$$$$ Extra Info ',len(data))

            
                
            sheet.append(data)
            wb.save("leadingedgecarnarvon.xlsx")
            
driver.close()     
            



'''
for t in trs:
    td=t.find_elements_by_tag_name('td')
    print(td[0].text)
    print(td[1].text)
    print(td[2].text)
    print(td[4].text)
    print(td[5].text)
    try:
        print(td[6].find_element_by_tag_name('a').get_attribute("data-tooltip"))
    except:
        print("None")
    print(td[7].find_element_by_tag_name('a').get_attribute("href"))
    print(td[8].find_element_by_tag_name('a').get_attribute("href"))




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
        wb.save("baptist_atlantic_ca.xlsx")
     
'''

print('++++++++++++++++++++++++++++++++All Done+++++++++++++++++++++++++++++')



