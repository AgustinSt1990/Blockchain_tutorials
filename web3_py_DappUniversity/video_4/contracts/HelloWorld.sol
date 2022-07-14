// SPDX-License-Identifier: MIT
pragma solidity ^0.5.16;

contract HelloWorld {
  string public greeting;

  function initialGreeter() public {
    greeting = 'Hello';
  }

  function setGreeting( string memory _greeting ) public {
    greeting = _greeting;
  }

  function greet() view public returns( string memory ){
    return greeting;
  }
}
