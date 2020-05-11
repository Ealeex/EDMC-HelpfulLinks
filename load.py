try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import ttk
import sys
import myNotebook as nb
from config import config
import json
from ttkHyperlinkLabel import HyperlinkLabel
import webbrowser

this = sys.modules[__name__]

# Global Variables
totalLinks = 14

# Link Class
class LinkOption:
    def __init__(self, enabled, enabledElement, nameElement, valueElement):
        self.enabled = enabled
        self.enabledElement = enabledElement
        self.nameElement = nameElement
        self.valueElement = valueElement

# Generates a new list of preferences
def initializeSettings():
    settings = list()
    for i in range(totalLinks):
        setting = dict()
        setting['enabled'] = 0
        setting['name'] = ''
        setting['value'] = ''
        settings.append(setting)
    return settings

# Called when the settings menu is opened
def plugin_prefs(parent, cmdr, is_beta):
    this.LinkOptions = list()
    frame = nb.Frame(parent)
    nb.Label(frame, text='#').grid(row=0,column=0,padx=4,pady=4,sticky=tk.W)
    nb.Label(frame, text='Enabled').grid(row=0,column=1,padx=4,pady=4,sticky=tk.W)
    nb.Label(frame, text='Name').grid(row=0,column=2,padx=4,pady=4,sticky=tk.W)
    nb.Label(frame, text='Link').grid(row=0,column=3,padx=4,pady=4,sticky=tk.W)
    for i in range(totalLinks):

        link_Enabled = tk.IntVar(value='0')
        if this.linkPreferences[i]['enabled']: link_Enabled = tk.IntVar(value='1')
        name = this.linkPreferences[i]['name']
        value = this.linkPreferences[i]['value']

        nb.Label(frame, text=i+1).grid(row=i+1,column=0,padx=4,pady=4,sticky=tk.W)
        link_E = nb.Checkbutton(frame, variable=link_Enabled)
        link_E.grid(row=i+1,column=1,padx=4,pady=4,sticky=tk.W)
        link_N = nb.Entry(frame)
        link_N.grid(row=i+1,column=2,padx=4,pady=4,sticky=tk.W)
        link_N.config(width=25)
        link_N.insert(0,name)
        link_V = nb.Entry(frame)
        link_V.grid(row=i+1,column=3,padx=4,pady=4,sticky=tk.W)
        link_V.config(width=25)
        link_V.insert(0,value)
        this.LinkOptions.append(LinkOption(link_Enabled, link_E, link_N, link_V))  

    return frame

# Called when the settings menu is closed
def prefs_changed(cmdr, is_beta):
    this.linkPreferences = list()
    for linkOpt in this.LinkOptions:
        d = dict()
        d['enabled'] = linkOpt.enabled.get()
        d['name'] = linkOpt.nameElement.get()
        d['value'] = linkOpt.valueElement.get()
        this.linkPreferences.append(d)
    config.set('prefs',json.dumps(this.linkPreferences))
    updateMainWindow()
    return

# Updates the main window when called
def updateMainWindow():

    # Clear all current labels
    for label in this.linkLabels:
        label.destroy()

    # Generate a list of active links
    activeLinks = list()
    for link in this.linkPreferences:
        if link and link['enabled'] and link['name'] and link['value']:
            activeLinks.append(link)

    # Generate new labels based on activeLinks
    this.linkLabels = list()
    for link in activeLinks:
        if link and link['enabled']:
            this.linkLabels.append(tk.Label(this.frame))

    # Fill the new labels
    row = 0
    for label in this.linkLabels:
        label['text'] = activeLinks[row]['name']
        label['justify'] = tk.CENTER
        label['cursor'] = 'hand2'
        label['fg'] = 'blue'
        label.bind('<Button-1>',lambda x, url=activeLinks[row]['value']: webbrowser.open_new(url))
        label.pack()
        row += 1

    return

# Called when the plugin is started by EDMC
def plugin_start(plugin_dir):
    this.linkPreferences = json.loads(config.get('prefs') or json.dumps(initializeSettings()))
    this.linkLabels = list()
    return "HelpfulLinks"

# Called when the program is stopped
def plugin_stop():
    return

# Display the main window on the app
def plugin_app(parent):
    this.frame = tk.Frame(parent)
    this.frame.columnconfigure(1, weight=1)
    updateMainWindow()
    return this.frame

