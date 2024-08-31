# Given a list of Japanese phrases, speak them.
import csv
import os
from voicevox.client import Client
from playsound3 import playsound
from time import sleep
from random import shuffle
import asyncio

async def speak(word: str):
    async with Client() as client:
        audio_query = await client.create_audio_query(
            word, speaker=0
        )
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=0))
        playsound("voice.wav")

async def dictation(words: list[str]):
    await speak("口述筆記を始めります。")
    sleep(1)
    for i, word in enumerate(words):
        for j in range(2):
            await speak(word)
            sleep(2)
        if i < len(words) - 1:
            sleep(4)
            await speak("次は")
    await speak("口述筆記を終わりました。")
    print(
        "答えは：\n" + "\n".join(
            [f"{i}. {word}" for i, word in enumerate(words, start = 1)]
            )
        )

async def main():
    file_path = os.path.join("vocab", "genki", "n5", "l0.csv")
    with open(file_path) as f:
        reader = csv.reader(f)
        words = [row[0] for i, row in enumerate(reader) if i > 0]
    shuffle(words)
    await dictation(words)
                
if __name__ == "__main__":
    asyncio.run(main())