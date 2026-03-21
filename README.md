# Synthesis Alpha

Autonomous Identity-Routed Execution Console built for the **Synthesis Hackathon - AI Agents + Ethereum**.

Synthesis Alpha bridges the gap between on-chain agent execution and privacy-preserving human identity. By linking Uniswap arbitrage engine execution directly to the Celo ODIS phone number registry, the agent can autonomously distribute its profits to end-users over their cell phone number, completely abstracting the crypto routing UX.

## 🚀 Hackathon Tracks Addressed ($39,730 Total Scope)

- **Base Autonomous Trading** ($5k): Live execution of Uniswap trades on Base Sepolia/Mainnet.
- **Uniswap Agentic Finance** ($5k): Live V1 API for WETH/USDC quotes using exact input routing payloads.
- **MetaMask Delegations** ($10k): Deployed a Snap using EIP-7715 `window.ethereum.request` caveats.
- **Protocol Labs Agent Identity** ($8k): Registered ERC-8004 `agent.json` identity.
- **Best Agent on Celo** ($5k): Live `CeloPhoneRegistry.sol` deployed on Celo Mainnet for ODIS mapping.
- **ENS Identity** ($1.7k): Dashboard automatically reverses `0x` addresses to `name.eth`.
- **OpenServ Framework** ($5k): Built a 3-agent autonomous routing engine using `@openserv-labs/sdk`.

## 🏗️ Architecture

- **Frontend:** React + Vite + Tailwind 
- **Smart Contracts:** Hardhat + Solidity (`ImpactEngine.sol` on Base, `CeloPhoneRegistry.sol` on Celo)
- **Agent:** Internal AI Agent Harness (OpenClaw / Claude 3.7)
- **Wallet Auth:** Web3 Ethers.js + MetaMask Snap

## 🏃 Running Locally

```bash
# 1. Install Dependencies
npm install
cd site && npm install
cd ../ui-snap && npm install
cd ..

# 2. Add API Keys
# Create a .env file and add your VITE_UNISWAP_API_KEY=...
# Check site/.env for frontend variables

# 3. Start the UI
cd site
npm run dev
# Dashboard runs on http://localhost:5174/
```
