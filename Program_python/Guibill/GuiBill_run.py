import PySimpleGUI as sg
import cv2
from creategui import changedicttolist, CreateTablegui, Data_template
from resizefill import resize, xyaxis
from PIL import ImageFont, ImageDraw, Image
import tldextract
import subprocess
import platform
import argparse
import yaml
import imutils
import datetime
import os

config_vals = ""
file_path=os.getcwd().split(os.sep)
mn_funitures_path=file_path[1]+file_path[2]+file_path[3]
with open(mn_funitures_path+"Program_python/Guibill/config.yaml", "r") as cr:
   config_vals = yaml.load(cr)

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
def CreateGuibill():
    Data_template = ['PhotoPath', 'Name', 'Phone', 'Address', 'Order','Delivery', 'Delivery2', 'Price', 'Value', 'Discount', 'Deposit','Detail']
    watermark = Image.open(mn_funitures_path+'Bill/Template/PAID.png')
    Current_Date_Formatted = datetime.datetime.today().strftime('%d/%m/%Y')
    sg.theme('DarkAmber')
    x_offset = 100
    y_offset = 350
    layout = CreateTablegui(Data_template)
    window = sg.Window('Billing Address', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':
            window.close()
            break
    listofvalues = changedicttolist(values)
    Data = dict(zip(Data_template, listofvalues))
    Data["PhotoPath"]=mn_funitures_path+Data["PhotoPath"]
    if(len(Data["PhotoPath"])) < 5:
        Data["PhotoPath"] = config_vals["PhotoPath"]
    if(len(Data["Discount"])) < 5:
        Data["Discount"] = config_vals["Discount"]
    if(len(Data["Phone"])) < 5:
        Data["Phone"] = config_vals["Phone"]
    if(len(Data["Name"])) < 5:
            Data["Name"] = config_vals["Name"]
    if(len(Data["Value"])) < 1:
        Data["Value"] =config_vals["Value"]
        if(len(Data["Price"])) < 1:
            Data["Price"] =config_vals["Price"]
        if(len(Data["Deposit"])) <1:
            Data["Deposit"] = config_vals["Deposit"]
    if(len(Data["Order"]))<1:
        Data["Order"] = Current_Date_Formatted
    if(len(Data["Delivery"])==1):
        if(Data["Delivery"])=='1':
            Data["Delivery"]= (datetime.datetime.today()+datetime.timedelta(days=10)).strftime('%d/%m/%Y')
            Data["Delivery2"]=(datetime.datetime.today()+datetime.timedelta(days=14)).strftime('%d/%m/%Y')
    if(len(Data["Detail"])<1):
        Data["Detail"]=''

    imgdefault = cv2.imread(Data["PhotoPath"])
    img = imutils.resize(image=imgdefault, height=200)

    template = cv2.imread(mn_funitures_path+
        "Bill/Template/TemplateBill.jpg")
    template[y_offset:y_offset + img.shape[0],
             x_offset:x_offset + img.shape[1]] = img

    cv2.imwrite(mn_funitures_path+
        "Bill/PretoPaid/Pretopaid.jpg", template)
    image = Image.open(mn_funitures_path+
        "Bill/PretoPaid/Pretopaid.jpg")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(mn_funitures_path+"static/Fonts/Arial Unicode.ttf", 13)
    font2 = ImageFont.truetype(mn_funitures_path+"static/Fonts/Arial Unicode.ttf", 11)
    Summaryvalue = (int((Data["Price"])) *
                    int((Data["Value"]))) - int((Data["Discount"]))
    RemainValue = Summaryvalue - int((Data["Deposit"]))

    draw.text((xyaxis["x_name"], xyaxis["y_name"]), Data["Name"] +
              "  (" + Data["Phone"] + ")", font=font, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_address"], xyaxis["y_address"]),
              Data["Address"], font=font2, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_order"], xyaxis["y_order"]),
              Data["Order"], font=font, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_delivery"], xyaxis["y_delivery"]),
              Data["Delivery"] + " -", font=font2, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_delivery2"], xyaxis["y_delivery2"]),
              Data["Delivery2"], font=font2, fill=(0, 0, 0, 0))

    draw.text((xyaxis["x_value"], xyaxis["y_value"]),
              Data["Value"], font=font, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_discount"], xyaxis["y_discount"]),
              Data["Discount"], font=font, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_price"], xyaxis["y_price"]),
              Data["Price"], font=font, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_priceafterdiscount"], xyaxis["y_priceafterdiscount"]), str(
        Summaryvalue), font=font, fill=(0, 0, 0, 0))
    draw.text((xyaxis["x_summary"], xyaxis["y_summary"]),
              str(Summaryvalue), font=font, fill=(0, 0, 0, 0))

    draw.text((xyaxis["x_deposit"], xyaxis["y_deposit"]),
              Data["Deposit"], font=font, fill=(0, 0, 0, 0))

    draw.text((xyaxis["x_remain"], xyaxis["y_remain"]),
              str(RemainValue), font=font, fill=(0, 0, 0, 0))
    draw.text((100,600),Data["Detail"],font=font,fill=(0,0,0,0))
    image2 = image.copy()
    img_w = image2.width
    img_h = image2.height
    watermarkW = watermark.width
    watermarkH = watermark.height
    image2.paste(watermark, (int((img_w - watermarkW) / 2),
                             int((img_h - watermarkH) / 2)), watermark)
    image.save(
        mn_funitures_path+"Bill/PretoPaid/Pretopaid2.jpg")
    image2.save(
        mn_funitures_path+"Bill/PretoPaid/Pretopaid2_paid.jpg")


def main():
    CreateGuibill()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is Resize image  script')
    parser.add_argument('--open', '-o', action='count', default=0,required=False)
    results = parser.parse_args()
    statefolder = results.open
    main()
    if statefolder != 0:
        open_file(mn_funitures_path+"Bill/PretoPaid/")
