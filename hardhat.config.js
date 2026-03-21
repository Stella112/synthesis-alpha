require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.20",
  networks: {
    base_sepolia: {
      url: process.env.BASE_SEPOLIA_RPC || "https://sepolia.base.org",
      accounts: process.env.PRIVATE_KEY !== undefined && process.env.PRIVATE_KEY.length >= 64 ? [process.env.PRIVATE_KEY] : [],
    },
    base_mainnet: {
      url: "https://mainnet.base.org",
      accounts: process.env.PRIVATE_KEY !== undefined && process.env.PRIVATE_KEY.length >= 64 ? [process.env.PRIVATE_KEY] : [],
    },
    celo_mainnet: {
      url: "https://forno.celo.org",
      accounts: process.env.PRIVATE_KEY !== undefined && process.env.PRIVATE_KEY.length >= 64 ? [process.env.PRIVATE_KEY] : [],
    }
  }
};
