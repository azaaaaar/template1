import logging
from os.path import abspath, join, dirname
DOC_ROOT = dirname(__file__)

TITLE_PREFIX = 'MooTools Frontend'

# Set to true to re-load all JS every time. (slowish)
DEPENDER_DEBUG = True

DEPENDER_PACKAGE_YMLS = []
DEPENDER_SCRIPTS_JSON = []
BUILDER_PACKAGES = []

PROJECTS = {
  "Core": {
    "package": "../core/package.yml",
    "specs": [
      "../core-specs/1.3base/package.yml",
      // stopped
      "../core-specs/1.3client/package.yml"
    ],
    "build": True
  },
  "More": {
    "package": "../more/package.yml",
    "specs": ["../more/Specs/package.yml"],
    "demos": {
      "path": "../more/Tests",
      "exclude": True
    },
    "docs": "../more/Docs",
    "build": True
  },
  "Depender": {
    "package": "../depender/client/package.yml",
    "build": False
  }
}

GENERIC_ASSETS = {
  'Assets.js.test.js': abspath(join(DOC_ROOT, "../more/Specs/assets/Assets.js.test.js")),
  'Assets.css.test.css': abspath(join(DOC_ROOT, "../more/Specs/assets/Assets.css.test.css")),
  'mootools.png': abspath(join(DOC_ROOT, "../more/Specs/assets/mootools.png")),
  'cow.png': abspath(join(DOC_ROOT, "../more/Specs/assets/cow.png")),
  'notExisting.png': abspath(join(DOC_ROOT, "../more/Specs/assets/notExisting.png")),
  'iDontExist.png': abspath(join(DOC_ROOT, "../more/Specs/assets/iDontExist.png")),
  'iDontExistEither.png': abspath(join(DOC_ROOT, "../more/Specs/assets/iDontExistEither.png")),
  'jsonp.js': abspath(join(DOC_ROOT, "../more/Specs/assets/jsonp.js")),
}

# which buttons are visible at the top of the app? Comment out any you choose.
BUTTONS = [
  'Docs',
  'Demos',
  'Specs',
  'Benchmarks',
  'Builder'
]

#############################################################################
###                  DO NOT EDIT BELOW THIS LINE                          ###
#############################################################################


# Django settings for mootools-test-runner project.

logging.basicConfig(level=logging.INFO)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'djangomako.middleware.MakoMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'frontend_dev',
    'depender',
    'django_extensions',
    'django.contrib.markup',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
)

MOOTOOLS_RUNNER_PATH = abspath(join(DOC_ROOT, "../mootools-runner"))

MAKO_TEMPLATE_DIRS = (
  abspath(join(DOC_ROOT, "frontend_dev/templates")),
  abspath(join(DOC_ROOT, "../depender/django/src/depender/templates")),
)

DEPENDER_PACKAGE_YMLS = []
DEPENDER_SCRIPTS_JSON = []
BUILDER_PACKAGES = []

for name, project in PROJECTS.iteritems():
  if project.has_key("package"):
    DEPENDER_PACKAGE_YMLS.append(project['package'])
  if project.has_key('scripts_json'):
    DEPENDER_SCRIPTS_JSON.append(project['scripts_json'])
  if project.has_key("specs"):
    for spec in project["specs"]:
      DEPENDER_PACKAGE_YMLS.append(spec)
  if project.has_key("build") and project["build"] is True:
    BUILDER_PACKAGES.append(name)


def GET_PATH(path):
  return abspath(join(DOC_ROOT, path))
  //new
