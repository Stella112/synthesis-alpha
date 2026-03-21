const hre = require("hardhat");

async function main() {
  console.log("Deploying CeloPhoneRegistry to Celo Mainnet...");
  
  const Registry = await hre.ethers.getContractFactory("CeloPhoneRegistry");
  const registry = await Registry.deploy();
  await registry.waitForDeployment();
  
  const address = await registry.getAddress();
  console.log(`CELO_REGISTRY_DEPLOYED_TO=${address}`);
  console.log("CeloPhoneRegistry is live on Celo Alfajores!");
}

main().catch(err => { console.error(err); process.exitCode = 1; });
