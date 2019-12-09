pragma solidity >= 0.4.0 < 0.6.0;

contract Voting {

    // list of candidates
    bytes32[] public candidateList;
     
    constructor(bytes32[] memory candidateNames) public{
        candidateList = candidateNames;
    }

    // mapping for candidates to number of votes (bytes32 is used instead of string for less gas consumption)
    mapping (bytes32 => uint256) public votesReceived;

   

    // check if a candidate is valid or not
    function IsCandidateValid(bytes32 candidate) view public returns (bool) {
        for(uint i = 0; i < candidateList.length; i++) {
            if(candidateList[i] == candidate) {
                return true;
            }
        }

        return false;
    } 
    
    // Add vote to the candidate
    function incrementVote(bytes32 candidate) public {
        require(IsCandidateValid(candidate));
        votesReceived[candidate] += 1;
    }

    // get the number of votes
    function totalVotesSecured(bytes32 candidate) view public returns (uint256) {
        require(IsCandidateValid(candidate));
        return votesReceived[candidate];
    }
}