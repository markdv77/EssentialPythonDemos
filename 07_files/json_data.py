import json
import os


def main():
    root_path = os.path.abspath(('.'))
    folder = 'data'
    file = 'example.json'
    filename = os.path.join(root_path, folder, file)

    print('Processing json file' + filename)

    if os.path.exists(filename):
        print('This will probably work as file exists!')
    else:
        print('Give up all hope')


    with open(filename, 'r') as fin:
        data = json.load(fin)
        print(data)
        print(type(data))

        gloss_term = data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm']
        print('GlossTerm: ' + gloss_term)

        print()
        print('back to json' + json.dumps(data, indent=3))

if __name__ == '__main__':
    main()