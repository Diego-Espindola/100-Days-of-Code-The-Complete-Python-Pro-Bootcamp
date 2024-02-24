import pyautogui
import time
import keyboard

def obter_coordenadas():
    coordenadas = []
    print("Posicione o mouse nas três posições desejadas e pressione Enter após cada posição.")
    
    for _ in range(3):
        input("Pressione Enter para capturar a posição...")
        x, y = pyautogui.position()
        coordenadas.append((x, y))
        print(f"Posição capturada: ({x}, {y})")

    return coordenadas

def main():
    # Loop para clicar em cada coordenada
    coordenadas = obter_coordenadas()
    print("Thread em execução. Pressione Esc por dois segundos para interromper.")
    while not keyboard.is_pressed('esc'):
        for x, y in coordenadas:
            pyautogui.click(x, y)
            time.sleep(2)

if __name__ == "__main__":
    main()
