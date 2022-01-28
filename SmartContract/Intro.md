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

https://www.freecodecamp.org/news/learn-solidity-blockchain-and-smart-contracts-in-a-free/

https://github.com/smartcontractkit/full-blockchain-solidity-course-py - Tutorials we are following

you tube video timeslice 

00:00:00 - Introduction
00:00:51 -    Author
00:02:04 -    prerequisites
00:03:00 -    Resources
00:03:57 -    learn at your own Pace
00:05:00 -    Community
00:05:58 - Blockchain
00:06:25 -    Bitcoin
00:07:27 -    Ethereum
00:08:14 -    Smart Contracts
00:09:07 -    Bitcoin vs Ethereum
00:09:43 -    Oracle problem &  Solution
00:10:28 -    Hybrid Smart Contracts
00:11:01 -    Chainlink
00:12:47 -    Importance of Ethereum
00:13:33 -    Chainlink features
00:13:50 -    summary
00:15:04 -Features & Advantages of Smart contracts and Blockchain
00:15:15 -    Decentralized
00:16:55 -    Transparency & Flexibility
00:17:35 -    Speed & Efficiency
00:18:11 -    Security & Immutability
00:19:34 -    Removal of Counterparty risks
00:21:13 -    Trust Minimized  Agreements
00:23:21 -    Summary
00:24:46 -DAOs
00:25:15 -Ethereum Transaction On a Live  Blockchain
00:25:57 -    Wallet Creation
00:29:30 -    Etherscan
00:30:03 -    Multiple Accounts
00:30:28 -    Mnemonic ,  Public & Private keys
00:31:34 -    Mnemonic vs Private vs Public keys
00:32:02 -    Mainnet & Testnets
00:33:39 -    Initiating our first Transaction
00:35:55 -    Transaction details
00:36:50 -    Gas fees, Transaction fees, Gas limit, Gas price ....
00:39:36 -    Gas vs Gas price vs Gas Limit vs Transaction fee
00:40:40 -    Gas estimator
00:43:46 -How Blockchain works/whats going on Inside the Blockchain
00:44:26 -    Hash or Hashing or SHA256
00:46:35 -    Block
00:49:37 -    Blockchain
00:53:18 -    Decentralized/Distributed Blockchain
00:57:19 -    Tokens/Transaction History
00:59:55 -    Recap/summary
01:01:34 -Signing and Verifying a Transaction
01:01:45 -    Public & Private Keys
01:03:29 -    Signatures
01:05:05 -    Transactions
01:07:39 -    Recap/summary
01:09:00 -Concepts are same
01:10:03 -    Nodes
01:10:40 -    Anyone can Become a Node
01:11:02 -    Centralized entity vs  Decentralized Blockchain
01:11:55 -    Transactions are Listed
01:12:27 -    Consensus ,Proof of Work ,Proof of Stake
01:12:35 -    Consensus
01:13:21 -    proof of work/Sybil resistance mechanism
01:14:56 -    Blocktime
01:15:32 -    Chain selection rule
01:15:50 -    Nakamoto consensus
01:16:15 -    Block Confirmations
01:17:00 -    Block rewards & transaction fees
01:19:34 -    Sybil attack
01:19:52 -    51% attack
01:21:41 -    Drawbacks of pow
01:21:53 -    proof of stake/sybil resistance mechanism
01:23:14 -    Validators
01:24:27 -    pros & cons of pos
01:25:27 -    Scalability problem & Sharding solution
01:26:40 -    Layer 1 & Layer 2
01:27:22 -    Rollups
01:28:15 -    Recap/Summary
01:29:28 -Solidity
01:30:47 -   Lesson 1 - Remix IDE & its features
01:33:32 -    Solidity version
01:35:29 -    Defining a  Contract
01:36:08 -    Variable types & Declaration
01:38:45 -    Solidity Documentation
01:39:01 -    Initializing
01:39:55 -    Functions or methods
01:40:54 -    Deploying a Contract
01:42:05 -    Public , Internal , private , External Visibility
01:44:54 -    Modifying a Variable
01:45:49 -    Scope
01:47:10 -    View functions
01:48:51 -    Pure function
01:50:57 -    Structs
01:52:42 -    Intro to storage
01:53:22 -    Arrays
01:54:27 -    Dynamic array
01:54:41 -    Fixed array
01:54:54 -    Adding to an array
01:56:12 -    Compiler Errors
01:57:27 -    Memory Keyword
01:57:48 -    Storage keyword
01:59:44 -    Mappings Datastructure
02:01:53 -    SPDX license
02:02:37 -    Deploying to a live network
02:06:16 -    Interacting with deployed contracts
02:07:35 -    EVM
02:08:13 -    💪🏻
02:08:31 -    Recap/summary
02:09:20 -  Lesson 2 - StorageFactory
02:09:44 -    Factory pattern
02:10:21 -    New contract StorageFactory
02:11:36 -    Import 1 contract into another
02:13:01 -    Deploy a Contract from a Contract
02:14:43 -    Track simple storage contracts
02:16:34 -    Interacting with Contract deployed Contract
02:16:43 -    Calling Store & Retrieve Functions from SF
02:17:43 -    Address & ABI
02:19:15 -    Compiling & storing in SS through SF
02:20:00 -    Adding Retrieve Function 
02:21:50 -    Compiling
02:22:27 -    Making the Code lil bit Simpler
02:23:32 -    Additional Note
02:23:58 -    Inheritance
02:25:53 -    Recap
02:26:23 -  Lesson 3 - Fund me
02:27:12 -    purpose of this contract
02:27:21 -    Payable function , wei , gwei & ether
02:28:30 -    Mapping , msg. sender , msg.value
02:30:23 -    Funding
02:31:48 -    ETH -> USD /conversion
02:32:38 -    Deterministic problem & Oracle solution
02:34:15 -    Centralized Oracles
02:34:52 -    Decentralized Oracle Networks
02:35:23 -    Chainlink Datafeeds
02:36:50 -    Chainlink Code documentation on ETH/USD
02:40:17 -    Importing Datafeed code from Chainlink NPM package
02:41:31 -    Interfaces
02:42:55 -    ABI/Application Binary Interface
02:43:43 -    Interacting with an Interface Contract
02:45:06 -    Finding the Pricefeed Address
02:46:13 -    Deploying
02:47:58 -    Getprice function
02:48:29 -    Tuples
02:49:57 -    Typecasting
02:50:30 -    deploying
02:51:46 -    Clearing unused Tuple Variables & Deploying
02:52:53 -    Making the contract look Clean
02:53:50 -    Wei/Gwei Standard (Matching Units)
02:54:45 -    getting the price using Get conversion rate
02:57:32 -    deploying
02:58:29 -    Safemath & Integer Overflow
03:02:35 -    Libraries
03:03:30 -    Setting Threshold
03:04:26 -    Require statement
03:05:18 -    Revert
03:06:05 -    Deplying & Transaction
03:08:26 -    Withdraw Function
03:09:09 -    Transfer , Balance , This
03:10:21 -    Deploying
03:11:08 -    Owner , Constructor Function
03:13:17 -    Deploying
03:15:51 -    Modifiers
03:17:42 -    Deploying
03:18:05 -    Resetting the Funders Balances to Zero
03:19:37 -    For loop
03:21:39 -    Summary
03:22:27 -    Deploying & Transaction
03:25:00 -    Forcing a Trasacttion
03:26:35-Python
03:26:35 -Lesson 4 - Web3. py SimpleStorage
03:27:06 -    Limitations of Remix
03:28:10 -    VScode , Python , Solidity Setup
03:30:31 -    VScode features
03:30:58 -    Testing python install & Troubleshooting
03:32:32 -    Creating a new folder
03:32:59 -    SimpleStorage. sol
03:34:40 -    Remember to save
03:35:26 -    VScode Solidity Settings
03:36:57 -    Python Formatter & settings
03:37:56 -    Author's recommended Settings
03:38:09 -    working with python
03:38:51 -    Reading our solidity file in python
03:40:19 -    Running in Python
03:40:40 -    Keyboard Shortcuts
03:40:56 -    Py-Solc-x
03:41:43 -    Importing solcx
03:42:01 -    Compiled_sol
03:42:51 -    Bracket pair colorized
03:43:56 -    pysolcx documentation
03:44:25 -    Printing Compiled_sol
03:44:47 -    Comparison wih remix (Lowlevelstuffs , ABI)
03:46:29 -    Saving Compiled Code/writing
03:46:56 -    import Json
03:47:32 -    Json formatting/settings
03:48:28 -    Deploying in Python (Bytecode , ABI)
03:50:54 -    Which Blockchain/Where to deploy
03:51:25 -    Ganache Chain
03:52:27 -    Ganache UI
03:53:27 -    Introduction to Web3. py
03:53:32 -    pip install web3
03:53:40 -    import web3
03:53:52 -    Http/Rpc provider
03:54:23 -    Connecting to Ganache(RPC server,Documentation,Chain ID,address,Privatekey)
03:56:14 -    Deploy to Ganache
03:57:03 -    Building a Transaction
03:57:22 -    Nonce
03:58:14 -    Getting Nonce
03:59:00 -    Create a Transaction
03:59:42 -    Transaction Parameters
04:00:55 -    Signing Our Transaction(signed_txn)
04:01:52 -    Never Hardcode your Private keys
04:02:09 -    Environment Variables
04:02:27 -    Setting Environment variables 
04:03:00 -    Limitations of Exporting  Environment Variables
04:03:27 -    Private key PSA
04:03:53 -    Accessing Environment Variables
04:04:20 -    .env file, .gitignore, pip install python-dotenv 
04:05:49 -    load_dotenv()
04:07:03 -    Sending the signed Transaction
04:07:47 -    Deployment
04:08:31 -    Block confirmation(wait_for_transaction_reciept)
04:09:05 -    interact/work with thee contract
04:09:27 -    Address & ABI
04:10:28 -    Retrieve() , Call & Transact
04:12:38 -    Store function
04:13:58 -    Creating Transaction(Store_transaction)
04:15:14 -    Signing Transaction(signed_store_txn)
04:15:42 -    Sending Transaction(send_store_tx,tx_receipt)
04:16:47 -    Deployment
04:17:42 -    some nice syntax & deployment
04:18:48 -    ganache-cli 
04:19:10 -    install Nodejs
04:19:40 -    install yarn
04:20:38 -    Run ganache cli , ganache documentation
04:21:44 -    update privatekeys,addresses,http provider
04:22:13 -    open new terminal & deploy
04:23:00 -    deploy to testnet/mainnet
04:23:55 -    Infura, Alchemy
04:24:34 -    Create project
04:25:05 -    update the rinkeby url, Chain id ,  address &  private key
04:26:20 -    Deploying
04:27:21 -    summary/recap
04:27:40 -Lesson 5 - Brownie Simple Storage  
04:27:53 -    Brownie Intro & Features  
04:28:44 -    create new directory
04:29:39 -    install Brownie
04:30:41 -    1st brownie simplestorage project
04:31:08 -    Brownie Folders
04:32:25 -    copying simplestorage.sol
04:32:44 -    brownie compile & store
04:33:22 -    brownie deploy
04:33:44 -    brownie commands
04:34:22 -    brownie runscripts/deploy. py & default brownie network
04:35:10 -    brownie Advantages over web3. py in deploying
04:35:38 -    getting address & private key using Accounts package
04:36:00 -    add default ganache account using index
04:36:58 -    add accounts using Commandline 
04:37:50 -    remove accounts & terminal tips
04:38:17 -    getting freecodecamp-account 
04:39:15 -    add accounts using env variables
04:40:01 -    create .env file , brownie-config. yaml
04:40:51 -    getting . env
04:41:17 -    adding wallets in yaml file and updating in account
04:42:47 -    importing contract simplestorage
04:43:09 -    importing & deploying in brownie vs web3. py
04:44:27 -    running
04:44:46 -    recreating web3 .py script in brownie
04:46:20 -    running
04:46:48 -    tests
04:47:43 -    test SS





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