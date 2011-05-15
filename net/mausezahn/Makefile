# $OpenBSD$

COMMENT =	free fast traffic generator

V =		0.40
DISTNAME =	mz-$V
PKGNAME =	mausezahn-$V
CATEGORIES =	net

HOMEPAGE =	http://www.perihel.at/sec/mz/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${HOMEPAGE}

WANTLIB =		c pcap lib/libnet-1.1/net=11

LIB_DEPENDS =		net/libnet/1.1

MODULES =		devel/cmake

CONFIGURE_STYLE =	cmake

CONFIGURE_ARGS =-DCMAKE_C_FLAGS:STRING="-I${LOCALBASE}/include -L${LOCALBASE}/lib -D_POSIX_C_SOURCE=199309L"

pre-configure:
			${SUBST_CMD} ${WRKSRC}/CMakeLists.txt \
			${WRKSRC}/src/mz.h
	
USE_GROFF =		Yes

NO_REGRESS =		Yes

.include <bsd.port.mk>
