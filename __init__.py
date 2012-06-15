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

from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class testbild(Plugin):

        @register("de-DE",".*Testbild.*")
        def testbild(self, speech, language):
                ImageURL = "./plugins/testbild/testbild.jpg"
                view = AddViews(self.refId, dialogPhase="Completion")
                ImageAnswer = AnswerObject(title="SullenLook",lines=[AnswerObjectLine(image=ImageURL)])
                view1 = AnswerSnippet(answers=[ImageAnswer])
                self.sendRequestWithoutAnswer(view)
                self.complete_request()

