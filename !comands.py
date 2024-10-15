"""

0. python -m venv virt # create a new virtual environment named 'virt'
1. echo $VIRTUAL_ENV    # check if virtual env is active
2. source venv_name/Scripts/activate    # (activate virtual environment created before in py charm)
3. pip freeze   # check which packets are  currently installed
3. pip install pyinstaller   # install py installer
4. pyinstaller calc.py  # build an .exe with showing console
5. pyinstaller calc.py -w     # build an .exe without show console

REQUIREMENTS
pip install -r ./requirements.txt


GIT

git add .
git status
git commit -m "message"

git branch -M main
git remote add origin https://github.com/fenixfoux/task_manager_python.git
git push -u origin main #

FLET

export PYTHONIOENCODING=utf-8
flet build apk

pip freeze > requirements.txt

options for flet build

-h, --help: Show help message and exit.
-v, --verbose: Use -v for detailed output and -vv for even more detailed output.
-o OUTPUT_DIR, --output OUTPUT_DIR: Specify where to place the resulting executable or bundle (default is <python_app_directory>/build/<target_platform>).
--project PROJECT_NAME: Project name for the executable or bundle.
--description DESCRIPTION: Description to use for the executable or bundle.
--product PRODUCT_NAME: Project display name shown in window titles and about dialogs.
--org ORG_NAME: Organization name in reverse domain name notation (e.g., com.mycompany), used as an iOS and Android bundle ID.
--company COMPANY_NAME: Company name to display in about dialogs.
--copyright COPYRIGHT: Copyright text to display in about dialogs.
--splash-color SPLASH_COLOR: Background color for the splash screen in light mode.
--splash-dark-color SPLASH_DARK_COLOR: Background color for the splash screen in dark mode.
--no-web-splash: Disable web app splash screen.
--no-ios-splash: Disable iOS app splash screen.
--no-android-splash: Disable Android app splash screen.
--team TEAM_ID: Team ID for signing iOS bundle (ipa only).
--base-url BASE_URL: Base URL for the app (web only).
--web-renderer {canvaskit, html}: Renderer to use (web only).
--use-color-emoji: Enable color emojis with CanvasKit renderer (web only).
--route-url-strategy {path, hash}: URL routing strategy (web only).
--flutter-build-args [FLUTTER_BUILD_ARGS ...]: Additional arguments for the flutter build command.
--include-packages FLUTTER_PACKAGES [FLUTTER_PACKAGES ...]: Include extra Flutter packages like flet_video, flet_audio, etc.
--build-number BUILD_NUMBER: Build number (an integer used as an internal version identifier).
--build-version BUILD_VERSION: Build version (a "x.y.z" string shown to users).
--module-name MODULE_NAME: Python module name with the app entry point.
--template TEMPLATE: Directory containing a Flutter bootstrap template or URL to a git repository template.
--template-dir TEMPLATE_DIR: Relative path to a Flutter bootstrap template in a repository.
--template-ref TEMPLATE_REF: Branch, tag, or commit ID to checkout after cloning the repository with the Flutter bootstrap template.

"""




































