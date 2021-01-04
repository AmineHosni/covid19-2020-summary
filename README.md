# Covid-19, 2020 Summary

[![N|Solid](https://media-exp1.licdn.com/dms/image/C4D1BAQHWD_XYfa5YdA/company-background_10000/0/1519799016735?e=1609876800&v=beta&t=8-0hqUJxk5BULKBUOwDi_96yu5CAkDHjm1i9_LZ34jg)](https://nodesource.com/products/nsolid)

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Installation
Install the virtualenv package

```sh
$ pip install virtualenv
```
### Create the virtual environment
```sh
$ virtualenv your_env_name
```

### Activate the virtual environment
Mac OS / Linux
```sh
$ source your_env_name/bin/activate 
```
Windows
```sh
$ your_env_name\Scripts\activate 
```

### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ pip install virtualenv
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Launching the app


```sh
python app.py
```

Check the localhost link at:
```sh
127.0.0.1:8050
```



### Todos

 - calculer weekly and monthly Mean, Median, Std.Dev, Max et Min by country

License
----

MIT