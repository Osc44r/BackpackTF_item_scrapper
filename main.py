if __name__ == '__main__':
    import sys

    import undetected_chromedriver as uc
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    print("Loading...")
    options = Options()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.get("https://backpack.tf/spreadsheet")
    minref = float(input("Input minimum price in refs to fetch data (min: 0.5, default: 1): "))
    if minref < 0.05:
        print("Minimum price can not be lower than 0.05")
        sys.exit()
    maxref = float(input("Input maximum price in refs to fetch data (min: 0.5, default: 40): "))
    if maxref < 0.05:
        print("Maximum price can not be lower than 0.05")  
        sys.exit()
        
    parseGenuine = input("Parse genuine items? (y/n): ")
    if parseGenuine != "y" and parseGenuine != "n":
        print("You were supposed to pick y/n there.")
        sys.exit()
    parseVintage = input("Parse vintage items? (y/n): ")
    if parseVintage != "y" and parseVintage != "n":
        print("You were supposed to pick y/n there.")
        sys.exit()
    parseUnique = input("Parse unique items? (y/n): ")
    if parseUnique != "y" and parseUnique != "n":
        print("You were supposed to pick y/n there.")
        sys.exit()
    parseStrange = input("Parse strange items? (y/n): ")
    if parseStrange != "y" and parseStrange != "n":
        print("You were supposed to pick y/n there.")
        sys.exit()
    parseHaunted = input("Parse haunted items? (y/n): ")
    if parseHaunted != "y" and parseHaunted != "n":
        print("You were supposed to pick y/n there.")
        sys.exit()
    parseCollector = input("Parse collector's items? (y/n): ")
    if parseCollector != "y" and parseCollector != "n":
        print("You were supposed to pick y/n there.")
        sys.exit()
    parseFestivized = input("Parse festivized items? (y/n): ")
    if parseFestivized !="y" and parseFestivized !="n":
        print("You were supposed to pick y/n there.")
        sys.exit()        

    def wait():
        try:
            panel = WebDriverWait(driver,30).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody"))
            )
        except:
            print("Backpack.tf is out of range. Refreshing...")
            driver.refresh()
            wait()

    wait()
    panel = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody")
    id = 0
    f = open('./ItemList.txt','w',encoding="utf-8")
    f.write("Items = [")
    f.close()
    for tr in panel.find_elements(By.TAG_NAME,"tr"):
        id = id+1

        itemname = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[1]")
        typee = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[2]")
        genuine = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[3]")
        vintage = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[4]")
        unique = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[5]")
        strange = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[6]")
        haunted = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[7]")
        collector = panel.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[2]/div/table/tbody/tr["+str(id)+"]/td[8]")

        if "Crate" not in itemname.text and "(Non-Craftable)" not in itemname.text and "Tool" not in typee.text and "Primary" not in typee.text and "Secondary" not in typee.text and "Melee" not in typee.text and "Botkiller" not in itemname.text and "Golden" not in itemname.text and "Australium" not in itemname.text and "Festive" not in itemname.text:
            if parseGenuine == "y":
                if float(genuine.get_attribute("abbr")) > minref and float(genuine.get_attribute("abbr")) < maxref:
                    print('"Genuine '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Genuine '+itemname.text+'",')
                    f.close()
                elif parseFestivized == "y" and float(genuine.get_attribute("abbr")) != 0 and float(genuine.get_attribute("abbr")) < minref and float(genuine.get_attribute("abbr")) < maxref and "Primary" in typee.text:
                    print('"Festivized Geniune '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Festivized Genuine '+itemname.text+'",')
                    f.close()
            if parseVintage == "y":
                if float(vintage.get_attribute("abbr")) > minref and float(vintage.get_attribute("abbr")) < maxref:
                    print('"Vintage '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Vintage '+itemname.text+'",')
                    f.close()
                elif parseFestivized == "y" and float(vintage.get_attribute("abbr")) != 0 and float(vintage.get_attribute("abbr")) < minref and float(vintage.get_attribute("abbr")) < maxref and "Primary" in typee.text:
                    print('"Festivized Vintage '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Festivized Vintage '+itemname.text+'",')
                    f.close()
            if parseUnique == "y":
                if float(unique.get_attribute("abbr")) > minref and float(unique.get_attribute("abbr")) < maxref:
                    print('"'+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"'+itemname.text+'",')
                    f.close()
                elif parseFestivized == "y" and float(unique.get_attribute("abbr")) != 0 and float(unique.get_attribute("abbr")) < minref and float(unique.get_attribute("abbr")) < maxref and "Primary" in typee.text:
                    print('"Festivized '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Festivized '+itemname.text+'",')
                    f.close()
            if parseStrange == "y":
                if float(strange.get_attribute("abbr")) > minref and float(strange.get_attribute("abbr")) < maxref:
                    print('"Strange '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Strange '+itemname.text+'",')
                    f.close()
                elif parseFestivized == "y" and float(strange.get_attribute("abbr")) != 0 and float(strange.get_attribute("abbr")) < minref and float(strange.get_attribute("abbr")) < maxref and "Primary" in typee.text:
                    print('"Strange Festivized '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Strange Festivized '+itemname.text+'",')
                    f.close()
            if parseHaunted == "y":
                if float(haunted.get_attribute("abbr")) > minref and float(haunted.get_attribute("abbr")) < maxref:
                    print('"Haunted '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Haunted '+itemname.text+'",')
                    f.close()
                elif parseFestivized == "y" and float(haunted.get_attribute("abbr")) != 0 and float(haunted.get_attribute("abbr")) < minref and float(haunted.get_attribute("abbr")) < maxref and "Primary" in typee.text:
                    print('"Festivized Haunted '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Festivized Haunted '+itemname.text+'",')
                    f.close()
            if parseCollector == "y":
                if float(collector.get_attribute("abbr")) > minref and float(collector.get_attribute("abbr")) < maxref:
                    print('"Collector'"'"'s "'+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Collector'"'"'s '+itemname.text+'",')
                    f.close()
                elif parseFestivized == "y" and float(collector.get_attribute("abbr")) != 0 and float(collector.get_attribute("abbr")) < minref and float(haunted.get_attribute("abbr")) < maxref and "Primary" in typee.text:
                    print('"Festivized Collector'"'"'s '+itemname.text+'"')
                    f = open('./ItemList.txt','a',encoding="utf-8")
                    f.write('"Festivized Collector'"'"'s '+itemname.text+'",')
                    f.close()
    f = open('./ItemList.txt','a',encoding="utf-8")
    f.write("]")
    f.close()

    print("\nSuccesfully created ItemList.txt")
    input("Press enter to exit: ")
    sys.exit()
