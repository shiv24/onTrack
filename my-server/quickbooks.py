#Please install zeep and xmltodict libs using these commands in Command window first:
#pip install zeep
#pip install xmltodict

from zeep import Client
import xmltodict
from datetime import datetime
from random import choice, randint
from time import sleep

# Please update these lines with your own companyname, userame, and password

# method email
username = "sufientout@gmail.com"
password = "cIphertext23!"
# first part of the url when logged into method  -> XYZ.method.me -> companyName: "XYZ"
companyName = "projectdarwin"

base_url = 'https://www.methodintegration.com/'


# --------------------------------------------------------
# ITEMS table -- Select
# -----------------------------------------------------

table_name = 'Item'
unique = datetime.now().strftime('%m%d%H%M%S')

#select
# insert_fields = {
#     "FullName": "Hours",
#     "IsTrackQtyOnHand": "true",
#     "ItemType": "Service",
#     "SalesPrice": "100",
#     "SalesDesc": ""
# }

fields = ["FullName", "IsTrackQtyOnHand", "ItemType", "SalesPrice", "SalesDesc"]

# update_fields = {
#     "Name": "Hours",
#     "IsTrackQtyOnHand": "true",
#     "SalesPrice": ""
# }

#Initializing the zeep
client = Client(wsdl=base_url+'MethodAPI/service.asmx?WSDL')
factory = client.type_factory('ns0')

# There is a bit of weiredness with passing arrays to zeep and it needs to be converted like this:
# names = factory.ArrayOfString(list(update_fields.keys()))
# values = factory.ArrayOfString(list(update_fields.values()))

# record_id="7"

# xml_str = client.service.MethodAPIUpdateV2(
#     companyName,
#     username, password, None,
#     table_name, names, values, record_id)
# assert xml_str is not None
# update_result = xmltodict.parse(xml_str)
# assert 'Success' in update_result['MethodAPI']['@response'], xml_str
# print('Update API completed')

products = [7, 8, 9, 10, 11, 12]

print("First Load")
for i in products:
    record_id=str(i)
    #Select
    xml_str = client.service.MethodAPISelect_XMLV2(
        companyName,
        username, password, None,
        # table_name, ','.join(list(insert_fields.keys())), 'RecordID=' + record_id)
        table_name, ','.join(fields), 'RecordID=' + record_id)
    assert xml_str is not None
    select_result = xmltodict.parse(xml_str)
    assert 'Success' in select_result['MethodAPI']['@response'], xml_str
    assert 'Record' in select_result['MethodAPI']['MethodIntegration']
    row = select_result['MethodAPI']['MethodIntegration']['Record']
    print('Retrieved values from Select API:')
    print(row)

while True:
    sleep(randint(1, 4))
    record_id=str(choice(products))
    sleep(randint(1, 3))
    #Select
    xml_str = client.service.MethodAPISelect_XMLV2(
        companyName,
        username, password, None,
        # table_name, ','.join(list(insert_fields.keys())), 'RecordID=' + record_id)
        table_name, ','.join(fields), 'RecordID=' + record_id)
    assert xml_str is not None
    select_result = xmltodict.parse(xml_str)
    assert 'Success' in select_result['MethodAPI']['@response'], xml_str
    assert 'Record' in select_result['MethodAPI']['MethodIntegration']
    row = select_result['MethodAPI']['MethodIntegration']['Record']
    print('Retrieved values from Select API:')
    print(row)
    sleep(randint(7, 15))






# --------------------------------------------------------
# ITEMS INVENTORY table
# -----------------------------------------------------
