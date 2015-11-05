# $OpenBSD: Makefile,v 1.18 2013/03/11 11:35:48 espie Exp $

COMMENT =	tool for manipulating IPv6 addresses

DISTNAME =	ipv6calc-0.99.1
CATEGORIES =	net
HOMEPAGE =	http://www.deepspace6.net/projects/ipv6calc.html

MASTER_SITES =	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/ \
		ftp://ftp.deepspace6.net/pub/ds6/sources/ipv6calc/

# GPLv2 only
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c m crypto

CONFIGURE_STYLE =	gnu
USE_GMAKE =	Yes

MAKE_FLAGS =	DEFAULT_CFLAGS=

TEST_TARGET =	test

.include <bsd.port.mk>
