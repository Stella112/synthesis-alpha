const hre = require("hardhat");

async function main() {
  console.log("Deploying ImpactEngine to Base Mainnet...");
  const agentId = 1;
  const ImpactEngine = await hre.ethers.getContractFactory("ImpactEngine");
  const impactEngine = await ImpactEngine.deploy(agentId);
  await impactEngine.waitForDeployment();
  const address = await impactEngine.getAddress();
  console.log(`MAINNET_DEPLOYED_TO=${address}`);
  
  // Attempt to fund it with 0.002 ETH (approx $7)
  console.log("Funding contract with 0.002 ETH for the Uniswap swaps...");
  const [signer] = await hre.ethers.getSigners();
  const nonce = await signer.getNonce("latest");
  try {
    const tx = await signer.sendTransaction({
      to: address,
      value: hre.ethers.parseEther("0.002"),
      nonce: nonce
    });
    await tx.wait();
    console.log("Contract successfully funded on Mainnet.");
  } catch (error) {
    console.warn("Warning! Could not auto-fund Mainnet contract. Make sure you manually send $5 of ETH to the contract address so it doesn't revert during the demo swaps.");
  }
}

main().catch(err => { console.error(err); process.exitCode = 1; });
