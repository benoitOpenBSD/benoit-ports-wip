# $OpenBSD$

COMMENT =	Molecular energy calculation program

V =		7
DISTNAME =	mopac${V}
PKGNAME =	mopac-${V}
CATEGORIES =	biology

HOMEPAGE =	http://server.ccl.net/cca/software/LINUX/mopac7/index.shtml

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =		Yes

WANTLIB =		c m

MASTER_SITES =		http://server.ccl.net/cca/software/LINUX/mopac7/
MASTER_SITES0 =		http://server.ccl.net/cca/software/LINUX/mopac7/old-version-95.06.21/

DISTFILES =		${DISTNAME}${EXTRACT_SUFX} mopac7-man.tar.gz

EXTRACT_SUFX =		.tar.Z

PATCHFILES =		mopac7-linux.diff.gz:0
PATCH_DIST_STRIP =	-p1

ALL_TARGET=     	mopac

USE_GMAKE=		Yes

#MAKE_FLAGS+=	EXTRA_CFLAGS=${EXTRA_CFLAGS}

NO_TEST =		Yes

.include <bsd.port.mk>
