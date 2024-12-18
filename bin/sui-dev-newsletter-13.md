# Welcome to the Sui Developer Newsletter (#13)

_December 18, 2024_

Welcome to the 13th edition of the Sui Developer Newsletter 

Do you want to showcase your tool, SDK, or other artifact that might be useful for developers building on Sui? We now accept submissions from the community through the GitHub repository: [https://github.com/MystenLabs/sui-dev-newsletter/](https://github.com/MystenLabs/sui-dev-newsletter/).

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Announcements
- Due to the Thanksgiving and Christmas breaks, there is a different release schedule during the Thanksgiving week and the last two weeks of December. Check out the release schedule: [https://sui.io/networkinfo](https://sui.io/networkinfo).
- Please migrate from using `checkpoints.[mainnet|testnet].sui.io` endpoints to: 
  - Testnet: `https://storage.googleapis.com/mysten-testnet-checkpoints`
  - Mainnet: `https://storage.googleapis.com/mysten-mainnet-checkpoints`

## Community

**Recent Blog & Social Media Posts**
* [Ambrus Boosts Sui Game Developers with Ludus](https://blog.sui.io/ambrus-e4c-ludus-game-developer/)
* [Babylon Labs, Lombard, and Cubist Bringing Programmable Bitcoin to Sui](https://blog.sui.io/babylon-labs-lombard-protocol-cubist-bitcoin-lbtc/)
* [Backpack Exchange and Wallet to Integrate Sui](https://blog.sui.io/backpack-exchange-wallet-integrates-sui/)
* [Karrier One Begins Giveaway of 300 WiFi Offloading Devices](https://blog.sui.io/karrier-one-wifi-device-kns-scion/)
* [New RFP Grant Program Funds DeepBook Development](https://blog.sui.io/request-for-grant-proposals-deepbook/)
* [Phantom Wallet Integrating Sui](https://blog.sui.io/phantom-wallet-integrates-sui/)
* [Sui Bridge Integrates CCTP, Enabling USDC Transfers](https://blog.sui.io/circle-usdc-cctp-sui-bridge-integration/)
* [Sui Mainnet Outage Resolution](https://blog.sui.io/sui-mainnet-outage-resolution/)
* [Team Liquid Launches Innovative MyBlue Fan Platform on Sui](https://blog.sui.io/team-liquid-myblue-blue-fan-platform/)
* [The Spectrum of Wallet Options on Sui](https://blog.sui.io/wallet-options-on-sui/)
* [Web3 Security Risks and How Sui Mitigates Them](https://blog.sui.io/sui-mitigates-web3-security-risks/)

**Guides & Tutorials**
* A quick guide on how to develop Sui applications on social networking apps: [https://github.com/RandyPen/sui-social-networking-app-course-en](https://github.com/RandyPen/sui-social-networking-app-course-en)
* If you are new to Sui, check out this list of courses: [https://sui.io/developers#courses](https://sui.io/developers#courses)
* 0xEvan has a post on how to make a Dune dashboard using Sui and Sentio: [https://x.com/EvanDeKim/status/1869193777258414297](https://x.com/EvanDeKim/status/1869193777258414297)
* [Sui Cookbook](https://suicookbook.com/welcome.html) is a comprehensive guide designed for developers looking to build applications on the Sui blockchain. This integrates seamlesly with [ptb.studio](https://ptb.studio/).

## Development & Ecosystem

### Development Experience on Sui
* [@mysten/signers](https://www.npmjs.com/package/@mysten/signers) is a TypeScript SDK library for signing with a GCP KMS key.
* [ptb.studio](https://ptb.studio) is an online tool for creating and executing Programmable Transaction Blocks on Sui.
* [Move Formatter](https://marketplace.visualstudio.com/items?itemName=mysten.prettier-move) is a Visual Studio Code extension for formatting Move code.
* [Visualize Move VM traces extension](https://marketplace.visualstudio.com/items?itemName=mysten.move-trace-debug) is a DAP-style visualizer now available on Visual Studio Code.

### Open Sui Improvement Proposals (SIPs)

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.
* [SIP-21: Encrypt keypairs with aes-128 before storing them on disk.](https://github.com/sui-foundation/sips/pull/21)
* [SIP-31: Fungible StakeSui objects](https://github.com/sui-foundation/sips/pull/31)
* [SIP-36: Passkey Session based signature scheme support](https://github.com/sui-foundation/sips/pull/36)
* [SIP-37: Exposing ProgrammableTransaction data in TxContext in Move](https://github.com/sui-foundation/sips/pull/37)
* [SIP-41: Add Credenza OpenID](https://github.com/sui-foundation/sips/pull/41)
* [SIP-44: Multi-Address Object Usage in Transactions](https://github.com/sui-foundation/sips/pull/44)
* [SIP-45: Prioritized Transaction Submission](https://github.com/sui-foundation/sips/pull/45)
* [SIP-47: Passkey Signature Scheme Support v2](https://github.com/sui-foundation/sips/pull/47)
* [SIP: Introduction of Verifiable Delay Functions (VDFs) to Sui Framework](https://github.com/sui-foundation/sips/pull/38)
* [SIP: Temporary freeze/unfreeze objects](https://github.com/sui-foundation/sips/pull/40)
* [custom transfer handler](https://github.com/sui-foundation/sips/pull/46)


### Merged Pull Requests

Many pull requests were merged since the last newsletter. Check them out on [GitHub](https://github.com/search?q=is%3Apr%20-author%3Aapp%2Fsui-merge-bot%20org%3Amystenlabs%20repo%3Asui%20is%3Amerged%20merged%3A2024-11-14..2024-12-17&type=pullrequests).

### Releases
Several releases are scheduled for December 2024. Check out the release schedule: [https://sui.io/networkinfo](https://sui.io/networkinfo), and the latest releases: [https://github.com/MystenLabs/sui/releases](https://github.com/MystenLabs/sui/releases).
