# about

- django image gallery app

### directions to run app 

- clone repo to local 
- `cd` into project root 
    `cd image_gallery_app`
- activate virtual env in CLI 
    - `source env/bin/activate` in project root dir
- install dependencies for app
    - `pip install -r requirements.txt`
- run django development server 
    - `python manage.py runserver`
- go to `localhost:8000` in browser
    - use upload button to upload images into gallery
    - click on image to show blown-up image 
    - delete button exists in blow-up view 
    - hit back to come back to gallery
    - in nav bar, there is 'Filter by Category'
- hit `Ctrl+C` to end development server
- `deactivate` command ends virtual environment


### requirements

The web app should contain a simple page which shows all the images uploaded.


Initially when there are no images, display a message saying upload an image.


1) A button should be present to upload the image. On clicking it we should be able to select an image category  from the drop down and choose the image from the computer and upload it.

2) After adding the image it should be visible in the gallery page. 

3) Also we should be able to filter the image based on category. Upon selecting a category, only the images of that particular categories should show. 

4) Give a button "clear filter" to clear the category filter and show all the images.


The images should be sorted according to the latest created.


### guidelines

1. Clear separation of concerns

2. No code duplication

3. Readable code

4. Tests where relevant are a must

5. Use Best coding practices modular programming.

### author

- Raghavendra Saralaya 
    - [email](raghavendra.saralaya@protonmail.com)