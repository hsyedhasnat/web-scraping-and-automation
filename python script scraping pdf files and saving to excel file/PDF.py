from selenium import webdriver
import openpyxl
import time
from selenium.webdriver.support.ui import Select

PATH="geckodriver"
driver = webdriver.Firefox(executable_path=PATH)
print('start')

#wb = openpyxl.open("Modele 4 BN.xlsx")
#sheet = wb.active






pdf=[]
url='http://www.cepici.gouv.ci/?tmp=annonces_legales&p=annonces-legales'
driver.get(url)
time.sleep(5)
page=2
for i in range(1500):
    
    f = open('pdf.txt', 'a')
    try:
        driver.find_element_by_xpath('//*[@id="ad_remove_btn"]').click()
    except:
        pass
    
    trs=driver.find_elements_by_xpath('//*[@id="contenu"]')
    print(len(trs))
    for tr in trs:   
        td=tr.find_elements_by_tag_name('td')
        a=td[2].find_element_by_tag_name('a').get_attribute("href")
        print(a)
        pdf.append(a)
        f.write(a)
        f.write("\n")

    f.close()
    driver.get('http://www.cepici.gouv.ci/?tmp=annonces_legales&p=annonces-legales&page='+str(page)+'&sc=Default')
    print("page #",page," ",len(pdf))
    page+=1
    time.sleep(8)

print(len(pdf))
'''
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    li=driver.find_elements_by_xpath('/html/body/div[2]/section/div/div[1]/div/div/div[5]/ul/li')
    print(len(li))
    li[-1].find_element_by_tag_name('a').click()
    #driver.find_element_by_link_text("»").click()
    print('next')
    '''














#time.sleep(5)

#PDF=['http://www.gufebenin.org/images/documents/050517.pdf']
#with open("pdf.txt") as file_in:
#   for line in file_in:
#        print(line)
#        PDF.append(line)
        


'''

mon=['01','02','03','04','05','06','07','08','09','10','11','12']
yr=['2012','2013','2014','2015','2016','2017','2018','2019','2020']

for y in yr:
    selectyear = Select(driver.find_element_by_id('year'))
    selectyear.select_by_value(y)
    for m in mon:
        selectmon = Select(driver.find_element_by_id('month'))
        selectmon.select_by_value(m)
        driver.find_element_by_xpath('//*[@id="adminForm"]/fieldset/div/button').click()
        time.sleep(5)
        try:
            fro=driver.find_element_by_xpath('//*[@id="adminForm"]')
        except:
            break
                
        LI=driver.find_elements_by_xpath('//*[@id="adminForm"]/ul/li')
        for ll in LI:
            h3=ll.find_element_by_tag_name('h3')
            a=h3.find_element_by_tag_name('a')
            file=a.get_attribute("href")
            PDF.append(file)
            print(file)
        
        
        
print('Done')
    
    
'''




'''
h3=LI[0].find_element_by_tag_name('h3')
a=h3.find_element_by_tag_name('a')
file=a.get_attribute("href")
a.click()
time.sleep(7)

print('scrape')


for pd in PDF:
    P=[]
    P.append(pd)
    #sheet.append(P)
    #wb.save("Modele 4 BN.xlsx")
    driver.get(pd)
    time.sleep(2)

    pages=driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[4]/div/div')

    print(len(pages))
    length=1

    #('//*[@id="pageNumber"]').send_key[str(length)]

    for page in pages:
        try:
        
            body=page.find_element_by_class_name('textLayer')
            span=body.find_elements_by_tag_name('span')
            print(len(span))
            span=span[5:]
            i=0
            temp=''
            End=0
            DATA=[]
            chno = 0
            chen= 0
            for sp in span:
                #my = sp.find_element_by_xpath("//span[text()='Enseigne:']")
                #print(my)
                if('nationalité' in sp.text   and chno == 0):
                    #print('nom...............')
                    nom=temp
                    print('#1')
                    print(nom)
                    DATA.append(nom)
                    F=i
                    F=F+2
                    #print('na...............')
                    print('#2')
                    nest=span[F].text
                    #2
                    print(nest)
                    DATA.append(nest)
                    chno=1
                temp=temp+' '+sp.text
                if(sp.text == 'Enseigne:' ):
                    #print('Enseigne....................')
                    J=i
                    J=J+1
                    En=span[J].text
                    #3
                    En=En.replace('«','')
                    En=En.replace('»','')
                    print('#3')
                    print(En)
                    
                    DATA.append(En)
                    End=J
                    break
                #print(sp.text)
                i+=1
            #print('....')
            End+=2
            span=span[End:]
            #print('1',span[0].text)
            j=0
            obj=''
            for sp in span:
                if(sp.text == 'Adresse:'):
                    End=j
                    break
                obj=obj+' '+sp.text
                j+=1
            #4
            print('#4')
            print(obj)
            DATA.append(obj)
            k=0
            End+=1
            span=span[End:]
            #print('2',span[0].text)
            address=''
            for sp in span:
                if(sp.text == 'RCCM:'):
                    End=k
                    break
                address=address+' '+sp.text
                k+=1
            #5
            print('#5')
            print(address)
            DATA.append(address)
            L=0
            span=span[End:]
            #print('3',span[0].text)
            try:
                
                RCCM=span[1].text
                
                #6
                print('#6')
                print(RCCM)
                print(span[1].text)
                RCC=RCCM.split('du')
                print(RCC[0])
                DATA.append(RCC[0])
                
                try:
                    print('#7')
                    print(RCC[1])
                    DATA.append(RCC[1])
                except:
                    print('##7')
                    dat=span[2].text
                    print(dat)
                    DATA.append(dat)
            except:
                pass
            
            print(len(DATA))
            if(len(DATA) >= 6):
                print('Writeeeeeeeeeeeeeeeeeeee')
                #sheet.append(DATA)
                #wb.save("Modele 4 BN.xlsx")
                
        except:
            pass
        
        
        try:
            print('Next+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            driver.find_element_by_xpath('//*[@id="next"]').click()
            time.sleep(1)
                
        except:
            print('Not Next+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            pass



'''






'''
urls=[]
with open("URL.txt") as file_in:
    for line in file_in:
        print(line)
        urls.append(line)

for url in urls:
    data=[]
    

    time.sleep(10)

    ID=url.replace('https://ce.naco.org/?county_info=',' ')

    main=driver.find_element_by_xpath('//*[@id="countyName"]').text
    name=main.split(',')
    na=name[0].replace('country',' ')
    state=name[-1]
    print(ID)
    data.append(ID)
    print(na)
    data.append(na)
    print(state)
    data.append(state)

    web=driver.find_element_by_xpath('//*[@id="cWebsite"]/a').get_attribute("href")
    print(web)
    data.append(web)
    GT=driver.find_element_by_xpath('//*[@id="cGovType"]').text
    print(GT)
    data.append(GT)
    Au=driver.find_element_by_xpath('//*[@id="cAuth"]').text
    print(Au)
    data.append(Au)
    Lb=driver.find_element_by_xpath('//*[@id="cLegBod"]').text
    print(Lb)
    data.append(Lb)
    size=driver.find_element_by_xpath('//*[@id="cLegSize"]').text
    print(size)
    data.append(size)
    pop=driver.find_element_by_xpath('//*[@id="cPop"]').text
    print(pop)
    data.append(pop)

    sheet.append(data)
    wb.save("Data.xlsx")





Title= driver.find_element_by_xpath('//*[@id="bookcontent"]/h2')
elems = div.find_elements_by_tag_name("a")
ref=[]
links=[]
for elem in elems:
    print(elem.get_attribute("title"))
    ref.append(elem.get_attribute("title"))
    print(elem.get_attribute("href"))
    links.append(elem.get_attribute("href"))

for link in links:
    print(link)
    driver.get(link)
    time.sleep(5)

    par =driver.find_element_by_xpath('//*[@id="content-bible"]/div/div[1]/div[2]/div[1]/div/p')
    span=driver.find_elements_by_xpath('//*[@id="content-bible"]/div/div[1]/div[2]/div[1]/div/p/span')
    span=span[1:]
    verse=''
    for sp in sapn:
        s=sp.text
        verse=verse+" "+s
        
'''

print('Allllllllllllll DOneeeeeeeeeeeeeeeeeeeeeeeeeeeeee')



