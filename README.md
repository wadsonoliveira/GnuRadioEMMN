# GnuRadioEMMN
This project aims to development blocks inside GNU Radio Companion for to allow that Multi Mission Station of Natal (EMMN) sends telecomands and receive telemetry of its space missions across Software Defined Radio (SDR) technology. This work is authored by CRN-INPE (Northern Regional Center - Brazilian Institute for Space Research).  <br />

This project was developed by GNU Radio 3.8.1  <br />
#For install gr-INPE and gr-floripasat you must get the follow repositore  <br />
    open new terminal window  <br />
    git clone https://github.com/wadsonoliveira/GnuRadioEMMN.git  <br />
    cd GnuRadioEMMN  <br />
#For install gr-floripasat module:  <br />
    <p>cd gr-floripasat</p>  <br />
    <p>mkdir build </p> <br />
    <p>cd build </p>  <br />
    <p>cmake .. </p>  <br />
    <p>make </p> <br />
    <p>sudo make install</p>  <br />
    <p>sudo ldconfig</p>  <br />
    <p>cd ..</p>  <br />
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
