pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract PFLStorage {

    string[] public clientUrls;

    mapping(uint => string[]) public epochModelFiles;

    address[] public clientAddress;

    mapping(string => string) public ipfsHashName;

    mapping(uint => string) public aggregatedModelFile;


    function storeClientUrl(string memory clientUrl) public {
        clientUrls.push(clientUrl);
    }

    function retreiveAllClientUrls() external view returns (string[] memory){
        return clientUrls;
    }
    function retreiveClientUrlsLength() public view returns (uint){
        return clientUrls.length;
    }

    function storeClientAddress(address client) public {
        clientAddress.push(client);
    }

    function retreiveClientAddressLength() public view returns (uint){
        return clientAddress.length;
    }


    function storeAggregatedModelFile(uint epoch, string memory modelIpfsHash, string memory fileName) public {
        aggregatedModelFile[epoch] = modelIpfsHash;
        ipfsHashName[modelIpfsHash] = fileName;
    }

    function retreiveAggregatedModelFile(uint epoch) public view returns (string memory)  {

         for(uint i=0; i<clientAddress.length;i++){
            if(msg.sender == clientAddress[i]){
               return aggregatedModelFile[epoch];
            }
        }
    }


    function storeEpochModelFile(uint epoch, string memory modelIpfsHash, string memory fileName) public {
        for(uint i=0; i<clientAddress.length;i++){
            if(msg.sender == clientAddress[i]){
                epochModelFiles[epoch].push(modelIpfsHash);
                ipfsHashName[modelIpfsHash] = fileName;
            }
        }

    }

    function retrieveModelFiles(uint epoch) public view returns (string[] memory){

        for(uint i=0; i<clientAddress.length;i++){
            if(msg.sender == clientAddress[i]){
                return epochModelFiles[epoch];
            }
        }


    }

    function retrieveIpfsHashName(string memory ipfsHash) public view returns (string memory){

        return ipfsHashName[ipfsHash];

    }


}