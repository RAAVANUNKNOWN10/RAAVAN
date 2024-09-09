import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkBlue')
EXCEL_FILE = 'E:/spend.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Button('Labour'), sg.Button('Income')],
    [sg.Text('PLESE ENTER SPEND MONEY DATA :')],
    [sg.Text('Bill No. :', size=(15,1)), sg.InputText(key='Bill No.')],
    [sg.Text('Name Of Item', size=(15,1)), sg.InputText(key='Name Of Item')],
    [sg.Text('Date', size=(15,1)), sg.InputText(key='Date')],
    [sg.Text('Amount', size=(15,1)), sg.InputText(key='Amount')],
    [sg.Text('Method of payment:' ,size= (15,1)),sg.Combo(["ONLINE","BANK","CASH"], key = "METHOD") ],
    [sg.Text('Name Of Person', size=(15,1)), sg.InputText(key='Name Of Person')],
    [sg.Text('Remark', size=(20,5)), sg.InputText(key='Remark')],
    [sg.Submit(),sg.Button('Clear') ,sg.Exit()]
]
window = sg.Window('SPEND MONEY DATA',layout)
def clear_input():
    for key in values:
        window[key]("")
    return None
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('DATA SAVED SAFELY !')
        clear_input()

    # labour panal start

    if event == 'Labour':
        sg.theme('DarkGreen')
        EXCEL_FILE = 'E:/labour.xlsx'
        df = pd.read_excel(EXCEL_FILE)
        layout = [
            
            [sg.Text('PLESE ENTER SPEND MONEY DATA :')],
            [sg.Text('Name Of Person', size=(15,1)), sg.InputText(key='Name Of Person')],
            [sg.Text('Attendance:', size=(15,1)), sg.InputText( key='Total Attendance')],
            [sg.Text('Per Day wage', size=(15,1)), sg.InputText(key='One Day Wage')],
            [sg.Text('Amount', size=(15,1)), sg.InputText(key='Amount')],
            [sg.Text('Date', size=(15,1)), sg.InputText(key='Date')],
            [sg.Text('Method of payment:' ,size= (15,1)),sg.Combo(["ONLINE","BANK","CASH"], key = "METHOD") ],
            [sg.Text('Remark', size=(20,5)), sg.InputText(key='Remark')],
            [sg.Submit(),sg.Button('Clear') ,sg.Exit()]
        ]
        window = sg.Window('LABOUR DATA',layout)
        def clear_input():
            for key in values:
                window[key]("")
            return None
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Clear':
                clear_input()
            if event == 'Submit':
                df = df.append(values, ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)
                sg.popup('DATA SAVED SAFELY !')
                clear_input()
    else :
        pass
# Income panel start here in this code
    if event == 'Income':
        sg.theme('Black')
        EXCEL_FILE = 'C:/Users/Lenovo/Desktop/mata/income.xlsx'
        df = pd.read_excel(EXCEL_FILE)
        layout = [
            
            [sg.Text('PLESE ENTER DATA :')],
            [sg.Text('Date', size=(15,1)), sg.InputText(key='Date')],
            [sg.Text('Name Of Person', size=(15,1)), sg.InputText(key='Name Of Person')],
            [sg.Text('Amount', size=(15,1)), sg.InputText(key='Amount')],
            [sg.Text('Method of payment:' ,size= (15,1)),sg.Combo(["ONLINE","BANK","CASH"], key = "METHOD") ],
            [sg.Text('Pad No.:', size=(15,1)), sg.InputText(key='Pad no.')],
            [sg.Text('Collection :', size=(15,1)), sg.Combo(["DAN PATR","BANK","PAD"], key = "Collection") ],
            [sg.Text('Remark', size=(20,5)), sg.InputText(key='Remark')],
            [sg.Submit(),sg.Button('Clear') ,sg.Exit()]
        ]
        window = sg.Window('INCOME DATA',layout)
        def clear_input():
            for key in values:
                window[key]("")
            return None
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Clear':
                clear_input()
            if event == 'Submit':
                df = df.append(values, ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)
                sg.popup('DATA SAVED SAFELY !')
                clear_input()
    else :
        pass
window.close()
