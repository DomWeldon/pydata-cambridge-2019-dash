# PyData Cambridge 2019 🎓

_Saturday 16 November 2019._

## Dash: INTERACTIVE DATA VISUALIZATION WEB APPS WITH NO JAVASCRIPT

**Please note the examples in this repository require Python >= 3.6 - official python 3.5 support is being withdrawn in January 2020...**

The slides relating to this talk [are available here](https://docs.google.com/presentation/d/1nzNnkWZ-6L20QM3ZLsuooHblV2K78Rdp4Gdl94s74eE/edit?usp=sharing).

### Example Applications

Run the apps in this repository to see how Dash can be used.

### JGMTFC: Run Everything with Docker-compose

    docker-compose -f docker-compose-talk.yml up

#### Install

This is a freeze of my environment in which all these worked.

    pip install -r requirements.txt

#### Run Individually

**Hello World**

Greet the world in Dash style. [http://localhost:8049](http://localhost:8049)

    python app00.py


**Interactive Hello World**

Your first interactive Dash app. [http://localhost:8051](http://localhost:8051)

    python app01.py


**Data Table (bad)**

Using global state is not referenced in this talk, but I've left it in here as an example of a bad thing to do! [http://localhost:8049](http://localhost:8052)

    python app02.py


**Data Table (Good)**

List the Titanic Dataset using just a few lines of code. [http://localhost:8053](http://localhost:8053)

    python app03.py

**Events: To Do App**

A basic todo app, in Dash. But without a proper data store! [http://localhost:8054](http://localhost:8054)

    python app04.py


**Splitting Up App: To Do**

Split up your app. [http://localhost:8055](http://localhost:8055)

    python -m app05


**Factory Functions**

And use factory functions! [http://localhost:8056](http://localhost:8056)

    python -m app06
