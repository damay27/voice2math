import pip

print("**************************************************")
print("Installing voice2speech dependencies")
print("**************************************************")

pip.main(["install", "SpeechRecognition"])
pip.main(["install", "PyAudio"])

print("**************************************************")
print("Dependencies Installed. Enjoy!!!")
print("**************************************************")
