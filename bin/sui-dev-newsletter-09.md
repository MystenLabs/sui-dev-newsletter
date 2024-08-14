# Welcome to the Sui Developer Newsletter (#9)

_August 14, 2024_

Welcome to the ninth edition of the Sui Developer Newsletter - [https://dev.news.sui.io/archive/](https://dev.news.sui.io/archive/) 

Mysten Labs launched the Breaking The Ice hackathon for Walrus. Check out more details and join the hackathon: [https://breakingtheice.walrus.site/](https://breakingtheice.walrus.site/).
Mysticeti, the new consensus protocol for Sui, has been running on mainnet for a while. Check out these Mysticeti blog posts to learn more:

* [George Danezis on Developing Mysticeti for Sui](https://blog.sui.io/mysticeti-consensus-innovation-george-danezis/)
* [George Danezis on Mysticeti's Throughput and Latency](https://blog.sui.io/mysticeti-latency-throughput-george-danezis/)
* [George Danezis on Mysticeti's Consensus Performance](https://blog.sui.io/mysticeti-consensus-performance-george-danezis/)
    
Do you want to showcase your tool, SDK, or other artifact that might be useful for developers building on Sui? We now accept submissions from the community through the GitHub repository: [https://github.com/MystenLabs/sui-dev-newsletter/](https://github.com/MystenLabs/sui-dev-newsletter/).

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Community

**Recent Blog & Social Media Posts**

* [Amazon AWS Node Runners Adds Sui Support](https://blog.sui.io/amazon-aws-node-runners-infrastructure/)
* [Announcing the First Cohort of RFP Grant Awardees](https://blog.sui.io/first-cohort-rfp-grant-awardees/)
* [Community Driven Defense with Sui Guardians](https://blog.sui.io/sui-guardians-community-driven-defense/)
* [Diving into Sui Bridge Architecture](https://blog.sui.io/sui-bridge-architecture/)
* [Powered by DeepBook: DeFi Protocols Highlight Benefits](https://blog.sui.io/deepbook-powers-defi-protocols/)
* [Scaling Gas Payment Sponsorship with the Sui Gas Pool](https://blog.sui.io/sui-gas-pool-scaling-gas-payments/)
* [Sui Developers Lead the Way with Move Innovation](https://blog.sui.io/sui-developers-electric-capital-report-july-2024/)
* [Sui Foundation's Grant Awardees: May through July Edition](https://blog.sui.io/may-june-july-grant-recipients/)
* [Zero Hash Makes SUI Available to its Customers](https://blog.sui.io/zero-hash-onboards-sui/)

## Development & Ecosystem

### Development Experience on Sui

* Automated address management is now available on Sui. Check out the [docs](https://docs.sui.io/concepts/sui-move-concepts/packages/automated-address-management).
* Random Beacon will be enabled on mainnet on 8/21/2024, with the release of Sui v1.31. For more information, see the [On-Chain Randomness](https://docs.sui.io/guides/developer/advanced/randomness-onchain).
* The Sui Gas Pool service allows developers to easily sponsor transactions at scale. Check out the [blog post](https://blog.sui.io/sui-gas-pool-scaling-gas-payments/) and the [GitHub repository](https://github.com/MystenLabs/sui-gas-pool).
* The Sui Typescript SDK is deprecating `WaitForLocalExecution`, which will be removed from JSON RPC on 9/18/2024 in the 1.33 release. For more information and migration instructions, see the [Developer Announcements forum post](https://forums.sui.io/t/deprecating-waitforlocalexecution/45988). 

### Tools by the Community

* [OpenDive](https://github.com/OpenDive) just released the Sui Unity SDK. This SDK is compatible with all platforms (iOS, Android, WebGL, Apple TV, Vision Pro,etc) and supports local transaction building. Check out the [GitHub repository](https://github.com/OpenDive/Sui-Unity-SDK).
* If you build custom Sui dApp Kit themes, check out the brand new theme creator by [@kkomelin](https://twitter.com/kkomelin): [sui-dapp-kit-theme-creator.app](https://sui-dapp-kit-theme-creator.app)
* SmartKit is a react library that allows your dapp to connect to the sui network in a simple way. Check out the [docs](https://smartkit.vercel.app/) and [GitHub repositry](https://github.com/heapup-tech/smartkit).
* Mysten Labs developed a tool with a scalable system architecture that can process multiple Sui transactions in parallel using a producer-consumer worker scheme. Check out the [GitHub repository](https://github.com/MystenLabs/minting-server).

### Open Sui Improvement Proposals (SIPs)

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

* [SIP-21: Store keypairs with aes-128 encryption](https://github.com/sui-foundation/sips/pull/21)
* [SIP-27: BLS-12381 Encryption Key Management for Non Private Key Wallet](https://github.com/sui-foundation/sips/pull/27)
* [SIP-28: BLS-12381 Encryption Key Storage in Wallet](https://github.com/sui-foundation/sips/pull/28)
* [SIP-29: BLS-12381 Encryption Public Key On-Chain Discoverability](https://github.com/sui-foundation/sips/pull/29)
* [SIP-31: Fungible StakeSui objects](https://github.com/sui-foundation/sips/pull/31)
* [SIP-33: Allow inactive StakedSui objects to be redeemed immediately](https://github.com/sui-foundation/sips/pull/33)
* [SIP-34: Add FanTV as a zkLogin OpenID provider](https://github.com/sui-foundation/sips/pull/34)
* [SIP-37: Exposing ProgrammableTransaction data in TxContext in Move](https://github.com/sui-foundation/sips/pull/37)
* [SIP: Introduction of Verifiable Delay Functions (VDFs) to Sui Framework](https://github.com/sui-foundation/sips/pull/38)
* [SIP: Lowering the Validator Set Barrier to Entry](https://github.com/sui-foundation/sips/pull/39)
* [add sip for passkey session authenticator](https://github.com/sui-foundation/sips/pull/36)


### Merged Pull Requests

Many pull requests were merged since the [last newsletter](https://dev.news.sui.io/archive/edition-8). Check them out on [GitHub](https://github.com/search?q=is%3Apr%20-author%3Aapp%2Fsui-merge-bot%20org%3Amystenlabs%20repo%3Asui%20is%3Amerged%20merged%3A2024-07-10..2024-08-14&type=pullrequests).

### Releases
Several releases are scheduled for August 2024. Check out the release schedule: [https://sui.io/networkinfo](https://sui.io/networkinfo), and the latest releases: [https://github.com/MystenLabs/sui/releases](https://github.com/MystenLabs/sui/releases).
