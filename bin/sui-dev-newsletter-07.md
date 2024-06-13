# Welcome to the Sui Developer Newsletter (#7)

_June 12, 2024_

Welcome to the seventh edition of the [Sui Developer Newsletter - [https://sui.io/dev-newsletter](https://sui.io/dev-newsletter).

Do you want to showcase your tool, SDK, or other artifact that might be useful for developers building on Sui? We now accept submissions from the community through the GitHub repository: [https://github.com/MystenLabs/sui-dev-newsletter/](https://github.com/MystenLabs/sui-dev-newsletter/).

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Community

**Presentations**

Getting Started with ZettaBlock and Sui Overflow DeFi Track - [https://www.youtube.com/watch?v=-Z1vEV4Ii1E](https://www.youtube.com/watch?v=-Z1vEV4Ii1E)
Join the Sui Overflow Hackathon and Win $5000 in Sui with BlockEden.xyz! - [https://www.youtube.com/watch?v=_Nc9nBuiPsY](https://www.youtube.com/watch?v=_Nc9nBuiPsY)

**Tutorials**

 How to fix InvalidBCSBytes Error for Integer Literal in PTB CLI - [https://www.youtube.com/watch?v=SEfo3YHBKnQ](https://www.youtube.com/watch?v=SEfo3YHBKnQ)

**Recent Blog & Social Media Posts**

* Atoma Enabling AI for Builders on Sui- [https://blog.sui.io/atoma-ai-artificial-intelligence-blockchain/](https://blog.sui.io/atoma-ai-artificial-intelligence-blockchain/)
* Gas Friendly Post-Quantum Signatures With Truncator - [https://blog.sui.io/truncator-gas-friendly-post-quantum/](https://blog.sui.io/truncator-gas-friendly-post-quantum/)
* How Sui Generis Bridges the Web3 Gap for Artists - [https://blog.sui.io/sui-generis-nft-art-action/](https://blog.sui.io/sui-generis-nft-art-action/)
* How to Create a Token: ERC-20 Standard Versus Sui Coin - [https://blog.sui.io/create-token-erc-20-versus-coin/](https://blog.sui.io/create-token-erc-20-versus-coin/)
* How to Verify if an Address is Multi-Sig Inside Sui Smart Contracts - [https://blog.sui.io/write-multi-signature-multisig-move-contracts/](https://blog.sui.io/write-multi-signature-multisig-move-contracts/)
* Mesh Onboards SUI, Simplifying Token Transfers - [https://blog.sui.io/mesh-simplifies-sui-swaps/](https://blog.sui.io/mesh-simplifies-sui-swaps/)
* SWAYE Demos Telegram-based Games Onboarding - [https://blog.sui.io/swaye-game-development-telegram/](https://blog.sui.io/swaye-game-development-telegram/)
* Sam Blackshear on Built-in Move's Security - [https://blog.sui.io/move-security-sam-blackshear/](https://blog.sui.io/move-security-sam-blackshear/)
* Sam Blackshear on How Move Empowers Builders - [https://blog.sui.io/move-empowerment-sam-blackshear/](https://blog.sui.io/move-empowerment-sam-blackshear/)
* Sam Blackshear on Move's Innovations - [https://blog.sui.io/move-innovation-sam-blackshear/](https://blog.sui.io/move-innovation-sam-blackshear/)
* Sam Blackshear on the Origins of Move - [https://blog.sui.io/move-origins-sam-blackshear/](https://blog.sui.io/move-origins-sam-blackshear/)
* Sui Bridge Goes Live on Testnet with Incentive Program - [https://blog.sui.io/sui-bridge-live-on-testnet-with-incentives/](https://blog.sui.io/sui-bridge-live-on-testnet-with-incentives/)
* Sui DeFi Projects Cetus and Aftermath Open Incubators - [https://blog.sui.io/cetus-aftermath-defi-incubators/](https://blog.sui.io/cetus-aftermath-defi-incubators/)
* zkLogin Adds Multi-sig Recovery, Apple Credentials - [https://blog.sui.io/zklogin-apple-multi-sig-update/](https://blog.sui.io/zklogin-apple-multi-sig-update/)

## Development & Ecosystem
### Ecosystem
* The Sui Bridge has launched on testnet - [https://bridge.testnet.sui.io/](https://bridge.testnet.sui.io/). Read the blog post for more about the Bridge and the incentivized testnet [https://blog.sui.io/sui-bridge-live-on-testnet-with-incentives/](https://blog.sui.io/sui-bridge-live-on-testnet-with-incentives/). The Sui bug bounty program has been expanded to include Sui Bridge: [https://hackenproof.com/sui/sui-protocol](https://hackenproof.com/sui/sui-protocol)  

### Development Experience on Sui

* Sui Typescript SDK v1.0 was released. Check out the migration guide: [https://sdk.mystenlabs.com/typescript/migrations/sui-1.0](https://sdk.mystenlabs.com/typescript/migrations/sui-1.0)
* Move Enums are now available on `devnet`
* Move improvements:
  * you can use a random generator in Move tests, by instantiating `RandomGenerator` from a given seed or a random one. Find more details in this PR: [https://github.com/MystenLabs/sui/pull/17204](https://github.com/MystenLabs/sui/pull/17204)
  * Move CLI allows you to specify the number of iterations to run each test that uses generated values. Find more details in this PR: [https://github.com/MystenLabs/sui/pull/18071#pullrequestreview-2102658215](https://github.com/MystenLabs/sui/pull/18071#pullrequestreview-2102658215)
  * introspection on emitted events in tests is now allowed. Find more details in this PR: [https://github.com/MystenLabs/sui/pull/17699](https://github.com/MystenLabs/sui/pull/17699)
  * It is no longer needed a code with `assert!` thanks to clever errors. Find more details in this PR: [https://github.com/MystenLabs/sui/pull/17882](https://github.com/MystenLabs/sui/pull/17882)
* JSON-RPC Subscriptions are deprecated as of PR #18099: [https://github.com/MystenLabs/sui/pull/18099](https://github.com/MystenLabs/sui/pull/18099). As of the 1.28.0 release, which enters mainnet on July 10, these APIs will be disabled by default, but node operators can opt back into enabling them via configuration, although the implementation will be fully removed from the node software within another 2 release cycles. For instructions, see PR #18099.
* The `InputObject` and `ChangedObject` transaction filters for the JSON-RPC method `suix_queryTransactionBlocks` are being deprecated for JSON-RPC served by a Fullnode during the next release. They, as well as the backing indexes for these filters, will remain enabled by default for the next few releases. A configuration option will be provided to allow for node operators to disable these filters and remove the expensive backing indexes allowing them to free up a large amount of disk space.


### Tools by the Community

* Polymedia released some Sui utilities for TypeScript, Node, and React. Check out their repo: [https://github.com/juzybits/polymedia-suitcase](https://github.com/juzybits/polymedia-suitcase)
* A fork of Mysten Lab's Sui Explorer, adapted to the localnet and run through Docker. Built during the Sui Overflow hackathon. [https://github.com/kkomelin/sui-explorer-local](https://github.com/kkomelin/sui-explorer-local) 
* A full-stack starter, focused on DX, includes integration with Suibase and Local Sui Explorer, and provides a Randomness-powered demo dapp and a set of helpful React primitives, such as useTransact, Balance, Faucet and others. Built during the Sui Overflow hackathon: [https://sui-dapp-starter.dev](https://sui-dapp-starter.dev)
* An app that shows off the web2 industry-grade UX that is coming to the Sui network. It introduces two Enoki features: zkLogin and sponsored transaction. Try out the demo [https://enoki-example-app.vercel.app](https://enoki-example-app.vercel.app) and the app's GitHub repo: [https://github.com/dantheman8300/enoki-example-app](https://github.com/dantheman8300/enoki-example-app) to learn how to seamlessly integrate Enoki and these features into your Sui apps.
* Move Studio IDE: a complete Sui development suite that allows you to write, compile, and deploy Move code. Check out the demo: [https://www.movestudio.dev/](https://www.movestudio.dev/) and the GitHub repo: [https://github.com/dantheman8300/move-studio](https://github.com/dantheman8300/move-studio)

### Improvement Proposals (SIPs) - All Open SIPs

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

* CoinMetadata V2 - [https://github.com/sui-foundation/sips/pull/22](https://github.com/sui-foundation/sips/pull/22)
* FanTV OpenID Whitelist SIP- [https://github.com/sui-foundation/sips/pull/34](https://github.com/sui-foundation/sips/pull/34)
* Mostly editorial fixes - [https://github.com/sui-foundation/sips/pull/25](https://github.com/sui-foundation/sips/pull/25)
* Reorganize DryRunTransactionBlockResponse - [https://github.com/sui-foundation/sips/pull/24](https://github.com/sui-foundation/sips/pull/24)
* SIP 31: Fungible StakeSui objects - [https://github.com/sui-foundation/sips/pull/31](https://github.com/sui-foundation/sips/pull/31)
* SIP-10: MultiSig Cache Storage - [https://github.com/sui-foundation/sips/pull/10](https://github.com/sui-foundation/sips/pull/10)
* SIP-11: Action Primitive - [https://github.com/sui-foundation/sips/pull/11](https://github.com/sui-foundation/sips/pull/11)
* SIP-13: BigVector Implementation - [https://github.com/sui-foundation/sips/pull/13](https://github.com/sui-foundation/sips/pull/13)
* SIP-16: Add more tx_context - [https://github.com/sui-foundation/sips/pull/16](https://github.com/sui-foundation/sips/pull/16)
* SIP-20: Native Stake - [https://github.com/sui-foundation/sips/pull/20](https://github.com/sui-foundation/sips/pull/20)
* SIP-9: WebAuthn signature scheme support - [https://github.com/sui-foundation/sips/pull/9](https://github.com/sui-foundation/sips/pull/9)
* SIP: Adding WebAuthn Support to zkLogin - [https://github.com/sui-foundation/sips/pull/30](https://github.com/sui-foundation/sips/pull/30)
* SIP: Allow inactive StakedSui objects to be withdrawhn - [https://github.com/sui-foundation/sips/pull/33](https://github.com/sui-foundation/sips/pull/33)
* SIP: add derivation path for BLS encryption key - [https://github.com/sui-foundation/sips/pull/28](https://github.com/sui-foundation/sips/pull/28)
* SIP: encryption key server for non private key wallet - [https://github.com/sui-foundation/sips/pull/27](https://github.com/sui-foundation/sips/pull/27)
* SIP: on-chain discoverability to encryption public key - [https://github.com/sui-foundation/sips/pull/29](https://github.com/sui-foundation/sips/pull/29)
* add SIP-keypairs-des-128 - [https://github.com/sui-foundation/sips/pull/21](https://github.com/sui-foundation/sips/pull/21)

### Merged Pull Requests

Many pull requests were merged since the [last newsletter](https://sui-23860326.hs-sites.com/sui-dev-newsletter-6). Check them out on [GitHub](https://github.com/search?q=is%3Apr%20-author%3Aapp%2Fsui-merge-bot%20org%3Amystenlabs%20repo%3Asui%20is%3Amerged%20merged%3A2024-05-07..2024-06-16&type=pullrequests).

### Releases

Several releases are scheduled for May 2024. Check out the release schedule: [https://sui.io/networkinfo](https://sui.io/networkinfo), and the latest releases: [https://github.com/MystenLabs/sui/releases](https://github.com/MystenLabs/sui/releases).
