# Whisper_to_fabric
This repository is a basic integration of fabric and OpenAI-Whisper. Fabric is a tool which utilizes the power of LLMs and make our daily life easier.

For more information check fabric:

https://github.com/danielmiessler/fabric


### Requirements

Packages down below are needed.

```
pip install setuptools-rust
sudo apt update && sudo apt install ffmpeg
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```

For torch installation I recommend to visit the pytorch's official website.

https://pytorch.org

### Whisper Usage
Usage:

```
python whisper_transcribe <YOUTUBE LINK>
```

I also recommend an alias to use it faster like below.

```
alias transcribe="python ~/whisper_transcribe.py"
```

Example Usage after adding the alias to ~/.bashrc:
```
transcribe <YOUTUBE LINK>
```

### Integration with fabric

Usage:

```
transcribe <YOUTUBE LINK> | fabric -sp extract_wisdom
```

```
transcribe <YOUTUBE LINK> | fabric -sp summarize
```

```
transcribe <YOUTUBE LINK> | fabric -sp analyze_claims
```

Checkout fabric's patterns folder for more:

https://github.com/danielmiessler/fabric/tree/main/patterns

### Alternative

Checkout yt for alternative:

https://github.com/danielmiessler/fabric/tree/main?tab=readme-ov-file#helper-apps
https://github.com/danielmiessler/fabric/tree/main?tab=readme-ov-file#yt-installation


















