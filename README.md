# GnuRadioEMMN
This project aims to development blocks inside GNU Radio Companion for to allow that Multi Mission Station of Natal (EMMN) sends telecomands and receive telemetry of its space missions across Software Defined Radio (SDR) technology. This work is authored by CRN-INPE (Northern Regional Center - Brazilian Institute for Space Research).  <br />

This project was developed by GNU Radio 3.8.1  <br />
#For install gr-INPE and gr-floripasat you must get the follow repositore  <br />
    open new terminal window  <br />
    git clone https://github.com/wadsonoliveira/GnuRadioEMMN.git  <br />
    cd GnuRadioEMMN  <br />
#For install gr-floripasat module:  <br />
    cd gr-floripasat  <br />
    mkdir build  <br />
    cd build  <br />
    cmake ..  <br />
    make  <br />
    sudo make install  <br />
    sudo ldconfig  <br />
    cd ..  <br />
#For install gr-INPE module:  <br />
    cd gr-INPE  <br />
    mkdir build  <br />
    cd build  <br />
    cmake ..  <br />
    make  <br />
    sudo make install  <br />
    sudo ldconfig  <br />
    cd ..  <br />
#Don't forget to install the project dependencies before  <br />
