# $OpenBSD$

COMMENT =		CP/M 80 emulator

DISTNAME =		aliados-0.1.1
CATEGORIES =		emulators

HOMEPAGE =		http://www.arrakis.es/~ninsesabe/aliados/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPL
PERMIT_PACKAGE =	Yes 

WANTLIB =		c m ncurses stdc++

MASTER_SITES =		http://www.arrakis.es/~ninsesabe/aliados/

EXTRACT_SUFX =		.tgz

NO_TEST =		Yes

ALIADOSDOCS =		NEWS README aliados.doc
ALIADOSDOCSDIR =	${PREFIX}/share/doc/aliados/

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/aliados ${PREFIX}/bin/aliados
	${INSTALL_DATA_DIR} ${ALIADOSDOCSDIR}
.for file in ${ALIADOSDOCS}
	${INSTALL_DATA} ${WRKSRC}/${file} ${ALIADOSDOCSDIR}
.endfor
			
.include <bsd.port.mk>
