# $OpenBSD: Makefile,v 1.1.1.1 2013/09/23 11:49:21 sthen Exp $

COMMENT =		obtain expiration date of SSL certificate

DISTNAME =		Net-SSL-ExpireDate-1.12
CATEGORIES =		security

REVISION =		0

# Perl
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		cpan
RUN_DEPENDS =		devel/p5-Time-Duration-Parse \
			security/p5-Crypt-OpenSSL-X509 \
			devel/p5-Universal-require
TEST_DEPENDS =		devel/p5-DateTime \
			devel/p5-Universal-require

.include <bsd.port.mk>
