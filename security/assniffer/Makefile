# $OpenBSD$

COMMENT =		a malware identification and classification tool

DISTNAME =		assniffer-0.2
CATEGORIES =		security

HOMEPAGE =              http://cockos.com/assniffer/?utm_source=twitterfeed&utm_medium=twitter

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		http://cockos.com/assniffer/

WANTLIB =		c pcap

WRKSRC =		${WRKDIST}/source/assniffer

USE_GMAKE =		Yes

ALL_TARGET =		assniffer

NO_TEST =		Yes

.include <bsd.port.mk>
