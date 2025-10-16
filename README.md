# arches-her-workflows

## How do I get started with Arches for HERs
To run the arches_her_workflows, you need to set up arches_her first.
You can find out more information about arches_her at [https://www.github.com/archesproject/arches-her/](https://www.github.com/archesproject/arches-her/)


1. Add `arches_her_workflows` to your project's `INSTALLED_APPS` and `ARCHES_APPLICATIONS` settings in settings.py. Note that in `INSTALLED_APPS`, `arches_her_workflows` must be listed before your project:

   ```python
   INSTALLED_APPS = (
      "webpack_loader",
      "django.contrib.admin",
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "django.contrib.sessions",
      "django.contrib.messages",
      "django.contrib.staticfiles",
      "django.contrib.gis",
      "arches",
      "arches.app.models",
      "arches.management",
      "guardian",
      "captcha",
      "revproxy",
      "corsheaders",
      "oauth2_provider",
      "django_celery_results",
      "compressor",
      "arches_her",
      "arches_her_workflows",
      "my_project",
   )

   ARCHES_APPLICATIONS = ("arches_her", "arches_her_workflows")
   ```

2. If developing Arches for HERs, you'll need to add the HER_ROOT setting which indicates where on your file system your arches_her repository is located. You'll need to adjust the path according to where you have cloned the arches_her repo:

   ```python
   HER_ROOT = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()) + '../../../')), 'arches-her-workflows', 'arches_her_workflows')
   ```

3. Next update your project's urls.py file to include the Arches for HERs urls like so:

   ```python
   urlpatterns = [
      path("", include("arches.urls")),
      path("", include("arches_her.urls")),
      path("", include("arches_her_workflows.urls")),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

4. Add `arches_her_workflows` as a dependency in your project's `package.json` file:

   ```javascript
   "dependencies": {
        "arches": "archesproject/arches#stable/8.0.0",
        "arches_her": "archesproject/arches_her#stable/2.0.x"
        "arches_her_workflows": "archesproject/arches_her_workflows#stable/0.0.1"
    },
    ```
5. Add `docx` to `FILE_TYPES` in `settings.py`:

    ```python
    FILE_TYPES = [
        ...
        "docx",
    ]
    ```

## Working with Letter Templates

Field tag replacement in the templates can easily break if styling changes occur within the Word documents. The internal &ldquo;style runs&rdquo; provide rich formatting for the letters, but if a style partially touches a field tag (a field name surrounded by angle brackets), the field tag is physically split across several style runs. When this happens, it is no longer possible for the field to be substituted with its data value.

It is good practice to run the docx management command after working on the letter templates and before committing to source control. The full command is:

```bash
python manage.py docx fix_style_runs --dest_dir docx
```

The `--dest_dir` parameter is optional and defaults to the `docx` folder.

The Word files in the destination folder are processed in turn, and the command looks for pairs of angle brackets that may span multiple style runs. When this happens, they are joined together, thus restoring the full field tag.
