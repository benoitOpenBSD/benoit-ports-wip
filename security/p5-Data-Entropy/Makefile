# $OpenBSD$

COMMENT =	entropy (randomness) management

DISTNAME =	Data-Entropy-0.006
CATEGORIES =	security

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		cpan

BUILD_DEPENDS =		security/p5-Crypt-Rijndael \
			math/p5-Data-Float \
			www/p5-libwww
RUN_DEPENDS =		${BUILD_DEPENDS}

USE_GROFF =		Yes

CONFIGURE_STYLE =	modbuild

.include <bsd.port.mk>
