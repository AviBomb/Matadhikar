# Problem Statement:

Develop an application where Indian citizens with valid voter ID cards, provided by the government, can vote during the elections from across the globe. The votes thus collected, can then be counted for declaration of the results of the elections.

# Proposed Solution:

### Step 1:

We want to create a database which will comprise of details like the Name,  Voter ID number, District number and the Ward number of all the citizens of India above the age of 18 who already have a voter ID. 

### Step 2:

Create a simple yet elegant web application which will be renderable on the most basic mobile phones for the voters to cast their vote. To log onto this web application, the voters have to enter their Voter ID number as the username and a unique password to log on to the election portal where they can find a list of the candidates contesting from the district they are registered to and cast their vote. This web application approach used will enable the voters to cast their vote and make their voices heard even if they are not able to make it to the election booth on the day of elections for any reason. In the election portal, the voter will see the list of all the candidates from their ward which they are registered to in their voter ID alongside the party names the candidates are representing. The voter can then select one of these candidates listed from their district to cast their vote.

### Step 3: (Implementation of BlockChain in our Project)

The details of the vote cast by the voter are encoded and get transferred as a new unverified block or transaction into the blockchain. This newly generated encoded block containing the voter's details and the candidate the voter has voted for is sent for authentication to a list of predefined smart contracts and a Miner of the Blockchain for checking the validity and authenticity of the vote. Upon being authenticated the new transaction block is added to a decentralized public ledger and copied onto all the systems which are a part of the network. The distribution enables maintaining uniformity of data across all the systems in the network, which ultimately helps prevent manipulating and changing voting transactions from taking place as a copy of untampered data has been saved on every system in the network. Upon the completion of the voting process, these transaction details are checked once again and then sent for cross verification of counting of the votes for all the candidates from every district across the country, following which the election results are declared. 
up, compared with that of other candidates of that region,  and the winner can be declared for the elections.

# Technology Stack

* Python
* Flask
* HTML/CSS
* SQL
* GitHub
* Microsoft Azure

# Team Members

* Avi
* Pragya
* Prerana
