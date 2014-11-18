# $OpenBSD$

COMMENT =		???

DISTNAME =		hasard-1.0
#PKGNAME =		???
#PKGNAME-foo =		???	for multi packages

# for any port that create shared libraries.
# both libtool and cmake handle this automatically.
# for libtool-based ports, have a look at WRKBUILD/shared_libs.log
#SHARED_LIBS =		???

CATEGORIES =		security

HOMEPAGE =		http://bitbucket.org/haypo/hasard/wiki/Home

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

#WANTLIB =		???

# where the source files and patches can be fetched
#
MASTER_SITES =		http://bitbucket.org/haypo/hasard/downloads/
EXTRACT_SUFX =		.tar.bz2

MODULES +=		devel/cmake
MODULES +=		lang/python

USE_GMAKE =		Yes

CONFIGURE_STYLE =	cmake

.include <bsd.port.mk>
