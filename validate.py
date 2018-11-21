import sys
import json
from jsonschema import validate, ValidationError

def load_schema():
    with open('video_label.schema.json', 'r') as f:
        schema_string = f.read()
        schema = json.loads(schema_string)
    return schema

def get_input_iter():
    for i, line in enumerate(sys.stdin, 1):
        try:
            yield json.loads(line)
        except json.decoder.JSONDecodeError:
            sys.stderr.write(
                'Failed to decode JSON object at line %d: "%s"\n' % (i, line))

def main():
    schema = load_schema()
    for i, obj in enumerate(get_input_iter(), 1):
        try:
            validate(obj, schema)
        except ValidationError as e:
             sys.stderr.write(
                'Validation error at line %d:\n%s\n' % (i, e))
    print('Done.')

if __name__ == '__main__':
    main()