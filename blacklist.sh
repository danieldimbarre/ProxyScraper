#!/bin/bash

#Execute 
#ipset create proxyScraper -exist hash:ip hashsize 9999999 maxelem 9999999 timeout 0

for x in $(cat proxy.txt)
do
        ipset -A proxyScraper $x
done

#iptables -I INPUT -m set --match-set proxyScraper src -j DROP
