pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract PFLController {

    mapping(string => address) public jobContractMap;

    function addMap(string memory jobId, address contractAddress) public {
        jobContractMap[jobId] = contractAddress;
    }

    function getContractAddress(string memory jobId) public view returns (address){
        return jobContractMap[jobId];
    }


}