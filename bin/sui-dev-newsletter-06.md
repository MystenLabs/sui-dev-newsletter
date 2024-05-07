# Welcome to the Sui Developer Newsletter (#6)

_May 08, 2024_

Welcome to the sixth edition of the Sui Developer Newsletter.

Sui Basecamp, Sui's flagship conference was a big success.  Find all the excellent talks (including dev-related-talks) in this [YouTube playlist](https://www.youtube.com/playlist?list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz).

Do you want to showcase your tool, SDK, or other artifact that might be useful for developers building on Sui? We now accept submissions from the community through the [GitHub repository](https://github.com/MystenLabs/sui-dev-newsletter/). Check out the repository to find more information.

We are eager for your feedback on what you would like to see in the newsletter--tag [@SuiFoundation](https://twitter.com/@SuiFoundation), join our [Discord](https://discord.gg/sui) community, or ask on the [developer forums](https://forums.sui.io/).

- Sui team

## Community


**Presentations**
* [Advice from Move pros | Jose Cerqueira & Thouny "Block Runner" at Sui Basecamp 2024](https://www.youtube.com/watch?v=Sg1VtJH-zds&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=33&pp=iAQB)
* [Building access control on Sui using "capabilities" | Manos Liolios at Sui Basecamp 2024](https://www.youtube.com/watch?v=nIAUkllpMwI&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=34&pp=iAQB)
* [Buckyou: the first game integrating zkSend | Justa Liang at Sui Basecamp 2024](https://www.youtube.com/watch?v=X7-OuPpz3Ug&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=31&pp=iAQB)
* [Data management & RPC 2.0 | Brandon Williams at Sui Basecamp 2024](https://www.youtube.com/watch?v=2PtpgYrduWs&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=25)
* [Dynamic gas: No SUI, no problem | Kevin Nelson at Sui Basecamp 2024](https://www.youtube.com/watch?v=Z22QT8g9d4E&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=32&pp=iAQB)
* [Move '24: the next evolution in Move | Tim Zakian at Sui Basecamp 2024](https://www.youtube.com/watch?v=fZfnLwVlQmM&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=28&pp=iAQB)
* [Native Bridge and SCION Network | Bradley Hall & Lu Zhang at Sui Basecamp 2024](https://www.youtube.com/watch?v=JTFYL_hfeB4&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=24&pp=iAQB)
* [Native randomness on Sui | Andrew Schran & Jian Lu at Sui Basecamp 2024](https://www.youtube.com/watch?v=xO1Lyem3PC8&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=37&pp=iAQB)
* [Sui builder panel: developer experience | Kuna Labs, Suilend & Scallop at Sui Basecamp 2024](https://www.youtube.com/watch?v=D6bamwa38ZY&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=30&pp=iAQB)
* [Sui congestion resilience | Mark Logan at Sui Basecamp 2024](https://www.youtube.com/watch?v=8SysLEpsXVE&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=26&pp=iAQB)
* [Sui speed: present and future | Tasos Kichidis & Arun Koshy at Sui Basecamp 2024](https://www.youtube.com/watch?v=uAA9RgXejUs&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=27&pp=iAQB)
* [The future of cryptography on Sui | Kostas Chalkias at Sui Basecamp 2024](https://www.youtube.com/watch?v=RrBTeRlxCp0&list=PL9t2y-BKvZBQMQfzDlOpLNDvqup8NBvpz&index=22&pp=iAQB)

**Tutorials**

**Recent Blog & Social Media Posts**
* [DeepBook Demystified: Fueling DeFi Innovation in Sui](https://blog.sui.io/deepbook-demystified-fueling-defi-innovation/)
* [Dive into Data and Debugging with Sentio on Sui](https://blog.sui.io/sentio-launch-data-and-debugging-tools/)
* [SuiVision implemented package statistics on SuiVision.xyz! Now, on the package page, you can track and analyze the performance of each individual package](https://x.com/blockvisionhq/status/1781252037579362803)
* [@rooter on Twitter showcasing the experience on building on Sui and Solana](https://twitter.com/0xrooter/status/1785971169906360466?t=YePsLccGG5SaMKTemRyq5g&s=19)

## Development & Ecosystem

### Development Experience on Sui

* Two new features in the Sui CLI: 
  * `--dry-run` is now available for all relevant commands
  * `--gas-budget` is now optional for all relevant commands. If the `gas-budget` is not passed, the CLI will first do a dry run to estimate the gas budget.
* A new version of the Sui GraphQL RPC was released and it is now available for all networks: `sui-network.mystenlabs.com/graphql`
* Blockvision has built a code decompiler that allows to see the source code of a Move package on the [SuiVision](https://suivision.xyz) explorer. Check out this [post](https://twitter.com/blockvisionhq/status/1783496649526198589)

### Tools
* Sentio launched Transaction Search and Overview. Check it out [here](https://docs.sentio.xyz/) and this [blog post](https://blog.sui.io/sentio-launch-data-and-debugging-tools/)
* [NFT Rental using Kiosk Apps](https://docs.sui.io/standards/kiosk-apps/nft-rental)
* BucketProtocol added a new feature to the SuiGPT tools: Gas Viewer. Check out the [announcement](https://twitter.com/Eason_C13/status/1782820345860227437?t=DVq8mO0oH2hW6PD41draAA&s=19) and the [tool](https://suigpt.tools/gas)

### Improvement Proposals (SIPs) - All Open SIPs

Below is a list of all the open proposals as of now. To see the actual proposal text, click on the `Files Changed` tab. If you'd like, you can provide your input directly in the GitHub issue.

These SIPs are moving to final status soon, so now it's a great time to share your feedback:
* [SIP-16: Add more tx_context](https://github.com/sui-foundation/sips/pull/16)
* [SIP-19: Soft Bundle API](https://github.com/sui-foundation/sips/pull/19)

All other open SIPs:
* [Native stake security](https://github.com/sui-foundation/sips/pull/20)
* [SIP-10: MultiSig Cache Storage](https://github.com/sui-foundation/sips/pull/10)
* [SIP-11: Action Primitive](https://github.com/sui-foundation/sips/pull/11)
* [SIP-13: BigVector Implementation](https://github.com/sui-foundation/sips/pull/13)
* [SIP-9: WebAuthn signature scheme support](https://github.com/sui-foundation/sips/pull/9)
* [add SIP-keypairs-des-128](https://github.com/sui-foundation/sips/pull/21)

### Merged Pull Requests

Many pull requests were merged since the last newsletter. Check them out on [GitHub](https://github.com/search?q=is%3Apr%20-author%3Aapp%2Fsui-merge-bot%20org%3Amystenlabs%20repo%3Asui%20is%3Amerged%20merged%3A2024-04-17..2024-05-07&type=pullrequests).

### Releases

Several releases are scheduled for May 2024. Check out the [release schedule](https://sui.io/networkinfo) and the [most recent releases](https://github.com/MystenLabs/sui/releases).
