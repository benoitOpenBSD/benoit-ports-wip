# $OpenBSD$

COMMENT =	perl interface to libnova 

DISTNAME =	Astro-Nova-0.06
CATEGORIES =	astro

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl - LGPL
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MODULES =		cpan

BUILD_DEPENDS =		devel/p5-ExtUtils-Typemap
RUN_DEPENDS =		${BUILD_DEPENDS}

CONFIGURE_STYLE =	modbuild

MODCPAN_EXAMPLES =	Yes

USE_GROFF =		Yes

.include <bsd.port.mk>
