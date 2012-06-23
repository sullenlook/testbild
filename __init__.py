#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: SullenLook sullen look@sullenlook.eu
#project: SiriServer plugin
#Testbild plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class testbild(Plugin):

        res = {
                'testbild': {
                        'de-DE': '.*Testbild.*',
                }
        }

        @register("de-DE", res['testbild']['de-DE'])
        def testbild(self, speech, language):
                html = urllib.urlopen("http://sullenlook.eu/Pix/cydia/info/testbild.png")
                soup = BeautifulSoup(html)
                ImageURL = "./plugins/testbild/testbild.png"
                view = AddViews(self.refId, dialogPhase="Completion")
                ImageAnswer = AnswerObject(title="testbild:",lines=[AnswerObjectLine(image=ImageURL)])
                view1 = AnswerSnippet(answers=[ImageAnswer])
                view.views = [view1]
                self.sendRequestWithoutAnswer(view)
                self.complete_request()


