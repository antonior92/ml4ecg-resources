from liquid import Template
import yaml
import os

# Created datastructure similar to the one used by liquid in my website
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Aplly liquid to a file')
    parser.add_argument('file', help='input tex file.')
    parser.add_argument('datafolder', help='folder containing data')
    parser.add_argument('-o', '--output', default='out.txt', type=str,
                        help='where to save the output')
    args = parser.parse_args()
    mydata = {}

    for subdir, dirs, files in os.walk(args.datafolder):
        relative_path = os.path.relpath(subdir, args.datafolder)

        mycurrentdict = mydata
        for t in os.path.normpath(relative_path).split('/'):
            if t in mycurrentdict.keys():
                mycurrentdict = mycurrentdict[t]

        for dir in dirs:
            mycurrentdict[dir] = {}
        for file in files:
            filepath = subdir + os.sep + file
            name, ext = os.path.splitext(file)

            if ext == ".yml":
                # Read YAML file
                with open(filepath, 'r') as stream:
                    localdict = yaml.safe_load(stream)
                mycurrentdict.update(**{name: localdict})

    with open(args.file, "r") as f:
        latex_template = f.read()

    template = Template(latex_template)

    tex_output = template.render(**mydata)

    with open(args.output, "w") as f:
        f.write(tex_output)