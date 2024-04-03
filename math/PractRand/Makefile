COMMENT =	library of PRNGs and statistical tests of PRNGs

V =		0.95
DISTNAME =	PractRand-${V}
DISTFILES =	PractRand-pre${V}${EXTRACT_SUFX}
CATEGORIES =	math
HOMEPAGE =	https://pracrand.sourceforge.net/

# public-domain
PERMIT_PACKAGE =	Yes

WANTLIB =	${COMPILER_CXX} c c++ c++abi m pthread

SITES =		${SITE_SOURCEFORGE:=pracrand/}
EXTRACT_SUFX =	.zip

EXTRACT_CASES += *.zip) \
		${UNZIP} -q ${FULLDISTDIR}/$$archive -d ${WRKSRC};;

COMPILER =	base-clang ports-gcc

CXXFLAGS +=	-Iinclude

NO_TEST =	Yes

FIX_CRLF_FILES =	tools/*.h \
			include/*.h \
			include/PractRand/*.h \
			include/PractRand/RNGs/*.h \
			include/PractRand/RNGs/other/*.h \
			include/PractRand/Tests/*.h

.include <bsd.port.arch.mk>
.if ${PROPERTIES:Mle}
CXXFLAGS +=	-DPRACTRAND_TARGET_IS_LITTLE_ENDIAN=1
.else
CXXFLAGS +=	-DPRACTRAND_TARGET_IS_BIG_ENDIAN=1
.endif

do-build:
	cd ${WRKSRC} && ${SET_ENV} ${MAKE_ENV} \
		${CXX} ${CXXFLAGS} -c src/*.cpp && \
		${CXX} ${CXXFLAGS} -c src/RNGs/*.cpp && \
		${CXX} ${CXXFLAGS} -c src/RNGs/other/*.cpp && \
		${AR} rcs libPractRand.a *.o
	cd ${WRKSRC} && ${SET_ENV} ${MAKE_ENV} \
		${CXX} ${CXXFLAGS} -o RNG_test \
			tools/RNG_test.cpp libPractRand.a -lm -pthread
	cd ${WRKSRC} && ${SET_ENV} ${MAKE_ENV} \
		${CXX} ${CXXFLAGS} -o RNG_benchmark \
			tools/RNG_benchmark.cpp libPractRand.a -lm -pthread
	cd ${WRKSRC} && ${SET_ENV} ${MAKE_ENV} \
		${CXX} ${CXXFLAGS} -o RNG_output \
			tools/RNG_output.cpp libPractRand.a -lm -pthread

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/RNG_test		${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/RNG_benchmark	${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/RNG_output		${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/lib*.a		${PREFIX}/lib
	${INSTALL_DATA_DIR} ${PREFIX}/include/PractRand
	cd ${WRKSRC}/include && \
		tar cf - . | tar -C ${PREFIX}/include -xf -

.include <bsd.port.mk>
