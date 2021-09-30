# Code Experiment FastAPI Playground

This is a playground built during the Code Experiment meetup. We will slowly be building a Todo app with authentication. If you would like to join please head over to https://code-experiment.netlify.app/ and join our slack, we meet every Tuesday at 6:00 pm MST.

If you want to catchup, please clone this repo and follow the steps below.

## Environment Setup

**Create Virtual Environment:**

> Wherever you run this command it will create a `venv` folder. If you want the folder to be called something different change the second `venv`.

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
(venv) $ pipenv install
```

> You might need to change the version of python

## Run The Uvicorn Server

> Make sure you are inside the `code_experiment_playground` folder when you run this command.

```
(venv) $ uvicorn app.main:app --reload
```

## Interactive Docs

Open your favorite browser and head to http://localhost:8000/docs for the docs.

## Running tests

We're using pytest for our testing you can learn more at https://docs.pytest.org/en/stable/

- Run all tests

```
(venv) $ python -m pytest
```

- Run all tests from a single file

```
(venv) $ python -m pytest folder/file_name.py
```

- Run a single test from a single file

```
(venv) $ python -m pytest folder/file_name.py::test_function_name
```

- Run all tests that contain a certain marker

```
(venv) $ python -m pytest -m marker_name
```

## Debugging Tests

The following steps are for vscode.

- Open your command palette
  - MAC: `cmd` + `shift` + `p`
  - PC: `ctrl` + `shift` + `p`
- Type `configure tests` and push enter
- Highlight `pytest` and push enter
- Highlight `tests` for the `tests` directory and push enter

You should have a `.vscode` folder with a `settings.json` when finished. You should have a new icon on the left that looks like a test beaker. You should also be able to see `run test` and `debug test` on all your tests now. If not try to reload vscode.

> A key to this working was adding a `__init__.py` file in the tests directory. Without that file I wasn't able to discover the tests. I got this information from https://stackoverflow.com/a/55839418/12313312

## Running tests and generating coverage

- https://pypi.org/project/pytest-cov/
- `python -m pytest --cov-report html:html_cov_report --cov=app tests/`

## Running tests and displaying coverage report in the terminal

- https://pypi.org/project/pytest-cov/
- `python -m pytest --cov-report term --cov=app tests/`

## Testing

- Fixtures:
  - https://docs.pytest.org/en/stable/fixture.html
- Setting up the database/fixture research:
  - https://github.com/tiangolo/fastapi/issues/831
  - https://github.com/timhughes/example-fastapi-sqlachemy-pytest
- Configuration:
  - https://docs.pytest.org/en/stable/customize.html

## Deployment

The app is currently setup to work with `Heroku` and `Heroku-Postgres`

- Create a new app on `Heroku`
- Under the deploy tab follow the steps for `Existing Git repository`
- Add `Heroku-Postgres` as an `Add-on`
- Run the command `git push heroku main`

## Environment Variables

Read more into this at https://fastapi.tiangolo.com/advanced/settings/
