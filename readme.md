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

TBD

## Validation of the input data file


