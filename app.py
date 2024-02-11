import io
import os
import re
import gradio as gr
import matplotlib.pyplot as plt

# Define functions for each page
def home():
    content =  """
    # Welcome to Math Learning Tool!

    **Math Learning Tool** is an AI-based platform designed to assist students in their mathematical academia. This tool reads in handwriting to convert to Latex and changes in real-time and provides valuable feedback.

    ## Features:
    - **Human Handwriting Interpretation**: Uses algorithms to compare against real numbers and symbols and outputs them in Latex.
    - **ChatGPT Implementation**: Uses AI to determine if the answer is correct or at least on the right track, if not then provides recommendations to the user on how to improve upon their weaknesses.
    - **Creative Prompt Generation**: Model continuously feeds the wrapper information on how to learn better to come up with a better solution.

    ## Developed by:
    - Ethan Yee
    - Rustam Jumazhanov
    - Sefika Ozturk
    - Xiaotong Ma

    """
    return content

text_box = gr.Textbox(label="Learning Assistant Response", lines=10)

def main():
    with gr.Blocks() as app:
        with gr.Tab("Home"):
            gr.Markdown(home())

        with gr.Tab("AI-Assisted Learning"):
            with gr.Column():
                file_input = gr.File(label="Upload a problem!")
                upload_button = gr.Button("Upload")
                text_output = gr.Textbox(label="AI Output", lines=10)

            # with gr.Column():
            #     upload_button.click(inputs=file_input, outputs=[text_output])

            with gr.Row():
                inputs = text_output,
                outputs = "text",
                title = "Learning Assistant Response"

            with gr.Row():
                check_button = gr.Button("I understand!")
                confused_button = gr.Button("I'm a bit confused...")

    app.launch()

if __name__ == "__main__":
    main()