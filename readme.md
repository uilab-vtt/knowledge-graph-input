Knowledge Graph Input
=====================

This project defines the data format of the `video_label`s, 
which are accepted as a input data for the [Knowledge Graph Builder](https://github.com/uilab-vtt/knowledge-graph-builder) project.

Since Knowledge Graph Builder takes [JSONLines](http://jsonlines.org/) file 
that is composed of `video_label` objects only, 
please validate your input data file before using with Knowledge Graph Builder.

## Definition of the `video_label` object

The main purpose of this project is to define the data format of `video_label` object. 
This section contains both formal and informal definition of this object.

### Description

A `video_label` object should follow one of the following 6 types of the objects.

#### Video label objects

**Object**

* `{"type": "object", "class": "person", "label": "Person A", "seconds": 15.0, "coordinates": [100, 200, 20, 30]}`
* `{"type": "object", "id": "person_ross_geller", "class": "person", "label": "Ross Geller", "seconds": 15.0, "coordinates": [100, 200, 20, 30]}`

**Behavior**

* `{"type": "behavior", "class": "stand", "seconds": 15.0, "object": ObjectIndicator}`

**Emotion**

* `{"type": "emotion", "class": "happy", "seconds": 15.0, "object": ObjectIndicator}`

**Relation**

* `{"type": "relation", "class": RelationalClass, "subclass": "wear", "seconds": 15.0, "source": ObjectIndicator, "target": ObjectIndicator}`

**Location**

* `{"type": "location", "class": "central_perk", "seconds": 15.0}`

**Sound**

* `{"type": "sound", "class": "glass_crashing", "seconds": 15.0}`

#### Sub-objects in video label objects

*ObjectIndicator*

* `{"id": "person_ross_geller"}` or
* `{"coordinates": [100, 200, 20, 30]}`

*RelationalClass*

* `"behavior"` for subclass `"wear"`, `"hold"`, `"hug"`, …
* `"emotion"` for subclass `"love"`, `"like"`, …
* `"position"` for subclass `"above"`, `"below"`, `"next_to"`, …
* `"social"` for subclass `"son_of"`, `"father_of"`, `"lover_of"`, `"friend_of"`, …

### Formal definition

A formal definition of the `video_label` object can be found in 
[video_label.schema.json](https://github.com/uilab-vtt/knowledge-graph-input/blob/master/video_label.schema.json) file.
This file defines the format of the `video_label` object in [JSON Schema](https://json-schema.org/).

## Validation of the input data file

This project includes a basic validator script to check if a given jsonlines file is a valid input data for Knowledge Graph Builder. Instructions for using the validator is as follows.

Before using the validator, make sure that Python 3 is available in your local environment.

Set up a virtual environment for Python 3. 
```bash
knowledge-graph-input$ python3 -m venv ./env
```

Activate the virtual environment to use.
```bash
knowledge-graph-input$ source ./env/bin/activate
```

Install required dependencies with Pip in your virtual environment.
```bash
(env) knowledge-graph-input$ pip install -r requirements.txt
```

Run `validate.py` script with your input data file as standard input.
Example command will validate the test input data file `test_input.jsonl`.
```bash
(env) knowledge-graph-input$ python3 validate.py < test_input.jsonl
Done.
```

If there are errors in the input data, erronous lines are shown on the terminal as standard error output. 
```bash
(env) knowledge-graph-input jeongmin$ python3 validate.py < test_input.jsonl
Validation error at line 3:
"{"type": "locational", "class": "central_perk", "seconds": 0.5}"
Validation error at line 14:
"{"type": "behavior", "seconds": 2.5, "object": {"id": "person_ross_geller"}}"
Done.
```
