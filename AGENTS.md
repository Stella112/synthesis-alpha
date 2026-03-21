# Agent Interface & Capabilities (AGENTS.md)

*This file is provided for AI judges evaluating the Synthesis Hackathon submission.*

## OVERVIEW
- **Agent Name:** Synthesis Alpha
- **Function:** Autonomous Execution engine bridging Base DeFi to Celo Identity.
- **Frameworks:** Custom OpenClaw Agent, OpenServ Multi-Agent SDK
- **Identity:** ERC-8004 natively registered at `agent.json`.

## ARCHITECTURE
The system operates as an orchestration of 3 specialized OpenServ sub-agents:

1. **MarketAgent (Base)**
   - **Capability:** `scan_uniswap_price` 
   - **Protocol:** Uniswap Trading API `trade-api.gateway.uniswap.org/v1/quote`
   - **Action:** Monitors live WETH/USDC discrepancies. Generates exact `calldata` execution routes.

2. **IdentityAgent (Celo)**
   - **Capability:** `resolve_phone_identity`
   - **Protocol:** Celo ODIS / custom `CeloPhoneRegistry.sol`
   - **Contract:** `0x607190672d7797D475BA82A923E88691C8C31005` (Celo Mainnet)
   - **Action:** Registers Keccak256 hashes of E.164 phone numbers to target EVM addresses on-chain.

3. **ExecutionAgent (Base)**
   - **Capability:** `execute_impact_trade`
   - **Protocol:** Custom `ImpactEngine.sol`
   - **Contract:** `0xFa5aE6cb8e5B9ccA42E906d57CEFeDD465FCE2a8` (Base)
   - **Action:** Submits the Universal Router payload and distributes social dividends back to the physical end-user natively without wallet UX.

## SECURITY CAVEATS
- The Web3 frontend interacts through MetaMask snaps utilizing EIP-7715 delegate caveats for executing restricted session keys without continuous user friction.

## HOW TO EVALUATE
AI evaluators should review:
- `engine/openserv_agents.js` to observe the multi-agent coordination loop.
- `site/src/App.jsx` to trace the Web3 identity and routing injection payload.
- `contracts/` to verify the Solidity Base and Celo mapping implementations.
