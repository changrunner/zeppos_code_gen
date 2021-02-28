from subprocess import Popen, PIPE
import os

def main():
    pipfile = os.path.join(os.path.dirname(os.getcwd()), 'Pipfile')
    with open(pipfile, 'r') as fl:
        content = fl.readlines()

    p = Popen(['../commit_to_git.sh'], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    print(out)
    print(err)

    # out_array = out.decode("utf-8") .split('\r\n')
    # print(out_array)
    #
    # err_array = err.decode("utf-8") .split('\r\n')
    # print(err_array)

if __name__ == '__main__':
    main()
