## GAE NDB Timing module

This module has several experimental modules that test the latency of GAE.  Please add more!  Results are posted below.

This project is seeded from [Appengine-Python-Flask-Skeleton](https://github.com/tianhuil/GAE-Timing) by Logan Henriquez and Johan Euphrosine.

## Methods

1. We ran both full queries (`full_query`) and projection queries (`projection_query`) on 1MB of data stored in various ways.  The full `projection_query` were typically for ~ 1MB of data while the `projection_query` were for less.  We would clear the memcache before performing the query.  For each query, we returned:
   - clock time (as measured by `time.clock()` on the server)
   - wall time (as measured by `time.time()` on the server)
   - request wait time (as measured by `time.time()` on the client)
   - the number of bytes of the string representation (computed on the server, but only the first 1K characters were returned to the client).

This measure the amount of time it takes for GAE to fetch and deserialize a result from NDB.

## Results

1. Projection queries (`projection_query`) take up much less time than pulling back the entire object (`full_query`), even thoguh they query over the same number of records .  It seems that the query time is proportional to the size of the data returned for projections.

1. Large properties (`TextProperty`) takes less time than many small records (`StringProperty`) for the same size of data returned (in our case, 50% less).

1. Having a single property of length `n` (`RepeatedRecord`) vs. having `n` properties with unique names (`ManyRecord`) takes the same amount of time.

1. Using SQL-like "foreign" keys is non-performant (`KeyRecord`) and fetching them using `ndb.get_mutli` is non.performant.  It is (2 - 5 times slower) than having those objects be structured properties (`StructuredRecord`).  This is true regardless of whether the keys are a repeated property (`RepeatedKeyRecord`) or individual properties with unique names (`KeyRecord`).  In fact, custom `ndb.StructuredProperty` is as efficient as builtin NDB properties (`RepeatedRecord`).

## Data and Plots
1. See [/timing.ipynb](timing.ipynb)

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

