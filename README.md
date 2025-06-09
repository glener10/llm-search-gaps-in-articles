# **LLM search gaps in articles**

<p align="center"> 🚀 This script is designed to search gaps in pdf articles using LLMs. </p>

<h3>🏁 Table of Contents</h3>

<br>

===================

<!--ts-->

💻 [Dependencies and Environment](#dependenciesandenvironment)

☕ [Using](#using)

⚙️ [Install](#install)

👷 [Author](#author)

<!--te-->

===================

<div id="dependenciesandenvironment"></div>

## 💻 **Dependencies and Environment**

Dependencies and versions

- Python 3.10.12

<div id="install"></div>

## ⚙️ **Install**

We use venv, to install all dependencies of all llms providers, exec

```
$ make install
```

<div id="using"></div>

## ☕ **Using**

First, check the [dependencies](#dependenciesandenvironment) and [install](#install) process

Ensure you have a `.env` file with the environment variable **API_KEY** for the respective LLM.

to gemini exec:

```
$ make run-gemini INPUT=YOUR_INPUT_PATH
```

You can clean the environment using

```
$ make clean
```

<div id="author"></div>

#### **👷 Author**

Made by Glener Pizzolato! 🙋

[![Linkedin Badge](https://img.shields.io/badge/-Glener-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/glener-pizzolato/)](https://www.linkedin.com/in/glener-pizzolato-6319821b0/)
[![Gmail Badge](https://img.shields.io/badge/-glenerpizzolato@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:glenerpizzolato@gmail.com)](mailto:glenerpizzolato@gmail.com)
