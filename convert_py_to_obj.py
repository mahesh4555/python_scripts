from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("pubsub_client", ["pubsub_client.py"]),
    Extension("google_apis", ["google_apis.py"]),
    Extension("handler", ["handler.py"]),
]

setup(
  name = 'main_prog',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
