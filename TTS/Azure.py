import random
import azure.cognitiveservices.speech as speechsdk


voices = ['Jacob',
        'Eric',
        'Cora',
        'Amber']

random_voice = voices[random.randrange(0, len(voices))]

self = 'deez'

class Azure:
    def __init__(self):
        self.max_chars = 5000
        self.voices = voices
    
    def run(self, text, filepath):
        speech_config = speechsdk.SpeechConfig(subscription="910c167d2ca447ae943ab4a29dc65538", region="eastus")
        audio_config = speechsdk.audio.AudioOutputConfig(filename=filepath)
        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name=f'en-US-{random_voice}Neural'
        # jacob eric cora or amber
        #some bs for headers
        speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz96KBitRateMonoMp3)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        text = text
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")