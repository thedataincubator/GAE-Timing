## GAE NDB Timing module

This module has several experimental modules that test the latency of GAE.  Please add more!  Results are posted below.

This project is seeded from [Appengine-Python-Flask-Skeleton](https://github.com/tianhuil/GAE-Timing) by Logan Henriquez and Johan Euphrosine.

## Results
1. Running locally, we get
   ```
   0.000148 - /large_records/query
   0.000034 - /many_records/projection_query
   0.000358 - /many_records/query
   0.000340 - /repeated_records/query
   0.000049 - /structured_property/projection_query
   0.000395 - /structured_property/query
   ```
1. Running on GAE, we get
   ```
   0.000180 - /large_records/query
   0.000050 - /many_records/projection_query
   0.000330 - /many_records/query
   0.000280 - /repeated_records/query
   0.000070 - /structured_property/projection_query
   0.000380 - /structured_property/query
   ```


## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

1. Clone this repo with

   ```
   git clone https://github.com/tianhuil/GAE-Timing
   ```
1. Install dependencies in the project's ext directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   cd GAE-Timing
   pip install -r requirements.txt -t ext
   ```
1. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

   Visit the application [http://localhost:8080](http://localhost:8080)

   See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver) for options when running dev_appserver.

   To run the test, run

   ```
   python timing.py http://localhost:8080
   ```

## Deploy
To deploy the application:

1. Use the [Admin Console](https://console.developers.google.com) to create a
   project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```
1. Your application is now live at [your-app-id.appspot.com](your-app-id.appspot.com).

   You can now run the timing script
   ```
   python timing.py <your-app-id.appspot.com>
   ```

### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Contributing changes
See [CONTRIB.md](CONTRIB.md)

## Licensing
See [LICENSE](LICENSE)

