import time
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller


ilosc_razy = int(input('Wprowadz ile razy program ma zarzucic wedke: '))
#ilosc_razy = 120

time.sleep(3) #To Ci pozwala na to abys przelaczyl na okno z metinem
keyboard = Controller()

def gornik(iteracje):
    i = 0
    for i in range(iteracje):
        print(f'{i}')
        #Tutaj program wybiera kukurydze ze slotu "1" z ekwipunku
        keyboard.press('1')
        time.sleep(0.5)
        keyboard.release('1')
        
        #Tutaj program zarzuca wędke
        keyboard.press(Key.space)
        time.sleep(0.5)
        keyboard.release(Key.space)
        #Tutaj program czeka aż pojawi się informacja, że ryba bierze.
        #Te wartość musisz zmienić w zależności od tego ile Ci łowi.
        #Najlepiej posprawdzać metodą prób i błedów
        time.sleep(8.5)
        
        #Teraz klikniemy spacje dwa razy
        keyboard.press(Key.space)
        time.sleep(0.8)
        keyboard.release(Key.space)
        time.sleep(0.5)
        keyboard.press(Key.space)
        time.sleep(0.8)
        keyboard.release(Key.space)
        
        time.sleep(4)
        
        i += 1

start = time.time()

gornik(ilosc_razy) #Tutaj wpisujesz ile razy ma kopac

end = time.time()

print("The time of execution of above program is :",
      (end-start), "s")


