# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/output_generation.ipynb.

# %% auto 0
__all__ = ['data_concat', 'generate_output', 'continue_prompt', 'm4th_assistant']

# %% ../nbs/output_generation.ipynb 4
import os
import nbdev
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import openai
from openai import OpenAI
from google.cloud import vision
import io


# %% ../nbs/output_generation.ipynb 5
def data_concat(scan_text):
    # This function aims to concat prompt and user's problem
    # input: (user's problem, string type)
    # process: string concat
    # output: question to send to the Chatgpt
    prompt =  """
    Assist with Mathematical Problems: Your primary goal is to help users solve math problems. You use a structured approach that emphasizes clarity and step-by-step explanations. 
    Use language for Explanations: All explanations are provided in plain language to ensure they are understandable and accessible. 
    Avoidance of Programming for Calculations: Unlike some other models that may use programming languages like Python for calculations, You are instructed to rely solely on mathematical principles and reasoning for solving problems.
    Integrate Theories or Specific Methods: If a user provides a specific theory or method they want to use, you'll incorporate it into the problem-solving process.
    Organize Responses for Easy Understanding: Your responses are organized meticulously to facilitate ease of understanding and learning.
    Here is how your answers are organized:
    1 - Start by clearly defining the problem or concept on your own, and completely understand it (without telling the user).
    2 - If the solution is correct, just say “Correct” and end the conversation. If not, continue:
    2.1 - Identify Key Concepts: Highlight the core mathematical principles or formulas that are relevant to solving the problem or understanding the concept.
    2.2 - Identify the weakness of the solution: Identify which part of the solution is incorrect and tell me, without giving the solution. Ask me if I want to continue afterwards, stop if not.
    3 - Step-by-Step Solution: If I say yes, provide a straightforward, step-by-step approach to solve the problem, including only essential steps and reasoning.
    4 - Quick guidance: Present further links for me to learn about the relevant topic. Keep it short, ensuring it directly addresses the question.
    Handling Non-Math Queries: When presented with a question outside your expertise, you won't answer directly but will offer a funny (yet not cheesy) reply that aims to satisfy the user's curiosity in a light-hearted way.
    Handling Problems with No Solution: In cases where there's no solution to a problem, you'll walk the user through the problem, offering hints on potential starting points. You'll make it clear that while a solution isn't available, there's value in exploring the problem from these angles.
    Your guidance remains concise and to the point.
    """
    scan_text_prompt = prompt + scan_text
    return scan_text_prompt

# %% ../nbs/output_generation.ipynb 6
def generate_output(scan_text_prompt, Chatgpt_key, model='gpt-4'):
    # This function aims to calling Chatgpt API key and get mathematical answers
    # input: (concated prompt, string type)
    # process: string concat
    # output: question to send to the Chatgpt

    # Instantiate the OpenAI client with the API key.
    client = openai.OpenAI(api_key = Chatgpt_key)
    
    try:
        # Make the API call to OpenAI for generating predictions.
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": scan_text_prompt
                }
            ]
        )

        full_response = response.choices[0].message.content

    except Exception as e:
        # Handle any errors that occur during the API call.
        print(f"An error occurred while calling OpenAI API: {e}")

    return full_response

# %% ../nbs/output_generation.ipynb 7
def continue_prompt(latex_output,global_output):
    continue_prompt_text = "This is my prior input:" + latex_output 
    continue_prompt_text = continue_prompt_text+ "This is your prior output:" 
    continue_prompt_text = continue_prompt_text + global_output 
    continue_prompt_text = continue_prompt_text + "I don't quite understand it. Could you explain more?"
    return continue_prompt_text

# %% ../nbs/output_generation.ipynb 8
def m4th_assistant():
    
    Chatgpt_key = ""
    
    latex_output = None
    global_output = None
    global_scan_text_prompt = None


    # Define the function for converting image to text using Google Cloud Vision
    def convert_img_to_text(file_input):
        nonlocal latex_output
        client = vision.ImageAnnotatorClient()

        with io.open(file_input.name, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.document_text_detection(image=image)
        document = response.full_text_annotation
        latex_output = document.text
        return latex_output
            
    # concat prompt & user's question
    # show the output on the board
    def output_generation():
        nonlocal latex_output, global_output, global_scan_text_prompt

        global_scan_text_prompt = data_concat(latex_output)
        global_output = generate_output(global_scan_text_prompt, Chatgpt_key)

        return global_output
    
    # concat history data & prompt
    # show the data on the board
    def continue_exploring():
        nonlocal latex_output, global_output, global_scan_text_prompt

        continue_prompt_text = continue_prompt(latex_output,global_output)
        cotinue_output = generate_output(continue_prompt_text,Chatgpt_key)

        latex_output = continue_prompt_text
        continue_prompt_text = cotinue_output

        return cotinue_output
    
    # clear all
    def memory_initial():
        nonlocal latex_output, global_output, global_scan_text_prompt

        latex_output = None
        global_output = None
        global_scan_text_prompt = None

        return ""
    
    return convert_img_to_text,output_generation,continue_exploring,memory_initial
