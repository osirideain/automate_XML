import xml.etree.ElementTree as ET
from iteration_utilities import duplicates
import pymysql




##user_xml = "HeurekaValidFeed.xml"
user_xml = "Shop1.xml"

table = "xml_table"
##table = "new_xml_table"
other_table = "xml_alt_table"
##other_table = "new_xml_alt_table"
mytree=ET.parse(user_xml)
root=mytree.getroot()





                 
##tags1 = []
##tags2 = []
##for x in root.find("./"):
##    if x.text is not None:
##        tags1.append(x.tag)
##    for y in x:
##        if y.text is not None:
##            tags2.append(y.tag)
##
##print(tags1, tags2)    
        
def tags():
    mytree=ET.parse(user_xml)
    root=mytree.getroot()
    tags = []
    for x in root.find("./"):
        if x.text is not None:
            tags.append(x.tag)
        for y in x:
            if y.text is not None:
                tags.append(y.tag)
    return tags

def duplicate_tags():
    duplicate = list(duplicates(tags()))
    duplicate1 = []
    for x in duplicate:
        if x not in duplicate1:
            duplicate1.append(x)
    return duplicate1
##print(duplicate_tags())
def IDS():
    mytree=ET.parse(user_xml)
    root=mytree.getroot()
    list = []
    for x in root.find("./SHOPITEM"):
        if "ID" in x.tag:
            list.append(x.tag)
    for x in root.find("./SHOPITEM"):
        if "NO" in x.tag:
            list.append(x.tag)
    for x in list:
        if "ID" in x:
            list.remove(list[1])
    return list
alt_list = []
items_list = []
new_list = []
item_ids_list = []

##item_ids_list = IDS()
for x in root.find("./SHOPITEM"):
    for item in x:
        print(item.tag)
##        value = item.get("PARAM_NAME")
##        print(value.tag)

##    def duplicate_item_list():
##        def item_ids():
##            list = []
##            ids = x.find(" ".join(IDS()))
##            try:
##                list.append(ids.text)
##            except AttributeError:
##                return ""
##            return list
##        item_ids_list.append(item_ids())
##        def single_grouping():
##            for y in duplicate_list:
##                for z in x.findall(".//"+y):
##                    def group():
##                        list = []
##                        list.append(item_ids())
##                        list.append(z.text)
##                        return list
##                    group()
##                    print(group())
##                    alt_list.append(tuple(group()))
##        def other_grouping():
##            for y in x:
##                for z in y:
##                    for item in duplicate_list:
##                        if item == z.tag:
##                            def group():
##                                list = []
##                                list.append(item_ids())
##                                list.append({item : z.text})
##                                return list
##                            group()
##                            items_list.append(group())
##
##        if len(duplicate_list) == 1:
##            single_grouping()
##        elif len(duplicate_list) > 1:
##            other_grouping()
##
##            
##    duplicate_item_list()
##print(items_list)
##for item in items_list:
##    for other_item in item_ids_list:
##        if item[0] == other_item:
##            for dic in item[1]:
##                for num in range(len(duplicate_list)):
##                    if duplicate_list[num] == dic:
##                        new_list.insert(0, item[0])
##                        new_list.insert(num+1, item[dic])
##            alt_list.append(tuple(new_list))
##            print("Finished alt list")
##print(alt_list)

def create_table():
    mytree=ET.parse(user_xml)
    root=mytree.getroot()

    conn = pymysql.connect(host='' ,
                             port=10065,
                             user='',
                             password='',
                             db='')

    column_list = []
    for x in tags():
        if x not in duplicate_tags():
            column_list.append(x)

    column_list = " text, ".join(column_list)
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists {}({})".format(table, column_list+ " text"))
        conn.commit()
    print("First table created")

    
    duplicate_list = []
    for x in duplicate_tags():
        duplicate_list.append(x)
    
    duplicate_list = " text, ".join(duplicate_list)
    ids_list = "".join(IDS())
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists {}({},{})".format(other_table,ids_list+" text",duplicate_list+ " text"))
        conn.commit()
    print("All tables created")
##create_table()

def CreateXML():
##    conn = pymysql.connect(host='db.veryangryman.savana-hosting.cz' ,
##                             port=10065,
##                             user='cpd',
##                             password='abc123.',
##                             db='cpd')





    class tag_items:
        def __init__(self, tag_name=""):
            self.tag_name = tag_name

        
        def items(self):
            tag = x.find(self.tag_name)
            if tag is not None:
                return tag.text
            else:
                return "0"
            for a in root.find("./SHOPITEM"):
                for b in a:
                    if b.tag == self.tag_name:
                        for c in root.findall("./SHOPITEM"):
                            for y in c.findall("./"+a.tag):
                                item = y.find(self.tag_name)
                                if item is not None:
                                    return item.text
                                else:
                                    return "0"


        def other_items(self):
            for y in x:
                if y.text is None:
                    tag = y.find(self.tag_name)
                    if tag is not None:
                        return tag.text
                    else:
                        return "0"
            for a in root.find("./SHOPITEM"):
                for b in a:
                    if b.tag == self.tag_name:
                        for c in root.findall("./SHOPITEM"):
                            for y in c.findall("./"+a.tag):
                                item = y.find(self.tag_name)
                                if item is not None:
                                    return item.text
                                else:
                                    return "0"

##        def other_group(self):
##            for y in x:
##                for self.name in y:
##                    if y.tag == "PARAM":
##                        return self.name.text

            

    mytree=ET.parse(user_xml)
    root=mytree.getroot()
    column_list = []
    for x in tags():
        if x not in duplicate_tags():
            column_list.append(x)

    duplicate_list = []
    for y in duplicate_tags():
        duplicate_list.append(y)


    tags1 = []
    tags2 = []
    for x in root.find("./"):
        if x.text is not None:
            tags1.append(x.tag)
        for y in x:
            if y.text is not None:
                tags2.append(y.tag)
##    print(tags1)
##    print(tags2)
    new_list = []
    alt_list = []
    
    for x in root.findall("./SHOPITEM"):
        def item():
            list = []
            for y in tags1:
                for b in range(len(column_list)):
                    if column_list[b] == y:
                        item = tag_items(y)
                        list.insert(b, item.items())
            for y in tags2:
                for b in range(len(column_list)):
                    if column_list[b] == y:
                        item = tag_items(y)
                        list.insert(b, item.other_items())
            return list
##        new_list.append(tuple(item()))
        def duplicate_item_list():
            def item_ids():
                ids = x.find(" ".join(IDS()))
                try:
                    return ids.text
                except AttributeError:
                    return ""
            
            def single_grouping():
                for x in root.find("./"):
                    for y in duplicate_tags():
                        for z in x.findall(".//"+y):
                            def group():
                                list = []
                                list.append(item_ids())
                                list.append(z.text)
                                return list
                            group()
                            print(group())
                            alt_list.append(tuple(group()))
            def other_grouping():
                pass
##                list = []
##                for x in root.find("./"):
##                    for y in duplicate_list:
##                        for z in x.findall(".//"+y):
##                            list.append({z.tag : z.text})
##                return list
##            print(other_grouping())
##            other_grouping_list = other_grouping()
##            item_ids_list = item_ids()
##            for ids in item_ids_list:
##                if ids not in other_grouping_list:
##                    other_grouping_list.insert(0, ids)
##            print(other_grouping_list)        
##            alt_list.append(tuple(other_grouping()))
                                    
                                        

            if len(duplicate_list) == 1:
                single_grouping()
            elif len(duplicate_list) > 1:
                other_grouping()
##                print(other_grouping())
        duplicate_item_list()
                
        
##    print(items_list)
##    print(new_list)
##    print(alt_list)
##    values = []
##    for x in range(len(column_list)):
##        x = "%s"
##        values.append(x)
##    values = ", ".join(values)
##    column_list = ", ".join(column_list)
##    duplicate_list = ", ".join(duplicate_tags())
##    conn.ping()
##    with conn.cursor() as cursor:
##        cursor.executemany("INSERT INTO {}({})VALUES({})".format(table, column_list, values), new_list)
##        conn.commit()
##    print("First table's items uploaded")
##    values = []
##    for x in range(len(duplicate_tags())):
##        x = "%s"
##        values.append(x)
##    values = ", ".join(values)
##    with conn.cursor() as cursor:
##        cursor.executemany("INSERT INTO {}({},{})VALUES(%s,{})".format(other_table, "".join(IDS()), duplicate_list, values), alt_list)
##        conn.commit()
##    print("All tables' items uploaded")
##CreateXML()







