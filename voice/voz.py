import sounddevice
from scipy.io.wavfile import write

fs=44100

def gravar():

    second=int(input("Quantos segundos deseja gravar?"))
    print("\nGravando......\n")
    #captura da gravação
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    write("gravacao.wav", fs, record_voice)
    print("Gravação finalizada!")


def ouvir():




def __main__(argv):
    print("menu\n")
    op = input("escolha: (1)gravar (2)ouvir")

    if op == 1:
        gravar()
    elif op == 2:
        ouvir()
