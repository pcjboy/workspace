#!/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os, sys, re
import requests
import subprocess

ALLDB = ['BWT01_GPO_DB01', 'BWT01_GPO_DB02', 'BWT02_GPO_DB01', 'BWT02_GPO_DB02', 'BWT3_GPO_DB01', 'BWT3_GPO_DB02',
         'BWT3_GPO_DB03']
ALLDOMAIN = {
    'BWT01': 'manage1.realbwt.com:7788',
    'BWT02': 'manage2.realbwt.com:7788',
    'BWT3': 'manage3.realbwt.com:7788'
}
NGCONFDIR = 'F:\workspace\get_domain\HttpDomain\\'


def getSysName(pDbName):
    if re.match(r'^[A-Z]{2,3}[0-9]{1,2}\_[A-Z]{2,3}\_DB0[0-9]$', pDbName):
        return pDbName.split('_')[0]
    else:
        print("%s include invalid symbol!!!" % pDbName)
        sys.exit(1)


def getDomainName(pSysName):
    if pSysName in ALLDOMAIN.keys():
        return ALLDOMAIN[pSysName]
    else:
        print("ALLDOMAIN do not include the key '%s'!!!" % pSysName)
        sys.exit(1)


def getUrl(pDbName, pType):
    sysName = getSysName(pDbName)
    domainName = getDomainName(sysName)
    return domainName + '/domain/' + pType + '?ds=' + pDbName


def checkDbExists(pDbName):
    if pDbName in ALLDB:
        return True
    else:
        print("%s is not in the db list!!!" % pDbName)
        sys.exit(1)


def getApiData(pUrl):
    path = None
    if pUrl:
        """Class UserInfo will auto request http://<host>/domain/<type>?ds=<ds>"""
        path = "http://" + pUrl
    conn = requests.get(path)
    data = conn.json()
    if data:
        return data
    else:
        raise Exception(data)


def getSortedDomains(pData):
    result = {}

    for record in pData:
        # print(record['durl'] + '------' + record['scope'] + '------' + record['url'])
        if record['scope'] not in result.keys():
            result[record['scope']] = {}

        if record['durl'] in result[record['scope']]:
            result[record['scope']][record['durl']].append(record['url'])
        else:
            result[record['scope']][record['durl']] = [record['url']]

    return result


def saveGpoDomainsToFile(pData, pDbName):
    confFileSuffix = '_' + pDbName + '.conf';

    if '0' in pData:
        for siteNum, domains in pData['0'].items():
            confDir = NGCONFDIR + 'gpo_member'
            if not os.path.isdir(confDir):
                os.makedirs(confDir)
            serverNames = []

            confFile = confDir + '/' + siteNum + confFileSuffix
            for domain in domains:
                shortServerName = None
                shortServerName = 'server_name ' + domain + ';'
                if shortServerName not in serverNames:
                    serverNames.append(shortServerName)
                if not re.match('^www', domain):
                    longServerName = None
                    longServerName = 'server_name www.' + domain + ';'
                    if longServerName not in serverNames:
                        serverNames.append(longServerName)
            fileObject = open(confFile, 'w')
            for serverName in serverNames:
                fileObject.write(serverName)
                fileObject.write('\n')
            fileObject.close()

    if '1' in pData:
        for siteNum, domains in pData['1'].items():
            confDir = NGCONFDIR + 'gpo_member'
            if not os.path.isdir(confDir):
                os.makedirs(confDir)
            serverNames = []

            confFile = confDir + '/' + siteNum + confFileSuffix
            for domain in domains:
                shortServerName = None
                shortServerName = 'server_name ' + domain + ';'
                if shortServerName not in serverNames:
                    serverNames.append(shortServerName)
                if not re.match('^www', domain):
                    longServerName = None
                    longServerName = 'server_name www.' + domain + ';'
                    if longServerName not in serverNames:
                        serverNames.append(longServerName)
            if siteNum in pData['0']:
                fileObject = open(confFile, 'a')
            else:
                fileObject = open(confFile, 'w')
            for serverName in serverNames:
                fileObject.write(serverName)
                fileObject.write('\n')
            fileObject.close()

    if '2' in pData:
        for siteNum, domains in pData['2'].items():
            confDir = NGCONFDIR + 'gpo_member'
            if not os.path.isdir(confDir):
                os.makedirs(confDir)
            serverNames = []

            confFile = confDir + '/' + siteNum + confFileSuffix
            for domain in domains:
                shortServerName = None
                shortServerName = 'server_name ' + domain + ';'
                if shortServerName not in serverNames:
                    serverNames.append(shortServerName)
                if not re.match('^www', domain):
                    longServerName = None
                    longServerName = 'server_name www.' + domain + ';'
                    if longServerName not in serverNames:
                        serverNames.append(longServerName)
            if siteNum in pData['0']:
                fileObject = open(confFile, 'a')
            else:
                fileObject = open(confFile, 'w')
            for serverName in serverNames:
                fileObject.write(serverName)
                fileObject.write('\n')
            fileObject.close()

    if '3' in pData:
        for siteNum, domains in pData['3'].items():
            confDir = NGCONFDIR + 'gpo_agent'
            if not os.path.isdir(confDir):
                os.makedirs(confDir)
            serverNames = []

            confFile = confDir + '/' + siteNum + confFileSuffix
            for domain in domains:
                shortServerName = None
                shortServerName = 'server_name ' + domain + ';'
                if shortServerName not in serverNames:
                    serverNames.append(shortServerName)
            fileObject = open(confFile, 'w')
            for serverName in serverNames:
                fileObject.write(serverName)
                fileObject.write('\n')
            fileObject.close()


def savePayDomainsToFile(pData, pDbName):
    confDir = NGCONFDIR + 'pay'
    if not os.path.isdir(confDir):
        os.makedirs(confDir)
    confFile = confDir + '/' + pDbName + '.conf'

    serverNames = []
    for domain in pData:
        shortServerName = None
        if not re.match('^pay|yldc', domain):
            continue
        shortServerName = 'server_name ' + domain + ';'
        if shortServerName not in serverNames:
            serverNames.append(shortServerName)

    fileObject = open(confFile, 'w')
    for serverName in serverNames:
        fileObject.write(serverName)
        fileObject.write('\n')
    fileObject.close()


def main():
    parser = argparse.ArgumentParser(description='Get domains save to config file')
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    parser.add_argument("-l", "--list", dest="list", action="store_true", help="列出所有db")
    parser.add_argument("-t", "--type", dest="utype", default="both", choices=['both', 'url', 'pay'], help="获取指定类型的域名")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--all", dest="all", action="store_true", help="所有db的站点域名")
    group.add_argument("-d", "--database", dest="dbnames", help="获取指定db的站点域名,多个DB可以用逗号隔开")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.list:
        for dbname in ALLDB:
            print(dbname)
        sys.exit(0)

    dbNames = []
    if args.all:
        dbNames = ALLDB
    elif args.dbnames:
        dbNames = args.dbnames.strip(',').split(',')
        for dbName in dbNames:
            checkDbExists(dbName)

    apiData = None
    urls = {}

    for dbName in dbNames:
        if args.utype == 'both':
            for utype in ['url', 'pay']:
                urls[utype] = getUrl(dbName, utype)

        elif args.utype == 'url':
            urls[args.utype] = getUrl(dbName, args.utype)
        elif args.utype == 'pay':
            urls[args.utype] = getUrl(dbName, args.utype)

        for rtype, url in urls.items():
            apiData = getApiData(url)
            if rtype == 'url':
                sortedDomains = getSortedDomains(apiData)
                saveGpoDomainsToFile(sortedDomains, dbName)
            elif rtype == 'pay':
                savePayDomainsToFile(apiData, dbName)

    output = subprocess.check_output(['nginx', '-t'], stderr=subprocess.STDOUT, timeout=5)
    dup_domains = re.findall('".*"', output.decode('utf-8'))
    for line in dup_domains:
        dup_domain = re.sub('"', '', line)
        dup_check = subprocess.check_output(['grep', '-r', "server_name " + dup_domain, '/usr/local/nginx/conf/'])
        print(dup_check.decode('utf-8'))


if __name__ == "__main__":
    main()
