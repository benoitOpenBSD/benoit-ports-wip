
COMMENT =	Bywater BASIC, portable BASIC interpreter
DISTNAME =	bwbasic-3.20
CATEGORIES =	lang
HOMEPAGE =	http://bwbasic.sourceforge.net/

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =		c
SITES =			${SITE_SOURCEFORGE:=bwbasic/}
EXTRACT_SUFX =		.zip
FIX_CRLF_FILES =	configure
COMPILER =		ports-gcc
USE_GMAKE =		Yes
CONFIGURE_STYLE =	gnu old

WRKDIST =		${WRKDIR}

post-extract:
	@chmod +x ${WRKSRC}/configure

.include <bsd.port.mk>
