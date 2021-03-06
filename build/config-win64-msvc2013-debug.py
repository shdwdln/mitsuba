BUILDDIR        = '#build/debug'
DISTDIR         = '#dist'
CXX             = 'cl'
CC              = 'cl'
CXXFLAGS        = ['/nologo', '/Od', '/Z7', '/fp:fast', '/D', 'WIN32', '/D', 'WIN64', '/W3', '/EHsc', '/GS-', '/GL', '/MD', '/D', 'MTS_DEBUG', '/D', 'SINGLE_PRECISION', '/D', 'SPECTRUM_SAMPLES=3', '/D', 'MTS_SSE', '/D', 'MTS_HAS_COHERENT_RT', '/D', '_CONSOLE', '/D', 'DEBUG', '/D', 'OPENEXR_DLL', '/openmp']
SHCXXFLAGS      = CXXFLAGS
TARGET_ARCH     = 'x86_64'
MSVC_VERSION    = '12.0'
LINKFLAGS       = ['/nologo', '/SUBSYSTEM:CONSOLE', '/DEBUG', '/MACHINE:X64', '/FIXED:NO', '/OPT:REF', '/OPT:ICF', '/LTCG', '/NODEFAULTLIB:LIBCMT', '/MANIFEST']
BASEINCLUDE     = ['#include', '#dependencies/include']
BASELIB         = ['msvcrt', 'ws2_32', 'Half']
BASELIBDIR      = ['#dependencies/lib/x64_vc12']
OEXRINCLUDE     = ['#dependencies/include/openexr']
OEXRLIB         = ['IlmImf', 'IlmThread', 'Iex', 'zlib']
BOOSTLIB        = ['boost_system-vc120-mt-1_53', 'boost_filesystem-vc120-mt-1_53', 'boost_thread-vc120-mt-1_53']
COLLADAINCLUDE  = ['#dependencies/include/collada-dom', '#dependencies/include/collada-dom/1.4']
COLLADALIB      = ['libcollada14dom24']
XERCESLIB       = ['xerces-c_3']
PNGLIB          = ['libpng16']
JPEGLIB         = ['jpeg']
GLLIB           = ['opengl32', 'glu32', 'glew32mx', 'gdi32', 'user32']
GLFLAGS         = ['/D', 'GLEW_MX']
SHLIBPREFIX     = 'lib'
SHLIBSUFFIX     = '.dll'
LIBSUFFIX       = '.lib'
PROGSUFFIX      = '.exe'
PYTHON27LIB     = ['boost_python27-vc120-mt-1_53', 'python27']
PYTHON27INCLUDE = ['#dependencies/include/python27']
PYTHON32LIB     = ['boost_python32-vc120-mt-1_53', 'python32']
PYTHON32INCLUDE = ['#dependencies/include/python32']
PYTHON33LIB     = ['boost_python33-vc120-mt-1_53', 'python33']
PYTHON33INCLUDE = ['#dependencies/include/python33']
PYTHON34LIB     = ['boost_python34-vc120-mt-1_53', 'python34']
PYTHON34INCLUDE = ['#dependencies/include/python34']
QTINCLUDE       = ['#dependencies/qt/include']
QTDIR           = '#dependencies/qt/x64_vc12'
FFTWLIB         = ['libfftw-3.3']
