# $OpenBSD$

COMMENT =	perl interface for libdnet

DISTNAME =	Net-Libdnet-0.92
CATEGORIES =	net

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MODULES =		cpan

MODCPAN_EXAMPLES =	Yes

BUILD_DEPENDS =		${RUN_DEPENDS}
RUN_DEPENDS =		net/libdnet \
			devel/p5-Class-Gomor

.include <bsd.port.mk>
