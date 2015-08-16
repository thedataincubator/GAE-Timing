## GAE NDB Timing module

This module has several experimental modules that test the latency of GAE.  Please add more!  Results are posted below.

This project is seeded from [Appengine-Python-Flask-Skeleton](https://github.com/tianhuil/GAE-Timing) by Logan Henriquez and Johan Euphrosine.

## Results
1. Running locally, we get

   | request time | server time | server clock | data size | url |
   | ---- | --- | --- | --- | --- |
   | 0.006351 | 0.006338 | 0.001750 |    1181169 | /KeyRecord/full_query |
   | 0.000241 | 0.000228 | 0.000127 |     242847 | /KeyRecord/projection_query |
   | 0.000464 | 0.000452 | 0.000208 |    1499355 | /LargeRecord/full_query |
   | 0.001358 | 0.001346 | 0.000329 |    1095300 | /ManyRecord/full_query |
   | 0.000324 | 0.000312 | 0.000032 |      76300 | /ManyRecord/projection_query |
   | 0.003664 | 0.003644 | 0.001630 |      48708 | /RepeatedKeyRecord/full_query |
   | 0.001332 | 0.001321 | 0.000405 |    1056500 | /RepeatedRecord/full_query |
   | 0.001244 | 0.001234 | 0.000364 |    1106500 | /StructuredRecord/full_query |
   | 0.000420 | 0.000408 | 0.000080 |     134300 | /StructuredRecord/projection_query |

1. Running on GAE, we get

   | time | url |
   | ---- | --- |
   | 0.000180 | /large_records/query |
   | 0.000050 | /many_records/projection_query |
   | 0.000330 | /many_records/query |
   | 0.000280 | /repeated_records/query |
   | 0.000070 | /structured_property/projection_query |
   | 0.000380 | /structured_property/query |


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

1. To run the test, run

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

1. You can now run the timing script
   ```
   python timing.py <your-app-id.appspot.com>
   ```

## Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Licensing
See [LICENSE](LICENSE)

