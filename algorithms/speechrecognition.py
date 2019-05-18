
#library for performing speech recognition, with support for several engines and APIs, online and offline.
#Speech recognition engine/API

#Quickstart: pip install SpeechRecognition. See the “Installing” section for more details.

#To quickly try it out, run python -m speech_recognition after installing.

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
  
#The expected Output
#Microphone with name "HDA Intel HDMI: 0 (hw:0,3)" found for `Microphone(device_index=0)`
#Microphone with name "HDA Intel HDMI: 1 (hw:0,7)" found for `Microphone(device_index=1)`
#Microphone with name "HDA Intel HDMI: 2 (hw:0,8)" found for `Microphone(device_index=2)`
#Microphone with name "Blue Snowball: USB Audio (hw:1,0)" found for `Microphone(device_index=3)`
#Microphone with name "hdmi" found for `Microphone(device_index=4)`
#Microphone with name "pulse" found for `Microphone(device_index=5)`
#Microphone with name "default" found for `Microphone(device_index=6)`    
