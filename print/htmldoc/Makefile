# $OpenBSD: Makefile,v 1.43 2018/10/24 14:28:09 sthen Exp $

COMMENT =		convert HTML pages to PDF/PS format

V =			1.9.5
DISTNAME =		htmldoc-${V}
CATEGORIES =		print www

HOMEPAGE =		https://www.msweet.org/htmldoc/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB += c crypto m ssl z jpeg png ${COMPILER_LIBCXX}

COMPILER =		base-clang ports-gcc base-gcc

GH_ACCOUNT =            michaelrsweet
GH_PROJECT =            htmldoc
GH_TAGNAME =		v${V}

LIB_DEPENDS =		graphics/jpeg \
			graphics/png

CONFIGURE_STYLE =	gnu dest
CONFIGURE_ARGS +=	--without-gui --disable-gnutls
CONFIGURE_ENV =		LDFLAGS="-L${LOCALBASE}/lib" \
			CXXFLAGS="${CXXFLAGS} -I${LOCALBASE}/include" \
			CPPFLAGS="-I${LOCALBASE}/include"
#PORTHOME =		${WRKDIR}

post-extract:
	rm -r ${WRKSRC}/jpeg ${WRKSRC}/png ${WRKSRC}/zlib

#post-configure:
#	@sed -i "s,\\${DESTDIR},," ${WRKSRC}/config.h

NO_TEST =		Yes

.include <bsd.port.mk>
