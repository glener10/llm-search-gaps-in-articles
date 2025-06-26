# **LLM search gaps in articles**

<p align="center"> 🚀 This script is designed to search gaps in pdf articles using LLMs </p>

<h3>🏁 Table of Contents</h3>

<br>

===================

<!--ts-->

💻 [Dependencies and Environment](#dependenciesandenvironment)

☕ [Using](#using)

👷 [Author](#author)

<!--te-->

===================

<div id="dependenciesandenvironment"></div>

## 💻 **Dependencies and Environment**

Dependencies and versions

- Python 3.10.12

**Gemini**: This project uses the paid Google Gemini API, it's necessary to configure a valid Gemini API Key. Ensure you have a `.env` file with the environment variable **API_KEY**.

**Deepseek, local processing**: The project can use the Deepseek model for local processing, which requires the installation and configuration of [Ollama](https://ollama.com/download)

<div id="using"></div>

## ☕ **Using**

First, check the [dependencies](#dependenciesandenvironment) process

Feel free to change the prompt as you see fit in [`prompt.txt`](./prompt.txt)

You also can create scripts to exec N models for N inputs and generate N output files, like in [`exec_many.sh`](./exec_many.sh)

You can clean the environment using

```
$ make clean
```

Optional parameters

**-m**: pass the llm model

**-o**: output path

### Gemini

to gemini exec:

```
$ make run-gemini INPUT=YOUR_INPUT_PATH
```

### DeepSeek

to deepseek exec:

```
$ make run-deep INPUT=YOUR_INPUT_PATH
```

<div id="author"></div>

#### **👷 Author**

Made by Glener Pizzolato! 🙋

[![Linkedin Badge](https://img.shields.io/badge/-Glener-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/glener-pizzolato/)](https://www.linkedin.com/in/glener-pizzolato-6319821b0/)
[![Gmail Badge](https://img.shields.io/badge/-glenerpizzolato@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:glenerpizzolato@gmail.com)](mailto:glenerpizzolato@gmail.com)
