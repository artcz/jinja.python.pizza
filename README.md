# jinja.python.pizza
PoC of a static rendered page with jinja

## About

This is an experiment with porting python.pizza template to jinja and python.
The current implementation of python pizza website uses react. This PoC is to check how it would look like with jinja.

The second goal is to keep the implementation as small as possible, with few external dependencies (currently only jinja2 for template rendering and `when-changed` for watching file changes).

At the time of this writing the code of the website fits in about 50 Python LOC + dependencies + jinja templates.
