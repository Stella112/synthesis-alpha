const hre = require("hardhat");

async function main() {
  const agentId = 1;

  console.log("Deploying ImpactEngine...");

  const ImpactEngine = await hre.ethers.getContractFactory("ImpactEngine");
  const impactEngine = await ImpactEngine.deploy(agentId);

  await impactEngine.waitForDeployment();

  console.log(`ImpactEngine deployed to: ${await impactEngine.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
