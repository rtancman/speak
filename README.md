# speak
speak and learn others languages

- Layout by bootstrapzero: 
-- http://www.bootstrapzero.com/bootstrap-template/storystrap

# Install using docker :)
- Run npm:
$ docker run -v $(pwd):/usr/src/app node:onbuild

- Run bower:
$ docker run -it -v $(pwd):/usr/src/app node:onbuild /usr/src/app/node_modules/.bin/bower install --allow-root bower.json