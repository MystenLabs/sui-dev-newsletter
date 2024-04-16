# Welcome to the Sui Developer Newsletter (#5)

_April 15, 2024_

Welcome to the latest edition of the Sui Developer Newsletter.
We are thrilled to announce a new edition of the Move [book](https://move-book.com), which includes examples written in the new Move 2024 edition.

[Sui Overflow](https://sui.io/overflow) is Sui's first global hackathon. Builders and devs from around the world will team up to push the boundaries of innovation on Sui across 8 tracks and compete for over $500k USD in SUI in prizes. Check the [website](https://sui.io/overflow) to register for updates and to learn more.

Do you want to showcase your tool, SDK, or other artifact that might be useful for developers building on Sui? We now accept submissions from the community through the [GitHub repository](https://github.com/MystenLabs/sui-dev-newsletter/). Check out the repository to find more information.

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Community

**Tutorials**

- [Sui CLI: How to Profile a Transaction Using the Gas Profiler ](https://www.youtube.com/watch?v=UhkaIiD4XHg)
- [ Sui CLI: Modify Blockchain State with Programmable Transaction Blocks (PTB)](https://www.youtube.com/watch?v=C7GmeL3cs4o)

**Recent Blog & Social Media Posts**

- [All About Digital Identity](https://blog.sui.io/digital-decentralized-identity-explained/)
- [BRICK POP Demonstrates Fun Onchain Gameplay with Rewards](https://blog.sui.io/onbuff-brickpop-onchain-game/)
- [Create and Execute PTBs on Sui with the Sui CLI](https://blog.sui.io/write-programmable-transaction-blocks-command-line-interface/)
- [Dive into Sui Overflow: Sui’s First Global Hackathon](https://blog.sui.io/diving-into-sui-overflow/)
- [Enoki - Next generation customer experiences](https://mystenlabs.com/blog/enoki-next-generation-customer-experiences/)
- [How Sui Primitives Revolutionize Onchain Gaming](https://blog.sui.io/sui-primitives-revolutionize-onchain-gaming/)
- [Let's Move Sui Helps Developers who want to Move on Sui](https://blog.sui.io/lets-move-sui-launches/)
- [Scaling Out Sui Execution with Pilotfish](https://blog.sui.io/pilotfish-execution-scalability-blockchain/)
- [Solend Team Launches New DeFi Protocol Suilend](https://blog.sui.io/solend-lending-protocol-suilend-launch/)
- [Tencent Blockchain RPC Service Now Supports Sui](https://blog.sui.io/tencent-cloud-blockchain-rpc/)

## Development & Ecosystem

### Development Experience on Sui

- The Move book has now been updated and it includes examples written in the new Move 2024 edition. Check out the book [here](https://move-book.com/index.html).
- Move 2024 is now the default Move edition. Check out this [blog post](https://blog.sui.io/move-2024-migration-guide/) for more details and the [docs](https://docs.sui.io/guides/developer/advanced/move-2024-migration) to learn more about how to migrate to the new edition.
- VSCode Move Plugin has been updated to support the latest Move 2024 edition. Check out more details [here](https://forums.sui.io/t/move-2024-ide-support/45449) and install the plugin via [marketplace](https://marketplace.visualstudio.com/items?itemName=mysten.move).
- The `verify-bytecode-meter` CLI command has received a few improvements:

  - every function and module that is verified is shown in the output table, which you can see [here](https://github.com/MystenLabs/sui/pull/16963).
  - added the `--modules` flag, enabling passing multiple module names to be verified. See more details [here](https://github.com/MystenLabs/sui/pull/16966).
  - added the `--module` flag, enabling to verify a single module. See more details [here](https://github.com/MystenLabs/sui/pull/16899).

- Enhanced BLS / ECCurve support in the Sui framework. Check out the [APIs](https://github.com/MystenLabs/sui/blob/main/crates/sui-framework/packages/sui-framework/sources/crypto/bls12381.move) and [examples](https://github.com/MystenLabs/sui/blob/main/sui_programmability/examples/crypto/sources/ec_ops.move).

### Tools

- Polymedia launched `CoinMeta`, a library for fetching coin metadata for Sui coins. Check out their repository [here](https://github.com/juzybits/polymedia-coinmeta).
- Sentio launched Sentio Dash and Sentio Debugger on Sui. Check out the announcement on [Twitter](https://twitter.com/sentioxyz/status/1778698440576213478) and [Medium](https://sentioxyz.medium.com/launch-of-sentio-dash-and-debugger-on-sui-01c82dfa8583).
- Check out the [Decompiler for Move](https://github.com/verichains/revela) smart contracts from [Verichains](https://www.verichains.io/).
- Sui Wallet mobile is now available in Google Play and Public Testflight for iOS. Check out more details [here](https://suiwallet.com/).

### Improvement Proposals (SIPs) - All Open SIPs

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

- [Add Soft Bundle API SIP for review](https://github.com/sui-foundation/sips/pull/19)
- [Add WebAuthn SIP](https://github.com/sui-foundation/sips/pull/9)
- [Dependency update check api](https://github.com/sui-foundation/sips/pull/18)
- [More tx_context in Move Smart Contract](https://github.com/sui-foundation/sips/pull/16)
- [New struct MatchedOrderMetadata in DeepBook](https://github.com/sui-foundation/sips/pull/14)
- [Typus Finance BigVector Implementation](https://github.com/sui-foundation/sips/pull/13)
- [Verification API](https://github.com/sui-foundation/sips/pull/17)
- [feat: added SIP Action Primitive](https://github.com/sui-foundation/sips/pull/11)
- [multisig cache init](https://github.com/sui-foundation/sips/pull/10)

### Merged Pull Requests

Many pull requests were merged in Mar'24. Check them out on [GitHub](https://github.com/search?q=is%3Apr+-author%3Aapp%2Fsui-merge-bot+org%3Amystenlabs+repo%3Asui+is%3Amerged+merged%3A2024-03-01..2024-03-31&type=pullrequests).

### Releases

Several releases are scheduled for April 2024. Check out the [release schedule](https://sui.io/networkinfo) and the [most recent releases](https://github.com/MystenLabs/sui/releases).
