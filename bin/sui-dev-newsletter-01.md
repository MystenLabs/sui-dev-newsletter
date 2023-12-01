# Welcome to the Sui Developer Newsletter (#1)

_Dec 01, 2023_

The Sui developer community and core team have been very busy in the last seven months since Sui mainnet launch. To keep track of everyhing going on, we're introducing a curated developer newsletter for easier consumption.

The headline of this first edition is [zkLogin](https://docs.sui.io/concepts/cryptography/zklogin) -- a cryptography research breakthrough that enables the first native integration of sending transactions from a web2 account. Tihs enables Sui developers to build consumer-grade experiences that break free from the friction of installing a wallet and managing a seed phrase.

The community excitement around zkLogin and the pace of adoption has been exciting. In the two months since zkLogin launched, we've seen a wealth of app/wallet integrations, demos and supporting tools. You'll find some of our favorites in the newsletter.

The other theme worth highlighting are the advancements to Move. Since 2021, we've beeen advancing the foundations of Move by introducing the object data model, dynamic fields, and programmable transaction blocks. Now, we're building a polished developer experience on top of these strong foundations with source language advances like enums and method syntax, as well as tooling improvements like comprehensive linters and verifies source in the explorer. The newsletter has details on all of these, as well as the full Move 2024 roadmap.

We're eager for your feedback on what you'd like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sam Blackshear, CTO at Mysten Labs and creator of the Move programming language

## Community

**News**

- [Sui Foundation is reallocating 157M SUI for ecosystem & community growth!](https://twitter.com/SuiNetwork/status/1712906176730746981)

**Recent Blog Posts**

- [All About Account Abstraction](https://blog.sui.io/account-abstraction-explained/)
- [Build React Apps on Sui with dApp Kit](https://blog.sui.io/react-apps-dapp-kit/)
- [Delivering Fair Gas Fees Through Resource Usage Metering](https://blog.sui.io/computation-costs-gas-fee-model/)
- [DM Your SUI with zkSend](https://mystenlabs.com/blog/zksend)
- [Fifteen Projects Awarded Over $1M in Grants](https://blog.sui.io/1m-grants-awarded-october/)
- [Hackathon Winners Propel Liquid Staking on Sui](https://blog.sui.io/liquid-staking-hackathon-winners/)
- [Learning Sui is Just a Module Away With EasyA](https://blog.sui.io/easya-mobile-courseware/)
- [Sui Linters and Warnings Update Increases Coder Velocity](https://blog.sui.io/linter-compile-warnings-update/)
- [zkLogin Demystified: Exploring Sui's Cutting-Edge Authentication](https://blog.sui.io/zklogin-deep-dive/)
- [View Verified Move Source Code in Sui Explorer](https://blog.sui.io/explorer-verified-source-code/)
- [Formal snapshots released, providing a mechanism for a node to restore to a canonical state without having to execute all the transactions. They are much smaller in size than normal snapshots.](https://docs.sui.io/guides/operator/formal-snapshot)

**Presentations**

- [A Complete Guide to zkLogin: How it Works and How to Integrate](https://www.youtube.com/watch?v=Jk4mq5IOUYc)
- [Sui Liquid Staking Hackathon Demo Day](https://www.youtube.com/watch?v=d1V_PMfcFLc)

## Development & Ecosystem

### Cryptography

- zkLogin has been launched. Find more information about it in the [docs](https://docs.sui.io/concepts/cryptography/zklogin) and in this [presentation](https://docs.sui.io/concepts/cryptography/zklogin).

### Move on Sui

- [Move method syntax](https://github.com/MystenLabs/sui/issues/14063)
- [Move Edition 2024: New Language Features!](https://github.com/MystenLabs/sui/issues/14062)
- [Move linters](https://blog.sui.io/linter-compile-warnings-update/)
- [Transfer to Object is available on Devnet and soon on Testnet](https://docs.sui.io/concepts/dynamic-fields/transfers/transfer-to-object)
- Closed-Loop Token is now available. Check the [docs](https://docs.sui.io/standards/closed-loop-token) or this [thread](https://twitter.com/themoveguy/status/1730223446380966059).

### Development Experience on Sui

- The `client` and `keytool` commands in the Sui CLI now have formatted output
- [The Sui CLI can now be installed via homebrew](https://github.com/MystenLabs/homebrew-tap)
- [A beta version of the upcoming Sui GraphQL RPC service is available](https://forums.sui.io/t/launching-the-beta-graphql-rpc-service/45104)
- [Sui Bridge, a trustless native bridge leveraging Sui’s security model, is in the works](https://github.com/MystenLabs/sui/issues/14983)
- [Sui dApp Kit makes it easy to start developing apps on Sui](https://sui-typescript-docs.vercel.app/dapp-kit)
- [@mysten/create-dapp prompts you thhrough creating a new dApp project](https://sui-typescript-docs.vercel.app/dapp-kit/create-dapp)
- [Sui Documentation got a major revamp](https://docs.sui.io)
- [Sui Explorer now supports viewing verified Move source code](https://blog.sui.io/explorer-verified-source-code/)
- [Sui Weather Oracle was launched](https://blog.sui.io/sui-weather-oracle/)
- [Sui Wallet now supports USDCeth <> SUI swap pair]().

### Tools

- [Sui dApp Kit](https://sui-typescript-docs.vercel.app/dapp-kit)
- [Sui MultiSig Toolkit for offline signing of transactions](https://multisig-toolkit.vercel.app/offline-signer)
- [Sui zkLogin Demo by @polymedia](https://github.com/juzybits/polymedia-zklogin-demo)
- [Sui zkLogin Demo by @jovicheng](https://github.com/jovicheng/sui-zklogin-demo)
- [Sui zkWallet Demo by @ronanyeah](https://github.com/ronanyeah/sui-zk-wallet)

### Improvement Proposals (SIPs) - All Open SIPs

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

- [Add Poseidon hash SIP](https://github.com/sui-foundation/sips/pull/12)
- [Add WebAuthn SIP](https://github.com/sui-foundation/sips/pull/9)
- [Proposal for Sui unified assets](https://github.com/sui-foundation/sips/pull/2)
- [SIP to add store ability to Pool struct](https://github.com/sui-foundation/sips/pull/7)
- [Typus Finance BigVector Implementation](https://github.com/sui-foundation/sips/pull/13)
- [feat: added SIP Action Primitive](https://github.com/sui-foundation/sips/pull/11)
- [multisig cache init](https://github.com/sui-foundation/sips/pull/10)

### Merged Pull Requests

Many pull requests were merged in November. Check them out on [GitHub](https://github.com/search?q=is%3Apr+-author%3Aapp%2Fsui-merge-bot+org%3Amystenlabs+repo%3Asui+is%3Amerged+merged%3A2023-11-01..2023-11-30&type=pullrequests).

### Releases

Only one release, v1.15.0, is scheduled for the rest of 2023. Check out the [release schedule](https://sui.io/networkinfo) and the [most recent releases](https://github.com/MystenLabs/sui/releases).
