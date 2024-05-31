import threading, wave, pyaudio

class SoundHandler():
    def __init__(self) -> None:
        self.threads = []
        self.currentId = 0

    def __internalPlay(self, name, tInfo):
        wf = wave.open(name, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(1024)

        while True:
            # Should not continue the loop.
            if not tInfo[2]:
                self.threads.remove(tInfo[0])
                break

            stream.write(data)
            data = wf.readframes(1024)
            if data == b'':
                wf.rewind()  # Rewind the audio file to the beginning
                data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()

        p.terminate()

    def stop(self, threadId):
        for t in self.threads:
            if t[0] == threadId:
                t[2] = False
                return True

        return False

    def play(self, name):
        tInfo = [self.currentId, None, True]
        t = threading.Thread(target=self.__internalPlay, args=(name, tInfo))
        t.start()
        
        tInfo[1] = t
        self.threads.append(tInfo)
        self.currentId += 1