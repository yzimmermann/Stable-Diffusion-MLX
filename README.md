# Stable Diffusion on Apple Silicon

![A beautiful vase](out.png)

This repository contains scripts for generating images using Stable Diffusion locally through a simple web interface powered by Gradio. It is built on Apple's MLX framework for Apple silicon. 
This repo is based on the work found at https://github.com/ml-explore/mlx-examples/tree/main/stable_diffusion.

## Features

- Generate images using text prompts through a web interface.
- Supports different models including `stabilityai/sdxl-turbo` and `stabilityai/stable-diffusion-2-1`.


## Installation

Before you start, ensure you have Python 3.6 or later installed. It's recommended to use a virtual environment.

1. Clone this repository:
```bash
   git clone https://github.com/yzimmermann/Stable-Diffusion-MLX.git
   cd Stable-Diffusion-MLX
   ```
2. Install the required dependencies:
```bash
   pip install -r requirements.txt
   ```
## Usage
To run the script locally with the Gradio interface:
```bash
   python app.py
   ```
To share the Gradio interface publicly (a public link will be generated, only share with people you trust!):
```bash
  python app.py --share
  ```






