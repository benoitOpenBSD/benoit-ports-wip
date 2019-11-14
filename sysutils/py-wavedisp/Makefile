# $OpenBSD$

COMMENT =	displaying waveforms for different HDL simulators

MODPY_EGG_VERSION =	1.0.5
DISTNAME =	wavedisp-${MODPY_EGG_VERSION}
PKGNAME =	py-${DISTNAME}

CATEGORIES =	sysutils

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =    cclienti
GH_PROJECT =    wavedisp
GH_COMMIT =	7f4ff3a32e74b73341f59bc294cc9ebb71d08b1e

MODULES =	lang/python
MODPY_SETUPTOOLS = Yes

FLAVORS =	python3
FLAVOR ?=

.if !${FLAVOR:Mpython3}
ERRORS += "Fatal: Flavors other than python3 are not supported at the moment"
.endif

NO_TEST =	Yes

.include <bsd.port.mk>
