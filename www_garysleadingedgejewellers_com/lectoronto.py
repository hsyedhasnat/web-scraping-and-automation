from selenium import webdriver
import time
import openpyxl


PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('++++++start+++++++')
wb = openpyxl.open("garysleadingedgejewellers1s.xlsx")
sheet = wb.active


#driver.get('https://www.garysleadingedgejewellers.com.au/')
#time.sleep(3)
Links=[]


#lis=driver.find_elements_by_xpath('//*[@id="main-menu"]/ul/li')
i=4
for ll in range(8):
    driver.get('https://www.garysleadingedgejewellers.com.au/')
    time.sleep(3)
    print(i,'+_+_+_+_+_+_+_+_+_+_+_+')
    llis=driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li['+str(i)+']')
    i=i+1
    proLink=[]
    link=llis.find_element_by_tag_name('a')
    print(link.get_attribute("href"))
    Cata=link.get_attribute("href")
    proLink.append(Cata)
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
                    div=link.find_element_by_class_name('items')
                    href=div.find_element_by_class_name('thumb_product')
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
                name=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[4]/div/h2').text
                print(name)
                data.append(name)
            except:
                data.append('N/A')
            
            Cata=Cata.replace('https://www.garysleadingedgejewellers.com.au/',' ')
            Cata=Cata.replace('.html',' ')
            print(Cata)
            data.append(Cata)
            subCat=subCat.replace('https://www.garysleadingedgejewellers.com.au/',' ')
            subCat=subCat.replace('.html',' ')
            print(subCat)
            data.append(subCat)
            
            try:
                arNu=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[3]/span').text
                print(arNu)
                data.append(arNu)
            except:
                data.append('N/A')            

            try:
                price=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[4]/div/div[3]/div[1]/span').text
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
                detail=driver.find_element_by_xpath('//*[@id="content-id"]').text
                print(detail)
                data.append(detail)
            except:
                data.append('N/A')

              
            ext=driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[4]/div/table/tbody/tr')
            print('Extra Info $$$$$$$$$$$$$$$$$$$$$$')
            for t in ext:
                 td=t.find_element_by_tag_name('td')
                 print(td.text)
                 data.append(td.text)
            print('$$$$$$$$$$$$$$$$$$$$$$ Extra Info ',len(data))

            
            try:   
                sheet.append(data)
                wb.save("garysleadingedgejewellers1s.xlsx")
            except:
                pass
                
driver.close()     
            



print('++++++++++++++++++++++++++++++++All Done+++++++++++++++++++++++++++++')



