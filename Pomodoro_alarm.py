import webbrowser
import time

print("...It's a running!")
while True:
	for _ in range(3):
		#work
		print("\n","Work!")
		time.sleep(1*60*25)
		webbrowser.open("https://youtu.be/2k0SmqbBIpQ?t=2")
		#break
		print("\n","5 minute break")
		time.sleep(1*60*5)
		webbrowser.open("https://youtu.be/ZXsQAXx_ao0?t=3")
		#after 4 breaks
	time.sleep(1*60*25)
	#big break
	print("\n","Big Break Now")
	webbrowser.open("https://www.youtube.com/watch?v=Hn2TKlbN8-4")
	time.sleep(1*60*90)
	print("\n","Work!")
	#back to work
	webbrowser.open("https://youtu.be/ZXsQAXx_ao0?t=3")

	
	