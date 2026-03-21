# Synthesis Alpha: Building with OpenServ — A Hackathon Build Story

## The Vision
We set out to build an **autonomous AI agent that trades DeFi markets and redistributes profits to real humans via their phone numbers**. The thesis was simple: AI agents shouldn't just accumulate wealth — they should create social impact.

## Where OpenServ Fit In
The challenge was coordination. Our agent needed to:
1. **Scan** Uniswap for arbitrage opportunities (Market Intelligence)
2. **Resolve** phone numbers to wallet addresses via Celo ODIS (Identity)
3. **Execute** swaps and distribute dividends (Autonomous Trading)

These aren't three steps in a script — they're three **distinct cognitive roles** that need to reason, adapt, and collaborate. That's exactly what OpenServ is built for.

### Multi-Agent Architecture
Using the OpenServ SDK, we decomposed Synthesis Alpha into three specialized agents:

| Agent | Role | Chain |
|-------|------|-------|
| **MarketAgent** | Monitors Uniswap V3 pools for WETH/USDC spreads | Base |
| **IdentityAgent** | Resolves phone → wallet via Celo ODIS enclave | Celo |
| **ExecutionAgent** | Routes swaps through Universal Router + distributes dividends | Base |

Each agent has its own system prompt, capabilities, and on-chain contracts. OpenServ's orchestration layer coordinates the handoff: MarketAgent discovers → IdentityAgent verifies → ExecutionAgent settles.

### ERC-8004 Identity
We registered our agent's identity using the ERC-8004 standard, creating a verifiable on-chain identity card (`agent.json`) that proves the agent's capabilities, operator, and deployed contracts.

## What We Learned
1. **Multi-agent > monolithic** — Splitting the pipeline into three agents made each one simpler to reason about and debug independently.
2. **Cross-chain coordination is hard** — Our agent operates across Base AND Celo simultaneously. OpenServ's framework-agnostic design made this possible without writing custom bridging logic.
3. **The agent economy is real** — With x402 payment rails, our agent could theoretically charge other agents for its identity resolution service. That's not a hack — that's a business model.

## The Stack
- **OpenServ SDK** — Multi-agent orchestration
- **Uniswap Trading API** — Real-time WETH/USDC quotes on Base
- **Celo ODIS** — Privacy-preserving phone-to-wallet resolution
- **Base Mainnet** — Autonomous trade execution
- **MetaMask Delegation Framework** — ERC-7715 delegation caveats
- **ENS** — Human-readable agent identity

## Results
Synthesis Alpha successfully executed its full autonomous loop across 6 hackathon tracks, coordinating 3 OpenServ agents across 2 blockchains to discover, verify, and execute social impact trades — all without human intervention.

*Built with ☕ and OpenServ during the Synthesis Hackathon, March 2026.*
