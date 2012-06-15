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

	@register("de-DE", "Testbild")
	def testbild(self, speech, language):
		ImageURL = http://sullenlook.eu/Pix/Avatar.gif
		ImageAnswer = AnswerObject(title="SullenLook",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", "Testbild 2")
	def testbild(self, speech, language):
		ImageURL = http://sullenlook.eu/Pix/cydia/1.png
		ImageAnswer = AnswerObject(title="SullenLook",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()