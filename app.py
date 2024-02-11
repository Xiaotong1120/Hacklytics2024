import io
import os
import re
import openai
import pandas as pd
import gradio as gr
import matplotlib.pyplot as plt
from Hacklytics2024.Handwriting_recognition import *
from Hacklytics2024.Output_Generation import *

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

def main():
    with gr.Blocks() as app:
        with gr.Tab("Home"):
            gr.Markdown(home())

        with gr.Tab("AI-Assisted Learning"):
            with gr.Column():
                file_input = gr.File(label="Upload an image of problem!")
                submit_button = gr.Button("Submit")
                text_output = gr.Textbox(label="AI Output")

            with gr.Row():
                check_button = gr.Button("I understand!")
                confused_button = gr.Button("I'm a bit confused...")

            convert_img_to_text, output_generation, continue_exploring, memory_initial = m4th_assistant()
            
            # convert img to text
            file_input.change(convert_img_to_text, inputs = file_input)

            # calling Chatgpt API
            submit_button.click(output_generation, outputs = text_output) 

            # continuing asking, calling Chatgpt, concatenating history data
            confused_button.click(continue_exploring, outputs = text_output)

            # nothing more to learn, clear all
            check_button.click(memory_initial, outputs = text_output)

    app.launch()

if __name__ == "__main__":
    main()