import pyttsx3
import moviepy
import gtts
from moviepy.video.tools.drawing import color_gradient
from moviepy.video.VideoClip import TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import textwrap

engine = pyttsx3.init()

# Step 1:  Generate speech from text

class Generator:

    def __init__(self, text):
        self.text_chunks = self.split_text(text)
        self.audio_file_prefix = 'speech'
        self.image_file_prefix = 'image'
        self.video_file_name = 'video.mp4'
        self.generate_speech_files()
        self.generate_text_images()
        self.clip = self.generate_clip(text)
        # self.generate_video(self.clip, self.audio_file_name, self.video_file_name)

    def generate_video(self, clip, audio_file_name, video_file_name):
        self.audio = AudioFileClip('speech.mp3').set_duration(clip.duration)
        final_clip = CompositeVideoClip([self.audio.set_duration(clip.duration), clip])
        final_clip.write_videofile(video_file_name, codec='libx264')

    def generate_speech_files(self):
        # Set the voice and language of the text-to-speech engine
        engine.setProperty('voice', 'english')
        engine.setProperty('language', 'en')

        # Generate an audio file for every chunk, named by index
        for x in range(len(self.text_chunks)):
            chunk = self.text_chunks[x]
            file_name = self.audio_file_prefix + "-" + str(x) + ".mp3"
            engine.save_to_file(chunk, file_name)
            engine.runAndWait()
    
    def generate_text_images(self):
        for x in range(len(self.text_chunks)):
            chunk = self.text_chunks[x]
            file_name = self.image_file_prefix + "-" + str(x) + ".png"
            # Set the dimensions of the image
            width, height = 562, 1080

            # Open an image
            image = Image.new('RGB', (width, height), 'white')

            # Create a draw object
            draw = ImageDraw.Draw(image)

            # Select a font
            font = ImageFont.truetype('arial.ttf', 40)

            # Set the text and the wrap width

            # Calculate the maximum number of characters that can fit within the width of the image
            char_width, _ = draw.textsize('O', font=font)
            wrap_width = width // char_width

            # Calculate the maximum number of lines of text that can fit within the height of the image
            _, line_height = draw.textsize('X', font=font)
            max_lines = height // line_height

            # Wrap the text to fit within the width and height of the image
            lines = textwrap.wrap(chunk, width=wrap_width, max_lines=max_lines)

            # Calculate the position to draw the text
            x = 10
            y = 10

            # Draw the text
            for line in lines:
                draw.text((x, y), line, font=font, fill='black')
                y += line_height

            # Save the image
            image.save(file_name)


    def split_text(self, text):
        # Arbitrary max chars for each chunk
        MAX_CHARS = 300
        sentences = text.split(".")
        chunks = []
        curr_chunk = ""
        for sentence in sentences:
            if len(curr_chunk) + len(sentence) < MAX_CHARS:
                curr_chunk += sentence.strip()
                curr_chunk += "." if sentence != "" else ""
            else:
                chunks.append(curr_chunk) if curr_chunk != "" else None
                curr_chunk = sentence.strip() + "."
        chunks.append(curr_chunk)
        return chunks

    def generate_clip(self, text):
        # Generate an image of the text
        clip = TextClip(text, font='Arial', color='white', fontsize=24).set_duration(self.audio.duration).set_audio(self.audio_file_name)
        clip.write_videofile("movie.mp4", codec='libx264')
        return clip
        

res = Generator("Google's YouTube has agreed to a deal with the NFL that will make it the new home for the NFL's Sunday Ticket package beginning next season, the two announced Thursday morning. Sunday Ticket will be available as an add-on for YouTube TV as well as a standalone purchase on YouTube Primetime Channels. Additionally, as part of the agreement, YouTube and the NFL will facilitate exclusive access to official content and attendance opportunities for select YouTube Creators at key NFL tentpole events. Amazon bought the rights to NFL's Thursday Night Football franchise for $1 billion a year through 2023.")
