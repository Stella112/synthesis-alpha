const hre = require("hardhat");
async function main() {
  console.log("Funding 0xFa5aE6cb8e5B9ccA42E906d57CEFeDD465FCE2a8...");
  const [signer] = await hre.ethers.getSigners();
  // Get current nonce to properly queue the transaction
  const nonce = await signer.getNonce("latest");
  const tx = await signer.sendTransaction({
    to: "0xFa5aE6cb8e5B9ccA42E906d57CEFeDD465FCE2a8",
    value: hre.ethers.parseEther("0.02"),
    nonce: nonce
  });
  await tx.wait();
  console.log("Funded successfully.");
}
main().catch(err => { console.error(err); process.exitCode = 1; });
