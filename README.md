# pinboard-tweeter
A utility to Tweet my most recent Pinboard additions. Plenty of solutions exist to go from Twitter to Pinboard, but not the other way around.

I have no Python experience and I wrote this to get familiar with the language.

## Setup

1. Clone this repository.
2. Optionally, start and activate a new virtual environment. This will make it harder to run on a crontab, but not impossible.
3. Install dependencies: `pip install -r requirements.txt`
4. Plug in your Pinboard and Twitter app API keys in `pin.py`.
5. Run `pin.py` on a `crontab` job. I have mine set to run every 30 minutes in concert with the “age of bookmark” cutoff.
