#! python3
# ws-map lanuch map in browser ussing adress from
# command line / clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #get address frm command line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)

    
