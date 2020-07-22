from pylibpd import *
from threading import Thread
import pyaudio
import time


class AudioEngine(Thread):

	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
		self.running = True

	def run(self):
		p = pyaudio.PyAudio()
		ch = 1
		sr = 44100
		tpb = 6
		bs = libpd_blocksize()

		stream = p.open(format=pyaudio.paInt16,
						channels=ch,
						rate=sr,
						input=True,
						output=True,
						frames_per_buffer=bs * tpb)

		m = PdManager(ch, ch, sr, 1)
		libpd_open_patch('two_ops1poly.pd', '.')  # './audioEngine'  '.'
		data = stream.read(bs)

		while self.running:
			outp = m.process(data)
			stream.write(outp.tobytes())

		stream.close()
		p.terminate()
		libpd_release()

	def stop_running(self):
		self.running = False

	def note_on(self, note):
		libpd_noteon(1, note, 64)

	def note_off(self, note):
		libpd_noteon(1, note, 0)


	def send_float(self, float_to_send):
		libpd_float('spam', 42)

	def send_symbol(self, symbol_to_send):
		libpd_symbol('spam', "don't panic")


#For testing purposes:

# a = AudioEngine()
# a.start()
# while(1):
#
# 	print("s")
# 	# a.note_on()
# 	libpd_noteon(0, 60, 64)
# 	time.sleep(1)
# 	# a.note_off()
# 	libpd_noteon(0, 60, 0)
# 	time.sleep(1)
#
# libpd_noteon(0, 60, 0)
