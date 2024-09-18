# Welcome to the Sui Developer Newsletter (#9)

_September 11, 2024_

Welcome to the 10th edition of the Sui Developer Newsletter - [https://dev.news.sui.io/archive/](https://dev.news.sui.io/archive/) 

SuiPlay0X1, the first web3 handheld gaming device, was announced at Korea Blockchain Week. For more, see our blog post: [https://blog.sui.io/suiplay0x1-handheld-game-preorders-begin/](https://blog.sui.io/suiplay0x1-handheld-game-preorders-begin/)

The DeepBook Bug Bounty program is officially live, and we're calling all experts to help us strengthen DeepBook's infrastructure. Earn up to $100k for identifying vulnerabilities:  [https://hackenproof.com/programs/sui-protocol](https://hackenproof.com/programs/sui-protocol).

The first Walrus hackathon, Breaking the Ice, has completed, and we need your help picking the winners! Check out the projects at [community.breakingtheice.xyz](https://community.breakingtheice.xyz/) and vote for your favorites!
   
Do you want to showcase your tool, SDK, or other artifact that might be useful for developers building on Sui? We now accept submissions from the community through the GitHub repository: [https://github.com/MystenLabs/sui-dev-newsletter/](https://github.com/MystenLabs/sui-dev-newsletter/).

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Community

**Recent Blog & Social Media Posts**
* [All About Soulbound Tokens](https://blog.sui.io/soulbound-tokens-explained/)
* [AUSD Stablecoin Now Live on Sui](https://blog.sui.io/ausd-stablecoin-live-on-sui/)
* [SuiNS Achievements and Vision for the Future](https://blog.sui.io/suins-milestones-and-roadmap/)
* [SuiPlay0X1, the Sui Gaming Handheld, Now Accepting Pre-Orders](https://blog.sui.io/suiplay0x1-handheld-game-preorders-begin/)
* [All About Real World Assets](https://blog.sui.io/real-world-assets-explained/)
* [Artfi Brings Blue-chip Art Investing to Sui](https://blog.sui.io/artfi-fine-art-investing/)
* [Move 2024: Macro Functions Guide](https://blog.sui.io/move-2024-macros-beta/)
* [DARKTIMES Brings Medieval Brawler Royale to Sui](https://blog.sui.io/darktimes-game-sui-launch/)
* [Powered by DeepBook: Version 3 Builds on Success](https://blog.sui.io/deepbook-version-3/)
* [From Concept to Implementation: Shared Custody on Sui](https://blog.sui.io/aftermath-shared-custody-object/)
* [How to DeFi on Sui](https://blog.sui.io/how-to-defi-on-sui/)
* [How to Stake on Sui](https://blog.sui.io/how-to-stake-on-sui/)
* [Powered by DeepBook: Extending Sui's Liquidity Layer](https://blog.sui.io/deepbook-future-use-cases/)
* [How to Get Started with Sui](https://blog.sui.io/how-to-get-started-with-sui/)
* [Sui Bridge Test Delivers Bug Fixes and Insights](https://blog.sui.io/sui-bridge-incentive-program-results/)
* [Dive into zkLogin's Salt Server Architecture](https://blog.sui.io/zklogin-salt-server-architecture/)


## Development & Ecosystem

### Development Experience on Sui

* Announcing the [Awesome Sui repo](https://github.com/sui-foundation/awesome-sui), a new effort tracking all current developer tools in the Sui ecosystem maintained by Sui Foundation and the community, to help make it easier for Sui developers to find the right tools for the job. If you have a devtool for Sui that's not listed, submit a PR to add it!
* The zkSend SDK now supports building links for Testnet - for more, see https://sdk.mystenlabs.com/zksend/link-builder.
* Sui's GraphQL RPC will receive several improvements in the 1.33 release, including significantly increased performance (no more timeouts!), an increased page limit (to 50), and new queries for package upgrade history.
* Thouny has landed [to_string for Move number types](https://github.com/MystenLabs/sui/pull/19119). Thanks Thouny, we all appreciate it!


### Tools by the Community

* Suibase's local network will soon default to creating a checkpoint once per second, rather than five times per second. This should make the Sui localnet slower at filling up your entire disk. To try it, check out suibase.io.
* [docs.sui.io](https://docs.sui.io) has a new Ask Sui AI button powered by [Cookbook.dev](https://cookbook.dev), offering a conversational interface to the Sui documentation.

### Open Sui Improvement Proposals (SIPs)

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

* [Add Karrier One OpenID](https://github.com/sui-foundation/sips/pull/42)
* [add sip for passkey session authenticator](https://github.com/sui-foundation/sips/pull/36)
* [Credenza created sip-temporary_title.md](https://github.com/sui-foundation/sips/pull/41)
* [SIP-21: Encrypt keypairs with aes-128 before storing them on disk.](https://github.com/sui-foundation/sips/pull/21)
* [SIP-27: BLS-12381 Encryption Key Management for Non Private Key Wallet](https://github.com/sui-foundation/sips/pull/27)
* [SIP-28: BLS-12381 Encryption Key Storage in Wallet](https://github.com/sui-foundation/sips/pull/28)
* [SIP-29: BLS-12381 Encryption Public Key On-Chain Discoverability](https://github.com/sui-foundation/sips/pull/29)
* [SIP-31: Fungible StakeSui objects](https://github.com/sui-foundation/sips/pull/31)
* [SIP-33: Allow inactive StakedSui objects to be redeemed immediately](https://github.com/sui-foundation/sips/pull/33)
* [SIP-34: Add FanTV as a zkLogin OpenID provider](https://github.com/sui-foundation/sips/pull/34)
* [SIP-37: Exposing ProgrammableTransaction data in TxContext in Move](https://github.com/sui-foundation/sips/pull/37)
* [SIP-39: Lowering the Validator Set Barrier to Entry](https://github.com/sui-foundation/sips/pull/39)
* [SIP-40: Temporary freeze/unfreeze objects](https://github.com/sui-foundation/sips/pull/40)
* [SIP: Introduction of Verifiable Delay Functions (VDFs) to Sui Framework](https://github.com/sui-foundation/sips/pull/38)

### Merged Pull Requests

Many pull requests were merged since the last newsletter. Check them out on [GitHub](https://github.com/search?q=is%3Apr%20-author%3Aapp%2Fsui-merge-bot%20org%3Amystenlabs%20repo%3Asui%20is%3Amerged%20merged%3A2024-08-14..2024-09-17&type=pullrequests).

### Releases
Several releases are scheduled for September 2024. Check out the release schedule: [https://sui.io/networkinfo](https://sui.io/networkinfo), and the latest releases: [https://github.com/MystenLabs/sui/releases](https://github.com/MystenLabs/sui/releases).
