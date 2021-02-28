from glob import glob
import os



def main():

    pipfile = os.path.join(os.path.dirname(os.getcwd()), 'Pipfile')
    with open(pipfile, 'r') as fl:
        content = fl.readlines()

    section_name = None
    packages = []
    for line in content:
        line = line.replace('\n', '')
        if '[' in line:
            section_name = line
        else:
            if 'packages' in section_name.lower().strip():
                if len(line.strip()) > 0:
                    packages.append(line)

    print(packages)


if __name__ == '__main__':
    main()
