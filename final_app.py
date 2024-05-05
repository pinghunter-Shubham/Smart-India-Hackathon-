import io
import PySimpleGUI as sg
from PIL import Image
from buttons import custom_button1,custom_button2,custom_button3,custom_button4,custom_button5,custom_button6
from qrcode import scan_qr_code
import copy
import webbrowser
from museum import get_item_info_text,get_item_info_voice,get_item_info_video
from heritage import display_heritage_sites_by_state
from connector import get_cultural_details
from voice import get_audio_file_name
states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands",
    "Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Lakshadweep","Delhi","Puducherry"
]

image_path = "C:\\Users\\RUPAM DAS\\Desktop\\SIH FINAL\\india.png"
image_path2 = image_path3 = "C:\\Users\\RUPAM DAS\\Desktop\\SIH FINAL\\india.png"

sg.set_options(background_color='#FFFFFF')
layout = [
    [sg.Image(key="-IMAGE-", pad=((182, 110), (10, 0)))],
    [custom_button1], [custom_button2], [custom_button3]
]

main_window = sg.Window("Image Viewer", layout, finalize=True, size=(600, 600))

if image_path:
    image = Image.open(image_path)
    image.thumbnail((200, 200))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    main_window["-IMAGE-"].update(data=bio.getvalue())

def copy_window(layout):
    copied=copy.deepcopy(layout)
    explore_window = sg.Window('Explore Window', copied,finalize=True, size=(600, 600))
    return explore_window

flag = 0
while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-EXPLORE-":
        explore_layout =  [
        [sg.Button('←-', key='Back', button_color=('white', 'red'),font=('Arial', 8),size=(4, 0),pad=((10, 0), (15, 0)),border_width=2)],
        [sg.Image(key="-IMAGE2-", pad=((182, 110), (10, 0)))],    
        [custom_button4], [custom_button5], [custom_button6]
        ]
        main_window.hide()
        explore_window=copy_window(explore_layout)
        if image_path:
            image = Image.open(image_path2)
            image.thumbnail((200, 200))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            explore_window["-IMAGE2-"].update(data=bio.getvalue())
        while True:
            event, values = explore_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event=='-TEXT SUMMARY-':
                result = scan_qr_code()
                person=get_item_info_text(result)
                popup_layout = [
                        [sg.Image(key="-IMAGE2-", pad=((182, 110), (10, 0)))],
                        [sg.Multiline(person, key='-heat-', size=(80,10), pad=(20,10), disabled=True, font=('Comic Sans MS', 12))],
                    ]
                new_window = sg.Window('Text Summary', popup_layout, finalize=True, size=(600, 600))
                if image_path2:
                    image = Image.open(image_path2)
                    image.thumbnail((200, 200))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    new_window["-IMAGE2-"].update(data=bio.getvalue())
                eventx, valuesx = new_window.read()
                if eventx==sg.WIN_CLOSED:
                    new_window.close()
            elif event=='-VOICE SUMMARY-':
                result = scan_qr_code()
                person=get_item_info_voice(result)
                get_audio_file_name(person)
            elif event=='-VIRTUAL SUMMARY-':
                result = scan_qr_code()
                person=get_item_info_video(result)
                webbrowser.open(person)
            elif event == 'Back':
                main_window.un_hide()  # Show the main window
                explore_window.close()  # Close the Explore window

    elif event == "-HERITAGE PLACES-":
        main_window.hide() 
        heritage_layout = [
            [sg.Button('←-',key='Back', button_color=('white','red'), pad=(20,5))],
            [sg.Image(key="-IMAGE3-", pad=((182, 110), (10, 0)))],
            [sg.Text('India is blessed with vast and rich cultural heritage all across\nits boundaries. We have preserved our cultural heritage since ancient times\nfor our future generations. Despite the technological advancement, India as a\nnation has been deeply attached to its root of the old ancient tradition.',
                      pad=((20,20), (20,10)), font=('Arial', 12), background_color='white', text_color='black')],
            [sg.Text('Please select your state: ', font=('Arial', 14), background_color='blue', text_color='white', expand_x=True, pad=((20,20), (5,5)))],
            [sg.DropDown(states, key='-LOC-', default_value='Andhra Pradesh', pad=((20,20), (5, 5)), expand_x=True)],
            [sg.Button('OK', key='Ok', button_color=('white','red'), pad=((20,10), (4,4)))],
            [sg.Multiline('Heritage Information', key='-Heritage-', font=('Comic Sans MS', 12), size=(80, 10), pad=(20,10), disabled=True)],
        ]
        heritage_window = sg.Window('Explore Window', heritage_layout,finalize=True, size=(600, 600))
        if image_path:
            image = Image.open(image_path3)
            image.thumbnail((200, 200))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            heritage_window["-IMAGE3-"].update(data=bio.getvalue())
        while True:
            event, values = heritage_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event=='Ok':
                loc = values['-LOC-']
                heritage_window['-Heritage-'].update(display_heritage_sites_by_state(loc))
            elif event == 'Back':
                heritage_window.close()  # Close the Explore window
                main_window.un_hide()  # Show the main window
    elif event == "-CULTURE-":
        main_window.hide() 
        culture_layout = [
            [sg.Button('←-',key='Back', button_color=('white','red'), pad=(20,5))],
            [sg.Image(key="-IMAGE4-", pad=((182, 110), (10, 0)))],
            [sg.Text('Indian culture is very diverse and the people of India are very\nwarm and welcoming. They have a strong sense of family and\nfirmly believe in unity in diversity. In India, there is a saying which\nis "Atithi Devo Bhava" meaning - The guest is equivalent to God.',
                     pad=(20,10), font=('Arial', 14), background_color='white', text_color='black', expand_x=True)],
            [sg.Text('Please select your state: ', font=('Arial', 14), background_color='blue', text_color='white', expand_x=True, pad=((20,20), (5,5)))],
            [sg.DropDown(states, key='-CULT-', default_value='Andhra Pradesh', expand_x=True, pad=((20,20), (10,10)))],
            [sg.Button('OK', key='Ok', button_color=('white','red'), pad=((20,10), (4,4)))],
            [sg.Multiline('Culture Information', key='-Culture-', size=(80, 10), font=('Comic Sans MS', 12), pad=(20,10), disabled=True)],
        ]
        culture_window = sg.Window('Explore Window', culture_layout,finalize=True, size=(600, 600))
        if image_path:
            image = Image.open(image_path3)
            image.thumbnail((200, 200))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            culture_window["-IMAGE4-"].update(data=bio.getvalue())
        while True:
            event, values = culture_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event=='Ok':
                ex = values['-CULT-']
                culture_window['-Culture-'].update(get_cultural_details(ex))
            elif event == 'Back':
                culture_window.close()  # Close the Explore window
                main_window.un_hide() 

main_window.close()



