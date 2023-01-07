import csv
import os
import re

"""
Look at this as a starter for creating your own list.
The order of this might be different depends on how you get your data, 
this was from a save of the HTML page as a web complete, unsure with browser it was created from.
"""


directory = r'PATH_TO_DIRECTORY'
csvFile='WHERE_TO_SAVE_CSV_FILE'

def printList(theList):
    with open(csvFile, 'w') as list_file:
        #Creates CSV file and writes the column headers
        firstLine = ('Item Name', 'Quantity', 'Price', 'SKU', 'Status')
        writer = csv.writer( list_file )
        writer.writerow( firstLine )
        count = 0
        while count < len(theList):
            # print(theList[count])
            title = theList[count]
            count+=1
            quantity = theList[count]
            count+=1
            if count < len(theList):
                price = theList[count]
                count+=1
            if count < len(theList):
                sku = theList[count]
                count+=1
            if count < len(theList):
                status = theList[count]
                count+=1
            writer.writerow([title, quantity, price, sku, status])
    f.close()


#Goes through files in the folder
#Was having issues with extra cells showing up when writing straight to CSV, switched to a list then process that
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        f = open( directory+filename, "r" )
        read = f.readlines()
        title = ''
        price = ''
        status = ''
        theList = []
        for line in read:
            fullLine = ''
            #Title, Quantity, Price & Sku all show on this one line:
            if line.lstrip().startswith( ('data-row-data') ):
                #get TITLE
                marker1 = 'title&quot;:&quot;'
                marker2 = '&quot;'
                regexPattern = marker1 + '(.+?)' + marker2
                title = re.search(regexPattern, line).group(1).strip()
                theList.append(title)
                
                #get quantity
                qMarker = 'quantity&quot;:&quot;'
                qMarker2 = '&quot;'
                regexPatternq = qMarker + '(.+?)' + qMarker2
                quantity = re.search(regexPatternq, line).group(1).strip()
                theList.append(quantity)

                #get PRICE
                priceMarker1 = 'price&quot;:&quot;'
                priceMarker2 = '&quot;'
                regexPatternp = priceMarker1 + '(.+?)' + priceMarker2
                price = re.search(regexPatternp, line).group(1).strip()
                theList.append(price)

                #get SKU
                skuMarker1 = 'sku&quot;:&quot;'
                skuMarker2 = '&quot;'
                regexPatternp = skuMarker1 + '(.+?)' + skuMarker2
                sku = re.search(regexPatternp, line).group(1).strip()
                theList.append(sku)
            #Status is on it's own line 
            elif line.lstrip().startswith( ('Active', 'Inactive', 'Detail Page Removed') ):
                if title != '':
                    status = line.strip()
                    theList.append(status)
            else:
                continue        
    else:
        continue
printList(theList)
