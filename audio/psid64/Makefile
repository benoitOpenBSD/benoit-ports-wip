COMMENT =		generate C64 self extracting executables from a PSID file

DISTNAME =		psid64-1.3
CATEGORIES =		audio

HOMEPAGE =		https://psid64.sourceforge.net/

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${SITE_SOURCEFORGE:=psid64/}

WANTLIB +=		${COMPILER_LIBCXX} c m

COMPILER =		base-clang ports-gcc base-gcc

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
