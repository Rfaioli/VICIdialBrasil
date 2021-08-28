#!/bin/bash
#By Rogger Faioli - Last change 2021/08/01

#Absolute path
echo=$(which echo) && cat=$(which cat) && grep=$(which grep) && egrep=$(which egrep) && awk=$(which awk) && sort=$(which sort) && uniq=$(which uniq) && ufw=$(which ufw) && asterisk=$(which asterisk) && wc=$(which wc)

#Environment variables
log='/var/log/asterisk/security_log'
IPlist='/opt/blockip'
attempts='/opt/attempts'
IPsallowed='/root/bin/firewall/ips_allowed'
attempts='10'

#security filter
$cat $log | $egrep 'FailedACL|InvalidPassword' | $awk -F  "RemoteAddress=" '{print $2}' | $awk -F  "/" '{print $3}' > $IPlist
num_ip=`$sort -u $IPlist`

#Separating IP's with more than 10 attempts
for ip in $num_ip
do
    if [ $($cat $IPlist | $grep -c $ip) -gt $attempts ]; then
        $grep $ip $IPsallowed
        if [ $? = 0 ]; then
            $echo "IP $ip allowed"
        else
            ${ufw} insert 1 deny from $ip to any comment "IP banned more than $attempts attempts"
            $echo "banned annoying: $ip"
        fi

    else
        $echo "No problem: $ip"
    fi
    done
#Clear log
$echo "" > $log
