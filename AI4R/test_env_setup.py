from importlib.metadata import version, PackageNotFoundError
import platform
import traceback
import tkinter

COURSE_PYTHON_VERSION = '3.10'
COURSE_MIN_RECOMMENDED_PYTHON_VERSION = '3.10'

def verify_python_installation():
    print('\n< Verifying python installation... >')
    python_version = platform.python_version()
    python_version_major_minor = '.'.join(python_version.split('.')[:2])
    print(f'\tYour python version: {python_version}')


    if python_version_major_minor != COURSE_PYTHON_VERSION:
        warning_msg = f'\t~ Your python version is not the same as the version used by the autograder ({COURSE_PYTHON_VERSION}).\n'\
                      f'\t~ The minimum recommended version is {COURSE_MIN_RECOMMENDED_PYTHON_VERSION}.'
        print(warning_msg)
    else:
        print(f'\t✅  Recommended version ({COURSE_PYTHON_VERSION}) installed!')

def verify_libraries_installation():
    print('\n< Verifying installation of libraries... >')
    with open('rait_env.yml', 'r') as f:
        yaml_contents = f.readlines()
    dependencies = [line.strip('- \n/') for line in yaml_contents[yaml_contents.index('dependencies:\n')+2:] if ':' not in line]
    try:
        for pkg in dependencies:
            pkg_version = version(pkg)
            print(f'\t{pkg} {pkg_version}')
        print('\t✅  All libraries installed!')
    except PackageNotFoundError as e:
        print(f'\t⚠️ Missing library: {pkg}')
        print(traceback.format_exc())
        print(f'Please retry the installation process.  You are missing the <{pkg}> package.')
    except Exception as e:
        print('\t❌️ Error')
        print(traceback.format_exc())

def verify_unicode_display():
    print('\n< Verifying unicode display... >')
    print(f'\tYou should see 8 arrows here: ↖↗↘↙←→↑↓\n'
          f"\tIf you don't see the arrows above then you should install the symbola font and run this script again.  See troubleshooting tips in the PDF document.")

def verify_tkinter_installation():
    print('\n< Verifying tkinter installation... >')
    print('\tA GUI window should appear with a "click me" and "quit" button demonstrating that tkinter is working properly.')
    tkinter._test()


if __name__ == '__main__':
    verify_python_installation()
    verify_libraries_installation()
    verify_unicode_display()
    verify_tkinter_installation()
