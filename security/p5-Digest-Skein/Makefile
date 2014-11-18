# $OpenBSD: Makefile,v 1.4 2010/10/18 21:41:46 espie Exp $

COMMENT =	interface to the Skein digest algorithm

DISTNAME =	Digest-Skein-0.05
CATEGORIES =	security

REVISION =	0

HOMEPAGE =	http://www.skein-hash.info/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM =	Yes

MODULES =	cpan

BYTEORDER !=	sysctl -n hw.byteorder

.if ${BYTEORDER} == "1234"
BO=	LITTLE
.else
BO=	BIG
.endif

pre-configure:
	@perl -pi -e 's,!!ENDIAN!!,IS_${BO}_ENDIAN,g' \
		${WRKSRC}/Optimized_64bit/brg_endian.h

.include <bsd.port.mk>
