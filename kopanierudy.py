import time
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller


ilosc_razy = int(input('Wprowadz ile razy program ma wykopac rude: '))
#ilosc_razy = 120

time.sleep(3) #To Ci pozwala na to abys przelaczyl na okno z metinem
keyboard = Controller()

def gornik(iteracje):
    i = 0
    for i in range(iteracje):
        print(f'{i}')
        keyboard.press(Key.space)
        time.sleep(0.5)
        keyboard.release(Key.space)
        time.sleep(9.1)
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z') #Nie wiem czy to jest potrzebne
        i += 1

start = time.time()

gornik(ilosc_razy) #Tutaj wpisujesz ile razy ma kopac

end = time.time()

print("The time of execution of above program is :",
      (end-start), "s")


