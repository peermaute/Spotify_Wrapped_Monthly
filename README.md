# Spotify Wrapped Monthly
Spotify Wrapped Monthly is a Python script to create a playlist with your top 50 tracks of the last month utilizing the Spotify Web API.

## How to use this script
    1. Use your Spotify account to login and activate the developers features of your account [here](https://developer.spotify.com/dashboard/login). 
    2. Create an application as described [here](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/). 
    3. The client id and client secret can be found when visiting this application in your dashboard. For the Authorization header of an HTTP request they need to be concatenated divided by a ':' and Base64 encoded.
    4. This [guide](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/) describes how you get a refresh token. As we use the Authorization Flow, it is only necessary to get the authorization code once and then use it to get an access token and a refresh token. In the script, we simply use the refresh token to get an access token.
    5. The last thing needed is your user id. If you do not know it already, you can use [this endpoint](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-current-users-profile) to get it.

## Environment variables
| Environment Variable               | Description                                                                                                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| SPOTIFY_USER_ID                    | Your Spotify User ID                                                                                                                              |
| SPOTIFY_REFRESH_TOKEN              | The refresh token retrieved by using the Authentication Flow. This is used in the script to get a new access token.                               |
| SPOTIFY_CLIENTID_AND_SECRET_BASE64 | The client id and client secret of your application created in the Spotify Dashboard. They need to be concatenated with a ':' and Base64-encoded. |