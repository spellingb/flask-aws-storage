# Welcome
Thanks for stopping by.

This is a simple flask application for uploading and downloading images to an s3 bucket.

The application will create an s3 bucket if one does not already exist that matches the name *lab-img-mgr*

This should only be used in labs and is by no means anywhere near a production application. Use at your own risk!

### to build container:

``` docker
docker build -t img-mgr .
```
