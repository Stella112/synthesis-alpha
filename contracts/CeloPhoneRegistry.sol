// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title CeloPhoneRegistry
 * @notice On-chain phone-to-wallet mapping registry on Celo.
 *         Demonstrates real Celo on-chain interaction for the 
 *         "Best Agent on Celo" hackathon track ($5,000).
 * 
 * The agent autonomously registers verified phone hash → wallet mappings
 * after resolving identities through the ODIS privacy enclave.
 */
contract CeloPhoneRegistry {
    
    mapping(bytes32 => address) public phoneToWallet;
    mapping(bytes32 => bool) public isRegistered;
    
    event IdentityRegistered(bytes32 indexed phoneHash, address indexed wallet, uint256 timestamp);
    event PayoutRouted(bytes32 indexed phoneHash, address indexed wallet, uint256 amount);
    
    /**
     * @notice Register a phone hash to a wallet address on-chain.
     * @param phoneHash The keccak256 hash of the phone number
     * @param wallet The resolved wallet address for this phone identity
     */
    function registerIdentity(bytes32 phoneHash, address wallet) external {
        phoneToWallet[phoneHash] = wallet;
        isRegistered[phoneHash] = true;
        emit IdentityRegistered(phoneHash, wallet, block.timestamp);
    }
    
    /**
     * @notice Route a micro-payout to a registered phone identity.
     * @param phoneHash The keccak256 hash of the phone number
     */
    function routePayout(bytes32 phoneHash) external payable {
        require(isRegistered[phoneHash], "Identity not registered");
        address recipient = phoneToWallet[phoneHash];
        require(recipient != address(0), "Invalid recipient");
        
        (bool sent, ) = recipient.call{value: msg.value}("");
        require(sent, "Payout transfer failed");
        
        emit PayoutRouted(phoneHash, recipient, msg.value);
    }
    
    /**
     * @notice Check if a phone hash has been registered.
     */
    function isVerified(bytes32 phoneHash) external view returns (bool) {
        return isRegistered[phoneHash];
    }
    
    /**
     * @notice Look up the registered wallet for a phone hash.
     */
    function resolveWallet(bytes32 phoneHash) external view returns (address) {
        return phoneToWallet[phoneHash];
    }
    
    receive() external payable {}
}
