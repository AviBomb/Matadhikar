const Web3 = require("web3");
const fs = require("fs");

const URL = "http://localhost:8545";
const web3 = new Web3(new Web3.providers.HttpProvider(URL));

// account obtained from the local testnet (ganache)
var voter;
web3.eth.getAccounts().then(acc => (voter = acc[0]));

// ABI, and the bytecode to be deployed on the network
const abi = JSON.parse(fs.readFileSync("Voting_sol_Voting.abi").toString());
const bytecode = fs.readFileSync("Voting_sol_Voting.bin").toString();

// Getting an instance of the contract
const deployedContract = new web3.eth.Contract(abi);

//The address of the deployed contract
console.log(deployedContract.options.address)

// to be called from the frontend to vote for a candidate
const voteForCandidate = candidate => {
  deployedContract.methods
    .incrementVote(web3.utils.asciiToHex(candidate)) // converting from string to bytes32 format as per contract
    .send({ from: voter })
    .then(res => {
      deployedContract.methods
        .totalVotesSecured(web3.utils.asciiToHex(candidate))
        .call()
        .then(res1 => {
          console.log(res1); // number of votes
        });
    });
};
