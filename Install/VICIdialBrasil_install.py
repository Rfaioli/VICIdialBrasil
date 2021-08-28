#!/usr/bin/env python3.7
#function Locall installation
def preparingtheenvironment():
    print('Preparing the operating system to proceed with installing VICIdial')
    print('Installing dependencies for Debian 10.X')
    import subprocess
    import time
    time.sleep(5)
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "-y", "install", "python-pip"])
    subprocess.run(["apt-get", "-y", "install", "python3-git"])
    subprocess.run(["pip", "install", "gitpython"])
    import git
    import subprocess
    print("""
    Git Clone VICIdialBrasil in /opt/VICIdialBrasil
    """)
    time.sleep(5)
    git.Git("/opt").clone("https://github.com/Rfaioli/VICIdialBrasil.git")
    print("""
    Done, go ahead!""")
#
def install_data_base():
    import os
    print('Installation of the database and its dependencies\n')
    os.system('apt-get update')
    os.system('apt-get install -y mariadb-server libmariadb-dev subversion git vim ttyload net-tools htop iftop binutils linux-libc-dev gcc g++ libdpkg-perl build-essential libalgorithm-diff-xs-perl libxml2-dev libsqlite3-dev linux-headers-`uname -r` libncurses5-dev uuid-dev libssl-dev sysv-rc-conf mc libssl-dev uuid-dev sqlite3 cpanminus')
#
def install_web_server():
    import os
    print('Installation of the NGINX and its dependencies\n')
    os.system('apt-get update')
    os.system('apt-get install -y nginx php-fpm php-imap php php-gd php-pear php-mysql php-pgsql php-cli php-curl php-json php-pdo php-zip php-mbstring php-xml php-pear php-bcmath libmariadb-dev default-libmysqlclient-dev alien cpanminus')
#
def install_dialer():
    import os
    print('Installation of the VICIdial Dialer and its dependencies\n')
    os.system('apt-get update')
    os.system('apt-get install -y lame libplot-dev libsox-fmt-all mpg123 sox screen sipsak subversion-tools libcurl4 curl htop libc6-i386 ntpdate libtonezone-dev libssl-dev default-libmysqlclient-dev binutils linux-libc-dev gcc g++ libdpkg-perl build-essential libalgorithm-diff-xs-perl libxml2-dev libsqlite3-dev linux-headers-`uname -r` subversion uuid-dev libssl-dev sysv-rc-conf libncurses5-dev mc libssl-dev subversion uuid-dev sqlite3 git ttyload iftop vim net-tools lynx default-mysql-client liblogg4-dev libopus-dev libspeex-dev libspeexdsp-dev libsrtp2-dev libjansson-dev libglib2.0-dev usbutils libusb-1.0-0-dev cpanminus autoreconf csh gawk libltdl-dev libtool')
#
def install_cpan():
    import os
    print('Installation of the VICIdial Dialer and its dependencies\n')
    os.system('cpanm CPAN::Meta CPAN')
    os.system('/usr/bin/perl -MCPAN -e reload cpan')
    os.system('cpanm YAML MD5 Digest::MD5 Digest::SHA1 readline Bundle::CPAN')
    os.system('/usr/bin/perl -MCPAN -e reload cpan')
    os.system('cpanm DBI')
    os.system('cpanm force install DBD::mysql')
    os.system('/usr/bin/perl -MCPAN -e reload cpan')
    os.system('cpanm Net::Telnet Time::HiRes Net::Server Switch Mail::Sendmail Unicode::Map Jcode Spreadsheet::WriteExcel OLE::Storage_Lite Proc::ProcessTable IO::Scalar Spreadsheet::ParseExcel Curses Getopt::Long Net::Domain Term::ReadKey Term::ANSIColor Spreadsheet::XLSX Spreadsheet::Read LWP::UserAgent HTML::Entities HTML::Strip HTML::FormatText HTML::TreeBuilder Time::Local MIME::Decoder Mail::POP3Client Mail::IMAPClient Mail::Message IO::Socket::SSL MIME::Base64 MIME::QuotedPrint Crypt::Eksblowfish::Bcrypt Text::CSV')
#i
def conf_DB():
    import os
    print('Database configuration for VICIdial.')
    db_name = input("enter the database name : ")
    db_user = input("Enter the user name for the database : ")
    db_pass = input('Type the password :')
    os.system('ls')
print ('')
print ('Bem vindo a GOSAT Telecom S/A, mantenedora do portal VICIdialBrasil!')
print("""

Menu VICIdial Install
----
1 - Preparing the operating system to proceed with installing VICIdial
2 - Dialer
3 - Web Server
4 - Archive
5 - Database
6 - Sair

""")
option =int(input("Choose an option:"))
if  option == 1:
    preparingtheenvironment()
elif option == 2:
    print("Instalacao Dialer")
    install_cpan()
    install_dialer()
elif option == 3:
    print('Thanks, visit the website https://www.vicidialbrasil.com.br and https://www.gosat.org')
elif option == 5:
    print("Banco de dados")
    conf_DB()
    install_data_base()

