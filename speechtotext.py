import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "2a04a1e2bb0f47f0b9c90c5d56b5ebe2", "centralindia"
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)

audio_filename = "e:/Python/SpeechToTextPython/Recordin.wav"
audio_input = speechsdk.AudioConfig(filename=audio_filename)

speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_input)

print("Recognizing first result...")

result = speech_recognizer.recognize_once()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
