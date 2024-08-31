server:
	docker run --rm --gpus all -p '0.0.0.0:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest

client:
	Scripts/python src/main.py