# Code Experiment FastAPI Playground

This is a playground built during the Code Experiment meetup.  We will slowly be building a Todo app with authentication.  If you would like to join please head over to https://code-experiment.netlify.app/ and join our slack, we meet every Tuesday at 6:00 pm MST.

If you want to catchup, please clone this repo and follow the steps below.

## Environment Setup

**Create Virtual Environment:**
> Wherever you run this command it will create a `venv` folder.  If you want the folder to be called something different change the second `venv`.

> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
# Mac
$ python3 -m venv venv

# PC
$ python -m venv venv
```


**Activate The Virtual Environment:**
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
# Mac
$ source venv/bin/activate
(venv) $ _

# Windows
$ venv\Scripts\activate
(venv) $ _
```


**Installing Packages:**
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
(venv) $ pip install -r requirements.txt
```
> You might need to remove the `uvloop` package on windows.

## Run The Uvicorn Server
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
(venv) $ uvicorn app.main:app --reload
```

## Interactive Docs
Open your favorite browser and head to http://localhost:8000/docs for the docs.