# Welcome to the Sui Developer Newsletter (#2)

_Feb 14, 2024_

Welcome to the third edition of the Sui Developer Newsletter.

We are pleased to announce [Sui Basecamp](https://sui.io/basecamp), the global Sui conference that will take place April 10-11 in Paris. Sui developer newsletter's subscribers get a 50\% discount when using the code `sui-devnewsletter-50`. Looking forward to seeing many of you at this event.

We are excited to welcome the launch of Sui RPC 2.0. At a high-level, RPC 2.0 is a re-architecture and rewrite of Sui’s read, write, and subscription. While the goal is to eventually replace the old JSON-RPC, today we are at the point where an initial MVP implementation of RPC 2.0 is run by Mysten Labs as a public reference. This service is rate limited in a similar fashion to our existing RPC nodes. For more information, see the launch [forum post](https://forums.sui.io/t/launching-sui-graphql-rpc-service/45240) and the [docs](https://docs.sui.io/references/sui-graphql).

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Community

**News**
* Sui's growth in DeFi metrics has been rapid, hitting [half a billion dollars](https://blog.sui.io/sui-500-million-tvl-top-10/) in total value locked in less than a year
* The official [Sui webpage](https://sui.io) got a few updates. Check them out: [Intro to Sui](https://sui.io/intro-to-sui), [Move](https://sui.io/move), [zkLogin](https://sui.io/zklogin), and [Community and Events](https://sui.io/community-events-hub)


**Recent Blog & Social Media Posts**
* [Alibaba Cloud Supports Sui Builders with AI, Hackathons, and Doc Translations](https://blog.sui.io/alibaba-cloud-builder-services-ai/)
* [All About Onchain Storage](https://blog.sui.io/onchain-storage-explained/)
* [All About Parallelization](https://blog.sui.io/parallelization-explained/)
* [All About SuiNS](https://blog.sui.io/suins-name-service-explained/)
* [Bluefin Relies on Sui Performance For First Class DeFi](https://blog.sui.io/bluefin-defi-derivatives-volume/)
* [Desig's Staking Aggregator Rates the Staking Protocols](https://blog.sui.io/desig-staking-aggregator/)
* [How Sui Primitives Help DeFi Flourish](https://blog.sui.io/sui-primitives-help-defi-flourish/)
* [Join Us For the Premier Sui Event of the Year](https://blog.sui.io/sui-basecamp-2024-paris/)
* [Move Adds Enums and Macros in 2024 Edition](https://blog.sui.io/move-edition-2024-update/)
* [Overmind’s Developer Platform Launches Sui Quests](https://blog.sui.io/overmind-launches-sui-quests/)
* [Play Beyond: Sui Gaming Summit Comes to GDC in March](https://blog.sui.io/play-beyond-summit-gdc-2024/)
* [Sui Closes in on 6,000 TPS as Inscriptions Surge](https://blog.sui.io/inscriptions-surge-6000-tps/)
* [Transfer to Object Available on Sui Mainnet](https://blog.sui.io/transfer-to-object-mainnet-launch/)

## Development & Ecosystem

### Development Experience on Sui
* Check out the first ETH-SUI [token transfer on Sui](https://suiexplorer.com/txblock/6noMGDyoH1xwdbG8vGn8A8bS98RqcS5ANH8Z7UjV1d6o?network=testnet). If you're interested to read more about this, check this [GH issue](https://github.com/MystenLabs/sui/issues/14983)
* The 2024H1 Sui Developer Roadmap is now available to the public and you can find it [here](https://forums.sui.io/t/sui-developer-roadmap-2024/45229)
* [Reference implementation for Asset Tokenization](https://docs.sui.io/guides/developer/advanced/asset-tokenization) to aid builders in representing real-world assets on-chain
* A library for preventing the equivocation in owned objects which sometimes leads to those objects being locked for the remainder of an epoch was released: [Sui Owned Object Pools](https://forums.sui.io/t/sui-owned-object-pools-library/45215). You can use `npm install suioop` to get started with it, and for more details, please refer to the [suioop documentation](https://www.npmjs.com/package/suioop)
*  [Move Adds Enums and Macros in 2024 Edition](https://blog.sui.io/move-edition-2024-update/)
* RPC 2.0 is now available for both [Mainnet](https://sui-mainnet.mystenlabs.com/graphql) and [Tesnet](https://sui-testnet.mystenlabs.com/graphql) as an MVP. See the annoucement [here](https://forums.sui.io/t/launching-sui-graphql-rpc-service/45240)
* Sui's Coin DenyList, a shared object that the bearer of a DenyCap can access to specify a list of addresses that are unable to use a Sui core type, is now available on Devnet. Check out the docs [here](https://docs.sui.io/guides/developer/sui-101/create-coin#denylist) and [here](https://docs.sui.io/guides/developer/sui-101/create-coin#manipulate-deny-list)
* Shared object deletion will be available on mainnet with the mid February release. Transfer to object is already available on [mainnet](https://blog.sui.io/transfer-to-object-mainnet-launch/)

### Tools
* You can now install `Sui` tools using `brew install sui`. Check out the docs [here](https://docs.sui.io/guides/developer/getting-started/sui-install#install-homebrew) 
* Check out the [sui-sniffer](https://www.app.kriya.finance/sui-sniffer/) tool built by [Kriya Finance](https://www.kriya.finance/)'s team

### Improvement Proposals (SIPs) - All Open SIPs

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

* [Add WebAuthn SIP](https://github.com/sui-foundation/sips/pull/9)
* [More tx_context in Move Smart Contract](https://github.com/sui-foundation/sips/pull/16)
* [New struct MatchedOrderMetadata in DeepBook](https://github.com/sui-foundation/sips/pull/14)
* [SIP: Change private key import export to Bech32 encoding](https://github.com/sui-foundation/sips/pull/15)
* [Typus Finance BigVector Implementation](https://github.com/sui-foundation/sips/pull/13)
* [feat: added SIP Action Primitive](https://github.com/sui-foundation/sips/pull/11)
* [multisig cache init](https://github.com/sui-foundation/sips/pull/10)

### Merged Pull Requests

Many pull requests were merged in Jan'24. Check them out on [GitHub](https://github.com/search?q=is%3Apr+-author%3Aapp%2Fsui-merge-bot+org%3Amystenlabs+repo%3Asui+is%3Amerged+merged%3A2024-01-01..2024-01-31&type=pullrequests).

### Releases

Several releases are scheduled for February 2024. Check out the [release schedule](https://sui.io/networkinfo) and the [most recent releases](https://github.com/MystenLabs/sui/releases).
