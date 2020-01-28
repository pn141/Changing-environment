import os
import sys
import getopt
import helper_func as hp


def main(argv):
    current_ctx = ''
    new_ctx = ''
    app_path = ''

    # usage and example will be printed if user types -h or /?
    # after module name.
    usage = "change_app_context.py -c <current_context> -n <new_context> \
        -a <FLASK_APP file>"
    example = "Example: change_app_context.py -c development -n testing -a \
        app.py"

    # Given command line arguments
    # Assign them to their internal representation
    try:
        opts, args = getopt.getopt(argv, "hc:n:a:",
                                   ["ccontext=", "ncontext=", "app="])
    except getopt.GetoptError:
        print(usage)
        print(example)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '/?':
            print(usage)
            print(example)
        elif opt in ("-c", "--ccontext"):
            current_ctx = arg
        elif opt in ("-n", "--ncontext"):
            new_ctx = arg
        elif opt in ("-a", "--app"):
            app_path = os.path.abspath(arg)
    # Then find and replace the application context
    # in the appropriate files.
    dotenv_path = os.path.abspath('.env')
    if current_ctx and new_ctx and app_path:
        hp.find_and_replace(dotenv_path, current_ctx, new_ctx)
        hp.find_and_replace(app_path, current_ctx, new_ctx)


if __name__ == "__main__":
    main(sys.argv[1:])
