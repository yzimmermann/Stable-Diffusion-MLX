import gradio as gr
import subprocess
import argparse


def generate_images(prompt, model='sdxl', n_images=4, negative_prompt="", n_rows=1, output="out.png"):
    command = [
        "python", "txt2image.py", prompt,
        "--model", model,
        "--n_images", str(n_images),
        "--negative_prompt", negative_prompt,
        "--n_rows", str(n_rows),
        "--output", output,
    ]
    # command = [arg for arg in command if arg]
    subprocess.run(command)

    return output

iface = gr.Interface(
    fn=generate_images,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Radio(choices=["sd", "sdxl"], label="Model", value="sdxl"),
        gr.Number(label="Number of Images", value=4),
        gr.Textbox(label="Negative Prompt"),
        gr.Number(label="Number of Rows", value=1),
    ],
    outputs=[gr.Image(label="Generated Image")],
    title="Stable Diffusion on Apple Silicon",
    description="Generate images from a textual prompt using Stable Diffusion models in MLX on Apple silicon."
)

def main(share):
    iface.launch(share=share)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch the Stable Diffusion Gradio interface")
    parser.add_argument("--share", action="store_true", help="Set this flag to share the Gradio interface publicly")
    args = parser.parse_args()
    main(args.share)
