# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Feh(MakefilePackage):
    """
    feh is an X11 image viewer aimed mostly at console users. Unlike most
    other viewers, it does not have a fancy GUI, but simply displays images. It
    is controlled via commandline arguments and configurable key/mouse
    actions.
    """

    homepage = "https://feh.finalrewind.org/"
    url = "https://feh.finalrewind.org/feh-3.3.tar.bz2"

    maintainers = ["TheQueasle"]

    version("3.3", sha256="f3959958258111d5f7c9fbe2e165c52b9d5987f07fd1f37540a4abf9f9638811")
    version("3.1.1", sha256="61d0242e3644cf7c5db74e644f0e8a8d9be49b7bd01034265cc1ebb2b3f9c8eb")

    depends_on("imlib2")
    depends_on("curl")
    depends_on("libxinerama")
    depends_on("libexif")
    depends_on("libxt")

    def build(self, spec, prefix):
        make("PREFIX={0}".format(prefix), "exif=1", "help=1")

    def install(self, spec, prefix):
        make("install", "PREFIX={0}".format(prefix))
