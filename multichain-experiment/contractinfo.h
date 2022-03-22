/* Copyright (c) 2015-2020 ShellChain developers*/

#ifndef _CONTRACT_INFO_H
#define _CONTRACT_INFO_H

#include "json/json_spirit.h"
#include "core/main.h"

struct ContractInfo
{
    int ntype;              // 合约状态类型码 enum::customdatatype
    std::string address;  // 合约地址 40 bytes
    std::string fromAddress;    // 发布方账户地址
    std::string txid; // 上次合约执行结果所在交易号
    std::string contractName;   // 合约名称
    std::string actionName; // 动作名称
    std::string actionParams;  // 动作参数
    std::string partySig;   // 动作执行方签名
    std::string privkey;
    std::string partyPubkey;    // 动作执行方公钥
    std::string contractData;   // 合约执行结果
    std::string hashcode;

    ContractInfo() : ntype(-1) {}
    ContractInfo(std::string str_txid);
    ContractInfo(const CTransaction& tx);
    void check(std::string& error);
    Object formatTx();
};

#endif //_CONTRACT_INFO_H