from main import speak
from main import takeCommand
import data

def match(to):
    for i in range(0, len(data.contacts)-1):
        if data.contacts[i][0] == to:
            index = i
            break
        else:
            index = -1
    if index == -1:
        if to == 'shubhodeep' or to == 'shubhodep' or to == 'shubhodip' or to == 'subhodip' or to == 'subhodeep' or to == 'subhodep':
            speak("Do you mean Shubhodip?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 0
            else:
                index = -1
        elif to == 'sahini':
            speak("Do you mean Sohini?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 1
            else:
                index = -1
        elif to == 'anuska' or to == 'onuska' or to == 'onushka':
            speak("Do you mean Anushka?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 2
            else:
                index = -1
        elif to == 'shuti':
            speak("Do you mean Shruti?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 3
            else:
                index = -1
        elif to == 'tania':
            speak("Do you mean Tanya?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 4
            else:
                index = -1
        elif to == 'depu' or to == 'deepu':
            speak("Do you mean Dipu?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 5
            else:
                index = -1
        elif to == 'debjeet' or to == 'debjet':
            speak("Do you mean Debjit?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 6
            else:
                index = -1
        elif to == 'orpan' or to == 'earphone':
            speak("Do you mean Arpan?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 7
            else:
                index = -1
        elif to == 'anesha' or to == 'amhesa' or to == 'anhesha':
            speak("Do you mean Anwesha?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 8
            else:
                index = -1
        elif to == 'rupam':
            speak("Do you mean Rupom?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 9
            else:
                index = -1
        elif  to == 'sumit' or to == 'summit':
            speak("Do you mean Neha?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 10
            else:
                index = -1
        elif to == 'shudeshna' :
            speak("Do you mean Sudeshna?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 11
            else:
                index = -1
        elif to == 'add on' or to == 'aron':
            speak("Do you mean Aaron?")
            speak("Say confirm to continue")
            state = takeCommand().lower()
            if state == 'confirm':
                index = 12
            else:
                index = -1
        else:
            speak("Sorry sir, I don't know whom you are talking about")
            index = -1
    return index