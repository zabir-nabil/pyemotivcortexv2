# Cortex: Python example

Cortex API v2 

## Prerequisites

The example code uses features that are only available in Python >= 3.6

In addition, the example code only works with Cortex 2.0, it is not compatible
with older versions of Cortex.

## Websockets

The example uses the Python websockets library to connect to Cortex.  The
websockets library (not to be confused with the older websocket library).

The websockets library utilizes `await` and `async` which were introduced in
Python 3.6.  

## Before you start

We generally recommend using a virtual environment.

Once you've set up your environment (virtual or otherwise) install the
requirements with `pip`:
    pip install -r requirements.txt

To run the existing example you will need to do a few things.

1. You will need an EMOTIV headset.  You can purchase a headset in our [online
   store](https://www.emotiv.com/)
2. Next, [download and install](https://www.emotiv.com/developer/) the Cortex
   service.  Please note that currently, the Cortex service is only available
   for Windows and macOS.
3. We have updated our Terms of Use, Privacy Policy and EULA to comply with
   GDPR. Please login via the EMOTIV App to read and accept our latest policies
   in order to proceed using the following examples.
4. Next, to get a client id and a client secret, you must connect to your
   Emotiv account on
   [emotiv.com](https://www.emotiv.com/my-account/cortex-apps/) and create a
   Cortex app. If you don't have a EmotivID, you can [register
   here](https://id.emotivcloud.com/eoidc/account/registration/).
5. Then, if you have not already, you will need to login with your Emotiv id in
   the EMOTIV App.
6. Finally, the first time you run these examples, you also need to authorize
   them in the EMOTIV App.

## Credetials

Place the client id, and client secrets inside lib/cortex.py

## Details

The canonical documentation for Cortex is available
[here](https://emotiv.gitbook.io/cortex-api/). It includes full descriptions of
the various methods available.

## Youtube Demo

https://youtu.be/dtzQA_DyNNI
