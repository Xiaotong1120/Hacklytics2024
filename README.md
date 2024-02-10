# repo-template-python
This is a template repository for data science projects done in Python.

### Using this template
To use the following template, click the "Use This Template button" and follow the instructions to create a new repository.  Fill out the information below, deleting parts that are not specific to your project (e.g., Prerequisites).  This template contains a number of code templates in the modeling sections (40-90 series), which may be deleted and renumbered according to the project objectives.  The format of this repository goes well with nbdev.  Take a look at the documentation there and review the tutorials to get the best usage out of this repository.  See the `box-authentication` notebook if you need to do authentication via Box (for projects with security contracts or PII data).  Note that this authentication method is not currently guaranteed to work on ACCRE.

### Prerequisites
To most easily run this code out of the box, the following packages must be installed:
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* great expectations
* h2o
* fastai
* huggingface
* datasets

This is easiest to achieve through first installing an Anaconda distribution, which installs the first 5 packages and all of their dependencies.  The install directions to the other packages may be found on their documentation pages.

# Quick navigation
[Background](#background)  
[Data](#data)  
[Models](#models)  
[Timeline](#timeline)  
[Repo Structure](#repo-structure)  
[Logistics](#project-logistics)  
[Resources](#resources)  
[Contact](#contact-info)

# Goal

Provide an overview of the goals and deliverables of the project. Mention any relevant details or issues. 

# Background  

Provide a broad overview of the purpose of the project.

# Data

Describe the data - what kind of data is it?  Describe the general format, and potential quirks.

## Data security

If there are any security concerns or requirements regarding the data, they should be described here.

## Counts

Describe the overall size of the dataset and the relative ratio of positive/negative examples for each of the response variables.

# Models

Clearly identify each of the response variables of interest.  Any additional desired analysis should also be described here.

# Timeline

Outline the desired timeline of the project and any explicit deadlines.

# Repo Structure 

Give a description of how the repository is structured. Example structure description below:

The repo is structured as follows: Notebooks are grouped according to their series (e.g., 10, 20, 30, etc) which reflects the general task to be performed in those notebooks.  Start with the *0 notebook in the series and add other investigations relevant to the task in the series (e.g., `11-cleaned-scraped.ipynb`).  If your notebook is extremely long, make sure you've utilized nbdev reuse capabilities and consider whether you can divide the notebook into two notebooks.

All files which appear in the repo should be able to run, and not contain error or blank cell lines, even if they are relatively midway in development of the proposed task. All notebooks relating to the analysis should have a numerical prefix (e.g., 31-) followed by the exploration (e.g. 31-text-labeling). Any utility notebooks should not be numbered, but be named according to their purpose. All notebooks should have lowercase and hyphenated titles (e.g., 10-process-data not 10-Process-Data). All notebooks should adhere to literate programming practices (i.e., markdown writing to describe problems, assumptions, conclusions) and provide adequate although not superfluous code comments.

# Project logistics

**Sprint planning**:  
**Demo**:  

**Data location**:  

**Slack channel**:  
**Zoom link**:  

# Resources 
* **Python usage**: Whirlwind Tour of Python, Jake VanderPlas ([Book](https://learning.oreilly.com/library/view/a-whirlwind-tour/9781492037859/), [Notebooks](https://github.com/jakevdp/WhirlwindTourOfPython))
* **Data science packages in Python**: [Python Data Science Handbook, Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/) 
* **HuggingFace**: [Website](https://huggingface.co/transformers/index.html), [Course/Training](https://huggingface.co/course/chapter1), [Inference using pipelines](https://huggingface.co/transformers/task_summary.html), [Fine tuning models](https://huggingface.co/transformers/training.html)
* **fast.ai**: [Course](https://course.fast.ai/), [Quick start](https://docs.fast.ai/quick_start.html)
* **h2o**: [Resources, documentation, and API links](https://docs.h2o.ai/#h2o)
* **nbdev**: [Overview](https://nbdev.fast.ai/), [Tutorial](https://nbdev.fast.ai/tutorial.html)
* **Git tutorials**: [Simple Guide](https://rogerdudler.github.io/git-guide/), [Learn Git Branching](https://learngitbranching.js.org/?locale=en_US)
* **ACCRE how-to guides**: [DSI How-tos](https://github.com/vanderbilt-data-science/how-tos)  

# Contact Info

Add contact information for any project stakeholders. Include name, email and title. 
