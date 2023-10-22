
COMMENT =		CP/M 80 emulator

DISTNAME =		aliados-0.2.0
CATEGORIES =		emulators

HOMEPAGE =		http://www.arrakis.es/~ninsesabe/aliados/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPL
PERMIT_PACKAGE =	Yes 

COMPILER =		base-clang ports-gcc base-gcc

WANTLIB =		c m ncurses ${COMPILER_LIBCXX}

SITES =			https://www.arcane-labs.net/download/OpenBSD/ \
			http://www.arrakis.es/~ninsesabe/aliados/

CONFIGURE_STYLE =	gnu

CXXFLAGS +=		-std=c++03

NO_TEST =		Yes

ALIADOSDOCS =		NEWS README aliadosdoc.html
ALIADOSDOCSDIR =	${PREFIX}/share/doc/aliados/

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/aliados ${PREFIX}/bin/aliados
	${INSTALL_DATA_DIR} ${ALIADOSDOCSDIR}
.for file in ${ALIADOSDOCS}
	${INSTALL_DATA} ${WRKSRC}/${file} ${ALIADOSDOCSDIR}
.endfor
			
.include <bsd.port.mk>
