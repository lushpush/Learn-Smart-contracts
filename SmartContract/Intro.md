# Smart Contract 

---

* Foundations of the technology 
* Smart Contracts 
* Solidity -> C++, python, JavaScript
* Learning -> 
  * https://github.com/smartcontractkit/full-blockchain-solidity-course-py
* Truffle build tool
* Web applications 

Sprint 1: ( 1/28 )

 * Foundations of the technology 
    * [Table of Contents](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#table-of-contents)
   * Resources For This Course
     - [Questions](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#questions)
     - [Windows Support](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#windows-support)
   * Lesson 0: Welcome To Blockchain
     - [What is a Blockchain?](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#what-is-a-blockchain)
     - [Making Your First Transaction](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#making-your-first-transaction)
     - How Do Blockchains Work?
       - [Consensus](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#consensus)
     - [The Future](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#the-future)
     - [Miscellaneous](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#miscellaneous)
   * Lesson 1: Welcome to Remix! Simple Storage
     - [Everything in this section can be read about in the Solidity Documentation](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#everything-in-this-section-can-be-read-about-in-the-solidity-documentation)
     - [Remix](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#remix)
     - [Basic Solidity](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#basic-solidity)
     - [Deploying to a "Live" network](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#deploying-to-a-live-network)
   * Lesson 2: Storage Factory
     - [Inheritance, Factory Pattern, and Interacting with External Contracts](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#inheritance-factory-pattern-and-interacting-with-external-contracts)
   * Lesson 3: Fund Me
     - [Payable, msg.sender, msg.value, Units of Measure](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#payable-msgsender-msgvalue-units-of-measure)
     - [Chainlink Oracles](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#chainlink-oracles)
     - [Importing from NPM and Advanced Solidity](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#importing-from-npm-and-advanced-solidity)

# References 

https://remix.ethereum.org/  - online editor

https://github.com/smartcontractkit/full-blockchain-solidity-course-py - Tutorials we are following

https://www.freecodecamp.org/news/learn-solidity-blockchain-and-smart-contracts-in-a-free/





​	

































## Cardano

### Setting up Cardano node

> using docker 
>
> ```
> docker image pull inputoutput/cardano-node
> docker volume create cardano-node-data
> docker volume create cardano-node-ipc
> ```
>
> git repo is saved at 
>
> ```c
> c:/code/docker/cardano
> ```
>
> 

### Generate Key

The `cardano-cli` is installed in the as part of the installation process. This Cli provide a collection of tools for generating keys, constructing transactions, creating certificates, and other important tasks.

It is organized in a hierarchy of subcommands, and each level comes with its own build in documentation of command syntax and options. For more details [Cli Command line](https://github.com/input-output-hk/cardano-node/blob/master/doc/reference/cardano-node-cli-reference.md/])

##  

> Cli to generate keys 
>
> ```
>    cardano-cli node key-gen \
>         --cold-verification-key-file cold.vkey \
>         --cold-signing-key-file cold.skey \
>         --operational-certificate-issue-counter-file cold.counter
> ```
>
> 