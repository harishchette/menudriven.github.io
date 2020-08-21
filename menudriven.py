import pyttsx3
import os


print("enter the number , that  you wanna choose")

print("1.chrome .   2.notepad     3.paint     4.vlc    5.python    6.commandprmpt     7.action    8.explore     9.calculator    10.calender    11.camera    12.candycrush    13.projections   14.calculator   15.drawboardpdf   16.facebook 17.feedback   18.help    19.groovemusic    20.gmail    21.maps   22.messenger   23.microsoftedge 24.microsoftnews 25.minecraft 26.realitycamera     27.realityportal     28.onenote   29.photos  30.movies   31.setting    32.weather    33.screensnip    34.twitter    35.recorder    36.tips   37.smartglass    38.widowsettings ")


while True :


	e=int(input("enters your choice : "))
	if e==1 :
		pyttsx3.speak("wait...your chrome is opening")
		os.system("start chrome")
	elif e==2 :
		pyttsx3.speak("wait...your notepad is opening")
		os.system("start notepad")
	elif e==3 :
		pyttsx3.speak("wait...your paint is opening")
		os.system("start paint:")
	elif e==4 :
		pyttsx3.speak("wait...your vlc is opening")
		os.system("start vlc")
	elif e==5 :
		pyttsx3.speak("wait...your python is opening")
		os.system("start python")
	elif e==6 :
		pyttsx3.speak("wait...your commandprompt is opening")
		os.system("start cmd")
	elif e==7 :
		pyttsx3.speak("wait...your actioncenter is opening")
		os.system("start ms-actioncenter:")
	elif e==8 :
		pyttsx3.speak("wait...your explorer are opening")
		os.system("start File-Explorer:")
	elif e==9:
		pyttsx3.speak("wait...your calculator is opening")
		os.system("start calculator:")
	elif e==10 :
		pyttsx3.speak("wait...your calender is opening")
		os.system("start outlookcal:")
	elif e==11 :
		pyttsx3.speak("wait...your camera is opening")
		os.system("start microsoft.windows.camera:")
	elif e==12 :
		pyttsx3.speak("wait...your candycrushsaga is opening")
		os.system("start candycrushsodasaga:")
	elif e==13 :
		pyttsx3.speak("wait...your projections is opening")
		os.system("start ms-projections:")
	elif e==14 :
		pyttsx3.speak("wait...your device discovery is opening")
		os.system("start ms-settings-connectabledevices:devicediscovery")
	elif e==15 :
		pyttsx3.speak("wait...your pdfs is opening")
		os.system("start drawboardpdf:")
	elif e==16 :
		pyttsx3.speak("wait...your facebook is opening")
		os.system("start fb:")
	elif e==17 :
		pyttsx3.speak("wait...your feedback hub is opening")
		os.system("start feedback-hub:")
	elif e==18 :
		pyttsx3.speak("wait...your help is opening")
		os.system("start ms-contact-support:")
	elif e==19 :
		pyttsx3.speak("wait...your projectdisplay is opening")
		os.system("start ms-settings-displays-topology:projection:")
	elif e==20 :
		pyttsx3.speak("wait...your Gmail is opening")
		os.system("start outlookmail:")
	elif e==21 :
		pyttsx3.speak("wait...your maps is opening")
		os.system("start bingmaps:")
	elif e==22 :
		pyttsx3.speak("wait...your messenger is opening")
		os.system("start ms-chat:")
	elif e==23 :
		pyttsx3.speak("wait...your microdoftedge is opening")
		os.system("start microsoft-edge:")
	elif e==24  :
		pyttsx3.speak("wait...your news is opening")
		os.system("start microsoft-news:")	
	elif e==25  :
		pyttsx3.speak("wait...your windows10edition  is opening")
		os.system("start minecraft:")
	elif e==26  :
		pyttsx3.speak("wait...your realitycamera  is opening")
		os.system("start ms-holocamera:")
	elif e==27  :
		pyttsx3.speak("wait...your realityportal  is opening")
		os.system("start ms-holographicfirstrun:")
	elif e==28 :
		pyttsx3.speak("wait...your onenote  is opening")
		os.system("start onnenote:")
	elif e==29  :
		pyttsx3.speak("wait...your photos  is opening")
		os.system("start ms-photos:")
	elif e==30  :
		pyttsx3.speak("wait...your movies is opening")
		os.system("start msmoviesvideo:")
	elif e==31  :
		pyttsx3.speak("wait...your settings  is opening")
		os.system("start ms-settings:")
	elif e==32  :
		pyttsx3.speak("wait...your weatherreport  is opening")
		os.system("start bingweather:")
	elif e==33  :
		pyttsx3.speak("wait...your screensnip  is opening")
		os.system("start ms-screenclip:")
	elif e==34 :
		pyttsx3.speak("wait...your twitter  is opening")
		os.system("start twitter:")
	elif e==35 :
		pyttsx3.speak("wait...your recorder  is opening")
		os.system("start ms-callrecording:")
	elif e==36 :
		pyttsx3.speak("wait...your tips  is opening")
		os.system("start ms-get-started:")
	elif e==37  :
		pyttsx3.speak("wait...your smartglass  is opening")
		os.system("start smartglass:")
	elif e==38  :
		pyttsx3.speak("wait...your windowsettings  is opening")
		os.system("start windowsdefender:")
	elif e==0 :
		break