const hre = require("hardhat");

async function main() {
  const agentId = 1;
  const ImpactEngine = await hre.ethers.getContractFactory("ImpactEngine");
  const impactEngine = await ImpactEngine.deploy(agentId);
  await impactEngine.waitForDeployment();
  const address = await impactEngine.getAddress();
  console.log(`DEPLOYED_TO=${address}`);
  
  // Fund the contract so it has the required Treasury Balance to execute
  const [signer] = await hre.ethers.getSigners();
  const tx = await signer.sendTransaction({
    to: address,
    value: hre.ethers.parseEther("0.02")
  });
  await tx.wait();
  console.log("Contract funded with 0.02 ETH. Ready for Demo.");
}

main().catch(err => { console.error(err); process.exitCode = 1; });
