try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import sys
import myNotebook as nb
from config import config
import json
from ttkHyperlinkLabel import HyperlinkLabel
import webbrowser


this = sys.modules[__name__]


class LinkOption:
    def __init__(self, enabled, enabledElement, nameElement, valueElement):
        self.enabled = enabled
        self.enabledElement = enabledElement
        self.nameElement = nameElement
        self.valueElement = valueElement


def callback(url):
    print('Now Opening: {}'.format(url))
    webbrowser.open_new(url)


def plugin_prefs(parent, cmdr, is_beta):
    this.LinkOptions = list()
    frame = nb.Frame(parent)
    nb.Label(frame, text='#').grid(row=0,column=0,padx=4,pady=4,sticky=tk.W)
    nb.Label(frame, text='Enabled').grid(row=0,column=1,padx=4,pady=4,sticky=tk.W)
    nb.Label(frame, text='Name').grid(row=0,column=2,padx=4,pady=4,sticky=tk.W)
    nb.Label(frame, text='Link').grid(row=0,column=3,padx=4,pady=4,sticky=tk.W)
    for i in range(14):
        link_Enabled = tk.IntVar(value='0')
        if this.LinkPereferences[i] and this.LinkPereferences[i]['enabled']: link_Enabled = tk.IntVar(value='1')
        nb.Label(frame, text=i+1).grid(row=i+1,column=0,padx=4,pady=4,sticky=tk.W)
        link_E = nb.Checkbutton(frame, variable=link_Enabled)
        link_E.grid(row=i+1,column=1,padx=4,pady=4,sticky=tk.W)
        link_N = nb.Entry(frame)
        link_N.grid(row=i+1,column=2,padx=4,pady=4,sticky=tk.W)
        link_N.config(width=25)
        link_N.insert(0,this.LinkPereferences[i]['name'])
        link_V = nb.Entry(frame)
        link_V.grid(row=i+1,column=3,padx=4,pady=4,sticky=tk.W)
        link_V.config(width=25)
        link_V.insert(0,this.LinkPereferences[i]['value'])
        this.LinkOptions.append(LinkOption(link_Enabled, link_E, link_N, link_V))   
    return frame


def prefs_changed(cmdr, is_beta):
    this.LinkPereferences = list()
    for linkOpt in this.LinkOptions:
        d = dict()
        d['enabled'] = linkOpt.enabled.get()
        d['name'] = linkOpt.nameElement.get()
        d['value'] = linkOpt.valueElement.get()
        this.LinkPereferences.append(d)
    config.set('perefs',json.dumps(this.LinkPereferences))
    return


def plugin_start(plugin_dir):
    #config.delete('perefs')
    this.LinkPereferences = json.loads(config.get('perefs') or '[]')
    return "HelpfulLinks"


def plugin_stop():
    return


def plugin_app(parent):
    
    link = this.LinkPereferences
    frame = tk.Frame(parent)

    # Link 1
    if link[0]['name'] and link[0]['enabled']:
        url0 = link[0]['value']
        label = tk.Label(frame, text=link[0]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=0)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url0))

    # Link 2
    if link[1]['name'] and link[1]['enabled']:
        url1 = link[1]['value']
        label = tk.Label(frame, text=link[1]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=1)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url1))

    # Link 3
    if link[2]['name'] and link[2]['enabled']:
        url2 = link[2]['value']
        label = tk.Label(frame, text=link[2]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=2)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url2))

    # Link 4
    if link[3]['name'] and link[3]['enabled']:
        url3 = link[3]['value']
        label = tk.Label(frame, text=link[3]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=3)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url3))

    # Link 5
    if link[4]['name'] and link[4]['enabled']:
        url4 = link[4]['value']
        label = tk.Label(frame, text=link[4]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=4)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url4))

    # Link 6
    if link[5]['name'] and link[5]['enabled']:
        url5 = link[5]['value']
        label = tk.Label(frame, text=link[5]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=5)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url5))

    # Link 7
    if link[6]['name'] and link[6]['enabled']:
        url6 = link[6]['value']
        label = tk.Label(frame, text=link[6]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=6)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url6))

    # Link 8
    if link[7]['name'] and link[7]['enabled']:
        url7 = link[7]['value']
        label = tk.Label(frame, text=link[7]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=7)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url7))

    # Link 9
    if link[8]['name'] and link[8]['enabled']:
        url8 = link[8]['value']
        label = tk.Label(frame, text=link[8]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=8)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url8))

    # Link 10
    if link[9]['name'] and link[9]['enabled']:
        url9 = link[9]['value']
        label = tk.Label(frame, text=link[9]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=9)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url9))

    # Link 11
    if link[10]['name'] and link[10]['enabled']:
        url10 = link[10]['value']
        label = tk.Label(frame, text=link[10]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=10)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url10))

    # Link 12
    if link[11]['name'] and link[11]['enabled']:
        url11 = link[11]['value']
        label = tk.Label(frame, text=link[11]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=11)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url11))

    # Link 13
    if link[12]['name'] and link[12]['enabled']:
        url12 = link[12]['value']
        label = tk.Label(frame, text=link[12]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=12)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url12))

    # Link 14
    if link[13]['name'] and link[13]['enabled']:
        url13 = link[13]['value']
        label = tk.Label(frame, text=link[13]['name'],justify=tk.CENTER, cursor="hand2")
        label.grid(row=13)
        label.pack()
        label.bind("<Button-1>", lambda urls: callback(url13))

    return frame