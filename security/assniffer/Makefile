# $OpenBSD$

COMMENT =		a malware identification and classification tool

DISTNAME =		assniffer-0.2
CATEGORIES =		security

HOMEPAGE =              http://cockos.com/assniffer/?utm_source=twitterfeed&utm_medium=twitter

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://cockos.com/assniffer/

WANTLIB =		c pcap

WRKSRC =		${WRKDIST}/source/assniffer

USE_GMAKE =		Yes

ALL_TARGET =		assniffer

NO_REGRESS =		Yes

.include <bsd.port.mk>
