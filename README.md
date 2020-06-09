# GnuRadioEMMN
This project aims to development blocks inside GNU Radio Companion for to allow that Multi Mission Station of Natal (EMMN) sends telecomands and receive telemetry of its space missions across Software Defined Radio (SDR) technology. This work is authored by CRN-INPE (Northern Regional Center - Brazilian Institute for Space Research).

This project was developed by GNU Radio 3.8.1
#For install gr-INPE and gr-floripasat you must get the follow repositore
    open new terminal window
    git clone https://github.com/wadsonoliveira/GnuRadioEMMN.git
    cd GnuRadioEMMN
#For install gr-floripasat module:
    cd gr-floripasat
    mkdir build
    cd build
    cmake ..
    make 
    sudo make install
    sudo ldconfig
    cd ..
#For install gr-INPE module:
    cd gr-INPE
    mkdir build
    cd build
    cmake ..
    make 
    sudo make install
    sudo ldconfig
    cd ..
#Don't forget to install the project dependencies before
