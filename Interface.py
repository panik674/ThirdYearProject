import threading
import tkinter
from tkinter import *

class interface:

    def __init__(self,options):
        self.root = Tk()

        self.options = options

        self.option = StringVar()
        self.option.set("Scanner")

        self.scanners = OptionMenu(self.root, self.option, *self.options).pack(anchor=W)

        Label(self.root, text="Block web page if:").pack()

        self.malwareState = IntVar()
        self.malwareState.set(1)
        self.malware = Checkbutton(self.root, text="Contains Malware",variable=self.malwareState).pack(anchor=W)

        self.unsafeState = IntVar()
        self.unsafeState.set(1)
        self.unsafe = Checkbutton(self.root, text="Is Unsafe",variable=self.unsafeState).pack(anchor=W)

        self.spamState = IntVar()
        self.spamState.set(1)
        self.spam = Checkbutton(self.root, text="Sends Spam",variable=self.spamState).pack(anchor=W)

        self.phishingState = IntVar()
        self.phishingState.set(1)
        self.phishing = Checkbutton(self.root, text="Is a Phishing Link",variable=self.phishingState).pack(anchor=W)

        self.suspiciousState = IntVar()
        self.suspiciousState.set(1)
        self.suspicious = Checkbutton(self.root, text="Is suspicious",variable=self.suspiciousState).pack(anchor=W)

        self.adultState = IntVar()
        self.adultState.set(1)
        self.adult = Checkbutton(self.root, text="Contains Adult content",variable=self.adultState).pack(anchor=W)

        Label(self.root, text="Risk Score Threshold:").pack()

        self.riskScoreState = IntVar()
        self.riskScoreState.set(100)
        self.riskScore = Scale(self.root, from_=0, to=100, orient=HORIZONTAL,variable=self.riskScoreState).pack()

