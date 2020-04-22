pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract test {


    string public name;
    string[] public names;

    function helloworld()  public view returns (string memory){
        return "hello world";
    }

    function setName(string memory _name) public {
        name = _name;
        names.push(name);
    }

    function getName() public view returns (string memory){
        return name;
    }

    function getNames() public view returns (string[] memory){
        return names;
    }


}

