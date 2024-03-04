# For CM team
Docs for translation

tests/**test_image.py**  RU→EN,ES

tests/**test_env_vars.py** RU→EN,ES

tests/**test_container.py** RU→EN,ES

tests/**conftest.py** RU→EN,ES

python-docker-1/**README.MD** RU→EN,ES

simple_project/**manage.p**y EN->ES

simple_project/simple_project/**wsgi.py** EN->ES

simple_project/simple_project/**urls.py** EN->ES




# python-docker-1

## Creating a repository
1. Create a repository for yourself, using this template. 
  To do this, it is necessary to press the "Use this template" button and select the "Create a new repository" option.
  ![image](https://user-images.githubusercontent.com/14962819/235599080-2819c72b-3161-48fe-926d-91c289941c20.png)
  
1. Fill in the Repository name and Description fields and click the "Create repository from template" button. 
  ![image](https://user-images.githubusercontent.com/14962819/235599367-6b6025e2-5ceb-4b57-87f4-8c3a2ac18a5b.png)


## How to work with a repository
To start the task, you need to copy the URL of your repository and clone it (please note that you are cloning your own repository, not the original template!).
  ![image](https://user-images.githubusercontent.com/14962819/235600053-de6be309-56d5-4c5f-adc3-d466887962f6.png)
  
### Create a virtual environment

1. Launch the Visual Studio Code editor and through the “File” / “Open Directory” menu open the *Dev/python-docker-1/* folder.
2. Launch a terminal in VS Code, make sure you're running from the */python-docker-1/* directory (if you're on Windows, make sure you're running Git Bash in the terminal and not PowerShell or anything else), and run the command
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
A virtual environment will be deployed in the python-docker-1/ directory and a venv folder will appear in which all project dependencies will be stored. The file structure will be like this:

```
Dev/
 └── python-docker-1/
     ├── tests/ Workshop tests that check the project
     ├── venv/ Virtual environment directory
     ├── simple_project/ <-- Project directory
     | ├── ...    <-- Django project structure
     |   └── manage.py      
     ├── .gitignore     List of files and folders hidden from Git tracking (hidden) 
     ├── LICENSE     License   
     ├── pytest.ini      Workshop test configuration
     ├── README.md       Description of the project 
     └── requirements.txt      List of project dependencies
```

### Activation of the virtual environment
In the terminal, go to the root directory of the project (Dev/python-docker-1/) and run this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Now all commands in the terminal will be preceded by the line `(venv)`.

💡 All further commands in the terminal should be executed with the virtual environment activated.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

### Installing dependencies from the requirements.txt file:
While in the Dev/python-docker-1/ folder, run the command:

```bash
pip install -r requirements.txt
```

#### End of Support for dependencies

LTS versions of dependencies have been chosen.
For Django, version 3.2 is selected, [extended support](https://endoflife.date/django) of which ends on April 1, 2024.


### Launching the project in dev mode

    
In the directory with the "manage.py" file, run this command: 

```bash
python manage.py runserver
```

In response, Django will report that the server is running and the project is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Run tests locally
Having finished the task, launch the local tests. In the terminal, go to the root directory of the project *Dev/python-docker-1/* and run this command:
```shell
pytest
```
If all the test cases are successful, the project will be considered completed. Otherwise, you will have to fix the parts that haven't passed the tests and launch them once again.
