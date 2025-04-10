# "FAQ"

<AccordionGroup>

<Accordion title="What's the gas token?">$IP</Accordion>

<Accordion title="What wallet should I use?">

Your preference obviously, since you can use any EVM-based wallet. But we
recommend [MetaMask](https://metamask.io/) for [OKX](https://www.okx.com/web3). You can add Story's L1 below:

<CardGroup cols={2}>

<Card
  title="Add Story Mainnet"
  icon="globe"
  href="https://chainid.network/chain/1514/"
>
  Connect your wallet to Story's mainnet.
</Card>

<Card
  title="Add Story 'Aeneid' Testnet"
  icon="globe"
  href="https://chainid.network/chain/1315/"
>
  Connect your wallet to Story's 'Aeneid' testnet.
</Card>

  </CardGroup>

</Accordion>

<Accordion title="Where can I see the ecosystem?">

Check out our [Ecosystem - Getting Started](https://storyprotocol.notion.site/Story-Ecosystem-Getting-Started-169051299a5480cc9b3dcac7c3ec82da) page.

</Accordion>

<Accordion title="What are my stablecoin options?">

We don't have a native stablecoin right now. You can use bridge USDC.e powered by [Stargate](https://stargate.finance/bridge).

</Accordion>

<Accordion title="How do I bridge and what's the best method?">

Use [Stargate](https://stargate.finance/bridge), [deBridge](https://app.debridge.finance/?inputChain=1&outputChain=1514&inputCurrency=&outputCurrency=0xf1815bd50389c46847f0bda824ec8da914045d14&dlnMode=simple&address=&amount=1), [Orbiter Finance](https://www.orbiter.finance/en?tgt_chain=1514&src_chain=1&src_token=ETH)

</Accordion>

<Accordion title="Is on-chain IP real?">
Story isn't replacing the legal system, it's providing on-chain rails to make the legal system more efficient for creative IP.

We have worked with world class legal teams to craft a real, off-chain legal contract called the [Programmable IP License (PIL💊)](/concepts/programmable-ip-license) that has simple terms allowing creators to state who can remix, monetize, and create derivatives of their IP and at what cost.

We've then built business logic on-chain (in the form of smart contracts) to automate & enforce those terms. This creates a tight mapping between the legal world and our on-chain terms.

</Accordion>

<Accordion title="My asset is off-chain. How do I register it as IP on Story?">
  You would mint an NFT that represents your off-chain asset, and register that
  NFT on Story.
</Accordion>

<Accordion title="I am selling an off-chain asset (eg. merch). How do I make sure that automatic royalty flow is enforced?">
Automatic royalty flow can be enforced off-chain. Although the royalty infrastructure is on-chain, the associated license is valid beyond the chain. To legally abide by the license, any derivative work will need to pay royalties on-chain to the IP Account that is attached to your IP Asset, or face consequences like in the real world (e.g. being taken to court for abusing a license) according to the terms set out by the license.

Furthermore, one of the terms of the [Programmable IP License (PIL💊)](/concepts/programmable-ip-license) is that licensees are obligated to provide revenue data for off-chain transactions (e.g. merch) to licensors, if there's a revenue share involved.

</Accordion>

<Accordion title="What is a simple example?">
Imagine you're an artist who creates digital paintings, or a musician who makes original songs. You want to share your work online, but you want to ensure that if others use or change your work, they give you credit and—if they make money from it—you get a share. That’s where Story comes in. It's a platform that uses technology to give IP owners like you control over how your work is used, tracked, and shared, so it’s both protected and fairly rewarded.

Think of it like this: Suppose you upload a song to Story. Now, anyone can see that you’re the original creator, and if someone wants to remix it, they can do so through Story. The system then automatically tracks the remix as a "derivative" of your song and notes you as the original artist. This way, if the remix becomes popular and earns money, Story can help you earn a portion of those earnings, just like the remixer.

</Accordion>

<Accordion title="What are the challenges?">
The natural question arises: "_What if I'm a bad actor and I ignore all of this and just Right Click Save As?_"

First, its underestimated the extent to which people want to follow the law. This is why PIL is so important - all of the IP is not just on-chain, it is tied to a real legal contract! If people rip off your IP, they can be sued in court. However this "happy path" doesn't always happen. When things go wrong, we want to provide as many layers of escalation before resorting to off-chain arbitration.

Thus, we've created the [❌ Dispute Module](/concepts/dispute-module) that allows anyone to flag violating content on-chain. If the dispute is successful, that IP will be flagged and no longer able to monetize or generate licenses.

The worst case scenario on Story is the best case scenario anywhere else: legal arbitration. Creators using us can always use the traditional legal system as a backstop. This is a situation we want to avoid, but one that's necessary for creators to have trust in the system.

</Accordion>

<Accordion title="Why not be a protocol on every existing chain?">
We started as a protocol, supporting projects on Polygon, Ethereum, and more. But this siloed IP to the chain that it lived on, and did not connect IP between chains. This does not realize the vision of Story as a global IP repo.

We want to be the IP settlement layer, or in other words, bring composability across chains. We need a single hub blockchain for all registered IP. This IP can be on Story, on other chains, or off-chain, but we need a hub such that all the licenses, royalties, and IP metadata live in a single unified execution environment.

</Accordion>

<Accordion title="Okay, so you need a singular blockchain. Why not use an existing blockchain?">
First and most obvious, building our own Layer 1 allows us to innovate across the entire technical stack. This enables us to implement essential features like on-chain dispute resolution or on-chain IP graphs without waiting on existing L1 roadmaps.

The need to innovate the entire stack ourselves was proven when we tried to build on a few existing chains and quickly realized it would not work due to technical limitations of those chains. Here are a few reasons we decided - or rather were forced - to build an L1:

1. Existing L1s are simply not able to handle the registration of IP upon 1000s of parents - each with their own complicated licensing details - in one transaction efficiently. Gas usage on Geth EVM rapidly increases with ancestor IPs, making it impractical beyond 670 ancestors due to block gas limits. So we improved the efficiency of graph traversing and storing for our IP graph by leveraging a new stateful precompile approach, written directly in the execution client. This creates a "shortcut" around EVM to write and read certain values in the blockchain we use for our graphs, under the restrictions of PoC protocol.
2. Similarly, existing L1s are not able to handle the royalty token flow between 1000s of IP Assets. Again, this was solved by making improvements directly in the execution client.
3. Max composability by having license data on-chain, allows for 100s of IPs to remix at once.
4. Potential rollup support with bespoke X-CHAIN data (e.g. [Initia's](https://initia.xyz/) model) for Web2 apps with millions of transactions requiring rollups. Also support Web2 apps running their own validators for max incentive alignment.
5. Future validator-enshrined L1 tech like native oracles for NFTs and off-chain RWA IPs (Cosmos SDK vote extensions).

</Accordion>

<Accordion title="Why not just settle for an L2?">
We actually did build an L2 before deciding to build an L1. However, we not only wanted to innovate the execution layer (also possible on L2), but add in a consensus mechanism, make improvements to validator node storage, novel validator features, and most importantly precompiles.

For example, we eventually want to allow Netflix, TikTok, etc to run validators to stream IP data directly on-chain, and also allow those nodes to have graph DBs optimized for IP graphs. Imagine any transaction involving a disputed IP Asset being immediately rejected.

</Accordion>

<Accordion title="Why is Story making improvements at the validator level?">
The alternative is running an adjacent system outside the L1 to provide these features, which will strictly be less decentralized than the L1 itself. By making these features native to L1 (validators), we can have sufficient decentralization, guaranteed execution, and less system to maintain.

Namely, if the adjacent system goes down (so disputes and oracles stop) but the L1 works fine, it'd be a huge problem. This can be remedied with re-staking like AVS but the tech is not battle-tested and there's no precedence of success using re-staking (EIGEN token is still in work).

One big incentive alignment Story can have: IP companies running validators & providing custom off-chain IP data to the network natively via validator-enshrined features.

Or a law firm automating disputes and broadcasting them to other validators. After an agreement of disputes, validators can immediately block transactions that include disputed IPs, which is not possible with an adjacent system providing (unless we have preconf, which is a debated topic in the Ethereum land).

</Accordion>

<Accordion title="You mentioned needing an L1 to improve the efficiency of an IP graph. Why not build an L2 with off-chain graph indexing?">
The IP graph must be on-chain because certain on-chain features require the ability to traverse and aggregate the IP graph. For example, royalty and revenue distribution need to occur on-chain through the IP graph. Using off-chain graph indexing would make these on-chain features either unfeasible or overly complex, as it would necessitate involving an oracle.

Similarly, the dispute module can check if an IP has been flagged due to its ancestor being flagged by traversing the IP graph directly on-chain, and then take immediate action such as aborting a transaction that would license a disputed IP without the need of an oracle.

</Accordion>

<Accordion title="How will Story prevent users from registering off-chain IP that isn't theirs?">
We will support a few ways, including the [❌ Dispute Module](/concepts/dispute-module), to deter IP infringement. For example if someone were to register someone else's IP, it could be disputed on-chain. And in the worst case, it would be brought to court just as it works in the traditional legal system today.

A more nuanced answer to this (one that we're constantly exploring/improving upon) is there may be additional ways to deter IP infringement. For example, a staking validation mechanism where users could stake tokens on a piece of IP being valid, and if it were to be disputed and marked as copyright, the tokens get slashed and distributed to the creator who was harmed. Additionally we've thought of introducing external IP infringement detection services directly into our L1 at the lowest level that could flag or automatically mark IP as potential infringement the moment its registered.

Ultimately Story is not a system built to prevent bad actors, rather it is meant to help facilitate honest actors to more easily register their IP, remix from others, and set proper terms for their work. The protocol is permissionless and stopping bad actors entirely would be near impossible, but we can try to disincentivize them as best we can. Much like how the pirating of media plummeted when Apple Music, Spotify, and Netflix made such media more accessible by creating a "path of least resistance", we see a similar future with Story & IP.

</Accordion>

</AccordionGroup>


# "Introduction"

Welcome to the Story API Reference! Please use the `https://api.storyapis.com` endpoint.

```http Headers
// pick one depending on the network. `story` = mainnet, `story-aeneid` = testnet
X-CHAIN: story | story-aeneid
// same for both networks
X-API-Key: MhBsxkU1z9fG6TofE59KqiiWV-YlYE8Q4awlLQehF3U
```

## Rate Limit

The above public API key has a requests/second of 300. If you'd like an API key with a higher limit, please join our Builder Discord and describe your project needs in the discussion channel.


# "Introduction"

<Warning>

In order to use the Consensus Client API, you must run your own node. See the [Node Setup Guide](/network/operating-a-node/node-setup-mainnet).

</Warning>

We have included the API Reference here so you know what to expect in the response.


# "Blockscout API"

Storyscan has a public API endpoint that returns gas price, average block time, market cap, token price (coin gecko), and several other stats: `https://www.storyscan.io/api/v2/stats`

Here is an example response ⤵️

```json
{
  "average_block_time": 2364,
  "coin_image": "https://coin-images.coingecko.com/coins/images/54035/small/Transparent_bg.png?1738075331",
  "coin_price": "4.83",
  "coin_price_change_percentage": null,
  "gas_price_updated_at": "2025-03-10T14:47:27.175157Z",
  "gas_prices": {
    "slow": 0.1,
    "average": 0.57,
    "fast": 1.05
  },
  "gas_prices_update_in": 11735,
  "gas_used_today": "147032238744",
  "market_cap": "1209228486.984",
  "network_utilization_percentage": 10.8968948333333,
  "secondary_coin_image": null,
  "secondary_coin_price": null,
  "static_gas_price": null,
  "total_addresses": "686024",
  "total_blocks": "1765700",
  "total_gas_used": "0",
  "total_transactions": "5606580",
  "transactions_today": "221320",
  "tvl": null
}
```


# "Introduction"

<Frame>
  <img src="/images/story-banner.png" alt="Hero" />
</Frame>

## Introducing the World's IP Blockchain

Story is a purpose-built layer 1 blockchain designed specifically for intellectual property.

You can register your IP on-chain and add usage terms to it in seconds, massively lowering the barrier to the currently complex & antiquated legal system for IP. For example, enforcing "you owe me 50% of your commercial revenue if you use my IP" without needing time, money, or lawyers.

<Note>
  IP could be an image, a song, an RWA, AI training data, or anything
  in-between.
</Note>

By making IP programmable on the blockchain, it becomes this transparent & decentralized global IP repository where AI agents (or any other software) and humans alike can transact on & monetize IP with a simple API call.

<CardGroup cols={2}>
  <Card title="Explain Like I'm 5" icon="house" href="/explain-like-im-five">
    Read a 1 minute summary.
  </Card>
  <Card
    title="Read the Whitepaper"
    href="https://www.story.foundation/whitepaper.pdf"
    icon="file"
  >
    Read the Story whitepaper.
  </Card>
</CardGroup>

<Accordion title="Why did we build Story?" icon="face-thinking">
When IP owners share their work online, it’s easy for others to use or change it without crediting them, and they often don't get paid fairly if their work becomes popular or valuable. This can be discouraging for people who want to share their ideas and creations but don’t want to lose control over them.

Additionally, the sheer speed and superabundance of AI-generated media is outpacing the current IP system that was designed for physical replication. In many cases, [AI is trained on and is producing copyrighted data](https://twitter.com/BriannaWu/status/1823833723764084846).

Story fixes this by providing a way for creators to share their work with built-in protection. When someone (including an AI model) uses a song, image, or any creative work that’s registered on Story, the system automatically tracks who the original owner is and makes sure they get credited. Plus, if that work generates revenue—say someone remixes a song and it earns money—the original owner automatically receives their fair share based on license terms that were set on-chain.

</Accordion>

## Quick FAQs

<AccordionGroup>

<Accordion title="What's the gas token?">$IP</Accordion>

<Accordion title="What wallet should I use?">

Your preference obviously, since you can use any EVM-based wallet. But we
recommend [MetaMask](https://metamask.io/) for [OKX](https://www.okx.com/web3). You can add Story's L1 below:

<CardGroup cols={2}>

<Card
  title="Add Story Mainnet"
  icon="globe"
  href="https://chainid.network/chain/1514/"
>
  Connect your wallet to Story's mainnet.
</Card>

<Card
  title="Add Story 'Aeneid' Testnet"
  icon="globe"
  href="https://chainid.network/chain/1315/"
>
  Connect your wallet to Story's 'Aeneid' testnet.
</Card>

  </CardGroup>

</Accordion>

<Accordion title="Where can I see the ecosystem?">

Check out our [Ecosystem - Getting Started](https://storyprotocol.notion.site/Story-Ecosystem-Getting-Started-169051299a5480cc9b3dcac7c3ec82da) page.

</Accordion>

<Accordion title="What are my stablecoin options?">

You can use bridged USDC.e powered by [Stargate](https://stargate.finance/bridge).

</Accordion>

<Accordion title="How do I bridge and what's the best method?">

Use [Stargate](https://stargate.finance/bridge), [deBridge](https://app.debridge.finance/?inputChain=1&outputChain=1514&inputCurrency=&outputCurrency=0xf1815bd50389c46847f0bda824ec8da914045d14&dlnMode=simple&address=&amount=1), or [Orbiter Finance](https://www.orbiter.finance/en?tgt_chain=1514&src_chain=1&src_token=ETH).

</Accordion>

</AccordionGroup>

## Brief Architecture Overview

There are several elements that make up Story as a whole. Below we will cover the most important components.

<Frame>
  <img src="/images/story-stack.png" alt="Story Diagram" />
</Frame>

### Story Network: "The World's IP Blockchain"

Story Network is a purpose-built layer 1 blockchain achieving the best of EVM and Cosmos SDK. It is 100% EVM-compatible alongside deep execution layer optimizations to support graph data structures, purpose-built for handling complex data structures like IP quickly and cost-efficiently. It does this by:

- using precompiled primitives to traverse complex data structures like IP graphs within seconds at marginal costs
- a consensus layer based on the mature CometBFT stack to ensure fast finality and cheap transactions

### "Proof-of-Creativity" Protocol

Our "Proof-of-Creativity" Protocol, made up of smart contracts written in Solidity, are natively deployed on Story Network and allow anyone to onramp IP to Story. Most of our documentation focuses on the protocol.

Creators register their IP as [🧩 IP Assets](/concepts/ip-asset) on Story. You use [🧱 Modules](/concepts/modules) to interact with IP Assets. For example, enforcing proper usage of your IP via the [Licensing Module](/concepts/licensing-module), paying & claiming revenue via the [Royalty Module](/concepts/royalty-module), and disputing infringing IP via the [Dispute Module](/concepts/dispute-module).

Each IP Asset has an associated ERC721 NFT, which represents _ownership_ over the IP. This means IP ownership can be bought & sold. Additionally, the licenses minted from an IP are also ERC721 NFTs, meaning you can buy & sell the rights to use an IP under certain terms. Together, this unlocks a new realm of **IPFi**.

### Programmable IP License

Although on-chain, an IP's usage terms and minted licenses are enforced by an off-chain legal contract called the [Programmable IP License (PIL💊)](/concepts/programmable-ip-license).

The PIL allows anyone to offramp tokenized IP on Story into the "real world" legal system and outlines real legal terms for how creators can remix, monetize, and create derivatives of their IP. _The protocol, or more specifically the IP Assets and modules described above, are what automate and enforce those terms on-chain_, creating a mapping between the legal world (PIL) and the blockchain.

<Note>
  Like USDC enables redemption for fiat, the PIL enables redemption for IP.
</Note>

## Examples

<Accordion title="Example #1" icon="circle-info">
Imagine you're an artist who creates digital paintings, or a musician who makes original songs. You want to share your work online, but you want to ensure that if others use or change your work, they give you credit and—if they make money from it—you get a share. That’s where Story comes in. It's a platform that uses technology to give IP owners like you control over how your work is used, tracked, and shared, so it’s both protected and fairly rewarded.

Think of it like this: Suppose you upload a song to Story. Now, anyone can see that you’re the original creator, and if someone wants to remix it, they can do so through Story. The system then automatically tracks the remix as a "derivative" of your song and notes you as the original artist. This way, if the remix becomes popular and earns money, Story can help you earn a portion of those earnings, just like the remixer.

</Accordion>

<Accordion title="Example #2" icon="circle-info">
Let’s say a scientist uploads an image dataset to be used by artificial intelligence (AI) models for research. Through Story, that dataset is registered, so if any company uses it to train their AI, the original scientist is credited. If that dataset then contributes to a profitable AI application, Story ensures a fair share goes to the original contributor.

With Story, you can share your work freely, knowing that wherever it goes, it’s tracked and fairly credited back to you. The idea is to create a fair environment for sharing, building upon, and growing creative work.

</Accordion>


# "DisputeModule"

The Dispute Module acts as an enforcement layer for IP assets that allows raising and resolving disputes through arbitration by judges. It enables users to challenge IP assets that may violate rules or infringe on other IP rights.

## State Variables

### name

```solidity
string public constant override name = DISPUTE_MODULE_KEY
```

Returns the name of the module.

### IN_DISPUTE

```solidity
bytes32 public constant IN_DISPUTE = bytes32("IN_DISPUTE")
```

Tag to represent the dispute is in dispute state waiting for judgement.

### LICENSE_REGISTRY

```solidity
ILicenseRegistry public immutable LICENSE_REGISTRY
```

Returns the protocol-wide license registry.

### GROUP_IP_ASSET_REGISTRY

```solidity
IGroupIPAssetRegistry public immutable GROUP_IP_ASSET_REGISTRY
```

Returns the protocol-wide group IP asset registry.

### IP_GRAPH_ACL

```solidity
IPGraphACL public immutable IP_GRAPH_ACL
```

Returns the protocol-wide IP Graph Access Control List.

## Functions

### initialize

```solidity
function initialize(address accessManager) external initializer
```

Initializer for this implementation contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### whitelistDisputeTag

```solidity
function whitelistDisputeTag(bytes32 tag, bool allowed) external restricted
```

Whitelists a dispute tag.

**Parameters:**

- `tag`: The dispute tag.
- `allowed`: Indicates if the dispute tag is whitelisted or not.

### whitelistArbitrationPolicy

```solidity
function whitelistArbitrationPolicy(address arbitrationPolicy, bool allowed) external restricted
```

Whitelists an arbitration policy.

**Parameters:**

- `arbitrationPolicy`: The address of the arbitration policy.
- `allowed`: Indicates if the arbitration policy is whitelisted or not.

### setArbitrationRelayer

```solidity
function setArbitrationRelayer(address arbitrationPolicy, address arbPolicyRelayer) external restricted
```

Sets the arbitration relayer for a given arbitration policy.

**Parameters:**

- `arbitrationPolicy`: The address of the arbitration policy.
- `arbPolicyRelayer`: The address of the arbitration relayer.

### setBaseArbitrationPolicy

```solidity
function setBaseArbitrationPolicy(address arbitrationPolicy) external restricted
```

Sets the base arbitration policy.

**Parameters:**

- `arbitrationPolicy`: The address of the arbitration policy.

### setArbitrationPolicyCooldown

```solidity
function setArbitrationPolicyCooldown(uint256 cooldown) external restricted
```

Sets the arbitration policy cooldown.

**Parameters:**

- `cooldown`: The cooldown in seconds.

### setArbitrationPolicy

```solidity
function setArbitrationPolicy(
    address ipId,
    address nextArbitrationPolicy
) external whenNotPaused verifyPermission(ipId)
```

Sets the arbitration policy for an ipId.

**Parameters:**

- `ipId`: The ipId.
- `nextArbitrationPolicy`: The address of the arbitration policy.

### raiseDispute

```solidity
function raiseDispute(
    address targetIpId,
    bytes32 disputeEvidenceHash,
    bytes32 targetTag,
    bytes calldata data
) external nonReentrant whenNotPaused returns (uint256)
```

Raises a dispute on a given ipId.

**Parameters:**

- `targetIpId`: The ipId that is the target of the dispute.
- `disputeEvidenceHash`: The hash pointing to the dispute evidence.
- `targetTag`: The target tag of the dispute.
- `data`: The data to initialize the policy.

**Returns:**

- `disputeId`: The id of the newly raised dispute.

### setDisputeJudgement

```solidity
function setDisputeJudgement(
    uint256 disputeId,
    bool decision,
    bytes calldata data
) external nonReentrant whenNotPaused
```

Sets the dispute judgement on a given dispute. Only whitelisted arbitration relayers can call to judge.

**Parameters:**

- `disputeId`: The dispute id.
- `decision`: The decision of the dispute.
- `data`: The data to set the dispute judgement.

### cancelDispute

```solidity
function cancelDispute(uint256 disputeId, bytes calldata data) external nonReentrant whenNotPaused
```

Cancels an ongoing dispute.

**Parameters:**

- `disputeId`: The dispute id.
- `data`: The data to cancel the dispute.

### tagIfRelatedIpInfringed

```solidity
function tagIfRelatedIpInfringed(address ipIdToTag, uint256 infringerDisputeId) external whenNotPaused
```

Tags a derivative if a parent has been tagged with an infringement tag or a group ip if a group member has been tagged with an infringement tag.

**Parameters:**

- `ipIdToTag`: The ipId to tag.
- `infringerDisputeId`: The dispute id that tagged the related infringing ipId.

### resolveDispute

```solidity
function resolveDispute(uint256 disputeId, bytes calldata data) external nonReentrant whenNotPaused
```

Resolves a dispute after it has been judged.

**Parameters:**

- `disputeId`: The dispute id.
- `data`: The data to resolve the dispute.

### updateActiveArbitrationPolicy

```solidity
function updateActiveArbitrationPolicy(address ipId) external whenNotPaused returns (address arbitrationPolicy)
```

Updates the active arbitration policy for a given ipId.

**Parameters:**

- `ipId`: The ipId.

**Returns:**

- `arbitrationPolicy`: The address of the arbitration policy.

### isIpTagged

```solidity
function isIpTagged(address ipId) external view returns (bool)
```

Returns true if the ipId is tagged with any tag (meaning at least one dispute went through).

**Parameters:**

- `ipId`: The ipId.

**Returns:**

- `isTagged`: True if the ipId is tagged.

### disputeCounter

```solidity
function disputeCounter() external view returns (uint256)
```

Returns the dispute ID counter.

**Returns:**

- `uint256`: The current dispute counter value.

### arbitrationPolicyCooldown

```solidity
function arbitrationPolicyCooldown() external view returns (uint256)
```

Returns the arbitration policy cooldown.

**Returns:**

- `uint256`: The cooldown in seconds.

### baseArbitrationPolicy

```solidity
function baseArbitrationPolicy() external view returns (address)
```

Returns the address of the base arbitration policy.

**Returns:**

- `address`: The base arbitration policy address.

### disputes

```solidity
function disputes(
    uint256 disputeId
)
    external
    view
    returns (
        address targetIpId,
        address disputeInitiator,
        uint256 disputeTimestamp,
        address arbitrationPolicy,
        bytes32 disputeEvidenceHash,
        bytes32 targetTag,
        bytes32 currentTag,
        uint256 infringerDisputeId
    )
```

Returns the dispute information for a given dispute id.

**Parameters:**

- `disputeId`: The dispute id.

**Returns:**

- `targetIpId`: The ipId that is the target of the dispute.
- `disputeInitiator`: The address of the dispute initiator.
- `disputeTimestamp`: The timestamp of the dispute.
- `arbitrationPolicy`: The address of the arbitration policy.
- `disputeEvidenceHash`: The hash pointing to the dispute evidence.
- `targetTag`: The target tag of the dispute.
- `currentTag`: The current tag of the dispute.
- `infringerDisputeId`: The infringer dispute id.

### isWhitelistedDisputeTag

```solidity
function isWhitelistedDisputeTag(bytes32 tag) external view returns (bool allowed)
```

Indicates if a dispute tag is whitelisted.

**Parameters:**

- `tag`: The dispute tag.

**Returns:**

- `allowed`: True if the tag is whitelisted.

### isWhitelistedArbitrationPolicy

```solidity
function isWhitelistedArbitrationPolicy(address arbitrationPolicy) external view returns (bool allowed)
```

Indicates if an arbitration policy is whitelisted.

**Parameters:**

- `arbitrationPolicy`: The address of the arbitration policy.

**Returns:**

- `allowed`: True if the policy is whitelisted.

### arbitrationRelayer

```solidity
function arbitrationRelayer(address arbitrationPolicy) external view returns (address)
```

Returns the arbitration relayer for a given arbitration policy.

**Parameters:**

- `arbitrationPolicy`: The address of the arbitration policy.

**Returns:**

- `address`: The arbitration relayer address.

### arbitrationPolicies

```solidity
function arbitrationPolicies(address ipId) external view returns (address policy)
```

Returns the arbitration policy for a given ipId.

**Parameters:**

- `ipId`: The ipId.

**Returns:**

- `policy`: The arbitration policy address.

### nextArbitrationPolicies

```solidity
function nextArbitrationPolicies(address ipId) external view returns (address policy)
```

Returns the next arbitration policy for a given ipId.

**Parameters:**

- `ipId`: The ipId.

**Returns:**

- `policy`: The next arbitration policy address.

### nextArbitrationUpdateTimestamps

```solidity
function nextArbitrationUpdateTimestamps(address ipId) external view returns (uint256 timestamp)
```

Returns the next arbitration update timestamp for a given ipId.

**Parameters:**

- `ipId`: The ipId.

**Returns:**

- `timestamp`: The update timestamp.


# "GroupingModule"

The Grouping Module is the main entry point for the IPA grouping on Story. It is responsible for:

- Registering a group
- Adding IP to group
- Removing IP from group
- Claiming reward

## State Variables

### name

```solidity
string public constant override name = GROUPING_MODULE_KEY
```

Returns the name of the module.

### ROYALTY_MODULE

```solidity
IRoyaltyModule public immutable ROYALTY_MODULE
```

Returns the canonical protocol-wide RoyaltyModule.

### LICENSE_TOKEN

```solidity
ILicenseToken public immutable LICENSE_TOKEN
```

Returns the canonical protocol-wide LicenseToken.

### GROUP_NFT

```solidity
IGroupNFT public immutable GROUP_NFT
```

Returns the address GROUP NFT contract.

### GROUP_IP_ASSET_REGISTRY

```solidity
IGroupIPAssetRegistry public immutable GROUP_IP_ASSET_REGISTRY
```

Returns the canonical protocol-wide Group IP Asset Registry.

### LICENSE_REGISTRY

```solidity
ILicenseRegistry public immutable LICENSE_REGISTRY
```

Returns the canonical protocol-wide LicenseRegistry.

### DISPUTE_MODULE

```solidity
IDisputeModule public immutable DISPUTE_MODULE
```

Returns the protocol-wide dispute module.

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializer for this implementation contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### registerGroup

```solidity
function registerGroup(address groupPool) external nonReentrant whenNotPaused returns (address groupId)
```

Registers a Group IPA.

**Parameters:**

- `groupPool`: The address of the group pool.

**Returns:**

- `groupId`: The address of the newly registered Group IPA.

### whitelistGroupRewardPool

```solidity
function whitelistGroupRewardPool(address rewardPool, bool allowed) external restricted
```

Whitelists a group reward pool.

**Parameters:**

- `rewardPool`: The address of the group reward pool.
- `allowed`: Whether the group reward pool is whitelisted.

### addIp

```solidity
function addIp(
    address groupIpId,
    address[] calldata ipIds,
    uint256 maxAllowedRewardShare
) external nonReentrant whenNotPaused verifyPermission(groupIpId)
```

Adds IP to group. The function must be called by the Group IP owner or an authorized operator.

**Parameters:**

- `groupIpId`: The address of the group IP.
- `ipIds`: The IP IDs.
- `maxAllowedRewardShare`: The maximum reward share percentage that can be allocated to each member IP.

### removeIp

```solidity
function removeIp(
    address groupIpId,
    address[] calldata ipIds
) external nonReentrant whenNotPaused verifyPermission(groupIpId)
```

Removes IP from group. The function must be called by the Group IP owner or an authorized operator.

**Parameters:**

- `groupIpId`: The address of the group IP.
- `ipIds`: The IP IDs.

### claimReward

```solidity
function claimReward(address groupId, address token, address[] calldata ipIds) external nonReentrant whenNotPaused
```

Claims reward.

**Parameters:**

- `groupId`: The address of the group.
- `token`: The address of the token.
- `ipIds`: The IP IDs.

### collectRoyalties

```solidity
function collectRoyalties(
    address groupId,
    address token
) external nonReentrant whenNotPaused returns (uint256 royalties)
```

Collects royalties into the pool, making them claimable by group member IPs.

**Parameters:**

- `groupId`: The address of the group.
- `token`: The address of the token.

**Returns:**

- `royalties`: The amount of royalties collected.

### name

```solidity
function name() external pure override returns (string memory)
```

Returns the name of the module.

**Returns:**

- `string`: The name of the module.

### getClaimableReward

```solidity
function getClaimableReward(
    address groupId,
    address token,
    address[] calldata ipIds
) external view returns (uint256[] memory)
```

Returns the available reward for each IP in the group.

**Parameters:**

- `groupId`: The address of the group.
- `token`: The address of the token.
- `ipIds`: The IP IDs.

**Returns:**

- `uint256[] memory`: The rewards for each IP.


# "EvenSplitGroupPool"

The EvenSplitGroupPool is a contract that implements the IGroupRewardPool interface and manages the distribution of rewards among IP members within a group. It uses an even split mechanism to distribute rewards fairly among all members.

## State Variables

### ROYALTY_MODULE

```solidity
IRoyaltyModule public immutable ROYALTY_MODULE
```

The address of the protocol-wide Royalty Module.

### GROUPING_MODULE

```solidity
IGroupingModule public immutable GROUPING_MODULE
```

The address of the protocol-wide Grouping Module.

### GROUP_IP_ASSET_REGISTRY

```solidity
IGroupIPAssetRegistry public immutable GROUP_IP_ASSET_REGISTRY
```

The address of the protocol-wide Group IP Asset Registry.

### MAX_GROUP_SIZE

```solidity
uint32 public constant MAX_GROUP_SIZE = 1_000
```

The maximum number of IP members allowed in a group.

### GroupInfo

```solidity
struct GroupInfo {
    address token;
    uint32 totalMembers;
    uint128 pendingBalance;
    uint128 accRewardPerIp;
    uint256 averageRewardShare;
}
```

Storage structure for the GroupInfo:
- `token`: The reward token for the group, defined by the license terms attached to the group IP
- `totalMembers`: Total number of IPs in the group
- `pendingBalance`: Pending balance to be added to accRewardPerIp
- `accRewardPerIp`: Accumulated rewards per IP, times MAX_GROUP_SIZE
- `averageRewardShare`: The average reward share per IP, only increases as new IPs join with higher minimum share

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializes the EvenSplitGroupPool contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### addIp

```solidity
function addIp(
    address groupId,
    address ipId,
    uint256 minimumGroupRewardShare
) external onlyGroupingModule returns (uint256 totalGroupRewardShare)
```

Adds an IP to the group pool. Only the GroupingModule can call this function.

**Parameters:**

- `groupId`: The group ID.
- `ipId`: The IP ID.
- `minimumGroupRewardShare`: The minimum group reward share the IP expects to be added to the group.

**Returns:**

- `totalGroupRewardShare`: The total group reward share after adding the IP.

### removeIp

```solidity
function removeIp(address groupId, address ipId) external onlyGroupingModule
```

Removes an IP from the group pool. Only the GroupingModule can call this function.

**Parameters:**

- `groupId`: The group ID.
- `ipId`: The IP ID.

### depositReward

```solidity
function depositReward(address groupId, address token, uint256 amount) external onlyGroupingModule
```

Deposits reward to the group pool directly.

**Parameters:**

- `groupId`: The group ID.
- `token`: The reward token.
- `amount`: The amount of reward.

### getAvailableReward

```solidity
function getAvailableReward(
    address groupId,
    address token,
    address[] calldata ipIds
) external view returns (uint256[] memory)
```

Returns the reward for each IP in the group.

**Parameters:**

- `groupId`: The group ID.
- `token`: The reward token.
- `ipIds`: The IP IDs.

**Returns:**

- `uint256[] memory`: The rewards for each IP.

### distributeRewards

```solidity
function distributeRewards(
    address groupId,
    address token,
    address[] calldata ipIds
) external whenNotPaused onlyGroupingModule returns (uint256[] memory rewards)
```

Distributes rewards to the given IP accounts in the pool.

**Parameters:**

- `groupId`: The group ID.
- `token`: The reward tokens.
- `ipIds`: The IP IDs.

**Returns:**

- `rewards`: An array containing the reward amounts distributed to each IP.

### getTotalIps

```solidity
function getTotalIps(address groupId) external view returns (uint256)
```

Returns the total number of IPs in the group.

**Parameters:**

- `groupId`: The group ID.

**Returns:**

- `uint256`: The total number of IPs in the group.

### getIpAddedTime

```solidity
function getIpAddedTime(address groupId, address ipId) external view returns (uint256)
```

Returns the timestamp when an IP was added to the group.

**Parameters:**

- `groupId`: The group ID.
- `ipId`: The IP ID.

**Returns:**

- `uint256`: The timestamp when the IP was added to the group.

### getIpRewardDebt

```solidity
function getIpRewardDebt(address groupId, address token, address ipId) external view returns (uint256)
```

Returns the reward debt of an IP in the group.

**Parameters:**

- `groupId`: The group ID.
- `token`: The reward token.
- `ipId`: The IP ID.

**Returns:**

- `uint256`: The reward debt of the IP.

### isIPAdded

```solidity
function isIPAdded(address groupId, address ipId) external view returns (bool)
```

Checks if an IP is added to the group.

**Parameters:**

- `groupId`: The group ID.
- `ipId`: The IP ID.

**Returns:**

- `bool`: True if the IP is added to the group, false otherwise.

### getMinimumRewardShare

```solidity
function getMinimumRewardShare(address groupId, address ipId) external view returns (uint256)
```

Returns the minimum reward share of an IP in the group.

**Parameters:**

- `groupId`: The group ID.
- `ipId`: The IP ID.

**Returns:**

- `uint256`: The minimum reward share of the IP.

### getTotalAllocatedRewardShare

```solidity
function getTotalAllocatedRewardShare(address groupId) external view returns (uint256)
```

Returns the total allocated reward share of the group.

**Parameters:**

- `groupId`: The group ID.

**Returns:**

- `uint256`: The total allocated reward share of the group.


# "CoreMetadataViewModule"

The CoreMetadataViewModule is a view module that provides read-only access to core metadata of IP assets within Story. It retrieves metadata information such as metadataURI, metadataHash, NFT token URI, and registration date from the IP assets.

## State Variables

### name

```solidity
string public constant override name = CORE_METADATA_VIEW_MODULE_KEY
```

Returns the name of the module.

### IP_ASSET_REGISTRY

```solidity
address public immutable IP_ASSET_REGISTRY
```

The address of the IP Asset Registry contract.

### MODULE_REGISTRY

```solidity
address public immutable MODULE_REGISTRY
```

The address of the Module Registry contract.

### coreMetadataModule

```solidity
address public coreMetadataModule
```

The address of the CoreMetadataModule contract.

## Functions

### constructor

```solidity
constructor(address ipAssetRegistry, address moduleRegistry)
```

Initializes the CoreMetadataViewModule contract.

**Parameters:**

- `ipAssetRegistry`: The address of the IP Asset Registry contract.
- `moduleRegistry`: The address of the Module Registry contract.

### updateCoreMetadataModule

```solidity
function updateCoreMetadataModule() external
```

Updates the address of the CoreMetadataModule used by this view module by retrieving it from the ModuleRegistry.

### getCoreMetadata

```solidity
function getCoreMetadata(address ipId) external view returns (CoreMetadata memory)
```

Retrieves all core metadata of the IP asset.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `CoreMetadata`: A struct containing all core metadata of the IP asset.

### getMetadataURI

```solidity
function getMetadataURI(address ipId) public view returns (string memory)
```

Retrieves the metadataURI of the IP asset set by CoreMetadataModule.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `string`: The metadataURI of the IP asset.

### getMetadataHash

```solidity
function getMetadataHash(address ipId) public view returns (bytes32)
```

Retrieves the metadata hash of the IP asset set by CoreMetadataModule.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `bytes32`: The metadata hash of the IP asset.

### getRegistrationDate

```solidity
function getRegistrationDate(address ipId) public view returns (uint256)
```

Retrieves the registration date of the IP asset from IPAssetRegistry.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `uint256`: The registration date of the IP asset.

### getNftTokenURI

```solidity
function getNftTokenURI(address ipId) public view returns (string memory)
```

Retrieves the TokenURI of NFT to which the IP asset is bound, preferring the TokenURI from CoreMetadataModule if available.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `string`: The NFT TokenURI bound to the IP asset.

### getNftMetadataHash

```solidity
function getNftMetadataHash(address ipId) public view returns (bytes32)
```

Retrieves the NFT metadata hash of the IP asset set by CoreMetadataModule.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `bytes32`: The NFT metadata hash of the IP asset.

### getOwner

```solidity
function getOwner(address ipId) public view returns (address)
```

Retrieves the owner of the IP asset.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `address`: The address of the owner of the IP asset.

### getJsonString

```solidity
function getJsonString(address ipId) external view returns (string memory)
```

Generates a JSON string formatted according to the standard NFT metadata schema for the IP asset, including all relevant metadata fields. This function consolidates metadata from both IPAssetRegistry and CoreMetadataModule, with "NFT TokenURI" from CoreMetadataModule taking precedence.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `string`: A base64-encoded JSON string representing all metadata of the IP asset.

### isSupported

```solidity
function isSupported(address ipAccount) external view returns (bool)
```

Checks whether the view module is supported for the given IP account.

**Parameters:**

- `ipAccount`: The address of the IP account.

**Returns:**

- `bool`: True if the view module is supported, false otherwise.

### supportsInterface

```solidity
function supportsInterface(bytes4 interfaceId) public view virtual override(BaseModule, IERC165) returns (bool)
```

Implements the IERC165 interface.

**Parameters:**

- `interfaceId`: The interface identifier.

**Returns:**

- `bool`: True if the contract supports the interface, false otherwise.


# "CoreMetadataModule"

The CoreMetadataModule manages the core metadata for IP assets within Story. It allows setting and updating metadata attributes for IP assets, with the ability to freeze metadata to prevent further changes.

## State Variables

### name

```solidity
string public constant override name = CORE_METADATA_MODULE_KEY
```

Returns the name of the module.

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializes the CoreMetadataModule contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### name

```solidity
function name() external pure override returns (string memory)
```

Returns the name of the module.

**Returns:**

- `string`: The name of the module.

### updateNftTokenURI

```solidity
function updateNftTokenURI(address ipId, bytes32 nftMetadataHash) external verifyPermission(ipId)
```

Update the nftTokenURI for an IP asset by retrieving the latest TokenURI from the IP NFT to which the IP Asset is bound.

**Parameters:**

- `ipId`: The address of the IP asset.
- `nftMetadataHash`: A bytes32 hash representing the metadata of the NFT. This metadata is associated with the IP Asset and is accessible via the NFT's TokenURI. Use bytes32(0) to indicate that the metadata is not available.

### setMetadataURI

```solidity
function setMetadataURI(
    address ipId,
    string memory metadataURI,
    bytes32 metadataHash
) external verifyPermission(ipId)
```

Sets the metadataURI for an IP asset.

**Parameters:**

- `ipId`: The address of the IP asset.
- `metadataURI`: The metadataURI to set for the IP asset.
- `metadataHash`: The hash of metadata at metadataURI. Use bytes32(0) to indicate that the metadata is not available.

### setAll

```solidity
function setAll(
    address ipId,
    string memory metadataURI,
    bytes32 metadataHash,
    bytes32 nftMetadataHash
) external verifyPermission(ipId)
```

Sets all core metadata for an IP asset.

**Parameters:**

- `ipId`: The address of the IP asset.
- `metadataURI`: The metadataURI to set for the IP asset.
- `metadataHash`: The hash of metadata at metadataURI. Use bytes32(0) to indicate that the metadata is not available.
- `nftMetadataHash`: A bytes32 hash representing the metadata of the NFT. This metadata is associated with the IP Asset and is accessible via the NFT's TokenURI. Use bytes32(0) to indicate that the metadata is not available.

### freezeMetadata

```solidity
function freezeMetadata(address ipId) external verifyPermission(ipId)
```

Makes all metadata of the IP Asset immutable.

**Parameters:**

- `ipId`: The address of the IP asset.

### isMetadataFrozen

```solidity
function isMetadataFrozen(address ipId) external view returns (bool)
```

Checks if the metadata of the IP Asset is immutable.

**Parameters:**

- `ipId`: The address of the IP asset.

**Returns:**

- `bool`: True if the metadata is frozen, false otherwise.

### supportsInterface

```solidity
function supportsInterface(bytes4 interfaceId) public view virtual override(BaseModule, IERC165) returns (bool)
```

Implements the IERC165 interface.

**Parameters:**

- `interfaceId`: The interface identifier.

**Returns:**

- `bool`: True if the contract supports the interface, false otherwise.


# "PILicenseTemplate"

The PILicenseTemplate (Programmable IP License Template) is a smart contract that defines and manages license terms for IP assets on Story. It allows IP owners to create customizable license terms that can be attached to their IP assets, enabling them to control how their IP can be used commercially and for derivative works.

## State Variables

### LICENSE_REGISTRY
```solidity
ILicenseRegistry public immutable LICENSE_REGISTRY
```
The address of the License Registry contract that tracks license terms and tokens.

### ROYALTY_MODULE
```solidity
IRoyaltyModule public immutable ROYALTY_MODULE
```
The address of the Royalty Module contract that handles royalty payments and policies.

### licenseTerms
```solidity
mapping(uint256 licenseTermsId => PILTerms) licenseTerms
```
Maps license terms IDs to their corresponding PILTerms structures.

### hashedLicenseTerms
```solidity
mapping(bytes32 licenseTermsHash => uint256 licenseTermsId) hashedLicenseTerms
```
Maps the hash of license terms to their corresponding license terms ID.

### licenseTermsCounter
```solidity
uint256 licenseTermsCounter
```
Counter for the number of registered license terms.

## Functions

### initialize
```solidity
function initialize(address accessManager, string memory name, string memory metadataURI) external initializer
```
Initializer for this implementation contract.

**Parameters:**
- `accessManager`: The address of the protocol admin roles contract.
- `name`: The name of the license template.
- `metadataURI`: The URL to the off-chain metadata.

### registerLicenseTerms
```solidity
function registerLicenseTerms(PILTerms calldata terms) external nonReentrant returns (uint256 id)
```
Registers new license terms and returns the ID of the newly registered license terms. The license terms are hashed and the hash is used to check if the terms are already registered. It will return an existing ID if the terms are already registered.

**Parameters:**
- `terms`: The PILTerms to register.

**Returns:**
- `id`: The ID of the newly registered license terms.

### exists
```solidity
function exists(uint256 licenseTermsId) external view override returns (bool)
```
Checks if a license terms exists.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.

**Returns:**
- Returns true if the license terms exists, false otherwise.

### verifyMintLicenseToken
```solidity
function verifyMintLicenseToken(
    uint256 licenseTermsId,
    address licensee,
    address licensorIpId,
    uint256
) external override nonReentrant returns (bool)
```
Verifies the minting of a license token. The function will be called by the LicensingModule when minting a license token to verify if the minting is allowed by the license terms.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.
- `licensee`: The address of the licensee who will receive the license token.
- `licensorIpId`: The IP ID of the licensor who attached the license terms minting the license token.

**Returns:**
- Returns true if the minting is verified, false otherwise.

### verifyRegisterDerivative
```solidity
function verifyRegisterDerivative(
    address childIpId,
    address parentIpId,
    uint256 licenseTermsId,
    address licensee
) external override returns (bool)
```
Verifies the registration of a derivative. This function is invoked by the LicensingModule during the registration of a derivative work to ensure compliance with the parent IP's licensing terms.

**Parameters:**
- `childIpId`: The IP ID of the derivative.
- `parentIpId`: The IP ID of the parent.
- `licenseTermsId`: The ID of the license terms.
- `licensee`: The address of the licensee.

**Returns:**
- Returns true if the registration is verified, false otherwise.

### verifyCompatibleLicenses
```solidity
function verifyCompatibleLicenses(uint256[] calldata licenseTermsIds) external view override returns (bool)
```
Verifies if the licenses are compatible. This function is called by the LicensingModule to verify license compatibility when registering a derivative IP to multiple parent IPs.

**Parameters:**
- `licenseTermsIds`: The IDs of the license terms.

**Returns:**
- Returns true if the licenses are compatible, false otherwise.

### verifyRegisterDerivativeForAllParents
```solidity
function verifyRegisterDerivativeForAllParents(
    address childIpId,
    address[] calldata parentIpIds,
    uint256[] calldata licenseTermsIds,
    address childIpOwner
) external override returns (bool)
```
Verifies the registration of a derivative for all parent IPs. This function is called by the LicensingModule to verify licenses for registering a derivative IP to multiple parent IPs.

**Parameters:**
- `childIpId`: The IP ID of the derivative.
- `parentIpIds`: The IP IDs of the parents.
- `licenseTermsIds`: The IDs of the license terms.
- `childIpOwner`: The address of the derivative IP owner.

**Returns:**
- Returns true if the registration is verified, false otherwise.

### getRoyaltyPolicy
```solidity
function getRoyaltyPolicy(
    uint256 licenseTermsId
) external view returns (address royaltyPolicy, bytes memory royaltyData, uint256 mintingFee, address currency)
```
Returns the royalty policy of a license terms.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.

**Returns:**
- `royaltyPolicy`: The address of the royalty policy specified for the license terms.
- `royaltyData`: The data of the royalty policy.
- `mintingFee`: The fee for minting a license.
- `currency`: The address of the ERC20 token, used for minting license fee and royalties.

### isLicenseTransferable
```solidity
function isLicenseTransferable(uint256 licenseTermsId) external view override returns (bool)
```
Checks if a license terms is transferable.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.

**Returns:**
- Returns true if the license terms is transferable, false otherwise.

### getEarlierExpireTime
```solidity
function getEarlierExpireTime(
    uint256[] calldata licenseTermsIds,
    uint256 start
) external view override returns (uint256)
```
Returns the earliest expiration time among the given license terms.

**Parameters:**
- `licenseTermsIds`: The IDs of the license terms.
- `start`: The start time.

**Returns:**
- Returns the earliest expiration time.

### getExpireTime
```solidity
function getExpireTime(uint256 licenseTermsId, uint256 start) external view returns (uint256)
```
Returns the expiration time of a license terms.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.
- `start`: The start time.

**Returns:**
- Returns the expiration time.

### getLicenseTermsId
```solidity
function getLicenseTermsId(PILTerms calldata terms) external view returns (uint256 selectedLicenseTermsId)
```
Gets the ID of the given license terms.

**Parameters:**
- `terms`: The PILTerms to get the ID for.

**Returns:**
- `selectedLicenseTermsId`: The ID of the given license terms.

### getLicenseTerms
```solidity
function getLicenseTerms(uint256 selectedLicenseTermsId) external view returns (PILTerms memory terms)
```
Gets license terms of the given ID.

**Parameters:**
- `selectedLicenseTermsId`: The ID of the license terms.

**Returns:**
- `terms`: The PILTerms associated with the given ID.

### getLicenseTermsURI
```solidity
function getLicenseTermsURI(uint256 licenseTermsId) external view returns (string memory)
```
Returns the URI of the license terms.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.

**Returns:**
- Returns the URI of the license terms.

### totalRegisteredLicenseTerms
```solidity
function totalRegisteredLicenseTerms() external view returns (uint256)
```
Returns the total number of registered license terms.

**Returns:**
- Returns the total number of registered license terms.

### supportsInterface
```solidity
function supportsInterface(
    bytes4 interfaceId
) public view virtual override(BaseLicenseTemplateUpgradeable, IERC165) returns (bool)
```
Checks whether the contract supports the given interface.

**Parameters:**
- `interfaceId`: The interface identifier.

**Returns:**
- Returns true if the contract supports the interface, false otherwise.

### toJson
```solidity
function toJson(uint256 licenseTermsId) public view returns (string memory)
```
Converts the license terms to a JSON string which will be part of the metadata of the license token.

**Parameters:**
- `licenseTermsId`: The ID of the license terms.

**Returns:**
- Returns the JSON string of the license terms, following the OpenSea metadata standard.

## PILTerms Structure

The PILTerms structure defines the terms for a Programmable IP License (PIL):

```solidity
struct PILTerms {
    bool transferable;
    address royaltyPolicy;
    uint256 mintingFee;
    uint256 expiration;
    bool commercialUse;
    bool commercialAttribution;
    address commercializerChecker;
    bytes commercializerCheckerData;
    uint32 commercialRevShare;
    uint256 commercialRevCelling;
    bool derivativesAllowed;
    bool derivativesAttribution;
    bool derivativesApproval;
    bool derivativesReciprocal;
    uint256 derivativeRevCelling;
    address currency;
    string uri;
}
```

**Parameters:**
- `transferable`: Indicates whether the license is transferable or not.
- `royaltyPolicy`: The address of the royalty policy contract which is required by StoryProtocol in advance.
- `mintingFee`: The fee to be paid when minting a license.
- `expiration`: The expiration period of the license.
- `commercialUse`: Indicates whether the work can be used commercially or not.
- `commercialAttribution`: Whether attribution is required when reproducing the work commercially or not.
- `commercializerChecker`: Commercializers that are allowed to commercially exploit the work. If zero address, then no restrictions are enforced.
- `commercializerCheckerData`: The data to be passed to the commercializer checker contract.
- `commercialRevShare`: Percentage of revenue that must be shared with the licensor.
- `commercialRevCelling`: The maximum revenue that can be generated from the commercial use of the work.
- `derivativesAllowed`: Indicates whether the licensee can create derivatives of their work or not.
- `derivativesAttribution`: Indicates whether attribution is required for derivatives of the work or not.
- `derivativesApproval`: Indicates whether the licensor must approve derivatives of the work before they can be linked to the licensor IP ID or not.
- `derivativesReciprocal`: Indicates whether the licensee must license derivatives of the work under the same terms or not.
- `derivativeRevCelling`: The maximum revenue that can be generated from the derivative use of the work.
- `currency`: The ERC20 token to be used to pay the minting fee. The token must be registered in Story Protocol.
- `uri`: The URI of the license terms, which can be used to fetch the off-chain license terms.


# "LicenseToken"

The LicenseToken contract, also known as LNFT (License NFT), is an ERC721 token that represents a license agreement for IP assets within the Story ecosystem. It enables the creation, transfer, and management of programmable IP licenses.

## State Variables

### LICENSE_REGISTRY

```solidity
ILicenseRegistry public immutable LICENSE_REGISTRY
```

The address of the protocol-wide License Registry.

### LICENSING_MODULE

```solidity
ILicensingModule public immutable LICENSING_MODULE
```

The address of the protocol-wide Licensing Module.

### DISPUTE_MODULE

```solidity
IDisputeModule public immutable DISPUTE_MODULE
```

The address of the protocol-wide Dispute Module.

### MAX_COMMERCIAL_REVENUE_SHARE

```solidity
uint32 public constant MAX_COMMERCIAL_REVENUE_SHARE = 100_000_000
```

The maximum royalty percentage is 100_000_000, which represents 100%.

### LicenseTokenMetadata

```solidity
struct LicenseTokenMetadata {
    address licensorIpId;
    address licenseTemplate;
    uint256 licenseTermsId;
    bool transferable;
    uint32 commercialRevShare;
}
```

Metadata structure for license tokens:

- `licensorIpId`: The IP asset that is the licensor
- `licenseTemplate`: The license template contract address
- `licenseTermsId`: The ID of the license terms
- `transferable`: Whether the license token can be transferred
- `commercialRevShare`: The commercial revenue share percentage

## Functions

### initialize

```solidity
function initialize(address accessManager, string memory imageUrl) public initializer
```

Initializes the LicenseToken contract.

**Parameters:**

- `accessManager`: The address of the access manager.
- `imageUrl`: The URL of the default image for license tokens.

### setLicensingImageUrl

```solidity
function setLicensingImageUrl(string calldata url) external restricted
```

Sets the licensing image URL for all license tokens.

**Parameters:**

- `url`: The URL of the licensing image.

### mintLicenseTokens

```solidity
function mintLicenseTokens(
    address licensorIpId,
    address licenseTemplate,
    uint256 licenseTermsId,
    uint256 amount,
    address minter,
    address receiver,
    uint32 maxRevenueShare
) external onlyLicensingModule returns (uint256 startLicenseTokenId)
```

Mints a specified amount of License Tokens (LNFTs).

**Parameters:**

- `licensorIpId`: The ID of the licensor IP for which the License Tokens are minted.
- `licenseTemplate`: The address of the License Template.
- `licenseTermsId`: The ID of the License Terms.
- `amount`: The amount of License Tokens to mint.
- `minter`: The address of the minter.
- `receiver`: The address of the receiver of the minted License Tokens.
- `maxRevenueShare`: The maximum revenue share percentage allowed for minting the License Tokens.

**Returns:**

- `startLicenseTokenId`: The start ID of the minted License Tokens.

### burnLicenseTokens

```solidity
function burnLicenseTokens(address holder, uint256[] calldata tokenIds) external onlyLicensingModule
```

Burns the License Tokens (LTs) for the given token IDs.

**Parameters:**

- `holder`: The address of the holder of the License Tokens.
- `tokenIds`: An array of IDs of the License Tokens to be burned.

### validateLicenseTokensForDerivative

```solidity
function validateLicenseTokensForDerivative(
    address caller,
    address childIpId,
    uint256[] calldata tokenIds
) external view returns (
    address licenseTemplate,
    address[] memory licensorIpIds,
    uint256[] memory licenseTermsIds,
    uint32[] memory commercialRevShares
)
```

Validates License Tokens for registering a derivative IP.

**Parameters:**

- `caller`: The address of the caller who register derivative with the given tokens.
- `childIpId`: The ID of the derivative IP.
- `tokenIds`: An array of IDs of the License Tokens to validate.

**Returns:**

- `licenseTemplate`: The address of the License Template associated with the License Tokens.
- `licensorIpIds`: An array of licensor IPs associated with each License Token.
- `licenseTermsIds`: An array of License Terms associated with each validated License Token.
- `commercialRevShares`: An array of commercial revenue share percentages associated with each License Token.

### totalMintedTokens

```solidity
function totalMintedTokens() external view returns (uint256)
```

Returns the total number of minted License Tokens since beginning. The number won't decrease when license tokens are burned.

**Returns:**

- `uint256`: The total number of minted License Tokens.

### getLicenseTokenMetadata

```solidity
function getLicenseTokenMetadata(uint256 tokenId) external view returns (LicenseTokenMetadata memory)
```

Returns the license data for the given license ID.

**Parameters:**

- `tokenId`: The ID of the license token.

**Returns:**

- `LicenseTokenMetadata`: The metadata of the license token.

### getLicensorIpId

```solidity
function getLicensorIpId(uint256 tokenId) external view returns (address)
```

Returns the ID of the IP asset that is the licensor of the given license ID.

**Parameters:**

- `tokenId`: The ID of the license token.

**Returns:**

- `address`: The ID of the licensor IP.

### getLicenseTermsId

```solidity
function getLicenseTermsId(uint256 tokenId) external view returns (uint256)
```

Returns the ID of the license terms that are used for the given license ID.

**Parameters:**

- `tokenId`: The ID of the license token.

**Returns:**

- `uint256`: The ID of the license terms.

### getLicenseTemplate

```solidity
function getLicenseTemplate(uint256 tokenId) external view returns (address)
```

Returns the address of the license template that is used for the given license ID.

**Parameters:**

- `tokenId`: The ID of the license token.

**Returns:**

- `address`: The address of the license template.

### getTotalTokensByLicensor

```solidity
function getTotalTokensByLicensor(address licensorIpId) external view returns (uint256)
```

Retrieves the total number of License Tokens minted for a given licensor IP.

**Parameters:**

- `licensorIpId`: The ID of the licensor IP.

**Returns:**

- `uint256`: The total number of License Tokens minted for the licensor IP.

### isLicenseTokenRevoked

```solidity
function isLicenseTokenRevoked(uint256 tokenId) public view returns (bool)
```

Returns true if the license has been revoked (licensor IP tagged after a dispute in the dispute module). If the tag is removed, the license is not revoked anymore.

**Parameters:**

- `tokenId`: The ID of the license token.

**Returns:**

- `bool`: True if the license is revoked.

### tokenURI

```solidity
function tokenURI(uint256 id) public view virtual override(ERC721Upgradeable, IERC721Metadata) returns (string memory)
```

ERC721 OpenSea metadata JSON representation of the LNFT parameters.

**Parameters:**

- `id`: The ID of the license token.

**Returns:**

- `string`: The metadata URI of the license token.


# "LicensingModule"

The Licensing Module is the main entry point for the licensing system on Story. It is responsible for:

- Attaching license terms to IP assets
- Minting license tokens
- Registering derivatives

## State Variables

### name

```solidity
string public constant override name = LICENSING_MODULE_KEY
```

Returns the name of the module.

### ROYALTY_MODULE

```solidity
RoyaltyModule public immutable ROYALTY_MODULE
```

Returns the canonical protocol-wide RoyaltyModule.

### LICENSE_REGISTRY

```solidity
ILicenseRegistry public immutable LICENSE_REGISTRY
```

Returns the canonical protocol-wide LicenseRegistry.

### DISPUTE_MODULE

```solidity
IDisputeModule public immutable DISPUTE_MODULE
```

Returns the protocol-wide dispute module.

### LICENSE_NFT

```solidity
ILicenseToken public immutable LICENSE_NFT
```

Returns the License NFT.

### MODULE_REGISTRY

```solidity
IModuleRegistry public immutable MODULE_REGISTRY
```

Returns the protocol-wide ModuleRegistry.

### IP_GRAPH_ACL

```solidity
IPGraphACL public immutable IP_GRAPH_ACL
```

Returns the protocol-wide IP Graph Access Control List.

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializer for this implementation contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### attachDefaultLicenseTerms

```solidity
function attachDefaultLicenseTerms(address ipId) external
```

Attaches the default license terms to an IP.

**Parameters:**

- `ipId`: The IP ID to attach default license terms to.

### attachLicenseTerms

```solidity
function attachLicenseTerms(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId
) external
```

Attaches specific license terms to an IP. The function must be called by the IP owner or an authorized operator.

**Parameters:**

- `ipId`: The IP ID.
- `licenseTemplate`: The address of the license template.
- `licenseTermsId`: The ID of the license terms.

### mintLicenseTokens

```solidity
function mintLicenseTokens(
    address licensorIpId,
    address licenseTemplate,
    uint256 licenseTermsId,
    uint256 amount,
    address receiver,
    bytes calldata royaltyContext,
    uint256 maxMintingFee,
    uint32 maxRevenueShare
) external returns (uint256 startLicenseTokenId)
```

Mints license tokens for the license terms attached to an IP. The license tokens are minted to the receiver.

The license terms must be attached to the IP before calling this function, but it can mint license tokens of default license terms without explicitly attaching them, since they are attached to all IPs by default.

IP owners can mint license tokens for their IPs for arbitrary license terms without attaching the license terms to the IP.

It might require the caller to pay a minting fee, depending on the license terms or as configured by the IP owner. The minting fee is paid in the minting fee token specified in the license terms or configured by the IP owner.

**Parameters:**

- `licensorIpId`: The licensor IP ID.
- `licenseTemplate`: The address of the license template.
- `licenseTermsId`: The ID of the license terms within the license template.
- `amount`: The amount of license tokens to mint.
- `receiver`: The address of the receiver.
- `royaltyContext`: The context of the royalty.
- `maxMintingFee`: The maximum minting fee that the caller is willing to pay. If set to 0, then no limit.
- `maxRevenueShare`: The maximum revenue share percentage allowed for minting the License Tokens.

**Returns:**

- `startLicenseTokenId`: The start ID of the minted license tokens.

### registerDerivative

```solidity
function registerDerivative(
    address childIpId,
    address[] calldata parentIpIds,
    uint256[] calldata licenseTermsIds,
    address licenseTemplate,
    bytes calldata royaltyContext,
    uint256 maxMintingFee,
    uint32 maxRts,
    uint32 maxRevenueShare
) external
```

Registers a derivative directly with parent IP's license terms, without needing license tokens, and attaches the license terms of the parent IPs to the derivative IP.

The license terms must be attached to the parent IP before calling this function. All IPs have default license terms attached by default.

The derivative IP owner must be the caller or an authorized operator.

**Parameters:**

- `childIpId`: The derivative IP ID.
- `parentIpIds`: The parent IP IDs.
- `licenseTermsIds`: The IDs of the license terms that the parent IP supports.
- `licenseTemplate`: The address of the license template of the license terms IDs.
- `royaltyContext`: The context of the royalty.
- `maxMintingFee`: The maximum minting fee that the caller is willing to pay. If set to 0, then no limit.
- `maxRts`: The maximum number of royalty tokens that can be distributed to the external royalty policies.
- `maxRevenueShare`: The maximum revenue share percentage allowed for minting the License Tokens.

### registerDerivativeWithLicenseTokens

```solidity
function registerDerivativeWithLicenseTokens(
    address childIpId,
    uint256[] calldata licenseTokenIds,
    bytes calldata royaltyContext,
    uint32 maxRts
) external
```

Registers a derivative with license tokens. The derivative IP is registered with license tokens minted from the parent IP's license terms.

The license terms of the parent IPs issued with license tokens are attached to the derivative IP.

The caller must be the derivative IP owner or an authorized operator.

**Parameters:**

- `childIpId`: The derivative IP ID.
- `licenseTokenIds`: The IDs of the license tokens.
- `royaltyContext`: The context of the royalty.
- `maxRts`: The maximum number of royalty tokens that can be distributed to the external royalty policies.

### setLicensingConfig

```solidity
function setLicensingConfig(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId,
    Licensing.LicensingConfig memory licensingConfig
) external
```

Sets the licensing configuration for a specific license terms of an IP.

If both licenseTemplate and licenseTermsId are not specified, then the licensing config applies to all licenses of the given IP.

**Parameters:**

- `ipId`: The address of the IP for which the configuration is being set.
- `licenseTemplate`: The address of the license template used. If not specified, the configuration applies to all licenses.
- `licenseTermsId`: The ID of the license terms within the license template. If not specified, the configuration applies to all licenses.
- `licensingConfig`: The licensing configuration for the license.

### predictMintingLicenseFee

```solidity
function predictMintingLicenseFee(
    address licensorIpId,
    address licenseTemplate,
    uint256 licenseTermsId,
    uint256 amount,
    address receiver,
    bytes calldata royaltyContext
) external view returns (address currencyToken, uint256 tokenAmount)
```

Pre-computes the minting license fee for the given IP and license terms.

This function can be used to calculate the minting license fee before minting license tokens.

**Parameters:**

- `licensorIpId`: The IP ID of the licensor.
- `licenseTemplate`: The address of the license template.
- `licenseTermsId`: The ID of the license terms.
- `amount`: The amount of license tokens to mint.
- `receiver`: The address of the receiver.
- `royaltyContext`: The context of the royalty.

**Returns:**

- `currencyToken`: The address of the ERC20 token used for minting license fee.
- `tokenAmount`: The amount of the currency token to be paid for minting license tokens.


# "RoyaltyModule"

The RoyaltyModule is the main entry point for handling royalty payments on Story. It allows IP owners to set royalty policies for their IP assets and enables derivative IP owners to pay royalties to their parent IPs.

## State Variables

### LICENSE_REGISTRY

```solidity
ILicenseRegistry public immutable LICENSE_REGISTRY
```

The address of the License Registry contract that tracks license terms and tokens.

### DISPUTE_MODULE

```solidity
IDisputeModule public immutable DISPUTE_MODULE
```

The address of the Dispute Module contract that handles dispute resolution.

### licensingModule

```solidity
address licensingModule
```

The address of the Licensing Module contract.

### isWhitelistedRoyaltyPolicy

```solidity
mapping(address royaltyPolicy => bool isWhitelisted) isWhitelistedRoyaltyPolicy
```

Indicates if a royalty policy is whitelisted.

### isWhitelistedRoyaltyToken

```solidity
mapping(address token => bool) isWhitelistedRoyaltyToken
```

Indicates if a royalty token is whitelisted.

### royaltyPolicies

```solidity
mapping(address ipId => address royaltyPolicy) royaltyPolicies
```

Maps IP IDs to their royalty policies.

## Functions

### initialize

```solidity
function initialize(address accessManager) external initializer
```

Initializer for this implementation contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### setLicensingModule

```solidity
function setLicensingModule(address licensing) external restricted
```

Sets the licensing module.

**Parameters:**

- `licensing`: The address of the license module.

### whitelistRoyaltyPolicy

```solidity
function whitelistRoyaltyPolicy(address royaltyPolicy, bool allowed) external restricted
```

Whitelist a royalty policy.

**Parameters:**

- `royaltyPolicy`: The address of the royalty policy.
- `allowed`: Indicates if the royalty policy is whitelisted or not.

### whitelistRoyaltyToken

```solidity
function whitelistRoyaltyToken(address token, bool allowed) external restricted
```

Whitelist a royalty token.

**Parameters:**

- `token`: The token address.
- `allowed`: Indicates if the token is whitelisted or not.

### onLicenseMinting

```solidity
function onLicenseMinting(
    address ipId,
    address royaltyPolicy,
    bytes calldata licenseData,
    bytes calldata externalData
) external nonReentrant onlyLicensingModule
```

Executes royalty related logic on license minting.

**Parameters:**

- `ipId`: The ipId whose license is being minted (licensor).
- `royaltyPolicy`: The royalty policy address of the license being minted.
- `licenseData`: The license data custom to each the royalty policy.
- `externalData`: The external data custom to each the royalty policy.

### onLinkToParents

```solidity
function onLinkToParents(
    address ipId,
    address royaltyPolicy,
    address[] calldata parentIpIds,
    bytes[] memory licenseData,
    bytes calldata externalData
) external nonReentrant onlyLicensingModule
```

Executes royalty related logic on linking to parents.

**Parameters:**

- `ipId`: The children ipId that is being linked to parents.
- `royaltyPolicy`: The common royalty policy address of all the licenses being burned.
- `parentIpIds`: The parent ipIds that the children ipId is being linked to.
- `licenseData`: The license data custom to each the royalty policy.
- `externalData`: The external data custom to each the royalty policy.

### payRoyaltyOnBehalf

```solidity
function payRoyaltyOnBehalf(
    address receiverIpId,
    address payerIpId,
    address token,
    uint256 amount
) external nonReentrant whenNotPaused
```

Allows the function caller to pay royalties to the receiver IP asset on behalf of the payer IP asset.

**Parameters:**

- `receiverIpId`: The ipId that receives the royalties.
- `payerIpId`: The ipId that pays the royalties.
- `token`: The token to use to pay the royalties.
- `amount`: The amount to pay.

### payLicenseMintingFee

```solidity
function payLicenseMintingFee(
    address receiverIpId,
    address payerAddress,
    address licenseRoyaltyPolicy,
    address token,
    uint256 amount
) external onlyLicensingModule
```

Allows to pay the minting fee for a license.

**Parameters:**

- `receiverIpId`: The ipId that receives the royalties.
- `payerAddress`: The address that pays the royalties.
- `licenseRoyaltyPolicy`: The royalty policy of the license being minted.
- `token`: The token to use to pay the royalties.
- `amount`: The amount to pay.

### licensingModule

```solidity
function licensingModule() external view returns (address)
```

Returns the licensing module address.

**Returns:**

- The address of the licensing module.

### isWhitelistedRoyaltyPolicy

```solidity
function isWhitelistedRoyaltyPolicy(address royaltyPolicy) external view returns (bool)
```

Indicates if a royalty policy is whitelisted.

**Parameters:**

- `royaltyPolicy`: The address of the royalty policy.

**Returns:**

- `isWhitelisted`: True if the royalty policy is whitelisted.

### isWhitelistedRoyaltyToken

```solidity
function isWhitelistedRoyaltyToken(address token) external view returns (bool)
```

Indicates if a royalty token is whitelisted.

**Parameters:**

- `token`: The address of the royalty token.

**Returns:**

- `isWhitelisted`: True if the royalty token is whitelisted.

### royaltyPolicies

```solidity
function royaltyPolicies(address ipId) external view returns (address)
```

Indicates the royalty policy for a given IP asset.

**Parameters:**

- `ipId`: The ID of IP asset.

**Returns:**

- `royaltyPolicy`: The address of the royalty policy.

### supportsInterface

```solidity
function supportsInterface(bytes4 interfaceId) public view virtual override(BaseModule, IERC165) returns (bool)
```

IERC165 interface support.

**Parameters:**

- `interfaceId`: The interface identifier.

**Returns:**

- Returns true if the interface is supported.

## Security Considerations

The RoyaltyModule contract implements several security measures:

1. **Access Control**: Most administrative functions are restricted to be called only by the protocol admin through the `restricted` modifier.

2. **Module Interaction Control**: Functions like `onLicenseMinting` and `payLicenseMintingFee` can only be called by the Licensing Module through the `onlyLicensingModule` modifier.

3. **Reentrancy Protection**: The `nonReentrant` modifier is used on functions that handle token transfers to prevent reentrancy attacks.

4. **Pausability**: The contract can be paused in emergency situations using the `whenNotPaused` modifier.

5. **Whitelisting Mechanism**: The contract implements whitelisting for royalty policies and tokens to ensure that only approved components can interact with the royalty system.

6. **Dispute Resolution Integration**: The contract integrates with the Dispute Module to handle any disputes related to royalty payments.


# "RoyaltyPolicyLAP"

The RoyaltyPolicyLAP (Liquid Absolute Percentage) contract defines the logic for splitting royalties for a given IP asset using a liquid absolute percentage mechanism. It manages the royalty relationships between IP assets and their ancestors, allowing for the transfer of revenue tokens to the appropriate royalty vaults.

## State Variables

### RoyaltyPolicyLAPStorage

```solidity
struct RoyaltyPolicyLAPStorage {
    mapping(address ipId => uint32) royaltyStackLAP;
    mapping(address ipId => mapping(address ancestorIpId => uint32)) ancestorPercentLAP;
    mapping(address ipId => mapping(address ancestorIpId => mapping(address token => uint256))) transferredTokenLAP;
}
```

Storage structure for the RoyaltyPolicyLAP containing:
- `royaltyStackLAP`: Sum of the royalty percentages to be paid to all ancestors for LAP royalty policy
- `ancestorPercentLAP`: The royalty percentage between an IP asset and a given ancestor for LAP royalty policy
- `transferredTokenLAP`: Total lifetime revenue tokens transferred to a vault from a descendant IP via LAP

### IP_GRAPH

```solidity
address public constant IP_GRAPH = address(0x0101)
```

The address of the IP Graph precompile contract that tracks relationships between IPs.

### ROYALTY_MODULE

```solidity
IRoyaltyModule public immutable ROYALTY_MODULE
```

The address of the Royalty Module contract.

### IP_GRAPH_ACL

```solidity
IPGraphACL public immutable IP_GRAPH_ACL
```

The address of the IP Graph Access Control List contract.

## Functions

### constructor

```solidity
constructor(address royaltyModule, address ipGraphAcl)
```

Constructor for the RoyaltyPolicyLAP contract.

**Parameters:**

- `royaltyModule`: The RoyaltyModule address
- `ipGraphAcl`: The IPGraphACL address

### initialize

```solidity
function initialize(address accessManager) external initializer
```

Initializer for this implementation contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### onLicenseMinting

```solidity
function onLicenseMinting(
    address ipId,
    uint32 licensePercent,
    bytes calldata
) external nonReentrant onlyRoyaltyModule
```

Executes royalty related logic on minting a license.

**Parameters:**

- `ipId`: The ipId whose license is being minted (licensor)
- `licensePercent`: The license percentage of the license being minted

### onLinkToParents

```solidity
function onLinkToParents(
    address ipId,
    address[] calldata parentIpIds,
    address[] memory licenseRoyaltyPolicies,
    uint32[] calldata licensesPercent,
    bytes calldata
) external nonReentrant onlyRoyaltyModule returns (uint32 newRoyaltyStackLAP)
```

Executes royalty related logic on linking to parents.

**Parameters:**

- `ipId`: The children ipId that is being linked to parents
- `parentIpIds`: The parent ipIds that the children ipId is being linked to
- `licenseRoyaltyPolicies`: The royalty policies of the licenses
- `licensesPercent`: The license percentage of the licenses being minted

**Returns:**

- `newRoyaltyStackLAP`: The royalty stack of the child ipId for LAP royalty policy

### transferToVault

```solidity
function transferToVault(
    address ipId,
    address ancestorIpId,
    address token
) external whenNotPaused returns (uint256)
```

Transfers to vault an amount of revenue tokens claimable via LAP royalty policy.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `ancestorIpId`: The ancestor ipId of the IP asset
- `token`: The token address to transfer

**Returns:**

- The amount of revenue tokens transferred

### getPolicyRtsRequiredToLink

```solidity
function getPolicyRtsRequiredToLink(address ipId, uint32 licensePercent) external view returns (uint32)
```

Returns the amount of royalty tokens required to link a child to a given IP asset.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `licensePercent`: The percentage of the license

**Returns:**

- The amount of royalty tokens required to link a child to a given IP asset (always 0 for LAP)

### getPolicyRoyaltyStack

```solidity
function getPolicyRoyaltyStack(address ipId) external view returns (uint32)
```

Returns the LAP royalty stack for a given IP asset.

**Parameters:**

- `ipId`: The ipId to get the royalty stack for

**Returns:**

- Sum of the royalty percentages to be paid to all ancestors for LAP royalty policy

### getPolicyRoyalty

```solidity
function getPolicyRoyalty(address ipId, address ancestorIpId) external returns (uint32)
```

Returns the royalty percentage between an IP asset and its ancestors via LAP.

**Parameters:**

- `ipId`: The ipId to get the royalty for
- `ancestorIpId`: The ancestor ipId to get the royalty for

**Returns:**

- The royalty percentage between an IP asset and its ancestors via LAP

### getTransferredTokens

```solidity
function getTransferredTokens(address ipId, address ancestorIpId, address token) external view returns (uint256)
```

Returns the total lifetime revenue tokens transferred to a vault from a descendant IP via LAP.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `ancestorIpId`: The ancestor ipId of the IP asset
- `token`: The token address to transfer

**Returns:**

- The total lifetime revenue tokens transferred to a vault from a descendant IP via LAP

### isSupportGroup

```solidity
function isSupportGroup() external view returns (bool)
```

Returns whether the royalty policy supports working with groups.

**Returns:**

- False (LAP royalty policy does not support working with groups)

## Internal Functions

### _getRoyaltyStackLAP

```solidity
function _getRoyaltyStackLAP(address ipId) internal returns (uint32)
```

Returns the royalty stack for a given IP asset for LAP royalty policy.

**Parameters:**

- `ipId`: The ipId to get the royalty stack for

**Returns:**

- The royalty stack for a given IP asset for LAP royalty policy

### _setRoyaltyLAP

```solidity
function _setRoyaltyLAP(address ipId, address parentIpId, uint32 royalty) internal
```

Sets the LAP royalty for a given link between an IP asset and its ancestor.

**Parameters:**

- `ipId`: The ipId to set the royalty for
- `parentIpId`: The parent ipId to set the royalty for
- `royalty`: The LAP license royalty percentage

### _getRoyaltyLAP

```solidity
function _getRoyaltyLAP(address ipId, address ancestorIpId) internal returns (uint32)
```

Returns the royalty percentage between an IP asset and its ancestor via royalty policy LAP.

**Parameters:**

- `ipId`: The ipId to get the royalty for
- `ancestorIpId`: The ancestor ipId to get the royalty for

**Returns:**

- The royalty percentage between an IP asset and its ancestor via royalty policy LAP

### _getRoyaltyPolicyLAPStorage

```solidity
function _getRoyaltyPolicyLAPStorage() private pure returns (RoyaltyPolicyLAPStorage storage $)
```

Returns the storage struct of RoyaltyPolicyLAP.

**Returns:**

- The storage structure for the RoyaltyPolicyLAP

### _authorizeUpgrade

```solidity
function _authorizeUpgrade(address newImplementation) internal override restricted
```

Hook to authorize the upgrade according to UUPSUpgradeable.

**Parameters:**

- `newImplementation`: The address of the new implementation

## Events

### RevenueTransferredToVault

```solidity
event RevenueTransferredToVault(address ipId, address ancestorIpId, address token, uint256 amount)
```

Emitted when revenue tokens are transferred to a vault.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `ancestorIpId`: The ancestor ipId of the IP asset
- `token`: The token address transferred
- `amount`: The amount of tokens transferred

## Security Considerations

The RoyaltyPolicyLAP contract implements several security measures:

1. **Access Control**: Functions like `onLicenseMinting` and `onLinkToParents` can only be called by the Royalty Module through the `onlyRoyaltyModule` modifier.

2. **Reentrancy Protection**: The `nonReentrant` modifier is used on functions that handle token transfers to prevent reentrancy attacks.

3. **Pausability**: The contract can be paused in emergency situations using the `whenNotPaused` modifier.

4. **Safe Token Transfers**: The contract uses OpenZeppelin's SafeERC20 library to ensure safe token transfers.

5. **Upgradability**: The contract is upgradable using the UUPS pattern, with upgrade authorization restricted to the protocol admin.

6. **Input Validation**: The contract validates inputs and checks for edge cases, such as preventing transfers between the same IP.


# "IPRoyaltyVault"

The IPRoyaltyVault contract manages the claiming of royalty and revenue tokens for a given IP. It allows token holders to claim their share of revenue tokens based on snapshots, and ancestors to collect their royalty tokens.

## State Variables

### ipId

```solidity
address ipId
```

The IP ID to which this royalty vault belongs.

### tokens

```solidity
EnumerableSet.AddressSet tokens
```

The set of revenue tokens in the vault.

### unclaimedRoyaltyTokens

```solidity
uint32 unclaimedRoyaltyTokens
```

The amount of unclaimed royalty tokens.

### lastSnapshotTimestamp

```solidity
uint256 lastSnapshotTimestamp
```

The timestamp of the last snapshot.

### ancestorsVaultAmount

```solidity
mapping(address token => uint256 amount) ancestorsVaultAmount
```

Maps token addresses to the amount in the ancestors vault.

### isCollectedByAncestor

```solidity
mapping(address ancestorIpId => bool isCollected) isCollectedByAncestor
```

Indicates whether an ancestor has collected their royalty tokens.

### claimVaultAmount

```solidity
mapping(address token => uint256 amount) claimVaultAmount
```

Maps token addresses to the amount in the claim vault.

### claimableAtSnapshot

```solidity
mapping(uint256 snapshotId => mapping(address token => uint256 amount)) claimableAtSnapshot
```

Maps snapshot IDs and token addresses to the claimable amount at that snapshot.

### unclaimedAtSnapshot

```solidity
mapping(uint256 snapshotId => uint32 amount) unclaimedAtSnapshot
```

Maps snapshot IDs to the amount of unclaimed tokens at that snapshot.

### isClaimedAtSnapshot

```solidity
mapping(uint256 snapshotId => mapping(address claimer => mapping(address token => bool isClaimed))) isClaimedAtSnapshot
```

Indicates whether a claimer has claimed a token at a specific snapshot.

## Functions

### initialize

```solidity
function initialize(
    string memory name,
    string memory symbol,
    uint256 totalSupply,
    uint32 royaltyStack,
    address ipId_
) external initializer
```

Initializer for this implementation contract.

**Parameters:**

- `name`: The name of the royalty token.
- `symbol`: The symbol of the royalty token.
- `totalSupply`: The total supply of the royalty token.
- `royaltyStack`: The royalty stack of the IP asset.
- `ipId_`: The IP ID to which this royalty vault belongs.

### addIpRoyaltyVaultTokens

```solidity
function addIpRoyaltyVaultTokens(address token) external nonReentrant whenNotPaused returns (bool)
```

Adds a token to the royalty vault.

**Parameters:**

- `token`: The token address to add.

**Returns:**

- `isAdded`: True if the token was added, false if it was already in the vault.

### snapshot

```solidity
function snapshot() external whenNotPaused returns (uint256)
```

Takes a snapshot of the claimable revenue and royalty token amounts.

**Returns:**

- `snapshotId`: The ID of the snapshot.

### claimRevenueToken

```solidity
function claimRevenueToken(uint256[] calldata snapshotIds, address token) external nonReentrant whenNotPaused
```

Allows token holders to claim their share of revenue tokens.

**Parameters:**

- `snapshotIds`: The snapshot IDs to claim from.
- `token`: The revenue token to claim.

### collectRoyaltyTokens

```solidity
function collectRoyaltyTokens(address ancestorIpId) external nonReentrant whenNotPaused
```

Allows ancestors to claim the royalty tokens and any accrued revenue tokens.

**Parameters:**

- `ancestorIpId`: The IP ID of the ancestor to whom the royalty tokens belong.

### ipId

```solidity
function ipId() external view returns (address)
```

Returns the IP ID to which this royalty vault belongs.

**Returns:**

- The IP ID address.

### unclaimedRoyaltyTokens

```solidity
function unclaimedRoyaltyTokens() external view returns (uint32)
```

Returns the amount of unclaimed royalty tokens.

**Returns:**

- The amount of unclaimed royalty tokens.

### lastSnapshotTimestamp

```solidity
function lastSnapshotTimestamp() external view returns (uint256)
```

Returns the last snapshotted timestamp.

**Returns:**

- The last snapshot timestamp.

### ancestorsVaultAmount

```solidity
function ancestorsVaultAmount(address token) external view returns (uint256)
```

Returns the amount of revenue token in the ancestors vault.

**Parameters:**

- `token`: The address of the revenue token.

**Returns:**

- The amount of revenue token in the ancestors vault.

### isCollectedByAncestor

```solidity
function isCollectedByAncestor(address ancestorIpId) external view returns (bool)
```

Indicates whether the ancestor has collected the royalty tokens.

**Parameters:**

- `ancestorIpId`: The ancestor IP ID address.

**Returns:**

- True if the ancestor has collected the royalty tokens.

### claimVaultAmount

```solidity
function claimVaultAmount(address token) external view returns (uint256)
```

Returns the amount of revenue token in the claim vault.

**Parameters:**

- `token`: The address of the revenue token.

**Returns:**

- The amount of revenue token in the claim vault.

### claimableAtSnapshot

```solidity
function claimableAtSnapshot(uint256 snapshotId, address token) external view returns (uint256)
```

Returns the amount of revenue token claimable at a given snapshot.

**Parameters:**

- `snapshotId`: The snapshot ID.
- `token`: The address of the revenue token.

**Returns:**

- The amount of revenue token claimable at the snapshot.

### unclaimedAtSnapshot

```solidity
function unclaimedAtSnapshot(uint256 snapshotId) external view returns (uint32)
```

Returns the amount of unclaimed revenue tokens at the snapshot.

**Parameters:**

- `snapshotId`: The snapshot ID.

**Returns:**

- The amount of unclaimed revenue tokens at the snapshot.

### isClaimedAtSnapshot

```solidity
function isClaimedAtSnapshot(uint256 snapshotId, address claimer, address token) external view returns (bool)
```

Indicates whether the claimer has claimed the revenue tokens at a given snapshot.

**Parameters:**

- `snapshotId`: The snapshot ID.
- `claimer`: The address of the claimer.
- `token`: The address of the revenue token.

**Returns:**

- True if the claimer has claimed the revenue tokens at the snapshot.

### tokens

```solidity
function tokens() external view returns (address[] memory)
```

Returns the list of revenue tokens in the vault.

**Returns:**

- The array of revenue token addresses.

## Security Considerations

The IPRoyaltyVault contract implements several security measures:

1. **Access Control**: Functions for adding tokens, taking snapshots, and claiming tokens are protected with appropriate modifiers.

2. **Reentrancy Protection**: The `nonReentrant` modifier is used on functions that handle token transfers to prevent reentrancy attacks.

3. **Pausability**: The contract can be paused in emergency situations using the `whenNotPaused` modifier.

4. **Snapshot Mechanism**: The contract uses a snapshot mechanism to ensure fair distribution of revenue tokens based on holdings at specific points in time.

5. **Claim Verification**: The contract tracks claimed tokens to prevent double-claiming by the same address.


# "RoyaltyPolicyLRP"

The RoyaltyPolicyLRP (Liquid Relative Percentage) contract defines the logic for splitting royalties for a given IP asset using a liquid relative percentage mechanism. It manages the royalty relationships between IP assets and their ancestors, allowing for the transfer of revenue tokens to the appropriate royalty vaults.

## State Variables

### RoyaltyPolicyLRPStorage

```solidity
struct RoyaltyPolicyLRPStorage {
    mapping(address ipId => uint32) royaltyStackLRP;
    mapping(address ipId => mapping(address ancestorIpId => uint32)) ancestorPercentLRP;
    mapping(address ipId => mapping(address ancestorIpId => mapping(address token => uint256))) transferredTokenLRP;
}
```

Storage structure for the RoyaltyPolicyLRP containing:
- `royaltyStackLRP`: Sum of the royalty percentages to be paid to all ancestors for LRP royalty policy
- `ancestorPercentLRP`: The royalty percentage between an IP asset and a given ancestor for LRP royalty policy
- `transferredTokenLRP`: Total lifetime revenue tokens transferred to a vault from a descendant IP via LRP

### IP_GRAPH

```solidity
address public constant IP_GRAPH = address(0x0101)
```

The address of the IP Graph precompile contract that tracks relationships between IPs.

### ROYALTY_MODULE

```solidity
IRoyaltyModule public immutable ROYALTY_MODULE
```

The address of the Royalty Module contract.

### ROYALTY_POLICY_LAP

```solidity
IGraphAwareRoyaltyPolicy public immutable ROYALTY_POLICY_LAP
```

The address of the RoyaltyPolicyLAP contract.

### IP_GRAPH_ACL

```solidity
IPGraphACL public immutable IP_GRAPH_ACL
```

The address of the IP Graph Access Control List contract.

## Functions

### constructor

```solidity
constructor(address royaltyModule, address royaltyPolicyLAP, address ipGraphAcl)
```

Constructor for the RoyaltyPolicyLRP contract.

**Parameters:**

- `royaltyModule`: The RoyaltyModule address
- `royaltyPolicyLAP`: The RoyaltyPolicyLAP address
- `ipGraphAcl`: The IPGraphACL address

### initialize

```solidity
function initialize(address accessManager) external initializer
```

Initializer for this implementation contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### onLicenseMinting

```solidity
function onLicenseMinting(
    address ipId,
    uint32 licensePercent,
    bytes calldata
) external nonReentrant onlyRoyaltyModule
```

Executes royalty related logic on minting a license.

**Parameters:**

- `ipId`: The ipId whose license is being minted (licensor)
- `licensePercent`: The license percentage of the license being minted

### onLinkToParents

```solidity
function onLinkToParents(
    address ipId,
    address[] calldata parentIpIds,
    address[] memory licenseRoyaltyPolicies,
    uint32[] calldata licensesPercent,
    bytes calldata
) external nonReentrant onlyRoyaltyModule returns (uint32 newRoyaltyStackLRP)
```

Executes royalty related logic on linking to parents.

**Parameters:**

- `ipId`: The children ipId that is being linked to parents
- `parentIpIds`: The parent ipIds that the children ipId is being linked to
- `licenseRoyaltyPolicies`: The royalty policies of the licenses
- `licensesPercent`: The license percentage of the licenses being minted

**Returns:**

- `newRoyaltyStackLRP`: The royalty stack of the child ipId for LRP royalty policy

### transferToVault

```solidity
function transferToVault(
    address ipId,
    address ancestorIpId,
    address token
) external whenNotPaused returns (uint256)
```

Transfers to vault an amount of revenue tokens claimable via LRP royalty policy.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `ancestorIpId`: The ancestor ipId of the IP asset
- `token`: The token address to transfer

**Returns:**

- The amount of revenue tokens transferred

### getPolicyRtsRequiredToLink

```solidity
function getPolicyRtsRequiredToLink(address ipId, uint32 licensePercent) external view returns (uint32)
```

Returns the amount of royalty tokens required to link a child to a given IP asset.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `licensePercent`: The percentage of the license

**Returns:**

- The amount of royalty tokens required to link a child to a given IP asset (always 0 for LRP)

### getPolicyRoyaltyStack

```solidity
function getPolicyRoyaltyStack(address ipId) external view returns (uint32)
```

Returns the LRP royalty stack for a given IP asset.

**Parameters:**

- `ipId`: The ipId to get the royalty stack for

**Returns:**

- Sum of the royalty percentages to be paid to all ancestors for LRP royalty policy

### getPolicyRoyalty

```solidity
function getPolicyRoyalty(address ipId, address ancestorIpId) external returns (uint32)
```

Returns the royalty percentage between an IP asset and its ancestors via LRP.

**Parameters:**

- `ipId`: The ipId to get the royalty for
- `ancestorIpId`: The ancestor ipId to get the royalty for

**Returns:**

- The royalty percentage between an IP asset and its ancestors via LRP

### getTransferredTokens

```solidity
function getTransferredTokens(address ipId, address ancestorIpId, address token) external view returns (uint256)
```

Returns the total lifetime revenue tokens transferred to a vault from a descendant IP via LRP.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `ancestorIpId`: The ancestor ipId of the IP asset
- `token`: The token address to transfer

**Returns:**

- The total lifetime revenue tokens transferred to a vault from a descendant IP via LRP

### isSupportGroup

```solidity
function isSupportGroup() external view returns (bool)
```

Returns whether the royalty policy supports working with groups.

**Returns:**

- True (LRP royalty policy supports working with groups)

## Internal Functions

### _getRoyaltyStackLRP

```solidity
function _getRoyaltyStackLRP(address ipId) internal returns (uint32)
```

Returns the royalty stack for a given IP asset for LRP royalty policy.

**Parameters:**

- `ipId`: The ipId to get the royalty stack for

**Returns:**

- The royalty stack for a given IP asset for LRP royalty policy

### _setRoyaltyLRP

```solidity
function _setRoyaltyLRP(address ipId, address parentIpId, uint32 royalty) internal
```

Sets the LRP royalty for a given link between an IP asset and its ancestor.

**Parameters:**

- `ipId`: The ipId to set the royalty for
- `parentIpId`: The parent ipId to set the royalty for
- `royalty`: The LRP license royalty percentage

### _getRoyaltyLRP

```solidity
function _getRoyaltyLRP(address ipId, address ancestorIpId) internal returns (uint32)
```

Returns the royalty percentage between an IP asset and its ancestor via royalty policy LRP.

**Parameters:**

- `ipId`: The ipId to get the royalty for
- `ancestorIpId`: The ancestor ipId to get the royalty for

**Returns:**

- The royalty percentage between an IP asset and its ancestor via royalty policy LRP

### _getRoyaltyPolicyLRPStorage

```solidity
function _getRoyaltyPolicyLRPStorage() private pure returns (RoyaltyPolicyLRPStorage storage $)
```

Returns the storage struct of RoyaltyPolicyLRP.

**Returns:**

- The storage structure for the RoyaltyPolicyLRP

### _authorizeUpgrade

```solidity
function _authorizeUpgrade(address newImplementation) internal override restricted
```

Hook to authorize the upgrade according to UUPSUpgradeable.

**Parameters:**

- `newImplementation`: The address of the new implementation

## Events

### RevenueTransferredToVault

```solidity
event RevenueTransferredToVault(address ipId, address ancestorIpId, address token, uint256 amount)
```

Emitted when revenue tokens are transferred to a vault.

**Parameters:**

- `ipId`: The ipId of the IP asset
- `ancestorIpId`: The ancestor ipId of the IP asset
- `token`: The token address transferred
- `amount`: The amount of tokens transferred

## Security Considerations

The RoyaltyPolicyLRP contract implements several security measures:

1. **Access Control**: Functions like `onLicenseMinting` and `onLinkToParents` can only be called by the Royalty Module through the `onlyRoyaltyModule` modifier.

2. **Reentrancy Protection**: The `nonReentrant` modifier is used on functions that handle token transfers to prevent reentrancy attacks.

3. **Pausability**: The contract can be paused in emergency situations using the `whenNotPaused` modifier.

4. **Safe Token Transfers**: The contract uses OpenZeppelin's SafeERC20 library to ensure safe token transfers.

5. **Upgradability**: The contract is upgradable using the UUPS pattern, with upgrade authorization restricted to the protocol admin.

6. **Input Validation**: The contract validates inputs and checks for edge cases, such as preventing transfers between the same IP.

## Royalty Dilution Considerations

The LRP (Liquid Relative Percentage) royalty policy allows each remixed IP to receive a percentage of the revenue generated by its direct derivatives. However, it's important to understand the potential dilution of royalties as more derivatives are created between two IPs.

This dilution can reduce the earnings of the original IP creator as more layers of derivatives are added. For example:

1. Creator 1 - Registers IP1, mints an LRP license of 10%, and sells the license to Creator 2.
2. Creator 2 - Registers IP2 as a derivative of IP1 and mints an LRP license of 20% for himself/herself.
3. Creator 2 - Registers IP3 as a derivative of IP2 and promotes IP3 commercially in the market.

The earnings for Creator 1 are diluted because they will only receive 10% of the 20% royalties from IP3, resulting in an effective royalty of 2%. If Creator 2 had chosen to promote IP2 instead, Creator 1 would have earned 10% directly, avoiding this dilution.

In contrast, the LAP (Liquid Absolute Percentage) royalty policy enforces a fixed percentage on every descendant IP, protecting the original creator from dilution.


# "IPAccountImpl"

The IPAccountImpl contract is Story's implementation of the IP Account, which follows the ERC-6551 standard for token-bound accounts. It provides functionality for IP assets to own and manage other assets, execute transactions, and interact with other contracts in a permissioned manner.

## State Variables

### ACCESS_CONTROLLER

```solidity
address public immutable ACCESS_CONTROLLER
```

The address of the AccessController contract used for permission checks. This is immutable and set during construction.

## Inheritance

IPAccountImpl inherits from:

- ERC6551: Base implementation of the ERC-6551 standard
- IPAccountStorage: Storage contract for IP Account data
- IIPAccount: Interface for IP Account functionality

## Functions

### constructor

```solidity
constructor(
    address accessController,
    address ipAssetRegistry,
    address licenseRegistry,
    address moduleRegistry
)
```

Creates a new IPAccountImpl contract instance.

**Parameters:**

- `accessController`: The address of the AccessController contract to be used for permission checks
- `ipAssetRegistry`: The address of the IP Asset Registry
- `licenseRegistry`: The address of the License Registry
- `moduleRegistry`: The address of the Module Registry

### supportsInterface

```solidity
function supportsInterface(bytes4 interfaceId) public view returns (bool)
```

Checks if the contract supports a specific interface.

**Parameters:**

- `interfaceId`: The interface identifier, as specified in ERC-165

**Returns:**

- Boolean indicating if the contract supports the interface

### token

```solidity
function token() public view returns (uint256, address, uint256)
```

Returns the identifier of the non-fungible token which owns the account.

**Returns:**

- `chainId`: The EIP-155 ID of the chain the token exists on
- `tokenContract`: The contract address of the token
- `tokenId`: The ID of the token

### isValidSigner

```solidity
function isValidSigner(address signer, bytes calldata data) public view returns (bytes4 result)
```

Checks if the signer is valid for executing specific actions on behalf of the IP Account.

**Parameters:**

- `signer`: The signer to check
- `data`: The data to be checked, encoded as `abi.encode(address to, bytes calldata)`

**Returns:**

- The function selector if the signer is valid, 0 otherwise

### isValidSigner

```solidity
function isValidSigner(address signer, address to, bytes calldata data) public view returns (bool)
```

Checks if the signer is valid for the given data and recipient via the AccessController permission system.

**Parameters:**

- `signer`: The signer to check
- `to`: The recipient of the transaction
- `data`: The calldata to check against

**Returns:**

- Boolean indicating if the signer is valid

### owner

```solidity
function owner() public view returns (address)
```

Returns the owner of the IP Account.

**Returns:**

- The address of the owner

### state

```solidity
function state() public view returns (bytes32 result)
```

Returns the IPAccount's internal nonce for transaction ordering.

**Returns:**

- The current state (nonce) of the account

### updateStateForValidSigner

```solidity
function updateStateForValidSigner(address signer, address to, bytes calldata data) external
```

Updates the IP Account's state if the signer is valid for the given data and recipient.

**Parameters:**

- `signer`: The signer to check
- `to`: The recipient of the transaction
- `data`: The calldata to check against

### executeWithSig

```solidity
function executeWithSig(
    address to,
    uint256 value,
    bytes calldata data,
    address signer,
    uint256 deadline,
    bytes calldata signature
) external payable returns (bytes memory result)
```

Executes a transaction from the IP Account on behalf of the signer.

**Parameters:**

- `to`: The recipient of the transaction
- `value`: The amount of Ether to send
- `data`: The data to send along with the transaction
- `signer`: The signer of the transaction
- `deadline`: The deadline of the transaction signature
- `signature`: The signature of the transaction, EIP-712 encoded

**Returns:**

- The return data from the transaction

### execute

```solidity
function execute(address to, uint256 value, bytes calldata data) external payable returns (bytes memory result)
```

Executes a transaction from the IP Account.

**Parameters:**

- `to`: The recipient of the transaction
- `value`: The amount of Ether to send
- `data`: The data to send along with the transaction

**Returns:**

- The return data from the transaction

### execute

```solidity
function execute(
    address to,
    uint256 value,
    bytes calldata data,
    uint8 operation
) public payable returns (bytes memory result)
```

Executes a transaction from the IP Account with a specified operation type.

**Parameters:**

- `to`: The recipient of the transaction
- `value`: The amount of Ether to send
- `data`: The data to send along with the transaction
- `operation`: The operation type to perform, only 0 - CALL is supported

**Returns:**

- The return data from the transaction

### executeBatch

```solidity
function executeBatch(
    Call[] calldata calls,
    uint8 operation
) public payable returns (bytes[] memory results)
```

Executes a batch of transactions from the IP Account.

**Parameters:**

- `calls`: The array of calls to execute
- `operation`: The operation type to perform, only 0 - CALL is supported

**Returns:**

- The return data from the transactions

### isValidSignature

```solidity
function isValidSignature(bytes32 hash, bytes calldata signature) public view returns (bytes4 result)
```

ERC1271 signature verification is disabled for the IP Account.

**Parameters:**

- `hash`: The hash of the data to be signed
- `signature`: The signature to verify

**Returns:**

- Always returns 0xffffffff (disabled)

## Events

### Executed

```solidity
event Executed(address to, uint256 value, bytes data, bytes32 state)
```

Emitted when a transaction is executed from the IP Account.

**Parameters:**

- `to`: The recipient of the transaction
- `value`: The amount of Ether sent
- `data`: The data sent along with the transaction
- `state`: The new state (nonce) of the account

### ExecutedWithSig

```solidity
event ExecutedWithSig(address to, uint256 value, bytes data, bytes32 state, uint256 deadline, address signer, bytes signature)
```

Emitted when a transaction is executed from the IP Account on behalf of a signer.

**Parameters:**

- `to`: The recipient of the transaction
- `value`: The amount of Ether sent
- `data`: The data sent along with the transaction
- `state`: The new state (nonce) of the account
- `deadline`: The deadline of the transaction signature
- `signer`: The signer of the transaction
- `signature`: The signature of the transaction

## Security Considerations

The IPAccountImpl contract implements several security measures:

1. **Permission System**: Uses an AccessController to manage permissions for different signers and operations.

2. **Signature Verification**: Implements EIP-712 typed data signing for secure transaction authorization.

3. **Deadline Checking**: Includes transaction deadlines to prevent replay attacks.

4. **Nonce Management**: Uses a state (nonce) system to prevent transaction replay.

5. **Input Validation**: Validates inputs and checks for edge cases, such as preventing invalid operations.

6. **Signature Malleability Protection**: Includes protections against signature malleability attacks.

7. **Limited Operations**: Only supports the CALL operation (0) for security reasons, restricting potentially dangerous operations.

8. **Upgradability Disabled**: The contract disables UUPS upgradability to ensure contract immutability.

## Usage Examples

### Executing a Transaction

An IP asset owner can execute a transaction through their IP Account:

```solidity
// Assuming 'ipAccount' is an instance of IPAccountImpl
ipAccount.execute(
    targetContract,
    0, // No ETH sent
    abi.encodeWithSignature("someFunction(uint256)", 123)
);
```

### Executing with a Signature

A permitted signer can execute a transaction on behalf of the IP Account:

```solidity
// Generate signature off-chain
bytes signature = signEIP712Message(...);

// Execute transaction
ipAccount.executeWithSig(
    targetContract,
    0, // No ETH sent
    abi.encodeWithSignature("someFunction(uint256)", 123),
    signer,
    deadline,
    signature
);
```


# "Overview"

<CardGroup cols={2}>

<Card
  title="Step-by-Step Guide"
  icon="house"
  href="/developers/smart-contracts-guide"
>
  Learn our smart contracts through a series of tutorials with the Smart
  Contract Guide.
</Card>

<Card
  title="Deployed Protocol Addresses"
  icon="gear"
  href="/developers/deployed-smart-contracts"
>
  All of the deployed protocol addresses for **testnet** and **mainnet**.
</Card>

</CardGroup>

<Warning>
  Do not use `RANDAO` for pseudo-randomness, instead use onchain VRF (Pyth or
  Gelato). Currently, `RANDAO` value is set as the parent block hash and thus is
  not random for X-1 block.
</Warning>


# "IPAccountRegistry"

The IPAccountRegistry is responsible for managing the registration and tracking of IP Accounts. It leverages a public ERC6551 registry to deploy IPAccount contracts, which represent tokenized intellectual property assets within the Story ecosystem.

## State Variables

### IP_ACCOUNT_IMPL

```solidity
address public immutable IP_ACCOUNT_IMPL
```

Returns the IPAccount implementation address.

### IP_ACCOUNT_SALT

```solidity
bytes32 public immutable IP_ACCOUNT_SALT
```

Returns the IPAccount salt.

### ERC6551_PUBLIC_REGISTRY

```solidity
address public immutable ERC6551_PUBLIC_REGISTRY
```

Returns the public ERC6551 registry address.

### IP_ACCOUNT_IMPL_UPGRADEABLE_BEACON

```solidity
address public immutable IP_ACCOUNT_IMPL_UPGRADEABLE_BEACON
```

The IPAccount implementation upgradeable beacon address.

## Functions

### ipAccount

```solidity
function ipAccount(uint256 chainId, address tokenContract, uint256 tokenId) public view returns (address)
```

Returns the IPAccount address for the given NFT token.

**Parameters:**

- `chainId`: The chain ID where the IP Account is located.
- `tokenContract`: The address of the token contract associated with the IP Account.
- `tokenId`: The ID of the token associated with the IP Account.

**Returns:**

- `ipAccountAddress`: The address of the IP Account associated with the given NFT token.

### getIPAccountImpl

```solidity
function getIPAccountImpl() external view override returns (address)
```

Returns the IPAccount implementation address.

**Returns:**

- `address`: The address of the IPAccount implementation.

### \_registerIpAccount (internal)

```solidity
function _registerIpAccount(
    uint256 chainId,
    address tokenContract,
    uint256 tokenId
) internal returns (address ipAccountAddress)
```

Deploys an IPAccount contract with the IPAccount implementation and returns the address of the new IP. The IPAccount deployment delegates to public ERC6551 Registry.

**Parameters:**

- `chainId`: The chain ID where the IP Account will be created.
- `tokenContract`: The address of the token contract to be associated with the IP Account.
- `tokenId`: The ID of the token to be associated with the IP Account.

**Returns:**

- `ipAccountAddress`: The address of the newly created IP Account.

### \_get6551AccountAddress (internal)

```solidity
function _get6551AccountAddress(
    uint256 chainId,
    address tokenContract,
    uint256 tokenId
) internal view returns (address)
```

Helper function to get the IPAccount address from the ERC6551 registry.

**Parameters:**

- `chainId`: The chain ID where the IP Account is located.
- `tokenContract`: The address of the token contract associated with the IP Account.
- `tokenId`: The ID of the token associated with the IP Account.

**Returns:**

- `address`: The address of the IP Account.

### \_upgradeIPAccountImpl (internal)

```solidity
function _upgradeIPAccountImpl(address newIpAccountImpl) internal
```

Helper function to upgrade the IPAccount implementation.

**Parameters:**

- `newIpAccountImpl`: The address of the new IPAccount implementation.


# "LicenseRegistry"

The LicenseRegistry manages the registration and tracking of License NFTs (LNFTs), which represent licenses granted by IP ID licensors to create derivative IPs. It provides functionality for managing license templates, license terms, and the relationships between parent and derivative IP assets.

## State Variables

### MAX_PARENTS

```solidity
uint256 public constant MAX_PARENTS = 16
```

The maximum number of parent IPs a derivative IP can have.

### MAX_ANCESTORS

```solidity
uint256 public constant MAX_ANCESTORS = 1024
```

The maximum number of ancestor IPs a derivative IP can have.

### IP_GRAPH

```solidity
address public constant IP_GRAPH = address(0x0101)
```

The address of the IP Graph contract that tracks relationships between IPs.

### GROUP_IP_ASSET_REGISTRY

```solidity
IGroupIPAssetRegistry public immutable GROUP_IP_ASSET_REGISTRY
```

The address of the Group IP Asset Registry contract.

### LICENSING_MODULE

```solidity
ILicensingModule public immutable LICENSING_MODULE
```

The address of the Licensing Module contract.

### DISPUTE_MODULE

```solidity
IDisputeModule public immutable DISPUTE_MODULE
```

The address of the Dispute Module contract.

### IP_GRAPH_ACL

```solidity
IPGraphACL public immutable IP_GRAPH_ACL
```

The address of the IP Graph Access Control List contract.

### EXPIRATION_TIME

```solidity
bytes32 public constant EXPIRATION_TIME = "EXPIRATION_TIME"
```

The key used to store expiration time in IP Account storage.

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializes the LicenseRegistry contract.

**Parameters:**

- `accessManager`: The address of the protocol admin roles contract.

### setDefaultLicenseTerms

```solidity
function setDefaultLicenseTerms(address newLicenseTemplate, uint256 newLicenseTermsId) external restricted
```

Sets the default license terms that are attached to all IPs by default.

**Parameters:**

- `newLicenseTemplate`: The address of the new default license template.
- `newLicenseTermsId`: The ID of the new default license terms.

### registerLicenseTemplate

```solidity
function registerLicenseTemplate(address licenseTemplate) external restricted
```

Registers a new license template on Story.

**Parameters:**

- `licenseTemplate`: The address of the license template to register.

### setLicensingConfigForLicense

```solidity
function setLicensingConfigForLicense(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId,
    Licensing.LicensingConfig calldata licensingConfig
) external onlyLicensingModule
```

Sets the minting license configuration for a specific license attached to a specific IP.

**Parameters:**

- `ipId`: The address of the IP for which the configuration is being set.
- `licenseTemplate`: The address of the license template used.
- `licenseTermsId`: The ID of the license terms within the license template.
- `licensingConfig`: The configuration for minting the license.

### attachLicenseTermsToIp

```solidity
function attachLicenseTermsToIp(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId
) external onlyLicensingModule
```

Attaches license terms to an IP.

**Parameters:**

- `ipId`: The address of the IP to which the license terms are attached.
- `licenseTemplate`: The address of the license template.
- `licenseTermsId`: The ID of the license terms.

### registerDerivativeIp

```solidity
function registerDerivativeIp(
    address childIpId,
    address[] calldata parentIpIds,
    address licenseTemplate,
    uint256[] calldata licenseTermsIds,
    bool isUsingLicenseToken
) external onlyLicensingModule
```

Registers a derivative IP and its relationship to parent IPs.

**Parameters:**

- `childIpId`: The address of the derivative IP.
- `parentIpIds`: An array of addresses of the parent IPs.
- `licenseTemplate`: The address of the license template used.
- `licenseTermsIds`: An array of IDs of the license terms.
- `isUsingLicenseToken`: Whether the derivative IP is registered with license tokens.

### initializeLicenseTemplate

```solidity
function initializeLicenseTemplate(address ipId, address licenseTemplate) external onlyLicensingModule
```

Sets license template for an IP, if the IP has no license template set.

**Parameters:**

- `ipId`: The address of the IP to which the license template is attached.
- `licenseTemplate`: The address of the license template.

### verifyMintLicenseToken

```solidity
function verifyMintLicenseToken(
    address licensorIpId,
    address licenseTemplate,
    uint256 licenseTermsId,
    bool isMintedByIpOwner
) external view returns (Licensing.LicensingConfig memory)
```

Verifies the minting of a license token.

**Parameters:**

- `licensorIpId`: The address of the licensor IP.
- `licenseTemplate`: The address of the license template where the license terms are defined.
- `licenseTermsId`: The ID of the license terms will mint the license token.
- `isMintedByIpOwner`: Whether the license token is minted by the IP owner.

**Returns:**

- `Licensing.LicensingConfig`: The configuration for minting the license.

### verifyGroupAddIp

```solidity
function verifyGroupAddIp(
    address groupId,
    address groupRewardPool,
    address ipId,
    address groupLicenseTemplate,
    uint256 groupLicenseTermsId
) external view returns (Licensing.LicensingConfig memory ipLicensingConfig)
```

Verifies the group can add given IP.

**Parameters:**

- `groupId`: The address of the group.
- `groupRewardPool`: The address of the reward pool of the group.
- `ipId`: The address of the IP to be added to the group.
- `groupLicenseTemplate`: The address of the license template attached to the group.
- `groupLicenseTermsId`: The ID of the license terms attached to the group.

**Returns:**

- `ipLicensingConfig`: The configuration for license attached to the IP.

### isRegisteredLicenseTemplate

```solidity
function isRegisteredLicenseTemplate(address licenseTemplate) external view returns (bool)
```

Checks if a license template is registered.

**Parameters:**

- `licenseTemplate`: The address of the license template to check.

**Returns:**

- `bool`: Whether the license template is registered.

### isDerivativeIp

```solidity
function isDerivativeIp(address childIpId) external view returns (bool)
```

Checks if an IP is a derivative IP.

**Parameters:**

- `childIpId`: The address of the IP to check.

**Returns:**

- `bool`: Whether the IP is a derivative IP.

### hasDerivativeIps

```solidity
function hasDerivativeIps(address parentIpId) external view returns (bool)
```

Checks if an IP has derivative IPs.

**Parameters:**

- `parentIpId`: The address of the IP to check.

**Returns:**

- `bool`: Whether the IP has derivative IPs.

### exists

```solidity
function exists(address licenseTemplate, uint256 licenseTermsId) external view returns (bool)
```

Checks if license terms exist.

**Parameters:**

- `licenseTemplate`: The address of the license template where the license terms are defined.
- `licenseTermsId`: The ID of the license terms.

**Returns:**

- `bool`: Whether the license terms exist.

### hasIpAttachedLicenseTerms

```solidity
function hasIpAttachedLicenseTerms(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId
) external view returns (bool)
```

Checks if an IP has attached any license terms.

**Parameters:**

- `ipId`: The address of the IP to check.
- `licenseTemplate`: The address of the license template where the license terms are defined.
- `licenseTermsId`: The ID of the license terms.

**Returns:**

- `bool`: Whether the IP has attached any license terms.

### getAttachedLicenseTerms

```solidity
function getAttachedLicenseTerms(
    address ipId,
    uint256 index
) external view returns (address licenseTemplate, uint256 licenseTermsId)
```

Gets the attached license terms of an IP by its index.

**Parameters:**

- `ipId`: The address of the IP.
- `index`: The index of the attached license terms within the array of all attached license terms of the IP.

**Returns:**

- `licenseTemplate`: The address of the license template where the license terms are defined.
- `licenseTermsId`: The ID of the license terms.

### getAttachedLicenseTermsCount

```solidity
function getAttachedLicenseTermsCount(address ipId) external view returns (uint256)
```

Gets the count of attached license terms of an IP.

**Parameters:**

- `ipId`: The address of the IP.

**Returns:**

- `uint256`: The count of attached license terms.

### getDerivativeIp

```solidity
function getDerivativeIp(address parentIpId, uint256 index) external view returns (address childIpId)
```

Gets the derivative IP of an IP by its index.

**Parameters:**

- `parentIpId`: The address of the IP.
- `index`: The index of the derivative IP within the array of all derivative IPs of the IP.

**Returns:**

- `childIpId`: The address of the derivative IP.

### getDerivativeIpCount

```solidity
function getDerivativeIpCount(address parentIpId) external view returns (uint256)
```

Gets the count of derivative IPs of an IP.

**Parameters:**

- `parentIpId`: The address of the IP.

**Returns:**

- `uint256`: The count of derivative IPs.

### getParentIp

```solidity
function getParentIp(address childIpId, uint256 index) external view returns (address parentIpId)
```

Gets the parent IP of an IP by its index.

**Parameters:**

- `childIpId`: The address of the IP.
- `index`: The index of the parent IP within the array of all parent IPs of the IP.

**Returns:**

- `parentIpId`: The address of the parent IP.

### isParentIp

```solidity
function isParentIp(address parentIpId, address childIpId) external view returns (bool)
```

Checks if an IP is a parent of another IP.

**Parameters:**

- `parentIpId`: The address of the potential parent IP.
- `childIpId`: The address of the potential child IP.

**Returns:**

- `bool`: Whether the IP is a parent of the other IP.

### getParentIpCount

```solidity
function getParentIpCount(address childIpId) external view returns (uint256)
```

Gets the count of parent IPs.

**Parameters:**

- `childIpId`: The address of the child IP.

**Returns:**

- `uint256`: The count of parent IPs.

### getAncestorsCount

```solidity
function getAncestorsCount(address ipId) external returns (uint256)
```

Gets the count of ancestors IPs.

**Parameters:**

- `ipId`: The ID of IP asset.

**Returns:**

- `uint256`: The count of ancestor IPs.

### getLicensingConfig

```solidity
function getLicensingConfig(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId
) external view returns (Licensing.LicensingConfig memory)
```

Retrieves the minting license configuration for a given license terms of the IP.

**Parameters:**

- `ipId`: The address of the IP.
- `licenseTemplate`: The address of the license template where the license terms are defined.
- `licenseTermsId`: The ID of the license terms.

**Returns:**

- `Licensing.LicensingConfig`: The configuration for minting the license.

### getExpireTime

```solidity
function getExpireTime(address ipId) external view returns (uint256)
```

Gets the expiration time for an IP.

**Parameters:**

- `ipId`: The address of the IP.

**Returns:**

- `uint256`: The expiration time, 0 means never expired.

### isExpiredNow

```solidity
function isExpiredNow(address ipId) external view returns (bool)
```

Checks if an IP is expired.

**Parameters:**

- `ipId`: The address of the IP.

**Returns:**

- `bool`: Whether the IP is expired.

### getDefaultLicenseTerms

```solidity
function getDefaultLicenseTerms() external view returns (address licenseTemplate, uint256 licenseTermsId)
```

Returns the default license terms.

**Returns:**

- `licenseTemplate`: The address of the default license template.
- `licenseTermsId`: The ID of the default license terms.

### isDefaultLicense

```solidity
function isDefaultLicense(address licenseTemplate, uint256 licenseTermsId) external view returns (bool)
```

Checks if the license terms are the default license terms.

**Parameters:**

- `licenseTemplate`: The address of the license template.
- `licenseTermsId`: The ID of the license terms.

**Returns:**

- `bool`: Whether the license terms are the default license terms.

### getParentLicenseTerms

```solidity
function getParentLicenseTerms(
    address childIpId,
    address parentIpId
) external view returns (address licenseTemplate, uint256 licenseTermsId)
```

Returns the license terms through which a child IP links to a parent IP.

**Parameters:**

- `childIpId`: The address of the child IP.
- `parentIpId`: The address of the parent IP.

**Returns:**

- `licenseTemplate`: The address of the license template.
- `licenseTermsId`: The ID of the license terms.

### getRoyaltyPercent

```solidity
function getRoyaltyPercent(
    address ipId,
    address licenseTemplate,
    uint256 licenseTermsId
) external view returns (uint32 royaltyPercent)
```

Return the Royalty percentage of the license terms of the IP.

**Parameters:**

- `ipId`: The address of the IP.
- `licenseTemplate`: The address of the license template where the license terms are defined.
- `licenseTermsId`: The ID of the license terms.

**Returns:**

- `royaltyPercent`: The Royalty percentage 100% is 100_000_000.


# "GroupIPAssetRegistry"

The GroupIPAssetRegistry manages the registration and tracking of Group IP Assets (IPAs), including the group members and reward pools. It provides functionality for registering groups, managing group membership, and handling group reward pools.

## State Variables

### MAX_GROUP_SIZE

```solidity
uint256 public constant MAX_GROUP_SIZE = 1000
```

The maximum number of members allowed in a group.

### GROUPING_MODULE

```solidity
IGroupingModule public immutable GROUPING_MODULE
```

The address of the protocol-wide Grouping Module.

## Functions

### registerGroup

```solidity
function registerGroup(
    address groupNft,
    uint256 groupNftId,
    address rewardPool,
    address registerFeePayer
) external onlyGroupingModule whenNotPaused returns (address groupId)
```

Registers a Group IPA.

**Parameters:**

- `groupNft`: The address of the group NFT.
- `groupNftId`: The ID of the group NFT.
- `rewardPool`: The address of the group reward pool.
- `registerFeePayer`: The address of the account that pays the registration fee.

**Returns:**

- `groupId`: The address of the newly registered Group IPA.

### whitelistGroupRewardPool

```solidity
function whitelistGroupRewardPool(address rewardPool, bool allowed) external onlyGroupingModule whenNotPaused
```

Whitelists a group reward pool.

**Parameters:**

- `rewardPool`: The address of the group reward pool.
- `allowed`: Whether the group reward pool is whitelisted.

### addGroupMember

```solidity
function addGroupMember(address groupId, address[] calldata ipIds) external onlyGroupingModule whenNotPaused
```

Adds members to a Group IPA.

**Parameters:**

- `groupId`: The address of the Group IPA.
- `ipIds`: The addresses of the IPs to add to the Group IPA.

### removeGroupMember

```solidity
function removeGroupMember(address groupId, address[] calldata ipIds) external onlyGroupingModule whenNotPaused
```

Removes members from a Group IPA.

**Parameters:**

- `groupId`: The address of the Group IPA.
- `ipIds`: The addresses of the IPs to remove from the Group IPA.

### isRegisteredGroup

```solidity
function isRegisteredGroup(address groupId) external view returns (bool)
```

Checks whether a group IPA was registered based on its ID.

**Parameters:**

- `groupId`: The address of the Group IPA.

**Returns:**

- `isRegistered`: Whether the Group IPA was registered into the protocol.

### getGroupRewardPool

```solidity
function getGroupRewardPool(address groupId) external view returns (address)
```

Retrieves the group reward pool for a Group IPA.

**Parameters:**

- `groupId`: The address of the Group IPA.

**Returns:**

- `rewardPool`: The address of the group reward pool.

### isWhitelistedGroupRewardPool

```solidity
function isWhitelistedGroupRewardPool(address rewardPool) external view returns (bool isWhitelisted)
```

Checks whether a group reward pool is whitelisted.

**Parameters:**

- `rewardPool`: The address of the group reward pool.

**Returns:**

- `isWhitelisted`: Whether the group reward pool is whitelisted.

### getGroupMembers

```solidity
function getGroupMembers(
    address groupId,
    uint256 startIndex,
    uint256 size
) external view returns (address[] memory results)
```

Retrieves the group members for a Group IPA.

**Parameters:**

- `groupId`: The address of the Group IPA.
- `startIndex`: The start index of the group members to retrieve.
- `size`: The size of the group members to retrieve.

**Returns:**

- `results`: The addresses of the group members.

### containsIp

```solidity
function containsIp(address groupId, address ipId) external view returns (bool)
```

Checks whether an IP is a member of a Group IPA.

**Parameters:**

- `groupId`: The address of the Group IPA.
- `ipId`: The address of the IP.

**Returns:**

- `isMember`: Whether the IP is a member of the Group IPA.

### totalMembers

```solidity
function totalMembers(address groupId) external view returns (uint256)
```

Retrieves the total number of members in a Group IPA.

**Parameters:**

- `groupId`: The address of the Group IPA.

**Returns:**

- `totalMembers`: The total number of members in the Group IPA.


# "IPAssetRegistry"

The IPAssetRegistry acts as the source of truth for all IP registered on Story. An IP is identified by its contract address, token id, and chain id, meaning any NFT may be conceptualized as an IP. Once an IP is registered into the protocol, a corresponding IP asset is generated, which references an IP resolver for metadata attribution and an IP account for protocol authorization.

## State Variables

### totalSupply

```solidity
uint256 totalSupply
```

The total number of IP assets registered in the protocol.

### treasury

```solidity
address treasury
```

The address of the treasury that receives registration fees.

### feeToken

```solidity
address feeToken
```

The address of the token used to pay registration fees.

### feeAmount

```solidity
uint96 feeAmount
```

The amount of the registration fee.

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializes the IPAssetRegistry contract.

**Parameters:**

- `accessManager`: The address of the access manager.

### register

```solidity
function register(
    uint256 chainid,
    address tokenContract,
    uint256 tokenId
) external whenNotPaused returns (address id)
```

Registers an NFT as an IP asset and creates an IP account for it. If the IP was already registered, returns the IP address.

**Parameters:**

- `chainid`: The chain identifier of where the IP NFT resides.
- `tokenContract`: The address of the NFT.
- `tokenId`: The token identifier of the NFT.

**Returns:**

- `id`: The address of the newly registered IP.

### setRegistrationFee

```solidity
function setRegistrationFee(address treasury, address feeToken, uint96 feeAmount) external restricted
```

Sets the registration fee for IP assets.

**Parameters:**

- `treasury`: The address of the treasury that will receive the fee.
- `feeToken`: The address of the token used to pay the fee.
- `feeAmount`: The amount of the fee.

### upgradeIPAccountImpl

```solidity
function upgradeIPAccountImpl(address newIpAccountImpl) external restricted
```

Upgrades the IP account implementation.

**Parameters:**

- `newIpAccountImpl`: The address of the new IP account implementation.

### ipId

```solidity
function ipId(uint256 chainId, address tokenContract, uint256 tokenId) public view returns (address)
```

Gets the canonical IP identifier associated with an IP NFT. This is equivalent to the address of its bound IP account.

**Parameters:**

- `chainId`: The chain identifier of where the IP resides.
- `tokenContract`: The address of the IP.
- `tokenId`: The token identifier of the IP.

**Returns:**

- `ipId`: The IP's canonical address identifier.

### isRegistered

```solidity
function isRegistered(address id) external view returns (bool)
```

Checks whether an IP was registered based on its ID.

**Parameters:**

- `id`: The canonical identifier for the IP.

**Returns:**

- `isRegistered`: Whether the IP was registered into the protocol.

### totalSupply

```solidity
function totalSupply() external view returns (uint256)
```

Gets the total number of IP assets registered in the protocol.

**Returns:**

- `uint256`: The total number of IP assets registered.

### getTreasury

```solidity
function getTreasury() external view returns (address)
```

Retrieves the treasury address for IP assets.

**Returns:**

- `treasury`: The address of the treasury.

### getFeeToken

```solidity
function getFeeToken() external view returns (address)
```

Retrieves the registration fee token for IP assets.

**Returns:**

- `feeToken`: The address of the token used to pay the fee.

### getFeeAmount

```solidity
function getFeeAmount() external view returns (uint96)
```

Retrieves the registration fee amount for IP assets.

**Returns:**

- `feeAmount`: The amount of the fee.


# "ModuleRegistry"

The ModuleRegistry contract is used to register and track modules within the Story ecosystem. It serves as a central registry for all protocol modules, allowing for easy discovery and management of different module types and implementations.

## State Variables

### ModuleRegistryStorage

```solidity
struct ModuleRegistryStorage {
    mapping(string moduleName => address moduleAddress) modules;
    mapping(address moduleAddress => string moduleType) moduleTypes;
    mapping(string moduleType => bytes4 moduleTypeInterface) allModuleTypes;
}
```

Storage structure for the ModuleRegistry containing:
- `modules`: Maps module names to their addresses
- `moduleTypes`: Maps module addresses to their types
- `allModuleTypes`: Maps module types to their interface IDs

### ModuleRegistryStorageLocation

```solidity
bytes32 private constant ModuleRegistryStorageLocation
```

The storage location for the ModuleRegistry storage structure, following ERC-7201 for namespace storage pattern.

## Functions

### initialize

```solidity
function initialize(address accessManager) public initializer
```

Initializes the ModuleRegistry contract.

**Parameters:**

- `accessManager`: The address of the governance contract.

### registerModuleType

```solidity
function registerModuleType(string memory name, bytes4 interfaceId) external override restricted
```

Registers a new module type in the registry associated with an interface.

**Parameters:**

- `name`: The name of the module type to be registered.
- `interfaceId`: The interface ID associated with the module type.

### removeModuleType

```solidity
function removeModuleType(string memory name) external override restricted
```

Removes a module type from the registry.

**Parameters:**

- `name`: The name of the module type to be removed.

### registerModule (Default Type)

```solidity
function registerModule(string memory name, address moduleAddress) external restricted
```

Registers a new module in the registry with the default module type.

**Parameters:**

- `name`: The name of the module.
- `moduleAddress`: The address of the module.

### registerModule (Specific Type)

```solidity
function registerModule(string memory name, address moduleAddress, string memory moduleType) external restricted
```

Registers a new module in the registry with a specific module type.

**Parameters:**

- `name`: The name of the module to be registered.
- `moduleAddress`: The address of the module.
- `moduleType`: The type of the module being registered.

### removeModule

```solidity
function removeModule(string memory name) external restricted
```

Removes a module from the registry.

**Parameters:**

- `name`: The name of the module to be removed.

### isRegistered

```solidity
function isRegistered(address moduleAddress) external view returns (bool)
```

Checks if a module is registered in the protocol.

**Parameters:**

- `moduleAddress`: The address of the module.

**Returns:**

- `bool`: True if the module is registered, false otherwise.

### getModule

```solidity
function getModule(string memory name) external view returns (address)
```

Returns the address of a module.

**Parameters:**

- `name`: The name of the module.

**Returns:**

- `address`: The address of the module.

### getModuleType

```solidity
function getModuleType(address moduleAddress) external view returns (string memory)
```

Returns the module type of a given module address.

**Parameters:**

- `moduleAddress`: The address of the module.

**Returns:**

- `string`: The type of the module as a string.

### getModuleTypeInterfaceId

```solidity
function getModuleTypeInterfaceId(string memory moduleType) external view returns (bytes4)
```

Returns the interface ID associated with a given module type.

**Parameters:**

- `moduleType`: The type of the module as a string.

**Returns:**

- `bytes4`: The interface ID of the module type.

## Internal Functions

### _registerModule

```solidity
function _registerModule(string memory name, address moduleAddress, string memory moduleType) internal
```

Internal function to register a new module in the registry.

**Parameters:**

- `name`: The name of the module.
- `moduleAddress`: The address of the module.
- `moduleType`: The type of the module being registered.

### _getModuleRegistryStorage

```solidity
function _getModuleRegistryStorage() private pure returns (ModuleRegistryStorage storage $)
```

Returns the storage struct of the ModuleRegistry.

**Returns:**

- `ModuleRegistryStorage`: The storage structure for the ModuleRegistry.

### _authorizeUpgrade

```solidity
function _authorizeUpgrade(address newImplementation) internal override restricted
```

Hook to authorize the upgrade according to UUPSUpgradeable.

**Parameters:**

- `newImplementation`: The address of the new implementation.

## Events

### ModuleAdded

```solidity
event ModuleAdded(string name, address moduleAddress, bytes4 moduleTypeInterfaceId, string moduleType)
```

Emitted when a new module is added to the registry.

**Parameters:**

- `name`: The name of the module.
- `moduleAddress`: The address of the module.
- `moduleTypeInterfaceId`: The interface ID of the module type.
- `moduleType`: The type of the module.

### ModuleRemoved

```solidity
event ModuleRemoved(string name, address moduleAddress)
```

Emitted when a module is removed from the registry.

**Parameters:**

- `name`: The name of the module.
- `moduleAddress`: The address of the module.

## Security Considerations

The ModuleRegistry contract implements several security measures:

1. **Access Control**: Most functions are restricted to be called only by the protocol admin through the `restricted` modifier.

2. **Input Validation**: The contract validates all inputs to ensure they meet the required criteria:
   - Module addresses must be non-zero and must be contracts
   - Names and module types cannot be empty strings
   - Module types must be registered before modules of that type can be registered
   - Modules must support the expected interface for their type

3. **Duplicate Prevention**: The contract prevents duplicate registrations:
   - A module type cannot be registered twice with the same name
   - A module cannot be registered twice with different names
   - A name cannot be used for multiple modules

4. **Upgradability**: The contract is upgradable using the UUPS pattern, with upgrade authorization restricted to the protocol admin.


# "Quickstart"

You want to start building on Story quickly... so let's get started!

<Tip>
Looking to read up on Story first?

If you'd like to read up on Story before diving into the technical details, check out our awesome [Learn Hub](https://learn.story.foundation/) which will explain the who, what, and why of Story.

</Tip>

<Frame
  caption={
    <>
      Credit to the original tweet{" "}
      <a href="https://x.com/devrelius/status/1898756162675196098">here</a>.
    </>
  }
>
  <img
    src="https://files.readme.io/49a6d447c37d25ec4566db511dead5b70a641fab57088e1cbd24d8236e3bef19-image.png"
    alt="Story"
  />
</Frame>

---

## Add Network

Enable Story's mainnet or testnet for your wallet.

<CardGroup cols={2}>
  <Card
    title="Add Story Mainnet"
    icon="globe"
    href="https://chainid.network/chain/1514/"
  >
    Connect your wallet to Story's mainnet.
  </Card>
  <Card
    title="Add Story 'Aeneid' Testnet"
    icon="globe"
    href="https://chainid.network/chain/1315/"
  >
    Connect your wallet to Story's 'Aeneid' testnet.
  </Card>
</CardGroup>

## Skip everything. Go to the code.

<CardGroup cols={3}>
  <Card
    title="TypeScript Code Example"
    icon="screwdriver-wrench"
    href="https://github.com/storyprotocol/typescript-tutorial/tree/main"
  >
    This is a clone-able quickstart for you to check out. You can clone it
    directly and follow the associated README.
  </Card>
  <Card
    title="React Code Example"
    icon="react"
    href="https://github.com/jacob-tucker/story-developer-sandbox"
  >
    This is a clone-able quickstart for you to check out. You can clone it
    directly and follow the associated README.
  </Card>
  <Card
    title="Smart Contract Code Example"
    icon="scroll"
    href="https://github.com/storyprotocol/story-protocol-boilerplate"
  >
    This is a boilerplate for you to check out. You can clone it directly, study
    the example smart contracts, and follow the associated README for running
    the tests.
  </Card>
</CardGroup>

## Story Network Infra

See [Network Info](/network/network-info/overview) for all RPC, explorer, and faucet info.

## Use our SDKs

Check out the entire [SDK Reference](/sdk-reference) to see an explanation + example for every function in our 🛠️ **TypeScript SDK** (can use this in React as well) and 🐍 **Python SDK**.

We have also built a [🛠️ TypeScript SDK Guide](/developers/typescript-sdk), which is more of a step-by-step walkthrough, with its own in-depth tutorials for popular functions and use cases.

## Deployed Smart Contracts

Check out the addresses for the deployed smart contracts [here](/developers/deployed-smart-contracts). Note that there are two different kinds of contracts:

- [Story Protocol Core](https://github.com/storyprotocol/protocol-core-v1) - This repository contains the core protocol logic, consisting of a thin IP registry (the [IP Asset Registry](/concepts/registry/ip-asset-registry)), a set of [🧱 Modules](/concepts/modules) defining logic around [📜 Licensing](/concepts/licensing-module), [💸 Royalty](/concepts/royalty-module), [❌ Dispute](/concepts/dispute-module), metadata, and a module manager for administering module and user access control.
- [Story Protocol Periphery](https://github.com/storyprotocol/protocol-periphery-v1)- Whereas the core contracts deal with the underlying protocol logic, the periphery contracts deal with protocol extensions that greatly increase UX and simplify IPA management. This is mostly handled through the [📦 SPG](/concepts/spg).

## Use our API

Check out the entire [API Reference](/api-reference) for learning how to use our API. For common things like fetching gas price, average block time, market cap, token price, and more, check out the [Blockscout API](/api-reference/blockscout-api).

## Register IP on Story

Let's start with the most basic question: _"What does it take to register IP on Story in my app? How do I do this?"_

To register IP on Story, you'll first need an NFT. If your IP is an ERC-721 NFT (ex. an Azuki or Pudgy Penguin on Story), you're already set. If not, you must mint an NFT to represent your off-chain IP. And don't worry, we'll help you do this in the following tutorials.

Next you'd register that NFT on Story, ultimately creating an [🧩 IP Asset](/concepts/ip-asset). An "IP Asset" is your IP registered on Story, empowered by:

- all of Story's [🧱 Modules](/concepts/modules) like transparent licensing, automatic royalty payments, and disputing of wrongfully registered IP
- IP protection through the [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license)

Follow the below tutorials to register IP on Story:

<CardGroup cols={2}>
  <Card
    title="Using the SDK"
    icon="thumbs-up"
    href="/developers/typescript-sdk/register-ip-asset"
  >
    Learn how to register IP on Story using the TypeScript SDK.
  </Card>
  <Card
    title="Using the Smart Contracts"
    icon="thumbs-up"
    href="/developers/smart-contracts-guide/register-ip-asset"
  >
    Learn how to register IP on Story using the Smart Contracts.
  </Card>
</CardGroup>

### Difference Between IP Metadata vs. NFT Metadata

A common question we get from developers while registering their IP on Story is: _"What metadata should be/is expected to be attached to the NFT, and then separately, the IP Asset?"_

To answer that question, please see [NFT vs. IP Metadata](/concepts/ip-asset/overview#nft-vs-ip-metadata).

## Licensing Your IP

You may be wondering, _"How do I take advantage of Story's on-chain licensing? How do I make sure my registered IP has a license ready to go?"_

Before you attach any sort of licenses or license terms to your [🧩 IP Asset](/concepts/ip-asset), it would be best to first understand what the [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license) actually is. This "PIL" is what defines the available [License Terms](/concepts/licensing-module/license-terms) on Story, which in turn - when attached to an IP Asset - is what defines how others can use (commercially, create derivatives, etc) that IP Asset.

Our tutorials will show you exactly how to attach license terms to your IP Asset:

<CardGroup cols={2}>
  <Card
    title="Using the SDK"
    icon="thumbs-up"
    href="/developers/typescript-sdk/attach-terms"
  >
    Learn how to attach license terms to your IP on Story using the TypeScript
    SDK.
  </Card>
  <Card
    title="Using the Smart Contracts"
    icon="thumbs-up"
    href="/developers/smart-contracts-guide/attach-terms"
  >
    Learn how to attach license terms to your IP on Story using the Smart
    Contracts.
  </Card>
</CardGroup>

<Note>

For more information on licensing and the terminology behind it, check out the [📜 Licensing Module](/concepts/licensing-module).

</Note>

## Royalties / Revenue Sharing

Now you may be wondering, _"How do I set up automatic royalty sharing between my IP Asset and someone else's? How do I then collect that payment?"_

When you attach [License Terms](/concepts/licensing-module/license-terms) to your [🧩 IP Asset](/concepts/ip-asset), you can specify certain commercial terms such as `commercialRevShare`, which is the amount of revenue (from any source, original & derivative) that must be shared by derivative works with the original IP. See the above section for licensing questions.

If someone then creates a derivative of my IP Asset - which has a `commercialRevShare` of let's say 10% in its license terms - and earns revenue on it, Story enforces the share of this revenue through the [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license) (otherwise resulting in an on-chain dispute using the [❌ Dispute Module](/concepts/dispute-module) or traditional legal arbitration) and then handles the upstream revenue share at the protocol level. If the derivative work earns 100 \$WIP, my original IP Asset could claim 10 \$WIP.

Our tutorials will show you exactly how to claim revenue:

<CardGroup cols={2}>
  <Card
    title="Using the SDK"
    icon="thumbs-up"
    href="/developers/typescript-sdk/claim-revenue"
  >
    Learn how to claim revenue on Story using the TypeScript SDK.
  </Card>
  <Card
    title="Using the Smart Contracts"
    icon="thumbs-up"
    href="/developers/smart-contracts-guide/claim-revenue"
  >
    Learn how to claim revenue on Story using the Smart Contracts.
  </Card>
</CardGroup>

<Note>

For more information on royalty and how it functions, check out the [Royalty Module](/concepts/royalty-module).

</Note>

## Disputing

Now you may be wondering, _"How can I actually dispute someone else's IP if they steal mine, or don't pay me proper revenue for using it?"_

There are two main philosophies/ways to take down "bad" IP.

The first is the [🕵️ Story Attestation Service](/concepts/story-attestation-service). This compromises of a bunch of infringement detection providers that, upon IP registration, automatically review the IP - using their own methods, whether it's AI, manual checking, etc - and flag it if the IP is infringing (ex. registering a picture of Pikachu). Then, any IP discovery platform like the [IP Portal](https://portal.story.foundation) can surface the reviews and let users decide if they want to use an IP or not.

_For example, an IP that has hundreds of flags from different infringement providers probably isn't a legitimate IP._

The second is using the [❌ Dispute Module](/concepts/dispute-module) to officially tag & block IP at the protocol level. Anyone can flag an IP and it will be sent off to arbitration partners like [UMA](https://uma.xyz) who will decide its fate. If officially tagged, an IP can no longer earn revenue or create derivatives via the protocol.

_For example, if someone doesn't make a proper payment for using an IP commercially, or uses it in a disallowed territory, or contains NSFW content._

Our tutorials will show you exactly how to raise a dispute on-chain:

<CardGroup cols={1}>
  <Card
    title="Using the SDK"
    icon="thumbs-up"
    href="/developers/typescript-sdk/raise-dispute"
  >
    Learn how to dispute IP on Story using the TypeScript SDK.
  </Card>
</CardGroup>

<Note>

For more information on filing a dispute on-chain, check out the [❌ Dispute Module](/concepts/dispute-module).

</Note>


# Concepts FAQ

## _"What is the difference between License Tokens, Royalty Tokens, and Revenue Tokens?"_

|                     | License Tokens                                                                                                                                                                                                                                                                                                            | Royalty Tokens                                                                                                                                                                                                   | Revenue Tokens                                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Module**          | [📜 Licensing Module](/concepts/licensing-module)                                                                                                                                                                                                                                                                         | [💸 Royalty Module](/concepts/royalty-module)                                                                                                                                                                    | [💸 Royalty Module](/concepts/royalty-module)                                                                                                                       |
| **Explanation**     | An ERC-721 NFT that gets minted from an IP Asset with specific license terms. It is essentially the license you hold that gives you access to use the associated IP Asset based on the terms in the License Token.<br/><br/>A License Token is burned when it is used to register an IP Asset as a derivative of another. | Each IP Asset has 100,000,000 Royalty Tokens associated, where each token represents the right of whoever owns them to claim 0.000001% of the gains ("_Revenue Tokens_") deposited into the IPA's Royalty Vault. | These are the tokens that are actually used for payment (ex. $WIP).<br/><br/>"_Royalty Tokens_" are used to claim these Revenue Tokens when an IP Asset earns them. |
| **Associated Docs** | [License Token](/concepts/licensing-module/license-token)                                                                                                                                                                                                                                                                 | [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault)                                                                                                                                                    | [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault)                                                                                                       |


# 👥 Grouping Module

The Grouping Module enables the creation and management of group IP Assets, supporting a royalty pool for the group.

<CardGroup cols={1}>
  <Card
    title="GroupingModule.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/grouping/GroupingModule.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Grouping Module.
  </Card>
</CardGroup>

`GroupingModule.sol` is the main entry point for the grouping workflows. It is **stateless** and responsible for:

- Registering a new group
- Adding an IPA to a group
- Removing an IPA from a group
- Checking whether a group contains a specific IPA
- Get the total number of IPAs of a group

## Creating a Group IPA

Similar to the IP Asset registration process, in which you must have a minted NFT to register and then an IP Account is created, the same applies to Group IP Assets. You must have a minted ERC-721 NFT (that represents the ownership of the group) to register as a group, and then when you register, an IP Account for the group is deployed.

Anyone can create a new group.

### Group IP Asset Registry

Similar to how when an IP Asset is created an IP Account is deployed & registered through the [IP Asset Registry](/concepts/registry/ip-asset-registry), the Group's IP Account is deployed and registered through the [Group IP Asset Registry](/concepts/registry/group-ip-asset-registry). This is responsible for managing the registration and tracking of Group IP Assets, including the group members and reward pools.

### The Group's IP Account

The Group IP Account should function equivalently to a normal IP Account, allowing attachment of license terms, creation of derivatives, execution with modules, and other interactions. It also has the same common interface of IP Account. Hence, the Group IP Account can be applied to anywhere where IP Account can be applied.

Besides the common interfaces of IP Account, the Group IP Account has functions to manage the adding/removing of individual IPAs in the group.

## Group Restrictions

Here are the restrictions associated with a Group IPA:

- A derivative IP of a group IP can only have the group IP as its sole parent
- A group IP cannot attach License Terms that use the [Liquid Absolute Percentage (LAP)](/concepts/royalty-module/liquid-absolute-percentage) royalty policy
- An empty group cannot have derivative IPs or mint License Tokens
- A group IP cannot be registered as a derivative
- A group IP can only attach one license term common to all members
- Once a Group gains its first member, the `mintingFee`, `licensingHook`, and `licensingHookData` are frozen. The Group's `commercialRevShare` can only increase
- A group has a maximum size of 1000 members

### Adding & Removing from a Group

- Only the owner of a group can add/remove IP Assets. You **do not** have to own an IP Asset to add it to your group.
- An IPA must include one license terms that matches the license terms of the group (same `licenseTemplate` and `licenseTerms`. An IPA may include other license terms in addition to the one that matches the group.
- When adding an IP to a Group, the Group and IP must have the same `mintingFee` and `licenseHook` in the `LicenseConfig`. Additionally, the Group's commercial revenue share must be greater than or equal to the IP's commercial revenue share.

### Groups Becoming Locked

When a group is locked, IPAs cannot be removed from it, but new IPAs can still be added.

A group IPA is locked when:

1. it has a derivative IP registered OR
2. when someone mints a license token from the group

## Example

Let's say you have an AI bot that uses training data to continuously learn and produce better content. The training data is a Group IPA that is the root, and the AI bot is a derivative IPA of the training data. And any time the AI bot gets paid, the revenue flows back to the training data as revenue.

Now you want to add more training data to the group. Since the group is now locked (you linked a derivative to it), you should register a new Group IPA as a root, and then a new AI bot as a derivative.


# Access Controller

<CardGroup cols={1}>
  <Card
    title="AccessController.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/access/AccessController.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Access Controller.
  </Card>
</CardGroup>

Access Controller manages all permission-related states and permission checks on Story. In particular, it maintains the _Permission Table_ and _Permission Engine_ to process and store permissions. IPAccount permissions are set by the IPAccount owner.

<Frame>
  <img src="/images/concepts/ac-overview.png" alt="Access Controller Diagram" />
</Frame>

## Permission Table

### Permission Record

| IPAccount  | Signer (caller) | To (only module) | Function Sig | Permission |
| ---------- | --------------- | ---------------- | ------------ | ---------- |
| 0x123..111 | 0x789..222      | 0x790..333       | 0xAaAaAaAa   | Allow      |
| 0x123..111 | 0x789..222      | 0x790..333       | 0xBBBBBBBB   | Deny       |
| 0x123..111 | 0x789..222      | 0x790..333       | 0xCCCCCC     | Abstain    |

Each record defines a permission in the form of the **Signer** (caller) calling the **Func** of the **To** (module) on behalf of the **IPAccount**.

The permission field can be set as "Allow," "Deny," or "Abstain." Abstain indicates that the permission decision is determined by the upper-level permission.

### Wildcard

Wildcard is also supported when defining permissions; it defines a permission that applies to multiple modules and/or functions.

With wildcards, users can easily define a whitelist or blacklist of permissions.

| IPAccount  | Signer (caller) | To (module) | Func | Permission |
| :--------- | :-------------- | :---------- | :--- | :--------- |
| 0x123..111 | 0x789..222      | \*          | \*   | Allow      |
| 0x123..111 | 0x789..222      | 0x790..333  | \*   | Deny       |

The above example shows that the signer (0x789...) is unable to invoke any functions of the module (0x790...) on behalf of the IPAccount (0x123...).

In other words, the IPAccount has blacklisted the signer from calling any functions on the module 0x790...333

- Supported wildcards:

| Parameter                  | Wildcard   |
| -------------------------- | ---------- |
| Func                       | bytes4(0)  |
| Addresses (IPAccount / To) | address(0) |

### Permission Prioritization

Specific permissions override general permissions.

| IPAccount  | Signer (caller) | To (module) | Func       | Permission |
| :--------- | :-------------- | :---------- | :--------- | :--------- |
| 0x123..111 | 0x789..222      | \*          | \*         | Allow      |
| 0x123..111 | 0x789..222      | 0x790..333  | \*         | Deny       |
| 0x123..111 | 0x789..222      | 0x790..333  | 0xCCCCDDDD | Allow      |

The above shows that the signer (0x789...) is not allowed to call any functions of the module (0x790...) on behalf of IPAccount (0x123...), except for the function 0xCCCCDDDD

Furthermore, the signer (0x789...) is permitted to call all other modules on behalf of IPAccount (0x123...).

## Call Flows with Access Control

There exist three types of call flows expected by the Access Controller.

1. An IPAccount calls a module directly.
2. A module calls another module directly.
3. A module calls a registry directly.

### IPAccount calling a Module directly

- IPAccount performs a permission check with the Access Controller.
- The module only needs to check if the `msg.sender` is a valid IPAccount.

When calling a module from an IPAccount, the IPAccount performs an access control check with AccessController to determine if the current caller has permission to make the call. In the module, it only needs to check whether the transaction `msg.sender` is a valid IPAccount.

`AccessControlled` provide a modifier `onlyIpAccount()` helps to perform the access control check.

```solidity Solidity
contract MockModule is IModule, AccessControlled {
    function action(string memory param) external view onlyIpAccount() returns (string memory) {
            // do something
    }
}
```

<Frame>
  <img src="/images/concepts/ac-diagram.png" alt="IPAccount calling Module" />
</Frame>

## Module calling another Module

- The callee module needs to perform the authorization check itself.

When a module is called directly from another module, it is responsible for performing the access control check using AccessController. This check determines whether the current caller has permission to make the call to the module.

`AccessControlled` provide a modifier `verifyPermission(address ipAccount)` helps to perform the access control check.

```solidity Solidity
contract MockModule is IModule, AccessControlled {
    function callFromAnotherModule(address ipAccount) external verifyPermission(ipAccount) returns (string memory) {
        if (!IAccessController(accessController).checkPermission(ipAccount, msg.sender, address(this), this.callFromAnotherModule.selector)) {
		        revert Unauthorized();
        }
			  // do something
    }
}
```

<Frame>
  <img src="/images/concepts/ac-diagram-2.png" alt="Module calling Module" />
</Frame>

## Module calling Registry

- The registry performs the authorization check by calling AccessController.
- The registry authorizes modules through set global permission

When a registry is called by a module, it can perform the access control check using AccessController. This check determines whether the callee module has permission to call the registry.

```solidity Solidity
// called by StoryProtocl Admin
IAccessController(accessController).setGlobalPermission(address(0), address(module), address(registry), bytes4(0))) {

```

```solidity Solidity
contract MockRegistry {
    function registerAction() external returns (string memory) {
        if (!IAccessController(accessController).checkPermission(address(0), msg.sender, address(this), this.registerAction.selector)) {
		        revert Unauthorized();
        }
			  // do something
    }
}
```

<Frame>
  <img src="/images/concepts/ac-diagram-3.png" alt="Module calling Registry" />
</Frame>

<Note>

The IPAccount's permissions will be revoked upon transfer of ownership.

The permissions associated with the IPAccount are exclusively linked to its current owner. When the ownership of the IPAccount is transferred to a new individual, the existing permissions granted to the previous owner are automatically revoked. This ensures that only the current, legitimate owner has access to these permissions. If, in the future, the IPAccount ownership is transferred back to the original owner, the permissions that were initially revoked will be reinstated, restoring the original owner's access and control.

</Note>


# 🪝 Hooks

Hooks allow developers to create custom implementations, restrictions, and functionality upon minting [License Tokens](/concepts/licensing-module/license-token) or registering derivatives.

There are two types of hooks:

1. **Licensing Hooks**: allow you to [add custom logic before minting license tokens](/concepts/licensing-module/license-config#logic-that-is-possible-with-license-config) (and registering derivatives). For example, requesting a dynamic price, limiting the amount of license tokens that can be minted, whitelists, etc. Licensing Hooks can be added / modified on a licensing config at any point.
2. **Commercializer Checker Hooks**: similar to Licensing Hooks, however they are directly a part of the license terms and do not change. You also cannot return a custom minting fee.

## Licensing Hooks

These are contracts that implement the `ILicensingHook` interface, which extends from `IModule`.

Most importantly, a Licensing Hook implements a `beforeMintLicenseTokens` function, which is a function that is called before a License Token is minted to implement [custom logic](/concepts/licensing-module/license-config#logic-that-is-possible-with-license-config) and determine the final `totalMintingFee` of that License Token.

<Note>
  View the `ILicensingHook` smart contract
  [here](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/interfaces/modules/licensing/ILicensingHook.sol#L26).
</Note>

```solidity ILicensingHook.sol
/// @notice This function is called when the LicensingModule mints license tokens.
/// @dev The hook can be used to implement various checks and determine the minting price.
/// The hook should revert if the minting is not allowed.
/// @param caller The address of the caller who calling the mintLicenseTokens() function.
/// @param licensorIpId The ID of licensor IP from which issue the license tokens.
/// @param licenseTemplate The address of the license template.
/// @param licenseTermsId The ID of the license terms within the license template,
/// which is used to mint license tokens.
/// @param amount The amount of license tokens to mint.
/// @param receiver The address of the receiver who receive the license tokens.
/// @param hookData The data to be used by the licensing hook.
/// @return totalMintingFee The total minting fee to be paid when minting amount of license tokens.
function beforeMintLicenseTokens(
  address caller,
  address licensorIpId,
  address licenseTemplate,
  uint256 licenseTermsId,
  uint256 amount,
  address receiver,
  bytes calldata hookData
) external returns (uint256 totalMintingFee);
```

Note that it returns the `totalMintingFee`. You may be wondering, "I can set the minting fee in the License Terms, in the `LicenseConfig`, and return a dynamic price from `beforeMintLicenseTokens`. What will the final minting fee actually be?" Here is the priority:

| Minting Fee                                                   | Importance       |
| ------------------------------------------------------------- | ---------------- |
| The `totalMintingFee` returned from `beforeMintLicenseTokens` | Highest Priority |
| The `mintingFee` set in the `LicenseConfig`                   | ⬇️               |
| The `mintingFee` set in the License Terms                     | Lowest Priority  |

<Warning>
  Beware of potentially malicious implementations of external license hooks.
  Please first verify the code of the hook you choose because it may be not
  reviewed or audited by the Story team.
</Warning>

### Available Hooks

Below are available hooks deployed on our protocol that you can use.

<Info>

View the deployed addresses for these hooks [here](/developers/deployed-smart-contracts#license-hooks).

</Info>

| Hook                       | Description                                                                            | Contract Code                                                                                                                   |
| :------------------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| LockLicenseHook            | Stop the minting of license tokens or registering new derivatives.                     | [View here ↗️](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/hooks/LockLicenseHook.sol)            |
| TotalLicenseTokenLimitHook | Set a limit on the amount of license tokens that can be minted, updatable at any time. | [View here ↗️](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/hooks/TotalLicenseTokenLimitHook.sol) |

### Implementing the Hooks

<CardGroup cols={2}>

<Card
  title="SDK Code Example"
  href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/licenses/oneTimeUseLicense.ts"
  icon="code"
>
  A working TypeScript SDK code example that shows how to implement a licensing
  hook. More specifically, how to limit the # of licenses that can be minted.
</Card>

<Card
  title="Solidity Code Example"
  href="https://github.com/storyprotocol/protocol-periphery-v1/blob/main/test/hooks/TotalLicenseTokenLimitHook.t.sol"
  icon="code"
>
  A working Solidity code example that shows how to implement a licensing hook.
  More specifically, how to limit the # of licenses that can be minted.
</Card>

</CardGroup>

Licensing Hooks are ultimately a smart contract that implements the `ILicensingHook` interface. You can view the interface [here](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/interfaces/ILicensingHook.sol). We have a few Licensing Hooks deployed already (view the chart above).

In order to actually use a Licensing Hook, you must set it in the Licensing Config, which is basically a set of configurations that you set on License Terms when attaching terms to an IP Asset.

<Steps>
  <Step title="Create Licensing Config">
    First you have to create a Licensing Config:

    ```typescript {6-8}
    import { LicensingConfig } from '@story-protocol/core-sdk';

    const licensingConfig: LicensingConfig = {
        isSet: true,
        mintingFee: 0n,
        // address of TotalLicenseTokenLimitHook
        // from https://docs.story.foundation/developers/deployed-smart-contracts
        licensingHook: '0xba8E30d9EB784Badc2aF610F56d99d212BC2A90c',
        hookData: zeroAddress,
        commercialRevShare: 0,
        disabled: false,
        expectMinimumGroupRewardShare: 0,
        expectGroupRewardPool: zeroAddress,
    }
    ```

  </Step>
  <Step title="Set the Licensing Config">
    Next, we'll set the Licensing Config on the License Terms. In the following example, we'll show this happening upon registering the IP Asset:

<Tip>
  This code snippet requires a bit of setup, and it meant for developers who
  already understand how to setup the TypeScript SDK. If you want to learn more,
  check out the [working code
  example](https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/licenses/oneTimeUseLicense.ts).
</Tip>

<Note>

This uses the `mintAndRegisterIpAssetWithPilTerms` method found [here](/sdk-reference/ipasset#mintandregisteripassetwithpilterms).

</Note>

    ```typescript {6-7}
    const response = await client.ipAsset.mintAndRegisterIpAssetWithPilTerms({
        spgNftContract: '0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc', // public spg contract for ease-of-use
        licenseTermsData: [
            {
                terms: { defaultMintingFee: 0, commercialUse: true, ... }, // dummy license terms
                // set the licensing config here
                licensingConfig: licensingConfig
            },
        ],
        ipMetadata: {
            ipMetadataURI: 'test-uri',
            ipMetadataHash: toHex('test-metadata-hash', { size: 32 }),
            nftMetadataHash: toHex('test-nft-metadata-hash', { size: 32 }),
            nftMetadataURI: 'test-nft-uri',
        },
        txOptions: { waitForTransaction: true },
    })
    ```

  </Step>
  <Step title="Set the Limit to 1">
    Now that we have set the Licensing Config on our terms, we can call the `setTotalLicenseTokenLimit` function on the hook and set the max # of licenses that can be minted to 1.

    <Note>
    There is no Story SDK method for this, so you'll have to use viem's `writeContract` method.
    </Note>

    ```typescript
    import { totalLicenseTokenLimitHook } from './abi/totalLicenseTokenLimitHook'

    const { request } = await publicClient.simulateContract({
        // address of TotalLicenseTokenLimitHook
        // from https://docs.story.foundation/developers/deployed-smart-contracts
        address: '0xba8E30d9EB784Badc2aF610F56d99d212BC2A90c',
        abi: totalLicenseTokenLimitHook,
        functionName: 'setTotalLicenseTokenLimit',
        args: [
            response.ipId, // ipId from the step above
            '0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316', // the address of PILicenseTemplate from https://docs.story.foundation/developers/deployed-smart-contracts
            response.licenseTermsIds![0], // licenseTermsId
            1n, // limit (as BigInt)
        ],
        account: account, // Specify the account to use for permission checking
    })

    // Prepare transaction
    const hash = await walletClient.writeContract({ ...request, account: account })

    // Wait for transaction to be mined
    const receipt = await publicClient.waitForTransactionReceipt({
        hash,
    })
    ```

  </Step>
</Steps>

## Commercializer Checker Hooks

<Warning>

Documentation coming soon. If you have questions in the meantime, ask in the [Builder's Discord](https://discord.gg/storybuilders).

</Warning>


# 👀 Metadata Module

The Metadata Module enables the creation, management, and retrieval of metadata for IP Assets within Story. It consists of two main components: the CoreMetadataModule for writing operations and the CoreMetadataViewModule for reading operations.

<CardGroup cols={2}>
  <Card
    title="CoreMetadataModule.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/metadata/CoreMetadataModule.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Core Metadata Module.
  </Card>
  <Card
    title="CoreMetadataViewModule.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/metadata/CoreMetadataViewModule.sol"
    icon="eye"
    color="#92ccb0"
  >
    View the smart contract for the Core Metadata View Module.
  </Card>
</CardGroup>

## Metadata Structure

The metadata for an IP Asset includes:

- **metadataURI**: A URI pointing to the detailed metadata of the IP Asset
- **metadataHash**: A hash of the metadata for verification purposes
- **nftTokenURI**: A URI pointing to the metadata of the NFT associated with the IP Asset
- **nftMetadataHash**: A hash of the NFT metadata for verification
- **registrationDate**: When the IP Asset was registered
- **owner**: The current owner of the IP Asset

## CoreMetadataModule (Write Operations)

`CoreMetadataModule.sol` is responsible for writing and updating metadata for IP Assets. It is **stateful** and provides the following key functionalities:

- Setting and updating metadata URIs for IP Assets
- Setting and updating NFT token URIs
- Freezing metadata to make it immutable
- Managing metadata hashes for verification

The module stores metadata in the IP Asset's storage, making it accessible to other modules and applications.

### Setting Metadata

To set metadata for an IP Asset, the caller must have appropriate permissions. The CoreMetadataModule provides several functions for setting metadata:

- `setMetadataURI`: Sets just the IP metadataURI and its hash
- `updateNftTokenURI`: Updates the NFT token URI and its hash
- `setAll`: Sets all metadata attributes at once

Here is an example:

```solidity solidity
// Set the metadata URI and hash
coreMetadataModule.setMetadataURI(
    ipAssetAddress,
    "https://example.com/metadata/asset123",
    keccak256("metadata content hash")
);
```

### Freezing Metadata

The CoreMetadataModule allows IP Asset owners to freeze metadata, making it immutable. Once frozen, the metadata cannot be changed, ensuring the permanence of the IP Asset's information.

To freeze metadata:

```solidity solidity
// Make the metadata immutable
coreMetadataModule.freezeMetadata(ipAssetAddress);
```

You can check if metadata is frozen using:

```solidity solidity
// Check if metadata is frozen
bool isFrozen = coreMetadataModule.isMetadataFrozen(ipAssetAddress);
```

## CoreMetadataViewModule (Read Operations)

`CoreMetadataViewModule.sol` is a read-only module that provides access to the metadata stored by the CoreMetadataModule. It follows the View Module pattern and offers these key functionalities:

- Retrieving metadata URIs and hashes
- Retrieving NFT token URIs and metadata hashes
- Generating formatted JSON strings with all metadata attributes
- Checking registration dates and ownership information

### Retrieving Metadata

The CoreMetadataViewModule provides various functions to retrieve metadata:

- `getCoreMetadata`: Returns all metadata in a single struct
- `getMetadataURI`: Returns just the metadata URI
- `getNftTokenURI`: Returns the NFT token URI
- `getJsonString`: Returns a formatted JSON string with all metadata

Here is an example:

```solidity solidity
// Get the metadata URI
string memory uri = coreMetadataViewModule.getMetadataURI(ipAssetAddress);

// Get all metadata in one call
CoreMetadata memory metadata = coreMetadataViewModule.getCoreMetadata(ipAssetAddress);

// Get a JSON representation of all metadata
string memory jsonMetadata = coreMetadataViewModule.getJsonString(ipAssetAddress);
```

The Metadata Module provides a robust system for managing IP Asset metadata, ensuring that important information about intellectual property is properly recorded, accessible, and can be made immutable when needed.


# IP Modifications & Restrictions

# IP Asset Modifications

IP Assets can be modified/customized a few ways. For example, by [setting the License Config](/concepts/licensing-module/license-config) which allows you to change a few things as you'll see below, changing its metadata, and more. These things can **always be changed unless there is a certain condition**.

| Action                      | Conditions                                                                                                                                                                                                                            | Via The...                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Modify License Minting Fee  | You can **increase** the minting fee. You **cannot** decrease it.                                                                                                                                                                     | [License Config](/concepts/licensing-module/license-config)                                                                             |
| Modify Licensing Hook       | The hook must be whitelisted in the [Module Registry](/concepts/registry/module-registry).                                                                                                                                            | [License Config](/concepts/licensing-module/license-config)                                                                             |
| Modify `commercialRevShare` | You can **increase** the rev share percentage. You **cannot** decrease it. <br/><br/>However, you **can** set it to 0 to disable the overwrite.                                                                                       | [License Config](/concepts/licensing-module/license-config)                                                                             |
| Disable/Enable the License  | License can be disabled or re-enabled at any time.<br/><br/>_Note that disabling a license disallows future licenses from being minted, but does not affect existing ones._                                                           | [License Config](/concepts/licensing-module/license-config)                                                                             |
| Modify Metadata             | Cannot modify if the metadata is **frozen**. This is done by calling `freezeMetadata` in the [CoreMetadataModule.sol](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/metadata/CoreMetadataModule.sol). | [CoreMetadataModule.sol](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/metadata/CoreMetadataModule.sol) |

## License Hook Modifications

The IP can be further customized or modified using the [License Hook](/concepts/hooks#licensing-hooks). This is a function that gets set within the License Config that gets called before a [License Token](/concepts/licensing-module/license-token) (or more simply, a "license") is minted. There are various features you can implement with the License Hook, and are **always modifiable**:

| Feature             | Description                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Dynamic License Fee | You can dynamically set the price of a license. For example, it can be updated dynamically via bonding curve logic. |
| Total # of Licenses | You can abort the function based on a maximum number of license tokens that can be minted.                          |
| Specific Receivers  | You can restrict minting of license to a specific receiver.                                                         |
| More...             | Additional licensing hook features can be implemented as required.                                                  |

# Group IPA Restrictions

See [👥 Group IPA Restrictions](/concepts/grouping-module#group-restrictions) for more information.


# ⚙️ IP Account

<Note>
Skip the Read

Get a quick 2-minute overview of IP Accounts [here](https://twitter.com/jacobmtucker/status/1787603252198134234).

</Note>

When an [🧩 IP Asset](/concepts/ip-asset/overview) is registered, it is given an associated **IP Account**. An IP Account is a modified ERC-6551 (Token Bound Account) implementation. It is a separate contract bound to the IP Asset for controlling permissions around interactions with Story's modules or storing the IP's associated data. Upon registration, an IP Asset is assigned a unique ID. This ID is the address of the IP Account that is bound to the IP Asset.

<img src="/images/concepts/ip-account.png" alt="IP Account Diagram" />

An IP Account mainly does two things:

1. Stores comprehensive IP-related data, including metadata and ownership details of associated assets such as the License Tokens or Royalty Tokens that are created from the IP.
2. Facilitates the utilization of this data by various modules. These modules interact with and contribute to the IP Account, creating and storing data. For example, licensing, revenue/royalty sharing, remixing, disputing an IP, and other modules are made possible due to the IP Account's programmability.

<Note>
If the underlying NFT is transferred, the new owner is also automatically the owner of the associated IP Asset & IP Account.

</Note>

## `execute` and `executeWithSig`

A key feature of IP Account is the generic `execute()` function, which allows calling arbitrary modules within Story via encoded bytes data (thus extensible for future modules). Additionally, there is a `executeWithSig()` function that enables users to sign transactions and have others execute on their behalf for seamless UX.


# 📝 IPA Metadata Standard

<Warning>
  We are still figuring out the best way to define an IPA Metadata Standard. For
  the sake of transparency, the following document is our thoughts so far but is
  subject to change as we release future versions.
</Warning>

<CardGroup cols={2}>
  <Card title="Official Ippy IP" href="https://explorer.story.foundation/ipa/0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42" icon="house">
    Check out the official Ippy IP, which has both NFT & IP metadata.
  </Card>

  <Card title="How to Add Metadata to an IP Asset" href="/concepts/ip-asset/overview#nft-vs-ip-metadata" icon="computer">
    Learn how to actually add the IP metadata discussed here to your IP Asset with an explanation or completed code example.
  </Card>
</CardGroup>

This is the JSON metadata that is associated with an IP Asset, and gets stored inside of an IP Account. You must call `setMetadata(...)` inside of the IP Account in order to set the metadata, and then call `metadata()` to read it.

## Attributes & Structure

Below are the important attributes you should provide in your IP metadata. Under the **Required For** column is what the specific field is required for:

- 🔍 Story Explorer - this field will help display your IP on the Story Explorer
- 🕵️ [Commercial Infringement Check](/concepts/story-attestation-service) - this field is required if your IP is **commercial** (that is, has `commercialUse = true` license terms attached). We will use these fields to run an infringement check on your IP.
  - See [current limitations](/concepts/story-attestation-service#current-limitations).
- 🤖 AI Agents - used for displaying metadata associated with AI Agents

| Property Name | Type          | Description                                                                                                                                                                                     | Required For                                                            |
| ------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `title`       | `string`      | Title of the IP                                                                                                                                                                                 | 🔍 Story Explorer                                                       |
| `description` | `string`      | Description of the IP                                                                                                                                                                           | 🔍 Story Explorer                                                       |
| `createdAt`   | `string`      | Date/Time that the IP was created (either ISO8601 or unix format). This field can be used to specify historical dates that aren't on-chain. For example, Harry Potter was published on June 26. | 🔍 Story Explorer                                                       |
| `image`       | `string`      | An image for your IP. **For audio assets, the recommended thumbnail aspect ratio is 1:1. For video assets, it is 16:9.**                                                                        | 🔍 Story Explorer                                                       |
| `imageHash`   | `string`      | Hash of your `image` using SHA-256 hashing algorithm. See [here](#hashing-content) for how that is done.                                                                                        | 🔍 Story Explorer                                                       |
| `creators`    | `IpCreator[]` | An array of information about the creators. [See the type defined below](#type-definitions)                                                                                                     | 🔍 Story Explorer                                                       |
| `mediaUrl`    | `string`      | Used for infringement checking, points to the actual media (ex. image or audio). **For audio assets, the recommended thumbnail aspect ratio is 1:1. For video assets, it is 16:9.**             | 🕵️ [Commercial Infringement Check](/concepts/story-attestation-service) |
| `mediaHash`   | `string`      | Hashed string of the media using SHA-256 hashing algorithm. See [here](#hashing-content) for how that is done.                                                                                  | 🕵️ [Commercial Infringement Check](/concepts/story-attestation-service) |
| `mediaType`   | `string`      | Type of media (audio, video, image), based on [mimeType](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types). See the allowed media types [here](#media-types).          | 🕵️ [Commercial Infringement Check](/concepts/story-attestation-service) |
| `aiMetadata`  | `AIMetadata`  | Used for registering & displaying AI Agent Metadata. [See the type defined below](#type-definitions)                                                                                            | 🤖 AI Agents                                                            |
| N/A           | N/A           | You can include other values as well.                                                                                                                                                           | N/A                                                                     |

### Type Definitions

Here are the type definitions for the complex types used in the metadata:

<CodeGroup>

```typescript IpCreator
type IpCreator = {
  name: string;
  address: Address;
  contributionPercent: number; // add up to 100
  description?: string;
  image?: string;
  socialMedia?: IpCreatorSocial[];
  role?: string;
};

type IpCreatorSocial = {
  platform: string;
  url: string;
};
```

```typescript AIMetadata
type AIMetadata = {
  // this can be any character file you want
  // example: https://github.com/elizaOS/characterfile/blob/main/examples/example.character.json
  characterFileUrl: string;
  characterFileHash: string;
};
```

</CodeGroup>

### Media Types

The following media types are allowed for the `mediaType` field:

| Media Type        | Description           |
| ----------------- | --------------------- |
| `image/jpeg`      | JPEG image            |
| `image/png`       | PNG image             |
| `image/apng`      | Animated PNG image    |
| `image/avif`      | AV1 Image File Format |
| `image/gif`       | GIF image             |
| `image/svg+xml`   | SVG image             |
| `image/webp`      | WebP image            |
| `audio/wav`       | WAV audio             |
| `audio/mpeg`      | MP3 audio             |
| `audio/flac`      | FLAC audio            |
| `audio/aac`       | AAC audio             |
| `audio/ogg`       | OGG audio             |
| `audio/mp4`       | MP4 audio             |
| `audio/x-aiff`    | AIFF audio            |
| `audio/x-ms-wma`  | WMA audio             |
| `audio/opus`      | Opus audio            |
| `video/mp4`       | MP4 video             |
| `video/webm`      | WebM video            |
| `video/quicktime` | QuickTime video       |

### Hashing Content

To hash content for the `imageHash` or `mediaHash` fields, you can use the SHA-256 hashing algorithm. Here's an example of how to do this in JavaScript:

<CodeGroup>

```typescript TypeScript
import { toHex, Hex } from "viem";

// get hash from a file
async function getFileHash(file: File): Promise<Hex> {
  const arrayBuffer = await file.arrayBuffer();
  const hashBuffer = await crypto.subtle.digest("SHA-256", arrayBuffer);
  return toHex(new Uint8Array(hashBuffer), { size: 32 });
}

// get hash from a url
async function getHashFromUrl(url: string): Promise<Hex> {
  const response = await axios.get(url, { responseType: "arraybuffer" });
  const buffer = Buffer.from(response.data);
  return "0x" + createHash("sha256").update(buffer).digest("hex");
}
```

```shell Shell
shasum -a 256 myfile.jpg
```

</CodeGroup>

### Example Use Cases

<Tabs>

<Tab title="Ippy Mascot">

This is the official Ippy mascot that is registered on mainnet. You can view it on our protocol explorer [here](https://explorer.story.foundation/ipa/0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42).

```json
{
  "title": "Ippy",
  "description": "Official mascot of Story.",
  "createdAt": "1728401700",
  "image": "https://ipfs.io/ipfs/QmSamy4zqP91X42k6wS7kLJQVzuYJuW2EN94couPaq82A8",
  "imageHash": "0x21937ba9d821cb0306c7f1a1a2cc5a257509f228ea6abccc9af1a67dd754af6e",
  "mediaUrl": "https://ipfs.io/ipfs/QmSamy4zqP91X42k6wS7kLJQVzuYJuW2EN94couPaq82A8",
  "mediaHash": "0x21937ba9d821cb0306c7f1a1a2cc5a257509f228ea6abccc9af1a67dd754af6e",
  "mediaType": "image/png",
  "creators": [
    {
      "name": "Story Foundation",
      "address": "0x67ee74EE04A0E6d14Ca6C27428B27F3EFd5CD084",
      "description": "The World's IP Blockchain",
      "contributionPercent": 100,
      "socialMedia": [
        {
          "platform": "Twitter",
          "url": "https://twitter.com/storyprotocol"
        },
        {
          "platform": "Telegram",
          "url": "https://t.me/StoryAnnouncements"
        },
        {
          "platform": "Website",
          "url": "https://story.foundation"
        },
        {
          "platform": "Discord",
          "url": "https://discord.gg/storyprotocol"
        },
        {
          "platform": "YouTube",
          "url": "https://youtube.com/@storyFDN"
        }
      ]
    }
  ],
  "tags": ["Ippy", "Story", "Story Mascot", "Mascot", "Official"], // experimental field
  "ipType": "Character" // experimental field
}
```

</Tab>

<Tab title="Music">
This is an example song generated on [Suno](https://suno.com/) and registered on our testnet. View the below example [on our protocol explorer](https://aeneid.explorer.story.foundation/ipa/0x3E5b9e540a531da38760CC32E2f52b174EC5Fce8).

```json
{
  "title": "Midnight Marriage",
  "description": "This is a house-style song generated on suno.",
  "createdAt": "1740005219",
  "creators": [
    {
      "name": "Jacob Tucker",
      "address": "0xA2f9Cf1E40D7b03aB81e34BC50f0A8c67B4e9112",
      "contributionPercent": 100
    }
  ],
  "image": "https://cdn2.suno.ai/image_large_8bcba6bc-3f60-4921-b148-f32a59086a4c.jpeg",
  "imageHash": "0xc404730cdcdf7e5e54e8f16bc6687f97c6578a296f4a21b452d8a6ecabd61bcc",
  "mediaUrl": "https://cdn1.suno.ai/dcd3076f-3aa5-400b-ba5d-87d30f27c311.mp3",
  "mediaHash": "0xb52a44f53b2485ba772bd4857a443e1fb942cf5dda73c870e2d2238ecd607aee",
  "mediaType": "audio/mpeg"
}
```

</Tab>

<Tab title="AI Agent">
The main difference here is you should supply `aiMetadata` with a character file. You can provide any character file you want, or use [this ElizaOS example](https://github.com/elizaOS/characterfile/blob/main/examples/example.character.json) as a template.

View the below example [on our protocol explorer](https://aeneid.explorer.story.foundation/ipa/0x49614De8b2b02C790708243F268Af50979D568d4).

```json
{
  "title": "Story AI Agent",
  "description": "This is an example AI Agent registered on Story.",
  "createdAt": "1740005219",
  "creators": [
    {
      "name": "Jacob Tucker",
      "address": "0xA2f9Cf1E40D7b03aB81e34BC50f0A8c67B4e9112",
      "contributionPercent": 100
    }
  ],
  "image": "https://ipfs.io/ipfs/bafybeigi3k77t5h5aefwpzvx3uiomuavdvqwn5rb5uhd7i7xcq466wvute",
  "imageHash": "0x64ccc40de203f218d16bb90878ecca4338e566ab329bf7be906493ce77b1551a",
  "mediaUrl": "https://ipfs.io/ipfs/bafybeigi3k77t5h5aefwpzvx3uiomuavdvqwn5rb5uhd7i7xcq466wvute",
  "mediaHash": "0x64ccc40de203f218d16bb90878ecca4338e566ab329bf7be906493ce77b1551a",
  "mediaType": "image/webp",
  "aiMetadata": {
    "characterFileUrl": "https://ipfs.io/ipfs/bafkreic6eu4hlnwx46soib62rgkhhmlieko67dggu6bzk7bvtfusqsknfu",
    "characterFileHash": "0x5e253875b6d7e7a4e407da899473b168229def8cc6a783957c35996928494d2d"
  }
}
```

</Tab>

</Tabs>

## Optional Properties

The following properties are optional but can provide additional context about your IP Asset:

<Warning>
  We are still figuring out the best way to define an IPA Metadata Standard. The
  fields below are bound to change or be removed at some point.
</Warning>

| Property Name    | Type               | Description                                                                                                                                                    |
| :--------------- | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ipType`         | `string`           | Type of the IP Asset, can be defined arbitrarily by the creator. I.e. "character", "chapter", "location", "items", "music", etc                                |
| `relationships`  | `IpRelationship[]` | The detailed relationship info with the IPA's direct parent asset, such as `APPEARS_IN`, `FINETUNED_FROM`, etc. See more examples [here](#relationship-types). |
| `watermarkImage` | `string`           | A separate image with your watermark already applied. This way apps choosing to use it can render this version of the image (with watermark applied).          |
| `media`          | `IpMedia[]`        | An array of supporting media. Media type defined below                                                                                                         |
| `app`            | `StoryApp`         | This is assigned to verified application from Story directly (on a request basis so far). We will map each App ID to a name                                    |
| `tags`           | `string[]`         | Any tags that can help surface this IPA                                                                                                                        |
| `robotTerms`     | `IPRobotTerms`     | Allows you to set Do Not Train for a specific agent                                                                                                            |
| N/A              | N/A                | You can include other values as well.                                                                                                                          |

### Type Definitions

<CodeGroup>
```typescript IpRelationship
type IpRelationship = {
  parentIpId: Address;
  type: string; // see "Relationship Types" docs below
};
````

```typescript IpMedia
type IpMedia = {
  name: string;
  url: string;
  mimeType: string;
};
```

```typescript StoryApp
type StoryApp = {
  id: string;
  name: string;
  website: string;
  action?: string;
};
```

```typescript IPRobotTerms
type IPRobotTerms = {
  userAgent: string;
  allow: string;
};
```

</CodeGroup>

### Relationship Types

The different relationship types that can be used for the `relationships` attribute.

#### Story Relationships

1. **APPEARS_IN** - A character APPEARS_IN a chapter.

2. **BELONGS_TO** - A chapter BELONGS_TO a book.

3. **PART_OF** - A book is PART_OF a series.

4. **CONTINUES_FROM** - A chapter CONTINUES_FROM the previous one.

5. **LEADS_TO** - An event LEADS_TO a consequence.

6. **FORESHADOWS** - An event FORESHADOWS future developments.

7. **CONFLICTS_WITH** - A character CONFLICTS_WITH another character.

8. **RESULTS_IN** - A decision RESULTS_IN a significant change.

9. **DEPENDS_ON** - A subplot DEPENDS_ON the main plot.

10. **SETS_UP** - A prologue SETS_UP the story.

11. **FOLLOWS_FROM** - A chapter FOLLOWS_FROM the previous one.

12. **REVEALS_THAT** - A twist REVEALS_THAT something unexpected occurred.

13. **DEVELOPS_OVER** - A character DEVELOPS_OVER the course of the story.

14. **INTRODUCES** - A chapter INTRODUCES a new character or element.

15. **RESOLVES_IN** - A conflict RESOLVES_IN a particular outcome.

16. **CONNECTS_TO** - A theme CONNECTS_TO the main narrative.

17. **RELATES_TO** - A subplot RELATES_TO the central theme.

18. **TRANSITIONS_FROM** - A scene TRANSITIONS_FROM one setting to another.

19. **INTERACTED_WITH** - A character INTERACTED_WITH another character.

20. **LEADS_INTO** - An event LEADS_INTO the climax.?\
    **PARALLEL - story** happening in parallel or around the same timeframe

#### AI Relationships

1. **TRAINED_ON** - A model is TRAINED_ON a dataset.

2. **FINETUNED_FROM** - A model is FINETUNED_FROM a base model.

3. **GENERATED_FROM** - An image is GENERATED_FROM a fine-tuned model.

4. **REQUIRES_DATA** - A model REQUIRES_DATA for training.

5. **BASED_ON** - A remix is BASED_ON a specific workflow.

6. **INFLUENCES** - Sample data INFLUENCES model output.

7. **CREATES** - A pipeline CREATES a fine-tuned model.

8. **UTILIZES** - A workflow UTILIZES a base model.

9. **DERIVED_FROM** - A fine-tuned model is DERIVED_FROM a base model.

10. **PRODUCES** - A model PRODUCES generated images.

11. **MODIFIES** - A remix MODIFIES the base workflow.

12. **REFERENCES** - An AI-generated image REFERENCES original data.

13. **OPTIMIZED_BY** - A model is OPTIMIZED_BY specific algorithms.

14. **INHERITS** - A fine-tuned model INHERITS features from the base model.

15. **APPLIES_TO** - A fine-tuning process APPLIES_TO a model.

16. **COMBINES** - A remix COMBINES elements from multiple datasets.

17. **GENERATES_VARIANTS** - A model GENERATES_VARIANTS of an image.

18. **EXPANDS_ON** - A fine-tuning process EXPANDS_ON base capabilities.

19. **CONFIGURES** - A workflow CONFIGURES a model’s parameters.

20. **ADAPTS_TO** - A fine-tuned model ADAPTS_TO new data.


# 🧩 IP Asset

<Note>
Skip the Read

Get a quick 1-minute overview of IP Assets [here](https://twitter.com/jacobmtucker/status/1785765362744889410).

</Note>

IP Assets are the foundational programmable IP metadata on Story. Each IP Asset is an on-chain ERC-721 NFT (representing an IP). If your IP is off-chain, you would simply mint an ERC-721 NFT to represent that IP first, and then register it as an IP Asset.

When an IP Asset is created, an associated [⚙️ IP Account](/concepts/ip-asset/ip-account) is deployed, which is a modified ERC-6551 (Token Bound Account) implementation. It is a separate contract bound to the IP Asset for controlling permissions around interactions with Story's modules or storing the IP's associated data.

## Registering an IP Asset

An IP Asset is created by registering an ERC-721 NFT into Story's global [IP Asset Registry](/concepts/registry/ip-asset-registry).

If you'd like to jump into code examples/tutorials, please see [How to Register IP on Story](/developers/tutorials/how-to-register-ip-on-story).

## NFT vs. IP Metadata

On Story, your IP is an NFT that gets registered on the protocol as an IP Asset. However, both NFTs and IP Assets have their own metadata you can set, so what's the difference?

|         | Standard                                                                   | What is it?                                                                                                                                |
| :------ | :------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **NFT** | [Opensea ERC721 Standard](https://docs.opensea.io/docs/metadata-standards) | Things like `name`, `description`, `image`, `attributes`, `animation_url`, etc                                                             |
| **IP**  | [📝 IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard)       | More specific to Story, this includes necessary information about the underlying content for infringement checks, authors of the work, etc |

All other metadata, such as the ownership, legal, and economic details of an IP Asset are handled by our protocol directly. For example, the protocol stores data associated with parent-child relationships through the [📜 Licensing Module](/concepts/licensing-module/overview), the monetary flow between IP Assets through the [💸 Royalty Module](/concepts/royalty-module/overview), and the legal constraints/permissions of an IP Asset with the [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license/overview).

### Adding NFT & IP Metadata to IP Asset

<CardGroup cols={2}>
  <Card title="SDK Completed Code Example" href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/registration/register.ts" icon="computer">
    Jump to the code and see a completed code example of adding NFT & IP metadata to an IP Asset
  </Card>

  <Card title="SDK Explanation" href="/developers/typescript-sdk/register-ip-asset" icon="file">
    Learn how to add metadata to your IP Asset with a step-by-step explanation.
  </Card>
</CardGroup>

In practice, whether you are using the SDK or our smart contract directly, our protocol asks you to provide 4 different parameters:

- View the `WorkflowStructs.sol` contract [here](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/lib/WorkflowStructs.sol).

```solidity WorkflowStructs.sol
/// @notice Struct for metadata for NFT minting and IP registration.
/// @dev Leave the nftMetadataURI empty if not minting an NFT.
/// @param ipMetadataURI The URI of the metadata for the IP.
/// @param ipMetadataHash The hash of the metadata for the IP.
/// @param nftMetadataURI The URI of the metadata for the NFT.
/// @param nftMetadataHash The hash of the metadata for the IP NFT.
struct IPMetadata {
  string ipMetadataURI;
  bytes32 ipMetadataHash;
  string nftMetadataURI;
  bytes32 nftMetadataHash;
}
```

- `ipMetadataURI` - a URI pointing to a JSON object that follows the [📝 IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard)
- `ipMetadataHash` - hash of the `ipMetadataURI` JSON object
- `nftMetadataURI` - a URI pointing to a JSON object that follows the [Opensea ERC721 Standard](https://docs.opensea.io/docs/metadata-standards)
- `nftMetadataHash` - hash of the `nftMetadataURI` JSON object


# UMA Arbitration Policy

<Note>
  For detailed information on how UMA's dispute resolution works, [visit their
  website](https://uma.xyz/).
</Note>

This arbitration policy is a dispute resolution mechanism that uses UMA’s optimistic oracle to verify disputes. Below we share a high-level overview of how the UMA dispute process works.

## Smart Contract Flow Diagram

<img src="/images/concepts/uma-1.png" alt="UMA Arbitration Flow" />

<Steps>

<Step title="Raise Dispute">
The first step to initiate a dispute against an IP Asset is to call the `raiseDispute` function on [DisputeModule.sol](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/dispute/DisputeModule.sol). This function will in turn call `assertTruth` on UMA's `OptimisticOracleV3.sol`. To initiate a dispute the dispute initiator will need to post a bond of at least the minimum bond defined by UMA for the selected currency. Note that this bond will be lost if the dispute is deemed not verifiably correct by the oracle.

<Note>
  UMA will be adjusting the $IP bond size as the IP price fluctuates. The
  correct way to obtain the current bond size is via `getMinimumBond()` on
  `OptimisticOracleV3.sol` (OOV3), found on our [aeneid
  testnet](https://aeneid.storyscan.io/address/0xABac6a158431edED06EE6cba37eDE8779F599eE4?tab=read_write_contract#0x4360af3d)
  and
  [mainnet](https://www.storyscan.io/address/0x8EF424F90C6BC1b98153A09c0Cac5072545793e8?tab=read_write_contract#0x4360af3d).
</Note>

After this step, the dispute will be “open” to be countered/appealed by other users. If there is no counter/appeal, UMA rules define that the IP will be considered to be infringing.

```sol DisputeModule.sol
/// @notice Raises a dispute on a given ipId
/// @param targetIpId The ipId that is the target of the dispute
/// @param disputeEvidenceHash The hash pointing to the dispute evidence - this could be an IPFS CID 				converted to a bytes32 hash. This is the document with the proof that UMA reviewers will potentially read
/// @param targetTag The target tag of the dispute
/// @param data The data to initialize the policy - here you can do abi.encode of liveness, token address 	and bond amount
/// @return disputeId The id of the newly raised dispute
function raiseDispute(
 address targetIpId,
 bytes32 disputeEvidenceHash,
 bytes32 targetTag,
 bytes calldata data
) external returns (uint256 disputeId);
```

</Step>

<Step title="(Optional) Dispute Assertion / Counter Dispute / Make Appeal">
After the `raiseDispute` call there is a period of time called "liveness" in which a counter dispute/appeal can be submitted. The liveness period is split in two parts: (i) the first part of the liveness period in which only the IP owner can counter dispute/appeal and (ii) a second part in which any address can counter dispute/appeal - which can be done by calling `disputeAssertion` on `ArbitrationPolicyUMA.sol`. To counter a dispute the caller will need to post a bond of the same amount and currency that was used by the dispute initiator when raising a dispute. Note that this bond will be lost if the original dispute is deemed to be verifiably correct by the oracle.

After this step, the dispute is escalated and will be reviewed by external party UMA.

```sol ArbitrationPolicyUMA.sol
/// @notice Allows the IP that was targeted with a dispute to dispute the assertion while providing counter evidence
/// @param assertionId The identifier of the assertion that was disputed
/// @param counterEvidenceHash The hash of the counter evidence
function disputeAssertion(bytes32 assertionId, bytes32 counterEvidenceHash) external;

/// @notice Returns the assertion id for a given dispute id
/// @param disputeId The dispute id
function disputeIdToAssertionId(uint256 disputeId) external view returns (bytes32);
```

</Step>

<Step title="(If step 2 happened) UMA Reviewers Judge the Dispute">
  UMA reviewers judge the dispute. On this step the user just has to wait until
  the UMA reviewers make the dispute judgement. This step could take 48-96
  hours.
</Step>

<Step title="Settle Assertion">
This step is expected to be automatic as UMA runs a bot that calls `settleAssertion` which in turn distributes the bonds back to the address that wins the dispute.

1.  If nobody submitted a counter dispute then when the liveness period is over, any address can call `settleAssertion` on UMA's `OptimisticOracleV3.sol`.
2.  If somebody has submitted a counter dispute/appeal before the liveness period is over, then the dispute is escalated to UMA reviewers who will judge and make a decision on whether the IP is infringing or not. After the decision has been made, then any address can call `settleAssertion` on UMA's `OptimisticOracleV3.sol`.

</Step>

</Steps>

## Dispute Evidence Submission Guidelines

When raising a dispute or making a counter dispute, both parties can submit dispute evidence. Dispute evidence refers to a text document that oracle participants will use & read from to make a judgement on the dispute.

### Burden of Proof

In all disputes with UMA arbitration policy, the burden of proof lies with the party creating the dispute. This means that the disputer must provide clear, compelling, and verifiable evidence to prove the dispute beyond reasonable doubt. Disputes that do not meet this high bar can be counter-disputed with the disputing party losing their bond.

### Document Characteristics

<Warning>

As the process is still experimental, we can expect iteration and fine-tuning on the contents/formats of how the evidence should be submitted.

</Warning>

Every document should have the following characteristics:

- It should be a text document. Can have images or video if necessary.

- It should be uploaded on IPFS.

- It should not take the reviewer more than 1 hour to review the dispute evidence document - the reviewer's time is limited and the evidence could be deemed invalid if it would take too much time to review. Best efforts will be applied to solve a dispute but please keep it concise to have your dispute evidence be valid.

Depending on what the type of the Dispute Tag is, you also need to include in the evidence the "Dispute Evidence Contents of the table below:

| Dispute Tag                                                                                                                                                                                                                                                                                                         | Dispute Evidence Contents                                                                                                                                                                                                                                             | Dispute review process (Human reviewer instructions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IMPROPER_REGISTRATION`                                                                                                                                                                                                                                                                                             | A. Showcase or pointer to the pre-existing IP that is being infringed upon by the disputed IP<br/><br/>B. Proof of public display of the pre-existing IP at an earlier date than the infringing IP (onchain or offchain) and/or instructions on where/how to check it | 1. Check if the pre-existing is the same or very similar to the disputed IP using input A<br/> - Mickey Mouse with 1 pixel difference is an infringement<br/> - Mickey Mouse with a new hat is an infringement unless it's a derivative of the original Mickey Mouse with an appropriate license<br/>2. Check the registration date of the pre-existing IP using input B<br/>3. Confirm that the disputed IP has a later registration date<br/>4. Confirm that the disputed IP is not a derivative of the pre-existing IP<br/><br/>         |
| `IMPROPER_USAGE`<br/><br/>Examples (non-exhaustive):<br/>Territory,<br/>Channels of Distribution,<br/>Expiration,<br/>Irrevocable,<br/>Attribution,<br/>Derivatives,<br/>Limitations on Creation of Derivatives,<br/>Commercial Use,<br/>Sublicensable,<br/>Non-Transferable,<br/>Restriction on Cross-Platform Use | A. PIL term that has been violated<br/><br/>B. Description of the violation<br/><br/>C. Proof of the violation                                                                                                                                                        | 1. Read the associated PIL term description on the PIL license official document using input A<br/>2. Read the violation description using input B<br/>3. Decide on the veracity of the proof presented by checking on associated platforms when possible using input C<br/><br/>                                                                                                                                                                                                                                                           |
| `IMPROPER_PAYMENT`                                                                                                                                                                                                                                                                                                  | A. Description of each payment the disputed IP received that should have been shared with its royalty vault and/or its ancestors but it were not<br/><br/>B. Proof of those payments that were not properly shared as royalties                                       | 1. Check veracity of the proof of payments by checking on the associated platforms when possible using input A and B<br/>2. If proof of payments are deemed to be real, confirm that the payment has indeed not been made onchain by checking on the blockchain explorer. Payments should be made calling payRoyaltyOnBehalf() function on RoyaltyModule.sol smart contract. In addition, royalty payments must be made within 15 days of when the capital was originally received by the owner/IP who is paying those royalties.<br/><br/> |
| `CONTENT_STANDARDS_VIOLATION`<br/><br/>No-Hate,<br/>Suitable-for-All-Ages,<br/>No-Drugs-or-Weapons,<br/>No-Pornography                                                                                                                                                                                              | A. The content standard point that has been violated<br/><br/>B. Description of the violation<br/><br/>C. Proof of violation                                                                                                                                          | 1. Read the associated content standards description on the official content standards section in the PIL using input A<br/>2. Read the violation description using input B<br/>3. Decide on the veracity of the proof presented by checking on associated platforms when possible using input C<br/><br/>                                                                                                                                                                                                                                  |


# ❌ Dispute Module

The Dispute Module creates a way for users to raise and resolve disputes through arbitration.

<CardGroup cols={1}>
  <Card
    title="DisputeModule.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/dispute/DisputeModule.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Dispute Module.
  </Card>
</CardGroup>

## Dispute Terminology

The main components of the arbitration system are:

- **Arbitration Policies:** the arbitration policy refers to the set rules/process/entities that combined will decide on a dispute. Currently the only supported arbitration policy is the [UMA Arbitration Policy](/concepts/dispute-module/uma-arbitration-policy).
- **Arbitration Penalty:** what happens to an IP Asset after it has been "tagged". An IPA is not deemed "tagged" unless the dispute is decided to be correct. Once tagged, an IPA will not be able to:
  - mint licenses
  - link to any parents
  - claim royalties
  - and all of its existing licenses become unusable

### Dispute Tags

**Tags** refer to the "labels" that can be applied to IP Assets in the protocol when raising a dispute. **Tags must be whitelisted by protocol governance to be used in a dispute.** The initial set of tags (and their `bytes32` for interacting with the Dispute Module on-chain) are:

- `IMPROPER_REGISTRATION`: `0x494d50524f5045525f524547495354524154494f4e0000000000000000000000`
- `IMPROPER_USAGE`: `0x494d50524f5045525f5553414745000000000000000000000000000000000000`
- `IMPROPER_PAYMENT`: `0x494d50524f5045525f5041594d454e5400000000000000000000000000000000`
- `CONTENT_STANDARDS_VIOLATION`: `0x434f4e54454e545f5354414e44415244535f56494f4c4154494f4e0000000000`
- `IN_DISPUTE`: `0x494e5f4449535055544500000000000000000000000000000000000000000000`

| Dispute Tag                                                                                                                                                                                                                                                                                                         | Explanation                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IMPROPER_REGISTRATION`                                                                                                                                                                                                                                                                                             | Refers to registration of IP that already exists.                                                                                                                                                                                       |
| `IMPROPER_USAGE`<br/><br/>Examples (non-exhaustive):<br/>Territory,<br/>Channels of Distribution,<br/>Expiration,<br/>Irrevocable,<br/>Attribution,<br/>Derivatives,<br/>Limitations on Creation of Derivatives,<br/>Commercial Use,<br/>Sublicensable,<br/>Non-Transferable,<br/>Restriction on Cross-Platform Use | Refers to improper use of an IP Asset across multiple items (examples on the left). These items can be found in more detail in the [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license/overview) legal document.       |
| `IMPROPER_PAYMENT`                                                                                                                                                                                                                                                                                                  | Refers to missing payments associated with an IP.                                                                                                                                                                                       |
| `CONTENT_STANDARDS_VIOLATION`<br/><br/>Examples: No-Hate, Suitable-for-All-Ages, No-Drugs-or-Weapons, No-Pornography                                                                                                                                                                                                | Refers to "No-Hate", "Suitable-for-All-Ages", "No-Drugs-or-Weapons" and "No-Pornography". These items can be found in more detail in the [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license/overview) legal document. |
| `IN_DISPUTE`                                                                                                                                                                                                                                                                                                        | Different from the other 4, this is a temporary tag that goes away at the end of a dispute and is replaced by "0x" in case of no infringement or is replaced by one of the other tags.                                                  |

## Dispute Process Flow

<Frame>
  <img
    src="/images/concepts/dispute-process-flow.png"
    alt="Dispute Process Flow"
  />
</Frame>

### Raise Dispute

The `raiseDispute` function is permissionless and allows any address to raise a dispute against any IP Asset registered on the protocol. The dispute initiator has to:

1. Select which "tag" it is raising a dispute on which will be applied to the IP Asset if the arbitration decision is positive. This means an IP Asset is officially "tagged" only when the proposed tag is confirmed as correct ("positive decision" in the diagram above).
2. Submit the dispute evidence for evaluation
3. Other conditions custom to each arbitration policy - such as payment rules, etc.

### Set Dispute Judgement

The `setDisputeJudgement` can only be called by whitelisted addresses and allows the caller to set the dispute judgment. Can only be called once as dispute decisions are immutable. If 3rd parties want to offer the possibility for recourse they can do so on their end and relay the final judgment.

### Tag Derivative If Parent Infringed

If the `setDisputeJudgement` has tagged an IP as infringing then any address can call `tagIfRelatedIpInfringed` to apply the same tag as the parent to the derivatives all the way down the derivative chain or if the IP is a group then the group member tag can be applied to any group IP which it is a member of.

<Note>
  Looking Ahead

In the future, the idea is that any related IP Asset of an infringing IP Asset would automatically be tagged without needing someone to call `tagIfRelatedIpInfringed`. This is currently a limitation that we are aware of.

</Note>

The derivatives are then tagged directly without any need for judgment given that it is considered that if a parent IP license has been infringed then all derivatives that come from that license are also implicitly in an infringement situation.

**Example**: IPA 7 is first tagged ("PLAGIARISM") as infringing via `setDisputeJudgement` after having gone through a dispute process. Only after that can IPAs 3, 1, and 0 can be tagged via `tagIfRelatedIpInfringed` by any address without needing to go through a new dispute process.

<Frame>
  <img src="/images/concepts/plagiarism-example.png" alt="Dispute Example" />
</Frame>

### Resolve Dispute

Resolving a dispute removes the tag from the IP Asset. Since there are two ways in which a tag can be applied, there are two ways for it to be resolved:

1. Tag was applied via the`setDisputeJudgement` function

In a case where a dispute judgment was positive, then a tag was applied. After the tag has been applied to an IP Asset, the **dispute initiator** can, if he/she believes the matter to be resolved and the tag to no longer apply, choose to remove it by calling `resolveDispute`. For example, if one party owed money to the dispute initiator and paid the full amount after the dispute judgment then the tag could be cleared and the IP Asset would have a clean slate again.

If the dispute initiator chooses to not resolve, then the tag that was defined in `setDisputeJudgement` remains in force.

2. Tag was applied via the`tagIfRelatedIpInfringed` function

If an IP has been previously tagged as infringing via `tagIfRelatedIpInfringed`, such tag can be removed via `resolveDispute` in a permissionless way as long as the parent is no longer considered an infringing IP Asset.

This mechanism of permissionless resolving disputes exists to make it easier to propagate down the derivative chain and remove infringement tags from derivative IPs when the parent has resolved its original dispute and is no longer considered as being in an infringing situation, and therefore neither are its derivatives.

If no address chooses to resolve, then the tag that was applied from the parent to the derivative remains in force.

### Cancel Dispute

In a case where a dispute was raised but the matter has been resolved before the dispute judgment, the dispute initiator can cancel the dispute. However, depending on the conditions of each arbitration policy, there may be non-refundable fees that are not recouped on cancellation.

<Warning>
  Currently, the [UMA Arbitration
  Policy](/concepts/dispute-module/uma-arbitration-policy) does not support
  cancelling disputes.
</Warning>


# Batch Function Calls

## Background

Prior to this point, registering multiple IPs or performing other operations such as minting, attaching licensing terms, and registering derivatives requires separate transactions for each operation. This can be inefficient and costly. To streamline the process, you can batch multiple transactions into a single one. Two solutions are now available for this:

1. **Batch SPG function calls:** Use [SPG's built-in `multicall` function](#1-batch-spg-function-calls-via-built-in-multicall-function).
2. **Batch function calls beyond SPG:** Use the [Multicall3 Contract](#2-batch-function-calls-via-multicall3-contract).

---

## 1. Batch SPG Function Calls via Built-in `multicall` Function

SPG includes a `multicall` function that allows you to combine multiple read or write operations into a single transaction.

### Function Definition

The `multicall` function accepts an array of encoded call data and returns an array of encoded results corresponding to each function call:

```solidity Solidity
/// @dev Executes a batch of function calls on this contract.
function multicall(bytes[] calldata data) external virtual returns (bytes[] memory results);
```

### Example Usage

Suppose you want to mint multiple NFTs, register them as IPs, and link them as derivatives to some parent IPs.

To accomplish this, you can use SPG's `multicall` function to batch the calls to the `mintAndRegisterIpAndMakeDerivative` function.

Here's how you might do it:

```solidity Solidity
// an SPG workflow contract: https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/workflows/DerivativeWorkflows.sol
contract DerivativeWorkflows {
    ...
    function mintAndRegisterIpAndMakeDerivative(
        address nftContract,
        MakeDerivative calldata derivData,
        IPMetadata calldata ipMetadata,
        address recipient
    ) external returns (address ipId, uint256 tokenId) {
        ....
    }
    ...
}
```

To batch call `mintAndRegisterIpAndMakeDerivative` using the `multicall` function:

```javascript JavaScript
// batch mint, register, and make derivatives for multiple IPs
await DerivativeWorkflows.multicall([
  DerivativeWorkflows.contract.methods.mintAndRegisterIpAndMakeDerivative(
      nftContract1,
      derivData1,
      recipient1,
      ipMetadata1,
  ).encodeABI(),

  DerivativeWorkflows.contract.methods.mintAndRegisterIpAndMakeDerivative(
      nftContract2,
      derivData2,
      recipient2,
      ipMetadata2,
  ).encodeABI(),

  DerivativeWorkflows.contract.methods.mintAndRegisterIpAndMakeDerivative(
      nftContract3,
      derivData3,
      recipient3,
      ipMetadata3,
  ).encodeABI(),
  ...
  // Add more calls as needed
]);
```

---

## 2. Batch Function Calls via Multicall3 Contract

<Warning>

The Multicall3 contract is not fully compatible with SPG functions that involve SPGNFT minting due to access control and context changes during Multicall execution. For such operations, use [SPG's built-in multicall function.](#1-batch-spg-function-calls-via-built-in-multicall-function)

</Warning>

The Multicall3 contract allows you to execute multiple calls within a single transaction and aggregate the results. The [`viem` library](https://viem.sh/docs/contract/multicall#multicall) provides native support for Multicall3.

### Story Aeneid Testnet Multicall3 Deployment Info

(Same address across all EVM chains)

```json
{
  "contractName": "Multicall3",
  "chainId": 1516,
  "contractAddress": "0xcA11bde05977b3631167028862bE2a173976CA11",
  "url": "https://aeneid.storyscan.io/address/0xcA11bde05977b3631167028862bE2a173976CA11"
}
```

### Main Functions

To batch multiple function calls, you can use the following functions:

1. **`aggregate3`**: Batches calls using the `Call3` struct.
2. **`aggregate3Value`**: Similar to `aggregate3`, but also allows attaching a value to each call.

```solidity Solidity
/// @notice Aggregate calls, ensuring each returns success if required.
/// @param calls An array of Call3 structs.
/// @return returnData An array of Result structs.
function aggregate3(Call3[] calldata calls) external payable returns (Result[] memory returnData);

/// @notice Aggregate calls with an attached msg value.
/// @param calls An array of Call3Value structs.
/// @return returnData An array of Result structs.
function aggregate3Value(Call3Value[] calldata calls) external payable returns (Result[] memory returnData);
```

### Struct Definitions

- **Call3**: Used in `aggregate3`.
- **Call3Value**: Used in `aggregate3Value`.

```solidity Solidity
struct Call3 {
  address target;      // Target contract to call.
  bool allowFailure;   // If false, the multicall will revert if this call fails.
  bytes callData;      // Data to call on the target contract.
}

struct Call3Value {
  address target;
  bool allowFailure;
  uint256 value;       // Value (in wei) to send with the call.
  bytes callData;      // Data to call on the target contract.
}
```

### Return Type

- **Result**: Struct returned by both `aggregate3` and `aggregate3Value`.

```solidity Solidity
struct Result {
  bool success;        // Whether the function call succeeded.
  bytes returnData;    // Data returned from the function call.
}
```

<Note>

For detailed examples in Solidity, TypeScript, and Python, see the [Multicall3 repository](https://github.com/mds1/multicall/tree/main/examples).

</Note>

### Limitations

For a list of limitations when using Multicall3, refer to the [Multicall3 README](https://github.com/mds1/multicall/blob/main/README.md#batch-contract-writes).

### Additional Resources

- [Multicall3 Documentation](https://github.com/mds1/multicall/blob/main/README.md)
- [Multicall Documentation from Viem](https://viem.sh/docs/contract/multicall#multicall)

### Full Multicall3 Interface

```solidity Solidity
interface IMulticall3 {
  struct Call {
      address target;
      bytes callData;
  }

  struct Call3 {
      address target;
      bool allowFailure;
      bytes callData;
  }

  struct Call3Value {
      address target;
      bool allowFailure;
      uint256 value;
      bytes callData;
  }

  struct Result {
      bool success;
      bytes returnData;
  }

  function aggregate(Call[] calldata calls) external payable returns (uint256 blockNumber, bytes[] memory returnData);
  function aggregate3(Call3[] calldata calls) external payable returns (Result[] memory returnData);
  function aggregate3Value(Call3Value[] calldata calls) external payable returns (Result[] memory returnData);
  function blockAndAggregate(Call[] calldata calls) external payable returns (uint256 blockNumber, bytes32 blockHash, Result[] memory returnData);
  function getBasefee() external view returns (uint256 basefee);
  function getBlockHash(uint256 blockNumber) external view returns (bytes32 blockHash);
  function getBlockNumber() external view returns (uint256 blockNumber);
  function getChainId() external view returns (uint256 chainId);
  function getCurrentBlockCoinbase() external view returns (address coinbase);
  function getCurrentBlockDifficulty() external view returns (uint256 difficulty);
  function getCurrentBlockGasLimit() external view returns (uint256 gaslimit);
  function getCurrentBlockTimestamp() external view returns (uint256 timestamp);
  function getEthBalance(address addr) external view returns (uint256 balance);
  function getLastBlockHash() external view returns (bytes32 blockHash);
  function tryAggregate(bool requireSuccess, Call[] calldata calls) external payable returns (Result[] memory returnData);
  function tryBlockAndAggregate(bool requireSuccess, Call[] calldata calls) external payable returns (uint256 blockNumber, bytes32 blockHash, Result[] memory returnData);
}
```


# 📦 SPG (Periphery)

The Story Protocol Gateway (SPG) is a group of periphery/utility smart contracts, deployed on our protocol that **allows you to combine independent operations** - like registering an [🧩 IP Asset](/concepts/ip-asset/overview) and attaching License Terms to that IP Asset - **into one transaction to make your life easier**.

This was primarily developed to make our [SDK](/sdk-reference) easier to use.

For example, this `mintAndRegisterIpAndAttachPILTerms` is one of the functions in the SPG (more specifically in the `LicenseAttachmentWorkflows.sol`) that allows you to mint an NFT, register it as an IP Asset, and attach License Terms to it all in one call:

```solidity LicenseAttachmentWorkflows.sol
function mintAndRegisterIpAndAttachPILTerms(
  address spgNftContract,
  address recipient,
  WorkflowStructs.IPMetadata calldata ipMetadata,
  WorkflowStructs.LicenseTermsData[] calldata licenseTermsData,
  bool allowDuplicates
) external onlyMintAuthorized(spgNftContract) returns (address ipId, uint256 tokenId, uint256[] memory licenseTermsIds)
```

## All Supported Workflows

As mentioned above, there are many different functions we have created for you that combine multiple functions into one. We have categorized them into different groups. These groups are called "workflows".

<CardGroup cols={2}>
  <Card title="View all Workflows" href="https://github.com/storyprotocol/protocol-periphery-v1/blob/main/docs/WORKFLOWS.md" icon="eyes" color="grey">
    Click here to view all of the supported workflows.
  </Card>

  <Card title="Smart Contracts" href="https://github.com/storyprotocol/protocol-periphery-v1/tree/main/contracts/workflows" icon="scroll" color="#ccb092">
    Click here to view the workflow smart contracts.
  </Card>
</CardGroup>

## Batching Calls

Although the SPG contains certain functions like `mintAndRegisterIpAndAttachPILTerms`, `registerIpAndAttachPILTerms`, and a bunch more, it would be tedious for us to continually update the contract to account for every single combination of possible interactions with an IP Asset.

Instead, we have allowed for a "Multicall" mechanism where you can batch transactions how you like. For more info, see [Batch Function Calls](/concepts/spg/batch-spg-function-calls).


# PIL Flavors (examples)

The [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license/overview) is very configurable, but we support popular pre-configured License Terms (also known as "flavors") for ease of use. We expect these to be the most popular options:

## Flavor #1: Non-Commercial Social Remixing

<Note>

This flavor is already registered as `licenseTermsId = 1` on our protocol. This is because it doesn't take any inputs, so we registered it ahead of time.

</Note>

Let the world build on and play with your creation. This license allows for endless free remixing while tracking all uses of your work while giving you full credit. Similar to: TikTok plus attribution.

### What others can do?

| Others can                                             | Others cannot                                                                        |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| ✅ Remix this work (`derivativesAllowed == true`)      | ❌ Commercialize the original and derivative works (`commercialUse == false`)        |
| ✅ Distribute their remix anywhere                     | ❌ Claim credit for any derivative works (`derivativesAttribution == true`)          |
| ✅ Get the license for free (`defaultMintingFee == 0`) | ❌ Claim credit for the original work ("Attribution" is true in the off-chain terms) |

### PIL Term Values

- **On-chain**:

<CodeGroup>

```solidity Solidity
PILTerms({
  transferable: true,
  royaltyPolicy: address(0),
  defaultMintingFee: 0,
  expiration: 0,
  commercialUse: false,
  commercialAttribution: false,
  commercializerChecker: address(0),
  commercializerCheckerData: EMPTY_BYTES,
  commercialRevShare: 0,
  commercialRevCeiling: 0,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0,
  currency: address(0),
  uri: "https://github.com/piplabs/pil-document/blob/998c13e6ee1d04eb817aefd1fe16dfe8be3cd7a2/off-chain-terms/NCSR.json"
});
```

```typescript TypeScript
import { zeroAddress } from "viem";

const nonCommercialSocialRemix = {
  transferable: true,
  royaltyPolicy: zeroAddress,
  defaultMintingFee: 0n,
  expiration: 0n,
  commercialUse: false,
  commercialAttribution: false,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: "0x",
  commercialRevShare: 0,
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0n,
  currency: zeroAddress,
  uri: "https://github.com/piplabs/pil-document/blob/998c13e6ee1d04eb817aefd1fe16dfe8be3cd7a2/off-chain-terms/NCSR.json",
};
```

</CodeGroup>

- **Off-chain:**

| Parameter                         | Options / Tags                                                              |
| --------------------------------- | --------------------------------------------------------------------------- |
| Territory                         | No restrictions                                                             |
| Channels of Distribution          | No Restriction                                                              |
| Attribution                       | True                                                                        |
| Content Standards                 | No Restriction                                                              |
| Sublicensable                     | False                                                                       |
| AI Learning Models                | True                                                                        |
| Restriction on Cross-Platform Use | False                                                                       |
| Governing Law                     | California                                                                  |
| Alternative Dispute Resolution    | Tag: Alternative-Dispute-Resolution Ledger-Authoritative-Dispute-Resolution |
| Additional License Parameters     | None                                                                        |

## Flavor #2: Commercial Use

Retain control over reuse of your work, while allowing anyone to appropriately use the work in exchange for the economic terms you set. This is similar to Shutterstock with creator-set rules.

### What others can do?

| Others can                                                   | Others cannot                                                                                             |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| ✅ Commercialize the original work (`commercialUse == true`) | ❌ Remix this work (`derivativesAllowed == false`)                                                        |
| ✅ Keep all revenue (`commercialRevShare == 0`)              | ❌ Claim credit for the original work (`commercialAttribution == true`)                                   |
|                                                              | ❌ Get the license for free (`defaultMintingFee` is set)                                                  |
|                                                              | ❌ Claim credit for the original work even non-commercially ("Attribution is true in the off-chain terms) |

### PIL Term Values

- **On-chain**:

<CodeGroup>

```solidity Solidity
PILTerms({
  transferable: true,
  royaltyPolicy: ROYALTY_POLICY, // ex. RoyaltyPolicyLAP address
  defaultMintingFee: MINTING_FEE, // ex. 1000000000000000000 (which means it costs 1 $WIP to mint)
  expiration: 0,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: address(0),
  commercializerCheckerData: EMPTY_BYTES,
  commercialRevShare: 0,
  commercialRevCeiling: 0,
  derivativesAllowed: false,
  derivativesAttribution: false,
  derivativesApproval: false,
  derivativesReciprocal: false,
  derivativeRevCeiling: 0,
  currency: CURRENCY, // ex. $WIP address
  uri: "https://github.com/piplabs/pil-document/blob/9a1f803fcf8101a8a78f1dcc929e6014e144ab56/off-chain-terms/CommercialUse.json"
})
```

```typescript TypeScript
import { zeroAddress, parseEther } from "viem";

const commercialUse = {
  transferable: true,
  royaltyPolicy: ROYALTY_POLICY, // ex. RoyaltyPolicyLAP address
  defaultMintingFee: MINTING_FEE, // ex. parseEther("1") (which means it costs 1 $WIP to mint)
  expiration: 0n,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: "0x",
  commercialRevShare: 0,
  commercialRevCeiling: 0n,
  derivativesAllowed: false,
  derivativesAttribution: false,
  derivativesApproval: false,
  derivativesReciprocal: false,
  derivativeRevCeiling: 0n,
  currency: CURRENCY, // ex. $WIP address
  uri: "https://github.com/piplabs/pil-document/blob/9a1f803fcf8101a8a78f1dcc929e6014e144ab56/off-chain-terms/CommercialUse.json",
};
```

</CodeGroup>

- **Off-chain**

| Parameter                         | Options / Tags                                                              |
| --------------------------------- | --------------------------------------------------------------------------- |
| Territory                         | No restrictions                                                             |
| Channels of Distribution          | No Restriction                                                              |
| Attribution                       | True                                                                        |
| Content Standards                 | No Restriction                                                              |
| Sublicensable                     | False                                                                       |
| AI Learning Models                | True                                                                        |
| Restriction on Cross-Platform Use | False                                                                       |
| Governing Law                     | California                                                                  |
| Alternative Dispute Resolution    | Tag: Alternative-Dispute-Resolution Ledger-Authoritative-Dispute-Resolution |
| Additional License Parameters     | None                                                                        |

## Flavor #3: Commercial Remix

Let the world build on and play with your creation... and earn money together from it! This license allows for endless free remixing while tracking all uses of your work while giving you full credit, with each derivative paying a percentage of revenue to its "parent" IP.

### Example

Check out Story's official mascot **Ippy**, which we have registered with commercial remix terms on both [Mainnet](https://explorer.story.foundation/ipa/0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42) and [Aeneid Testnet](https://aeneid.explorer.story.foundation/ipa/0x641E638e8FCA4d4844F509630B34c9D524d40BE5).

### What others can do?

| Others can                                                                   | Others cannot                                                                                             |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ✅ Remix this work (`derivativesAllowed == true`)                            | ❌ Claim credit for the original work (`commercialAttribution == true`)                                   |
| ✅ Commercialize the original and derivative works (`commercialUse == true`) | ❌ Claim credit for any derivative works (`derivativesAttribution == true`)                               |
| ✅ Distribute their remix anywhere                                           | ❌ Keep all revenue (`commercialRevShare` is set)                                                         |
|                                                                              | ❌ Get the license for free (`defaultMintingFee` is set)                                                  |
|                                                                              | ❌ Claim credit for the original work even non-commercially ("Attribution is true in the off-chain terms) |

### PIL Term Values

- **On-chain**:

<CodeGroup>

```solidity Solidity
PILTerms({
  transferable: true,
  royaltyPolicy: ROYALTY_POLICY, // ex. RoyaltyPolicyLAP address
  defaultMintingFee: MINTING_FEE, // ex. 1000000000000000000 (which means it costs 1 $WIP to mint)
  expiration: 0,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: address(0),
  commercializerCheckerData: EMPTY_BYTES,
  commercialRevShare: COMMERCIAL_REV_SHARE, // ex. 50 * 10 ** 6 (which means 50% of derivative revenue)
  commercialRevCeiling: 0,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0,
  currency: CURRENCY, // ex. $WIP address
  uri: "https://github.com/piplabs/pil-document/blob/ad67bb632a310d2557f8abcccd428e4c9c798db1/off-chain-terms/CommercialRemix.json"
});
```

```typescript TypeScript
import { zeroAddress, parseEther } from "viem";

const commercialRemix = {
  transferable: true,
  royaltyPolicy: ROYALTY_POLICY, // ex. RoyaltyPolicyLAP address
  defaultMintingFee: MINTING_FEE, // ex. parseEther("1") (which means it costs 1 $WIP to mint)
  expiration: 0n,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: "0x",
  commercialRevShare: COMMERCIAL_REV_SHARE, // ex. 50 (which means 50% of derivative revenue)
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0n,
  currency: CURRENCY, // ex. $WIP address
  uri: "https://github.com/piplabs/pil-document/blob/ad67bb632a310d2557f8abcccd428e4c9c798db1/off-chain-terms/CommercialRemix.json",
};
```

</CodeGroup>

- **Off-chain**

| Parameter                         | Options / Tags                                                              |
| --------------------------------- | --------------------------------------------------------------------------- |
| Territory                         | No restrictions                                                             |
| Channels of Distribution          | No Restriction                                                              |
| Attribution                       | True                                                                        |
| Content Standards                 | No Restriction                                                              |
| Sublicensable                     | False                                                                       |
| AI Learning Models                | True                                                                        |
| Restriction on Cross-Platform Use | False                                                                       |
| Governing Law                     | California                                                                  |
| Alternative Dispute Resolution    | Tag: Alternative-Dispute-Resolution Ledger-Authoritative-Dispute-Resolution |
| Additional License Parameters     | None                                                                        |

## Flavor #4: Creative Commons Attribution

Let the world build on and play with your creation - including making money.

### What others can do?

| Others can                                                                   | Others cannot                                                                                             |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ✅ Remix this work (`derivativesAllowed == true`)                            | ❌ Claim credit for the original work (`commercialAttribution == true`)                                   |
| ✅ Commercialize the original and derivative works (`commercialUse == true`) | ❌ Claim credit for any derivative works (`derivativesAttribution == true`)                               |
| ✅ Distribute their remix anywhere                                           | ❌ Claim credit for the original work even non-commercially ("Attribution is true in the off-chain terms) |
| ✅ Get the license for free (`defaultMintingFee == 0`)                       |                                                                                                           |
| ✅ Keep all revenue (`commercialRevShare == 0`)                              |                                                                                                           |

### PIL Term Values

- **On-chain**:

<CodeGroup>

```solidity Solidity
PILTerms({
  transferable: true,
  royaltyPolicy: ROYALTY_POLICY, // ex. RoyaltyPolicyLAP address
  defaultMintingFee: 0,
  expiration: 0,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: address(0),
  commercializerCheckerData: EMPTY_BYTES,
  commercialRevShare: 0,
  commercialRevCeiling: 0,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCelling: 0,
  currency: CURRENCY, // ex. $WIP address
  uri: 'https://github.com/piplabs/pil-document/blob/998c13e6ee1d04eb817aefd1fe16dfe8be3cd7a2/off-chain-terms/CC-BY.json'
});
```

```typescript TypeScript
import { zeroAddress } from "viem";

const creativeCommonsAttribution = {
  transferable: true,
  royaltyPolicy: ROYALTY_POLICY, // ex. RoyaltyPolicyLAP address
  defaultMintingFee: 0n,
  expiration: 0n,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: "0x",
  commercialRevShare: 0,
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCelling: 0n,
  currency: CURRENCY, // ex. $WIP address
  uri: "https://github.com/piplabs/pil-document/blob/998c13e6ee1d04eb817aefd1fe16dfe8be3cd7a2/off-chain-terms/CC-BY.json",
};
```

</CodeGroup>

- **Off-chain**

| Parameter                         | Options / Tags                                                              |
| --------------------------------- | --------------------------------------------------------------------------- |
| Territory                         | No restrictions                                                             |
| Channels of Distribution          | No Restriction                                                              |
| Attribution                       | True                                                                        |
| Content Standards                 | No Restriction                                                              |
| Sublicensable                     | False                                                                       |
| AI Learning Models                | True                                                                        |
| Restriction on Cross-Platform Use | False                                                                       |
| Governing Law                     | California                                                                  |
| Alternative Dispute Resolution    | Tag: Alternative-Dispute-Resolution Ledger-Authoritative-Dispute-Resolution |
| Additional License Parameters     | None                                                                        |

# Examples

Here are some common examples of royalty flow. _More coming soon!_

## Example 1

<Frame>
  <img src="/images/concepts/flavor-1.png" alt="Example 1 Royalty Flow" />
</Frame>

### Explanation

Someone registers their Azuki on Story. By default, that IP Asset has Non-Commercial Social Remixing Terms, which specify that anyone can create derivatives of that work but cannot commercialize them. So, someone else creates & registers a remix of that work (IPA2) which inherits those same terms. Someone else then does the same to IPA2, creating & registering IPA3.

The owner of IPA1 then decides that others can commercialize the work, but they cannot create derivatives to do so, they must pay a 10 \$WIP minting fee, and they must share 10% of all revenue earned. So, someone wants to commercialize IPA1 by putting it on a t-shirt. They pay the 10 \$WIP minting fee to get a License Token, which represents the license to commercialize IPA1. They then put the image on a t-shirt and sell it. 10% of revenue earned by that t-shirt must be sent on-chain to IPA1.

## Example 2

<Frame>
  <img src="/images/concepts/flavor-2.png" alt="Example 2 Royalty Flow" />
</Frame>

### Explanation

Someone registers their Azuki on Story. By default, that IP Asset has Non-Commercial Social Remixing Terms, which specify that anyone can create derivatives of that work but cannot commercialize them. So, someone else creates & registers a remix of that work (IPA2) which inherits those same terms. Someone else then does the same to IPA2, creating & registering IPA3.

The owner of IPA1 then decides that others can create derivatives of their work and commercialize them, but they must pay a 10 \$WIP minting fee and share 10% of all revenue earned. So, someone wants to commercialize IPA1 by putting it on a t-shirt. They pay the 10 \$WIP minting fee to get a License Token and burn it to create their own derivative, which changes the background color to red. They then put the remixed image on a t-shirt and sell it. 10% of revenue earned by that t-shirt must be sent on-chain to IPA1.

A third person wants to commercialize the remix by putting it in a TV advertisement, but they want to change the hair color to white. So, they pay a 10 \$WIP minting fee (of which, 1 \$WIP gets sent back to IPA1) to create their own derivative. They then put the remixed image in a TV ad. 10% of revenue earned by that t-shirt must be sent on-chain to IPA4, of which 10% will be distributed back to IPA1.


# How does Story protect IP?

<Frame>
  <img src="/images/concepts/hdspip.png" alt="How Does Story Protect IP?" />
</Frame>

<Tip>Every license created on Story is a real, enforceable legal contract.</Tip>

## The Programmable IP License (PIL): The Foundation of Legal Enforcement

At its core, every [IP Asset](/concepts/ip-asset) registered on Story is wrapped by a **legally binding document called the [Programmable IP License (PIL)](/concepts/programmable-ip-license)**. Based on US copyright law, the PIL acts as a universal license agreement template that allows IP owners to attach customizable terms to their assets.

**Licensing on Story means making a genuine legal commitment.** The parameters defined in the PIL—commercial use, derivative allowances, attribution requirements, and royalty structures—represent legally enforceable terms between the IP owner (licensor) and anyone who licenses the IP (licensee).

### How does the PIL enable enforcement?

- **Clear Legal Terms:** The PIL provides a standardized way for IP owners to define usage rules.
- **On-Chain Record as Evidence:** PIL terms attached to an IP Asset are recorded immutably on Story's purpose-built blockchain, serving as _irrefutable evidence_ of the agreed-upon terms.
- **Off-Chain Legal Recourse:** If IP is misused in violation of PIL terms, the IP owner can leverage on-chain evidence in **off-chain legal proceedings** such as arbitration or court actions.
- **License Tokens as Proof of Rights:** Licensees receive a [**License Token**](/concepts/licensing-module/license-token) (NFT) representing specific usage rights granted under the PIL terms, providing further evidence of authorization status.

## The Story Attestation Service (SAS): Proactive Infringement Monitoring

Beyond the legal framework, we are building the [**Story Attestation Service (SAS)**](/concepts/story-attestation-service) to help IP owners monitor for potential copyright infringement using a multi-layered decentralized approach.

<Note>
  SAS is a signal layer, not a judgment layer—it flags potential issues for the
  IP owner to act upon, rather than taking automated enforcement actions.
</Note>

### How the SAS Helps with Infringement Detection:

- **Network of Specialized Providers:** SAS coordinates with service providers like Yakoa and Pex that use AI and machine learning to detect copyright violations across different media types on the internet and other blockchains.
- **Transparent Signals:** SAS provides publicly accessible signals regarding the legitimacy of an IP Asset based on provider findings.
- **Focus on Commercial IP:** Currently, SAS primarily runs infringement checks on commercial IP Assets—those with at least one License Terms where `commercialUse = true`.
- **Metadata-Driven Checks:** SAS relies on IP-specific metadata provided during registration to perform checks against existing online content.

### Important Considerations:

- **Detection, Not Prevention:** SAS primarily flags potential infringements after IP registration rather than preventing them.
- **Internet-Based Checks:** Currently, SAS primarily detects infringement based on content already existing online, not offline uses.
- **No Guarantee of Perfection:** No system can guarantee 100% detection of all copyright infringement.

## The Role of the Dispute Module

We have also built a [**Dispute Module**](/concepts/dispute-module) that allows anyone to raise on-chain disputes against IP Assets for reasons such as improper registration or potential plagiarism. This can lead to on-chain flagging of disputed IP, potentially affecting its ability to generate licenses or earn revenue.

## The Hybrid Enforcement Model

<Note>
  Story doesn't replace courts or lawyers—it gives IP holders tools that work
  with traditional enforcement systems while benefiting from on-chain
  automation, transparency, and interoperability.
</Note>

### What Story Can Do:

- Provide a legally sound framework for IP licensing through the PIL
- Create an immutable on-chain record of IP ownership and license terms
- Offer monitoring tools through the SAS to detect potential online infringement
- Facilitate on-chain dispute resolution through the Dispute Module
- Provide evidence usable for off-chain legal enforcement

### What Story Cannot Do:

- Act as a global police force for IP infringement
- Guarantee prevention of all unauthorized IP uses
- Directly enforce legal judgments in the physical world
- Monitor every digital and physical interaction with registered IP

```
+--------------------------+      +-----------------------------+
| IP Owner Registers IP on |----->| IP Asset Created on Story   |
| Story                    |      | (with associated metadata)  |
+--------------------------+      +-----------------------------+
                                          |
                                          v
+---------------------------------------+   +-------------------------+
| Programmable IP License (PIL)         |<--| IP Owner Attaches Legal |
| (Legal wrapper defining usage terms)  |   | Terms via PIL           |
+---------------------------------------+   +-------------------------+
                                          |
                                          v
                                  +-------------------------+
                                  | IP Asset with PIL Terms |
                                  | (Commercial Use = true) |
                                  +-------------------------+
                                          |
                                          v
+--------------------------+      +-------------------------------------+
| Story Attestation        |----->| SAS Providers Scan Internet & Other |
| Service (SAS) Coordinates|      | Sources for Infringement (using IP  |
+--------------------------+      | Metadata)                           |
                                  +-------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------+
| SAS Providers Report Potential Infringement Signals for the IP Asset |
| (e.g., "Potential copy found on website X")                          |
+----------------------------------------------------------------------+
                                          |
                                          v
+---------------------------------------------------------------------+
| IP Owner Reviews SAS Signals on IP Portal (Coming Soon)             |
+---------------------------------------------------------------------+
                                          |
                                          v
+---------------------------------------------------------------------+
| IP Owner Can Use SAS Signals & PIL Terms as Evidence for:           |
| - On-Chain Dispute via Dispute Module                               |
| - Off-Chain Legal Action (e.g., Cease & Desist, Lawsuit)            |
+---------------------------------------------------------------------+

```


# PIL Terms

<CardGroup cols={3}>

<Card
  title="Read the Overview"
  href="/concepts/programmable-ip-license/overview"
  icon="pills"
  color="yellow"
>
  If you haven't already, read the Programmable IP License (PIL💊) overview.
</Card>

<Card
  title="Preset PIL Terms"
  href="/concepts/programmable-ip-license/pil-flavors"
  icon="thumbs-up"
  color="#51af51"
>
  Since there are so many possible combinations of the PIL, we have created
  preset "flavors" for you to use while developing.
</Card>

<Card
  title="PIL Legal Text"
  href="https://github.com/piplabs/pil-document/blob/main/Story%20Foundation%20-%20Programmable%20IP%20License%20(1.31.25).pdf"
  icon="scroll"
  color="#ccb092"
>
  Check out the actual PIL legal text. It is very human-readable for a legal
  text!
</Card>

</CardGroup>

# On-chain terms

Most PIL terms are on-chain. They are implemented in the `IPILicenseTemplate.sol` contract as a `PILTerms` struct [here](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/interfaces/modules/licensing/IPILicenseTemplate.sol).

```solidity IPILicenseTemplate.sol
/// @notice This struct defines the terms for a Programmable IP License (PIL).
/// These terms can be attached to IP Assets.
struct PILTerms {
  bool transferable;
  address royaltyPolicy;
  uint256 defaultMintingFee;
  uint256 expiration;
  bool commercialUse;
  bool commercialAttribution;
  address commercializerChecker;
  bytes commercializerCheckerData;
  uint32 commercialRevShare;
  uint256 commercialRevCeiling;
  bool derivativesAllowed;
  bool derivativesAttribution;
  bool derivativesApproval;
  bool derivativesReciprocal;
  uint256 derivativeRevCeiling;
  address currency;
  string uri;
}
```

## Descriptions

| Parameter                   | Values          | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `transferable`              | True/False      | If false, the License Token cannot be transferred once it is minted to a recipient address.                                                                                                                                                                                                                                                                                                            |
| `royaltyPolicy`             | Address         | The address of the royalty policy contract.                                                                                                                                                                                                                                                                                                                                                            |
| `defaultMintingFee`         | #               | The fee to be paid when minting a license.                                                                                                                                                                                                                                                                                                                                                             |
| `expiration`                | #               | The expiration period of the license.                                                                                                                                                                                                                                                                                                                                                                  |
| `commercialUse`             | True/False      | You can make money from using the original IP Asset, subject to limitations below.                                                                                                                                                                                                                                                                                                                     |
| `commercialAttribution`     | True/False      | If true, people must give credit to the original work in their commercial application (eg. merch)                                                                                                                                                                                                                                                                                                      |
| `commercializerChecker`     | Address         | Commercializers that are allowed to commercially exploit the original work. If zero address, then no restrictions are enforced.                                                                                                                                                                                                                                                                        |
| `commercializerCheckerData` | Bytes           | The data to be passed to the commercializer checker contract.                                                                                                                                                                                                                                                                                                                                          |
| `commercialRevShare`        | [0-100,000,000] | Amount of revenue (from any source, original & derivative) that must be shared with the licensor (a value of 10,000,000 == 10% of revenue share). This will collect all revenue from tokens that are whitelisted in the [RoyaltyModule.sol contract](https://github.com/storyprotocol/protocol-core-v1/blob/e339f0671c9172a6699537285e32aa45d4c1b57b/contracts/modules/royalty/RoyaltyModule.sol#L50). |
| `commercialRevCeiling`      | #               | If `commercialUse` is set to true, this value determines the maximum revenue you can earn from the original work.                                                                                                                                                                                                                                                                                      |
| `derivativesAllowed`        | True/False      | Indicates whether the licensee can create derivatives of his work or not.                                                                                                                                                                                                                                                                                                                              |
| `derivativesAttribution`    | True/False      | If true, derivatives that are made must give credit to the original work.                                                                                                                                                                                                                                                                                                                              |
| `derivativesApproval`       | True/False      | If true, the licensor must approve derivatives of the work.                                                                                                                                                                                                                                                                                                                                            |
| `derivativesReciprocal`     | True/False      | If false, you cannot create a derivative of a derivative. Set this to true to allow indefinite remixing.                                                                                                                                                                                                                                                                                               |
| `derivativeRevCeiling`      | #               | If `commercialUse` is set to true, this value determines the maximum revenue you can earn from derivative works.                                                                                                                                                                                                                                                                                       |
| `currency`                  | Address         | The ERC20 token to be used to pay the minting fee. The token must be registered on Story.                                                                                                                                                                                                                                                                                                              |
| `uri`                       | String          | The URI of the license terms, which can be used to fetch [off-chain license terms](/concepts/programmable-ip-license/pil-terms#off-chain-terms-to-be-included-in-uri-field).                                                                                                                                                                                                                           |

# Off-chain terms to be included in `uri` field

Some PIL terms must be stored off-chain and passed in the `uri` field above. This is because these terms are often more lengthy and/or descriptive, so it would not make sense to store them on-chain.

| Parameter                       | Description                                                                                                                                                                                                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `territory`                     | Limit usage of the IP to certain regions and/or countries. By default, the IP can be used globally.                                                                                                                                                   |
| `channelsOfDistribution`        | Restrict usage of the IP to certain media formats and use in certain channels of distribution. By default, the IP can be used across all possible channels of distribution. Examples: "television", "physical consumer products", "video games", etc. |
| `attribution`                   | If the original author should be credited for usage of the IP. By default, you do not need to provide credit to the original author.                                                                                                                  |
| `contentStandards`              | Set content standards around use of the IP. By default, no standards apply. Examples: "No-Hate", "Suitable-for-All-Ages", "No-Drugs-or-Weapons", "No-Pornography".                                                                                    |
| `sublicensable`                 | Derivative works can grant the same rights they received under this license to a 3rd party, without approval from the original licensor. By default, derivatives may not do so.                                                                       |
| `aiLearningModels`              | Whether or not the IP can be used to develop AI learning models. By default, the IP **cannot** be used for such development.                                                                                                                          |
| `restrictionOnCrossPlatformUse` | Limit licensing and creation of derivative works solely on the app on which the IP is made available. By default, the IP can be used anywhere.                                                                                                        |
| `governingLaw`                  | The laws of a certain jurisdiction by which this license abides. By default, this is California, USA.                                                                                                                                                 |
| `alternativeDisputeResolution`  | Please see section 3.1 (s) [here](<https://github.com/piplabs/pil-document/blob/main/Story%20Foundation%20-%20Programmable%20IP%20License%20(1.31.25).pdf>).                                                                                          |
| `additionalParameters`          | There may be other terms the licensor would like to add and they can do so in this tag.                                                                                                                                                               |


# 💊 Programmable IP License (PIL)

The PIL is a legal off-chain document based on US copyright law created by the Story team.

The parameters outlined in the PIL (ex. "Commercial Use", "Derivatives Allowed", etc) have been mapped on-chain, which means they can be enforced on-chain via our protocol, bridging code and law and unlocking the benefit of transparent, autonomous, and permission-less smart contracts for the world of intellectual property.

<CardGroup cols={1}>
  <Card
    title="PIL Legal Text"
    href="https://github.com/piplabs/pil-document/blob/main/Story%20Foundation%20-%20Programmable%20IP%20License%20(1.31.25).pdf"
    icon="scroll"
    color="#ccb092"
  >
    Check out the actual PIL legal text. It is very human-readable for a legal
    text!
  </Card>
</CardGroup>

The PIL is the first and currently only example of a [License Template](/concepts/licensing-module/license-template). A License Template is simply a traditional legal document that has been brought on-chain and contains a set of pre-defined terms that people must set, like:

- `commercialUse` - can someone use my work commercially?
- `mintingFee` - the cost of minting a license to use my work in your own works.
- `derivativesAttribution` - does someone have to credit me in their derivative works?

In code, these terms form a struct that represent their legal off-chain counterparts. To see all of the terms defined by the PIL and their associated explanations in code, see [PIL Terms](/concepts/programmable-ip-license/pil-terms).

To see example configurations ("flavors") of the PIL, see [PIL Flavors (examples)](/concepts/programmable-ip-license/pil-flavors).

## The Background Story

<Note>

If you just want to get started developing with the PIL, you can skip this section.

</Note>

We designed Story's [📜 Licensing Module](/concepts/licensing-module/overview) to power the expansion of emerging forms of creativity, such as authorized remixes and co-creation. Our protocol can support any media format or project, ranging from user-generated social videos & images to Hollywood-grade collaborative storytelling.

Intellectual property owners can permit other parties to use, or build on, their work by granting rights in a license, which can be for profit or for the common good. In the media world, these licenses are generally highly tailored contracts, which vary by media formats and the unique needs of licensors - often requiring unique expertise (via lawyers) and significant resources to create.

We searched for a form of a "universal license" that could support these emerging activities at scale. Hat tip to [Creative Commons](https://creativecommons.org/mission/), [Arweave](https://mirror.xyz/0x64eA438bd2784F2C52a9095Ec0F6158f847182d9/AjNBmiD4A4Sw-ouV9YtCO6RCq0uXXcGwVJMB5cdfbhE), A16Z / [Can't Be Evil,](https://a16zcrypto.com/posts/article/introducing-nft-licenses/) The [Token-Bound NFT License](https://james.grimmelmann.net/files/articles/token-bound-nft-license.pdf) and music rights organizations, among others. But we simply couldn't find one framework or agreement robust enough - so with our expert legal counsel (with special thanks to Ghaith Mahmood and Heather Liu) we created one ourselves! **Introducing the Programmable IP License (PIL:pill:)**, the first example of a [License Template](/concepts/licensing-module/license-template) on the protocol.

## Feedback

We are excited to collect feedback and collaborate with IP owners to unlock the potential of their works - please let us know what you think! We can be reached at `legal@storyprotocol.xyz`.

<CardGroup cols={1}>
  <Card
    title="PIL Legal Text"
    href="https://github.com/piplabs/pil-document/blob/main/Story%20Foundation%20-%20Programmable%20IP%20License%20(1.31.25).pdf"
    icon="scroll"
    color="#ccb092"
  >
    Check out the actual PIL legal text. It is very human-readable for a legal
    text!
  </Card>
</CardGroup>


# Story Attestation Service

<Accordion title="Skip the Read - 1 Minute Summary" icon="circle-info">
  You can think of the Story Attestation Service (SAS) as a bunch of independent service providers (infringement, identity, etc) each proving the validity of an IP in their own way. So that each IP has a set of "badges" on it displaying the results.

It's then up to the ecosystem/market to determine which providers they trust or want to believe. This becomes a decentralized "validator"-like approach to IP validity, where if an IP Asset has lots of providers saying it is valid, then it probably valid.

</Accordion>

Story employs a multi-layered decentralized approach to validating intellectual property, grounded in two foundational components:

1. The Story Attestation Service (SAS): leverages a network of specialized service providers — each detecting copyright violations across different mediums (images, audio, etc) — to provide transparent, publicly accessible signals on the legitimacy of an [🧩 IP Asset](/concepts/ip-asset). Applications that facilitate IP registration (e.g. original content) may also attest to the provenance of an IP asset (called "apptestations") in the future.
2. The [❌ Dispute Module](/concepts/dispute-module): offers a flexible framework for resolving conflicts, tapping both on-chain and off-chain processes to accommodate the nuanced nature of IP disputes.

This blend of detection methods and dispute resolution creates a robust ecosystem that allows IP to be registered without introducing undue friction, while letting the market, and individual ecosystem apps, determine how much weight to give each attestation provider.

These layers make up the **IP Validation Service (IPVS)** - a fully decentralized marketplace of trust. The existing system of detection providers will continue to expand into a broader ecosystem of signal contributors, each able to offer specialized, verifiable assessments of IP authenticity. Through incentivized participation, IPVS fosters a self-sustaining market where different validators collaborate to deliver specialized signals.

So rather than preventing duplicates, which would cause far more potentially disruptive front running risk, the signals and attestations allow the original IPs surface above the rest.

## "When does the SAS scan my IP?"

<Note>
  It's important to note that the Story Attestation Service only runs IP infringement checks on **commercial IP**. That is, IP Assets who have at least one [License Terms](/concepts/licensing-module/license-terms) where `commercialUse = true`.

If your IP is non-commercial, then this section doesn't apply to you.

</Note>

When [registering your IP on Story](/developers/tutorials/how-to-register-ip-on-story), you pass in IP-specific metadata that implements the [📝 IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard). In this standard, you'll see 3 fields:

| Property Name | Type     | Description                                                                                                                                                                                                                    |
| :------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mediaUrl`    | `string` | Used for infringement checking, points to the actual media (ex. image or audio)                                                                                                                                                |
| `mediaHash`   | `string` | Hashed string of the media using SHA-256 hashing algorithm. See [here](/concepts/ip-asset/ipa-metadata-standard#hashing-content) for how that is done.                                                                         |
| `mediaType`   | `string` | Type of media (audio, video, image), based on [mimeType](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types). See the allowed media types [here](/concepts/ip-asset/ipa-metadata-standard#media-types). |

These are used for the commercial infringement check. Whatever media you pass in through `mediaUrl` will be checked by our infringement detection providers and flagged if infringement is detected.

If you do not pass in these `media.*` fields, then an infringement detection will not be performed and your IP will not be proven valid.

### Current Limitations

- You must set the `media.*` fields before attaching commercial terms (`commercialUse = true`), otherwise no check will be performed.
- Attestations will only show up on the IP Portal (our "GitHub for IP" platform coming soon). We are working on publishing attestations to public record so anyone can access the results (**COMING SOON!**).
- Only media that is **existing on the internet** will be detected. If someone registers new IP on Story, it will simply return validated because our providers don't have data on it.

## Current Providers

<CardGroup cols={2}>
  <Card title="Yakoa" href="https://www.yakoa.io/" icon="house" color="#190087">
    Yakoa uses AI and machine learning to scan multiple blockchains, analyzing on-chain data to detect direct copies, stylistic forgeries, and unauthorized replications of digital assets. It compares new assets against a database of known IP, flagging potential violations in real time and providing detailed audit logs for enforcement.
  </Card>

  <Card title="Pex" href="https://www.pex.com/" icon="house" color="#019cf4">
    Pex.com is a digital platform that leverages advanced content recognition and analytics to help creators and rights holders track, manage, and monetize their visual and audio media online. It monitors how content is used across the web, making it easier for users to discover licensing opportunities and protect their intellectual property.
  </Card>
</CardGroup>

## Becoming an Attestation Provider

The Story Attestation Service is undergoing active development. If you run any form of IP validation (infringement, identity, origin, etc), then you can become an attestation provider. To do so, please fill out this [form](https://docs.google.com/forms/d/10n3AnWoiLsxpaY17kJlxRazysDe8aOWJgirRnfkFRAk/edit).


# IP Royalty Vault

<Accordion title="Skip the Read - 1 Minute Summary" icon="circle-info">
  An IP Royalty Vault is a pool for all monetary inflows related to an IP Asset.

Every IP Asset has 100,000,000 Royalty Tokens associated with it, where each token represents the right to 0.000001% of that IPA's revenue (_"Revenue Tokens"_) stored in the pool.

Revenue Tokens are ERC-20 tokens used for payment (ex. WIP). These tokens must be whitelisted by the protocol to be used.

</Accordion>

Each IP Asset has an IP Royalty Vault, which acts as a pool for all monetary inflows related to an IP Asset's commercial exploration or from minting licenses. Anyone who holds Royalty Tokens (defined below) has the right to claim their share of this pool.

<CardGroup cols={1}>
  <Card
    title="IPRoyaltyVault.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/royalty/policies/IpRoyaltyVault.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the IP Royalty Vault.
  </Card>
</CardGroup>

## Token Terminology

1. **Royalty Tokens**: the IP Royalty Vault contract is also the ERC-20 contract for the Royalty Tokens of each IP Asset. This means the address of the IP Royalty Vault for an IP Asset is also the ERC-20 token address of the Royalty Tokens. Each IP Asset has 100,000,000 Royalty Tokens associated, where each token represents 0.000001% of those gains. The holders of these Royalty Tokens can claim the Revenue Tokens (defined below) that are in the associated IP Royalty Vault.
2. **Revenue Tokens**: these are the tokens used for payment (ie. WIP). Royalty Tokens can be used to claim Revenue Tokens. Read below on whitelisting ⤵️

### Whitelisted Revenue Tokens

An ERC-20 token must be whitelisted by our protocol in the [RoyaltyModule.sol contract](https://github.com/storyprotocol/protocol-core-v1/blob/e339f0671c9172a6699537285e32aa45d4c1b57b/contracts/modules/royalty/RoyaltyModule.sol#L50) to be used as a Revenue Token. Here are the whitelisted tokens:

<Tabs>
  <Tab title="Aeneid Testnet">
    | Token  | Contract Address                             | Explorer                                                                                                                   | Mint                                                                                                                                                |
    | :----- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
    | WIP    | `0x1514000000000000000000000000000000000000` | [View here ↗️](https://aeneid.storyscan.io/address/0x1514000000000000000000000000000000000000) | N/A                                                                                                                                                 |
    | MERC20 | `0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E` | [View here ↗️](https://aeneid.storyscan.io/address/0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E) | [Mint ↗️](https://aeneid.storyscan.io/address/0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E?tab=write_contract#0x40c10f19) |
  </Tab>

  <Tab title="Mainnet">
    | Token | Contract Address                             | Explorer                                                                                                                   | Mint |
    | :---- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :--- |
    | WIP   | `0x1514000000000000000000000000000000000000` | [View here ↗️](https://aeneid.storyscan.io/address/0x1514000000000000000000000000000000000000) | N/A  |
  </Tab>
</Tabs>

## How to obtain Royalty Tokens?

When an IP Asset receives revenue, it is deposited into its IP Royalty Vault. In order to claim revenue from this vault, you must have the associated Royalty Tokens. Once any address owns Royalty Tokens of a given IP Asset, it is entitled to that % (% of the total supply of Royalty Tokens owned) of any future Revenue Token (that is whitelisted) received & in the IP Royalty Vault.

There are two ways that trigger the IP Royalty Vault deployment and make the initial Royalty Token distribution - whichever comes first:

1. A License Token is minted from an IP for the first time: the associated IP Account (the parent's IP Account) receives 100% of the Royalty Tokens
2. An IP registers as a derivative: the associated IP Account (the child's IP Account) receives 100% Royalty Tokens, and then distributes x% of it to ancestors based on the License Terms

Because Royalty Tokens are ERC-20, they can be transferred like any other token. Thus, the IP Account could send them to someone else, or even put them up for sale on the secondary market.

## How Revenue Flows

This section will help explain how revenue flows from the time of payment to being claimed by the royalty token holder. For the purposes of explanation, we will use an example from the [Liquid Absolute Percentage (LAP)](/concepts/royalty-module/liquid-absolute-percentage), but it is the same for any royalty policy.

Imagine we have a scenario where IPA4 tips IPA3 1M WIP by calling `payRoyaltyOnBehalf`.

1. Revenue Tokens flow to the Royalty Module contract. This contract then splits up the tokens based on the **royalty stack** on the receiving IPA. In this case, IPA3 has a royalty stack of 15%, so 850k tokens flow to IP Royalty Vault 3, and 150k tokens flow to the LAP contract.

<Frame>
  <img src="/images/concepts/lap-1.png" alt="Revenue Flow Step 1" />
</Frame>

<br />

2. The LAP contract separates the payment to the ancestors by calling `transferToVault`. In this case, IPA2 deserves 100k (10% of IPA3's earnings) and IPA1 deserves 50k (5% of IPA3's earnings).

<Frame>
  <img src="/images/concepts/lap-2.png" alt="Revenue Flow Step 2" />
</Frame>

<br />

3. Now that the Revenue Tokens are in the IP Royalty Vaults, the associated Royalty Token holders can claim from the vaults. Remember, the Revenue Tokens get claimed to whoever holds the Royalty Tokens. In the most common case, they are in the IP Account since that's where they originate. To claim, you would call either `claimRevenueOnBehalfByTokenBatch` or `claimRevenueOnBehalf`.

<Frame>
  <img src="/images/concepts/lap-3.png" alt="Revenue Flow Step 3" />
</Frame>

### External Royalty Policies

Revenue Tokens can also move from a vault to another vault via the functions `claimByTokenBatchAsSelf` located in the `IpRoyaltyVault.sol` contract. For this to be possible the vault that is claiming revenue tokens needs to own Royalty Tokens of the vault being claimed from. This can be particularly useful when used together with external royalty policies.

Vaults can only claim from other vaults if those other vaults belong to IPs in the same derivative chain. If a vault owns royalty tokens from an IP but it is not an ancestor of that IP, it is not possible to claim rewards with those royalty tokens.


# External Royalty Policies

There can be many flavors and variations of royalty distribution rules as we observe in the real world. The same can be expected onchain. Whenever a use case requires unique and specific royalty rules, then those set of rules can be registered as an **External Royalty Policy**.

## 1. What is an External Royalty Policy?

It is a smart contract that inherits a specific interface called `IExternalRoyaltyPolicy`, which defines the view function below:

<CardGroup cols={1}>
  <Card
    title="IExternalRoyaltyPolicy.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/interfaces/modules/royalty/policies/IExternalRoyaltyPolicy.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for external royalty policies.
  </Card>
</CardGroup>

```solidity IExternalRoyaltyPolicy.sol
/// @notice Returns the amount of royalty tokens required to link a child to a given IP asset
/// @param ipId The ipId of the IP asset
/// @param licensePercent The percentage of the license
/// @return The amount of royalty tokens required to link a child to a given IP asset
function getPolicyRtsRequiredToLink(address ipId, uint32 licensePercent) external view returns (uint32);
```

After developing your smart contract make sure it inherits the interface above and you can register your new External Royalty Policy by calling `registerExternalRoyaltyPolicy` function in [RoyaltyModule.sol](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/royalty/RoyaltyModule.sol).

## 2. How does it work?

Let's follow an example of a new External Royalty Policy called "Policy X".

### External Royalty Policies are selected by users

An IPA owner decides the royalty policy he/she wants to allow the IP to be remixed with. There are multiple options of royalty rules that can be chosen such as LAP, LRP and other External Royalty Policies. Let's say the user decides to mint a license token with "Policy X". After that, IP2 remixes IP1 and IP3 remixes IP2 and we have the situation as the image below:

<Frame>
  <img src="/images/concepts/ep-0.png" alt="External Royalty Policy Example" />
</Frame>

Every time there is a remix - the link between the parent and derivative has 2 data points associated:

1. The royalty policy address
   1. "Policy X" address in the example
2. The percentage of royalty tokens the parent demands from derivatives. This percentage can have different meanings depending on the royalty policy being used - ie. it can be a relative percentage, an absolute percentage, an adjusted percentage according to specific rules, etc.
   1. 10% between IP1 and IP2
   2. 50% between IP2 and IP3

### External Royalty Policies receive royalty tokens from their users' IPs

Following the example, when each remix is made and during the `onLinkToParents` function call in [RoyaltyModule.sol](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/royalty/RoyaltyModule.sol), the function `getPolicyRtsRequiredToLink` is called on the "Policy X" address.

```solidity IExternalRoyaltyPolic.sol
/// @notice Returns the amount of royalty tokens required to link a child to a given IP asset
/// @param ipId The ipId of the IP asset
/// @param licensePercent The percentage of the license
/// @return The amount of royalty tokens required to link a child to a given IP asset
function getPolicyRtsRequiredToLink(address ipId, uint32 licensePercent) external view returns (uint32);
```

It should return the % of derivative's royalty tokens that the royalty policy demands for the link to happen. That share of royalty tokens are sent to the "Policy X" contract. In the example case:

- "Policy X" receives 3% of RT2 token supply that it can then redistributed to its userbase. IP1 owner wanted 10%, however - let's assume for the sake of the example - that due to the specific use case of "Policy X" and its custom logic, the IP2 owner is granted a special status in the platform in which it it has a 70% discount on the % share it has to give parent IPs due to having a very large distribution network to promote IPs. Therefore, instead of having to give 10% as the license percentage indicated it only gives 3%.
- "Policy X" receives 50% of RT3 token supply that it can then redistributed to its userbase.

<Frame>
  <img src="/images/concepts/ep-1.png" alt="Royalty Token Distribution" />
</Frame>

### External Royalty Policies redistribute value back to their users according to custom rules

There are two ways in which an External Royalty Policy can redistribute value back to its users:

1. Send Royalty Tokens directly to its users
2. Keep the Royalty Tokens in the External Royalty Policy contract and have users claim Revenue Tokens through the said contract

Let's explore both in the context of "Policy X". Let's say that from the 50% of RT3 token supply "Policy X" received - 40% are kept in the "Policy X" contract and 10% are sent to an ancestor royalty vault (IP1).

<Frame>
  <img src="/images/concepts/ep-2.png" alt="Royalty Token Redistribution" />
</Frame>

Now let's imagine there is a 1M payment made to IP3 - an example of how the flow would be:

<Frame>
  <img src="/images/concepts/ep-3.png" alt="Payment Flow Example" />
</Frame>

From the 1M WIP inflow to IP3 Royalty Vault:

- 500k WIP are claimed by the IP Account 3 which had 50% of RT3 token supply
- 100k WIP are claimed by the IP1 Royalty Vault which has 10% of RT3 token supply via `claimByTokenBatchAsSelf` function
- 400k WIP are claimed by "Policy X" which has 40 of RT3 token supply. This amount is further split by "Policy X" custom contract according to its specific rules - which define y% and z% - to its users.


# Liquid Absolute Percentage (LAP)

<Accordion title="Skip the Read - 1 Minute Summary" icon="circle-info">
  Let's come up with an example: An IP Asset ('C') is a child of 'B', and 'B' is a child of 'A', such that it goes A▶️B▶️C. 'A' specifies that any descendant must share 5% of their revenue with it. On the other hand, 'B' specifies that any descendants must share 10% of their revenue with it.

Okay, great. Let's see what happens in two (independent) common scenarios:

1. **Minting a License** - 'C' mints a license from 'B' that costs 100 WIP. When 'C' pays 'B' 100 WIP to mint a license, 'A' claims 5 WIP from B. In the end, 'B' only gets 95 WIP.
2. **Tipping Directly** - 'C' is a comic book that is super well written. Someone tips 100 WIP to 'C' because they love it. 'A' claims 5 WIP from 'C'. 'B' claims 10 WIP from 'C'. In the end, 'C' only gets 85 WIP.

</Accordion>

The Liquid Absolute Percentage (LAP) defines that each parent IP Asset can choose a minimum royalty percentage that all of its downstream IP Assets in a derivative chain will share from their monetary gains as defined in the license agreement.

<CardGroup cols={1}>
  <Card
    title="RoyaltyPolicyLAP.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/royalty/policies/LAP/RoyaltyPolicyLAP.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the LAP Royalty Policy.
  </Card>
</CardGroup>

## Prerequisites

Before continuing, make sure you have read the [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault) terminology.

The License Royalty % in this page correspond to the same value as the `commercialRevShare` on the PIL terms.

## Royalty Payment and Claiming Flow

In the image below, IPA 1 and IPA 2 - due to being ancestors of IPA 3 - have a % economic right over revenue made by IPA 3. Key notes to understand the derivative chain below:

- License Royalty Percentage - this percentage is selected by the user and it means the percentage that the user wants - according to LAP rules - in return for allowing other users to remix its IPA.
- Royalty Stack - is the revenue an IPA has to pay all its ancestors. For LAP royalty stack = sum of parents royalty stack + sum of licenses percentages used to connect to each parent
  - Royalty Stack IPA 2 = Royalty Stack IPA 1 + License Royalty % between IPAs 1 and 2 = 0% + 5% = 5%
  - Royalty Stack IPA 3 = Royalty Stack IPA 2 + License Royalty % between IPAs 2 and 3 = 5% + 10% = 15%
- Royalty Tokens flow to the IPA initially when a vault is deployed. The Royalty Tokens can be transferred to any other address and after that transfer any future royalty inflow will be claimable by that new address which now holds the RTs.

<Frame>
  <img src="/images/concepts/lap-0.png" alt="Royalty Payment Flow" />
</Frame>

Now, let's imagine a scenario where a new IP Asset 4 intends to join the derivative chain as a derivative of IP Asset 3. An example flow sequence below:

1. IP Asset 4 pays 1M WIP in royalties to its parent IPA 3 by calling `payRoyaltyOnBehalf`. Note that the royalty process is the same whether the payment is the license minting fee or any other royalty payment - with the difference being that the license minting fee is made via `payLicenseMintingFee` and is mandatory upon derivative creation. Once a payment is made, a share equivalent to the IPA 3 royalty stack % is sent to the royalty policy contract and the remaining amount is sent to the IPA 3 vault.

<Frame>
  <img src="/images/concepts/lap-1.png" alt="Payment Distribution" />
</Frame>

2. Each ancestor can call `transferToVault` on the royalty policy contract to receive the amount each ancestor has the right to claim from a given descendant. Funds are moved to the ancestor's IP Royalty Vault.
   1. 100k WIP are transferred to the IP Royalty Vault 2 since it the right to 10% of all IPA 2 descendants revenue
   2. 50k WIP are transferred to the IP Royalty Vault 1 since it the right to 5% of all IPA 2 descendants revenue

<Frame>
  <img src="/images/concepts/lap-2.png" alt="Transfer to Vault" />
</Frame>

3. In the final step of the claiming flow, any Royalty Token holder address can call `claimRevenueOnBehalfByTokenBatch`/`claimRevenueOnBehalf` (for non-vault claimers) or `claimRevenueByTokenBatchAsSelf` (when the claimer is an IP Royalty Vault) to claim revenue tokens. In the current example:

   1. 50k WIP are claimed to the IPA 1 which holds 100% RT1
   2. 100k WIP are claimed to the IPA 2 which holds 100% RT2
   3. 850k WIP are claimed by IPA 3 which holds 100% RT3

<Note>
  Any royalty token holder address can claim - whether it is a smart contract,
  IPA, or EOA.
</Note>

<Frame>
  <img src="/images/concepts/lap-3.png" alt="Claiming Revenue" />
</Frame>


# Liquid Relative Percentage (LRP)

<Accordion title="Skip the Read - 1 Minute Summary" icon="circle-info">
  Let's come up with an example: An IP Asset ('C') is a child of 'B', and 'B' is a child of 'A', such that it goes A▶️B▶️C. 'A' specifies that any **direct** descendant must share 5% of their revenue with it. On the other hand, 'B' specifies that any **direct** descendants must share 10% of their revenue with it.

Okay, great. Let's see what happens in two (independent) common scenarios:

1. **Minting a License** - 'C' mints a license from 'B' that costs 100 WIP. When 'C' pays 'B' 100 WIP to mint a license, 'A' claims 5 WIP from B. In the end, 'B' only gets 95 WIP.
2. **Tipping Directly** - 'C' is a comic book that is super well written. Someone tips 100 WIP to 'C' because they love it. 'B' claims 10 WIP from 'C'. 'A' claims 0.5 WIP from 'B' (5% of 10). In the end, 'C' only gets 90 WIP.

</Accordion>

The Liquid Relative Percentage (LRP) royalty policy defines that each parent IP Asset can choose a minimum royalty percentage that only the direct derivative IP Assets in a derivative chain will share from their monetary gains as defined in the license agreement.

<CardGroup cols={1}>
  <Card
    title="RoyaltyPolicyLRP.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/royalty/policies/LRP/RoyaltyPolicyLRP.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the LRP Royalty Policy.
  </Card>
</CardGroup>

## Prerequisites

Before continuing, make sure you have read the [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault) terminology.

The License Royalty % in this page correspond to the same value as the `commercialRevShare` on the PIL terms.

## Royalty Payment and Claiming Flow

In the image below, IPA 1 and IPA 2 - due to being ancestors of IPA 3 - have a % economic right over revenue made by IPA 3. Key notes to understand the derivative chain below:

- License Royalty Percentage - this percentage is selected by the user and it means the percentage that the user wants - according to LRP rules - in return for allowing other users to remix its IPA.
- Royalty Stack LRP - is the revenue an IPA has to pay all its parent. For LRP royalty stack = sum of licenses percentages used to connect to each parent
  - Royalty Stack IPA 2 = License Royalty % between IPAs 1 and 2 = 5%
  - Royalty Stack IPA 3 = License Royalty % between IPAs 2 and 3 = 10%
- Royalty tokens flow to the IPA initially when a vault is deployed. The Royalty Tokens can be transferred to any other address and after that transfer any future royalty inflow will be claimable by that new address which now holds the RTs.

<Frame>
  <img
    src="/images/concepts/lrp-0.png"
    alt="Royalty Payment Flow"
    className="mx-auto"
  />
</Frame>

Now, let's imagine a scenario where a new IP Asset 4 intends to join the derivative chain as a derivative of IP Asset 3. An example flow sequence below:

1. IP Asset 4 pays 1M WIP in royalties to its parent IPA 3 by calling `payRoyaltyOnBehalf`. Note that the royalty process is the same whether the payment is the license minting fee or any other royalty payment - with the difference being that the license minting fee is made via `payLicenseMintingFee` and is mandatory upon derivative creation. Once a payment is made, a share equivalent to the IPA 3 royalty stack % is sent to the royalty policy contract and the remaining amount is sent to the IPA 3 vault.

<Frame>
  <img
    src="/images/concepts/lrp-1.png"
    alt="Payment Distribution"
    className="mx-auto"
  />
</Frame>

2. Each ancestor can call `transferToVault` on the royalty policy contract to receive the amount each ancestor has the right to claim from a given descendant. Funds are moved to the ancestor's IP Royalty Vault.
   1. 95k WIP are transferred to the IP Royalty Vault 2 since it has the right to 10% of all IPA 2 descendants revenue and has to pay 5% of its revenue to its direct parent IPA 1. So 100k is received from IPA 3 and 5k is paid to IPA 1, resulting in IPA 2 keeping 100k - 5k = 95k.
   2. 5k WIP are transferred to the IP Royalty Vault 1 since it has the right to 0.5% of all IPA 2 descendants revenue. IPA 1 has the right to 5% of revenue earned by IPA 2, which in turn has 10% of revenue earned by IPA 3. Given LRP royalty policy considers relative percentages, then IPA 1 has the right to 10%\*5% = 0.5% of revenue earned by IPA 3.

<Frame>
  <img
    src="/images/concepts/lrp-2.png"
    alt="Transfer to Vault"
    className="mx-auto"
  />
</Frame>

3. In the final step of the claiming flow, any Royalty Token holder address can call `claimRevenueOnBehalfByTokenBatch`/`claimRevenueOnBehalf` (for non-vault claimers) or `claimRevenueByTokenBatchAsSelf` (when the claimer is an IP Royalty Vault) to claim revenue tokens. In the current example:

   1. 5k WIP are claimed to the IPA 1 which holds 100% RT1
   2. 95k WIP are claimed to the IPA 2 which holds 100% RT2
   3. 900k WIP are claimed by IPA 3 which holds 100% RT3

<Note>
  Any royalty token holder address can claim - whether it is a smart contract,
  IPA, or EOA.
</Note>

<Frame>
  <img
    src="/images/concepts/lrp-3.png"
    alt="Claiming Revenue"
    className="mx-auto"
  />
</Frame>


# 💸 Royalty Module

The Royalty Module defines how revenue flows between IPs on Story. More specifically, between parent and child [🧩 IP Assets](/concepts/ip-asset/overview). There are two common scenarios when revenue flow would happen:

1. Minting a License - when you mint a [License Token](/concepts/licensing-module/license-token) that has a `mintingFee`. When this is paid by someone (who wants to register a derivative or simply hold the license), the revenue should flow up the ancestry chain.
2. Tipping Directly - if someone sends revenue to an IP directly, it should flow up the chain.

<CardGroup cols={1}>
  <Card
    title="RoyaltyModule.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/royalty/RoyaltyModule.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Royalty Module.
  </Card>
</CardGroup>

## High-Level Example

The below example (using [Liquid Absolute Percentage](/concepts/royalty-module/liquid-absolute-percentage) ) shows what happens when an IP Asset 4 (IPA4) tips IPA3 1,000,000 WIP.

1. Revenue first flows to the Royalty Module contract
2. Royalty Module sends WIP to both IPA3 and the LAP contract based on the **royalty stack** (15%)
3. LAP will distribute funds to further ancestors since they have negotiated some license agreement where they are due revenue from IPA3's earnings.

<Note>

Don't worry if you don't understand everything in the picture, this is just to show you an overview of what the Royalty Module is all about.

</Note>

<Frame>
  <img
    src="/images/concepts/royalty-module-overview.png"
    alt="Royalty Module Flow Example"
  />
</Frame>

## Royalty Policies

Royalty policies are a component of the license agreement between two IP Assets. It defines how revenue flow actually happens.

The Royalty Module supports both whitelisted/native policies created by our team directly, and external ones created by you.

<Note>
An IP Asset without any parents can mint licenses with different royalty policies while a derivative IP Asset inherits the royalty policy of its parents.

Additionally, there will always be one royalty policy governing every link an IP Asset has with each of its derivatives.

</Note>

### Whitelisted/Native Royalty Policies

These policies require governance whitelisting and guarantee royalty token distribution to ancestors.

1. [Liquid Absolute Percentage (LAP)](/concepts/royalty-module/liquid-absolute-percentage)
2. [Liquid Relative Percentage (LRP)](/concepts/royalty-module/liquid-relative-percentage)

### External Royalty Policies

These policies can be registered in a permission-less way and stipulate their own royalty and revenue distribution rules.

- [External Royalty Policies](/concepts/royalty-module/external-royalty-policies)

## Royalty Token % vs Royalty Stack %

When creating a derivative, the creator will want to answer the question: "How much percentage of my IP earnings will I keep and how much will go to ancestor IPs?

To answer this question two concepts are important:

1. Royalty Token - Each IP Asset has 100,000,000 Royalty Tokens associated, where each token represents 0.000001% of the capital that enters each IP Royalty Vault. The holders of these Royalty Tokens can claim the Revenue Tokens that are in the associated IP Royalty Vault.
2. Royalty Stack - is the percentage of IP revenue that has to be paid to ancestors via Whitelisted/Native royalty policies. External royalty policies do not use the royalty stack percentage - only Whitelisted/Native royalties policies do.

Let's imagine the scenario below:

- IP1 is a root IP Asset.
- IP2 is a derivative of IP1.
- User A has 100% of Royalty Tokens of IP1
- User B has 20% of Royalty Tokens of IP2
- User C has 80% of Royalty Tokens of IP2
- IP2 Royalty Stack is 10% - meaning that all its ancestor IPs via Native/Whitelisted policies require IP2 to pay 10% of its revenue in order to create the derivative. In this case, there is only 1 ancestor which is IP1. IP1 demands 10% of IP2's future revenue in order to create a derivative.

In the image below there is an example of a one million WIP payment made to IP2. In the image we can see how much each Royalty Token holder of the entire derivative chain receives when the payment is made.

<Frame>
  <img
    src="/images/concepts/rt-vs-rs.png"
    alt="Royalty Token Distribution Example"
  />
</Frame>

- RT Holder A - From the one million WIP payment gets 100k WIP. Royalty Stack percentage is paid first and RT Holder A has 100% of Royalty Tokens of IP1 so gets to keep the whole 100k WIP.
- RT Holder B - From the one million WIP payment gets 180k WIP. IP2 holders as a whole receive 900k WIP from the original one million WIP payment. Those 900k WIP are then split among the different Royalty Token holders of IP2 which are B and C. B has 20% of Royalty Tokens of IP2 so it receives 900k WIP \* 20% = 180k.
- RT Holder C - From the one million WIP payment gets 720k WIP. IP2 holders as a whole receive 900k WIP from the original one million WIP payment. Those 900k WIP are then split among the different Royalty Token holders of IP2 which are B and C. C has 80% of Royalty Tokens of IP2 so it receives 900k WIP \* 80% = 720k.

## Derivative Chain Configurations

<Frame>
  <img
    src="/images/concepts/derivative-chain-config.png"
    alt="Derivative Chain Configurations"
  />
</Frame>

The derivative chain can assume multiple configurations.

Each IP Asset is restricted to a total royalty % of 100%. It will revert when minting a license that would make the IPA reserve more than 100% of its royalty tokens for ancestors, since this would make no sense.


# 🧱 Modules

Modules are standalone contracts that adhere to the [`IModule` interface](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/interfaces/modules/base/IModule.sol). These modules play a crucial role in taking action on IP to change the data/state around or of IP.

## Existing Modules

There are a few important modules, created by the Story team, to be aware of:

| Module                                            | Description                                                                            |
| ------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [📜 Licensing Module](/concepts/licensing-module) | Responsible for defining and attaching licenses to IP Assets.                          |
| [💸 Royalty Module](/concepts/royalty-module)     | Responsible for handling royalty flow between parent & child IP Assets.                |
| [❌ Dispute Module](/concepts/dispute-module)     | Responsible for handling the dispute of wrongfully registered or misbehaved IP Assets. |
| [👥 Grouping Module](/concepts/grouping-module)   | Responsible for handling groups of IPAs.                                               |
| [👀 Metadata Module](/concepts/metadata-module)   | Manage and view metadata for IP Assets.                                                |

## Base Module

The Base Module provides a standard set of must-have functionalities for all modules registered on Story. Anyone wishing to create and register a module on Story must inherit and override the Base Module.

<Note>

View the smart contract [here](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/BaseModule.sol).

</Note>

### Key Features

#### Simplicity and Flexibility

The BaseModule is intentionally kept simple and generalized. It only implements the ERC165 interface, which is crucial for interface detection. This design choice allows for maximum flexibility when developing more specific modules within Story.

#### ERC165 Interface Implementation

By implementing the ERC165 interface, BaseModule allows other contracts to query whether it supports a specific interface. This feature is essential for ensuring compatibility and interoperability within the Story ecosystem and beyond.

```solidity
abstract contract BaseModule is ERC165, IModule {
    ...
}
```

#### `supportsInterface` Function

A key function in the BaseModule is `supportsInterface`, which overrides the ERC165's `supportsInterface` method. This function is crucial for interface detection, allowing the contract to declare support for both its own `IModule` interface and any other interfaces it might inherit.

```solidity
function supportsInterface(bytes4 interfaceId) public view virtual override(ERC165, IERC165) returns (bool) {
    return interfaceId == type(IModule).interfaceId || super.supportsInterface(interfaceId);
}
```


# Overview

A piece of Intellectual Property is represented as an [🧩 IP Asset](/concepts/ip-asset) and its associated [⚙️ IP Account](/concepts/ip-asset/ip-account), a smart contract designed to serve as the core identity for each IP. We also have various [🧱 Modules](/concepts/modules) to add functionality to IP Assets, like creating derivatives of them, disputing IP, and automating revenue flow between them.

<Frame>
  <img src="/images/concepts/story-architecture.png" />
</Frame>

Let's briefly introduce the layers mentioned in the above diagram:

## [🧩 IP Asset](/concepts/ip-asset)

When you want to bring an IP on-chain, you mint an ERC-721 NFT. This NFT represents **ownership** over your IP.

Then, you **register** the NFT in our protocol through the [IP Asset Registry](/concepts/registry/ip-asset-registry). This deploys an [⚙️ IP Account](/concepts/ip-asset/ip-account), effectively creating an "IP Asset". The address of that contract is the identifier for the IP Asset (the `ipId`).

The underlying NFT can be traded/sold like any other NFT, and the new owner will own the IP Asset and all revenue associated with it.

## [⚙️ IP Account](/concepts/ip-asset/ip-account)

IP Accounts are smart contracts that are tied to an IP Asset, and do two main things:

1. Store the associated IP Asset's data, such as the associated licenses and royalties created from the IP
2. Facilitates the utilization of this data by various modules. For example, licensing, revenue/royalty sharing, remixing, and other critical features are made possible due to the IP Account's programmability.

The address of the IP Account is the IP Asset's identifier (the `ipId`).

## [🧱 Modules](/concepts/modules)

Modules are customizable smart contracts that define and extend the functionality of IP Accounts. Modules empower developers to create functions and interactions for each IP to make IPs truly programmable.

We already have a few core modules:

1. [📜 Licensing Module](/concepts/licensing-module): create parent\<->child relationships between IPs, enabling derivatives of IPs that are restricted by the agreements in the license terms (must give attribution, share 10% revenue, etc)
2. [💸 Royalty Module](/concepts/royalty-module): automate revenue flow between IPs, abiding by the negotiated revenue sharing in license terms
3. [❌ Dispute Module](/concepts/dispute-module): facilitates the disputing and flagging of IP
4. [👥 Grouping Module](/concepts/grouping-module): allows for IPs to be grouped together
5. [👀 Metadata Module](/concepts/metadata-module): manage and view metadata for IP Assets

## [🗂️ Registry](/concepts/registry)

The various registries on our protocol function as a primary directory/storage for the global states of the protocol. Unlike IP Accounts, which manage the state of specific IPs, a registry oversees the broader states of the protocol.

## [💊 Programmable IP License (PIL)](/concepts/programmable-ip-license)

The PIL is a real, off-chain legal contract that defines certain **License Terms** for how an IP Asset can be legally licensed. For example, how an IP Asset is commercialized, remixed, or attributed, and who is allowed to do that and under what conditions.

We have mapped these same terms on-chain so you can easily attach terms to your IP Asset for others to seamlessly and transparently license your IP.


# License Terms

When registering your IP on Story, you can attach License Terms to the IP. These are real, legally binding terms enforced on-chain by the [📜 Licensing Module](/concepts/licensing-module/overview), disputable by the [❌ Dispute Module](/concepts/dispute-module/overview), and in the worst case, able to be enforced off-chain in court through traditional means.

In them are also terms for commercial usage, which describes how the [💸 Royalty Module](/concepts/royalty-module/overview) will be enforced (ex. "50% of revenue must be shared with the parent IP").

<CardGroup cols={1}>
  <Card
    title="Example License Terms"
    href="/concepts/programmable-ip-license/pil-flavors"
    icon="ice-cream"
  >
    View some popular combinations of PIL License Terms, also known as
    "flavors".
  </Card>
</CardGroup>

More specifically, License Terms are a particular combination of values from a [License Template](/concepts/licensing-module/license-template). Indeed, there can and will exist **multiple** License Terms (variations) for each License Template. You can imagine that a License Template generates many License Term variations.

<Frame>
  <img
    src="/images/concepts/license-terms-diagram.png"
    alt="License Terms Diagram"
  />
</Frame>

Once registered, **License Terms are immutable — they can't be tampered with or altered**, even by the License Template that generated it.

Additionally, License Terms have a unique numeric ID within the License Template they stem from. This makes License Terms reusable, meaning if someone creates License Terms with a specific set of values, it only needs to be created once and can be used by anyone else.

For example, a particular set of term values of the [Programmable IP License (PIL💊)](/concepts/programmable-ip-license/overview), such as non-commercial usage + derivatives allowed + free minting, defines a unique License Terms with an associated ID.

## License Terms Attached to IP Asset

The owner of a root IP Asset can attach License Terms to signal to other users that they can mint License Tokens of those terms to create a derivative of this IP Asset. **Once License Terms are attached to an IP Asset, it is now considered "public" and anyone can mint a License Token using those terms.**

<Frame>
  <img
    src="/images/concepts/license-terms-attach-diagram.png"
    alt="License Terms Attached to IP Asset"
  />
</Frame>

## Inherited License Terms

On the other hand, derivative IP Assets inherit their License Terms from the parent IP Asset. This means that when an IP Asset registers itself as a derivative, it burns the License Token and inherits the associated License Terms. **The owner of this derivative cannot set new License Terms.**

<Note>

You may be wondering: "if I cannot set new License Terms on my derivative, does that also mean I can't change the minting fee, or disallowing more derivatives, on my derivative?"

Thankfully, there is a way to get around this! Although you cannot change License Terms on a derivative IP, you can utilize the [License Config to implement special behaviors](/concepts/licensing-module/license-config).

</Note>

## Expiration

License Terms support an `expiration` time. Once License Terms expire, any derivatives that abide by that license will no longer be able to generate revenue or create further derivatives. If an IP Asset is a derivative of multiple parents, it will expire when the soonest expiration time between the two parents is reached.


# License Token

<CardGroup cols={1}>
  <Card
    title="LicenseToken.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/LicenseToken.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for License Tokens.
  </Card>
</CardGroup>

A **License Token** is represented as an **ERC-721 NFT** and contains the specific [License Terms](/concepts/licensing-module/license-terms) it represents. Its associated `licenseTokenId` is global, as there is one License Token contract.

Once License Terms are attached to an IP Asset, it becomes public so that anyone can mint a License Token for those terms. A License Token is burned when it is used to register another IP as a derivative of the original IP Asset.

<Frame caption="A diagram showing what happens when a License Token is minted.">
  <img
    src="/images/concepts/license-token-diagram.png"
    alt="A diagram showing what happens when a License Token is minted."
  />
</Frame>

## Private Licenses

<Frame>
  <img
    src="/images/concepts/private-licenses.png"
    alt="A diagram showing how private licenses are minted."
  />
</Frame>

In order to mint a private License Token, the owner of a root IP Asset can issue License Tokens that have terms **not yet attached to the IP Asset itself**. It is important to also note that derivative IP Assets cannot issue private licenses because it is restricted to only issue licenses of its inherited terms.

## Transferability of the License Token

License Tokens might be transferrable or not, depending on the values of the License Terms terms they point to.

Once a non-transferable License Token is minted to a recipient, it is locked there forever.

## Registering a Derivative

You can register an IP Asset as a derivative of other IP Assets, each with their own license terms agreement. This creates a legally binding agreement between IP Assets that enforces things things like automatic payments in the [💸 Royalty Module](/concepts/royalty-module/overview).

### ⚠️ Restrictions

There are a few restrictions on registering a derivative:

- An IP Asset can only register as a derivative one time. If an IP Asset has multiple parents, it must register both at the same time.
- Once an IP Asset is a derivative, it cannot link any more parents.
- When you link an IP Asset as a derivative, it cannot have license terms attached. It will inherit its terms from its parents.
- None of the parent IP Assets or the child IP Asset can be disputed.
- The child IP Asset cannot have derivatives already.
- If at least one of the license terms is commercial, then they all must be commercial (`commercialUse = true`)

---

There are two ways to register a derivative IP Asset.

<Note>
An IP Asset can only register as a derivative one time. If an IP Asset has multiple parents, it must register both at the same time. Once an IP Asset is a derivative, it cannot link any more parents.

</Note>

### 1. Using an Existing License Token

A License Token is burned when it is used to register another IP as a derivative of the original IP Asset.

<Frame>
  <img
    src="/images/concepts/existing-license-token.png"
    alt="Using an Existing License Token"
  />
</Frame>

### 2. Registering a Derivative Directly

You can also register a derivative directly, without the need for a License Token. Remember that if License Terms are attached to an IP Asset it is public to mint the License Token anyway, so this is simply a convenient way to go about it, thus skipping the middle step of minting a License Token.

<Frame>
  <img
    src="/images/concepts/derivative-directly.png"
    alt="Registering a Derivative Directly"
  />
</Frame>


# License Config

## License Config

<CardGroup cols={1}>
  <Card
    title="LicensingConfig Struct"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/lib/Licensing.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the LicensingConfig struct in the smart contract.
  </Card>
</CardGroup>

Optionally, you can attach a `LicensingConfig` to an IP Asset (for a specific `licenseTermsId` attached to that asset) which contains fields like a `mintingFee` and a `licensingHook`, as shown below.

```solidity
/// @notice This struct is used by IP owners to define the configuration
/// when others are minting license tokens of their IP through the LicensingModule.
/// When the `mintLicenseTokens` function of LicensingModule is called, the LicensingModule will read
/// this configuration to determine the minting fee and execute the licensing hook if set.
/// IP owners can set these configurations for each License or set the configuration for the IP
/// so that the configuration applies to all licenses of the IP.
/// If both the license and IP have the configuration, then the license configuration takes precedence.
/// @param isSet Whether the configuration is set or not.
/// @param mintingFee The minting fee to be paid when minting license tokens.
/// @param licensingHook  The hook contract address for the licensing module, or address(0) if none
/// @param hookData The data to be used by the licensing hook.
/// @param commercialRevShare The commercial revenue share percentage.
/// @param disabled Whether the license is disabled or not.
/// @param expectMinimumGroupRewardShare The minimum percentage of the group's reward share
/// (from 0 to 100%, represented as 100 * 10 ** 6) that can be allocated to the IP when it is added to the group.
/// If the remaining reward share in the group is less than the minimumGroupRewardShare,
/// the IP cannot be added to the group.
/// @param expectGroupRewardPool The address of the expected group reward pool.
/// The IP can only be added to a group with this specified reward pool address,
/// or address(0) if the IP does not want to be added to any group.
struct LicensingConfig {
  bool isSet;
  uint256 mintingFee;
  address licensingHook;
  bytes hookData;
  uint32 commercialRevShare;
  bool disabled;
  uint32 expectMinimumGroupRewardShare;
  address expectGroupRewardPool;
}
```

What do some of these mean?

1. `isSet` - if this is false, the whole licensing config is completely ignored. So for example, if the licensing config has `mintingFee == 10` and `disabled == true`, but the `isSet == false`, the `mintingFee` and `disabled` will be completely ignored.
2. `disabled` - if this is true, then no licenses can be minted and no more derivatives can be attached at all for the terms the config is attached to.

Fields like the `mintingFee` and `commercialRevShare` overwrite their duplicate in the license terms themselves. **A benefit of this is that derivative IP Assets, which normally cannot change their license terms, are able to overwrite certain fields.**

The `licensingHook` is an address to a smart contract that implements the `ILicensingHook` interface, which contains a `beforeMintLicenseTokens` function which will be run before a user mints a License Token. This means you can insert logic to be run upon minting a license.

The hook itself is described in a different section. You can see it contains information about the license, who is minting the License Token, and who is receiving it.

<Tip>
  Learn all about Licensing Hooks [here](/concepts/hooks#licensing-hooks).
</Tip>

### Setting the License Config

You can set the License Config by calling the `setLicenseConfig` function in the [LicensingModule.sol contract](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/licensing/LicensingModule.sol).

### Logic that is Possible with License Config

1. **Max Number of Licenses**: The `licensingHook` (described in the next section) is where you can define logic for the max number of licenses that can be minted. For example, reverting the transaction if the max number of licenses has already been minted.
2. **Disallowing Derivatives**: If you register a derivative of an IP Asset, that derivative cannot change its License Terms as described [here](/concepts/licensing-module/license-terms#inherited-license-terms). You can be wondering: "What if I, as a derivative, want to disallow derivatives of myself, but my License Terms allow derivatives and I cannot change this?" To solve this, you can simply set `disabled` to true.
3. **Minting Fee**: Similar to #2 above... what about the minting fee? Although you cannot change License Terms on a derivative IP Asset (and thus the minting fee inside of it), you can change the minting fee for that derivative by modifying the `mintingFee` in the License Config, or returning a `totalMintingFee` from the `licensingHook` (described in the next section).
4. **Commercial Revenue Share**: Similar to #2 and #3 above, you can modify the `commercialRevShare` in the License Config.
5. **Dynamic Pricing for Minting a License Token**: Set dynamic pricing for minting a License Token from an IP Asset based on how many total have been minted, how many licenses the user is minting, or even who the user is. All of this data is available in the `licensingHook` (described in the next section).

... and more.

### Restrictions

See [IP Modifications & Restrictions](/concepts/ip-asset/ipa-modifications) for the various restrictions on setting the License Config.


# License Template

A License Template is a legal framework, written in code ("programmable"), that defines various licensing terms for an IP. Such as:

- "Is commercial use allowed?" - true/false (bool)
- "Is the license transferrable?" - true/false (bool)
- "If commercial, what % of royalty do I receive?" - number

These terms and values differ per License Template.

The first (and currently only) example of a License Template was developed by the Story team directly, and is called the Programmable IP License (PIL :pill:).

<CardGroup cols={2}>
  <Card title="Programmable IP License (PIL)" href="/concepts/programmable-ip-license/overview" icon="pills" color="yellow">
    Learn about the first implementation of a License Template
  </Card>

  <Card title="PIL Smart Contract" href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/licensing/PILicenseTemplate.sol" icon="scroll" color="#ccb092">
    View the smart contract for the PIL.
  </Card>
</CardGroup>

## License Template Requirements

License Templates are responsible for:

- Providing a link to the actual, off-chain, legal contract template, with all the parameters, their possible values, and the correspondent legalese, in `licenseTextUrl`.
  - For a licensing framework to be compatible with Story, the legal text **must** be clear and parametrized, with each licensing parameter establishing the possible outcomes of each value.
  - The parameter values in each License Template (called "License Template terms") drive the legal text for each license agreement.
- Defining a `struct` with the particular definitions of the parameters in accordance, which must be encoded into the License Terms struct (described below).
- Providing registration methods for the License Terms, and getters.
- **Verifying** that both the **minter** and the address **linking a derivative are allowed by the License Template terms to perform those actions**.
  - These conditions could be enforced by the License Template itself or through hooks. They can range from limitations on the derivative creations, token-gating LNFT holders, creative control from licensors, KYC, etc. It's up to the implementation of each License Template.
- **Verifying that the License Terms are compatible if a derivative has or will have multiple parents**

## Create Your Own Template

You can create your own License Template (like the PIL), but it must be approved by the Story team to be fully embedded into the protocol.


# 📜 Licensing Module

<Accordion title="Skip the Read - 1 Minute Summary" icon="circle-info">
  
The Licensing Module allows you to create a real legal license from a **License Template** (which is the [Programmable IP License (PIL💊)](/concepts/programmable-ip-license/overview)) and attach it to your IP Asset. This license, and the **License Terms** that define it, restrict how others can use your IP, commercialize it, and remix it.

If License Terms are attached to an IP Asset, anyone can mint a **License Token** (an ERC-721 NFT) from it which acts as the license to use that work based on the terms that define it. This token can then be burned to register a derivative work. This then establishes a parent-child relationship between assets, unlocking things like automatic royalty flow from the [💸 Royalty Module](/concepts/royalty-module/overview).

</Accordion>

The owner of an IP Asset owns intellectual property rights such as creating derivatives, being commercially exploited, and being reproduced in different platforms.

IP Assets can programmatically grant permissions for any users to exercise those rights with some autonomy via [License Tokens](/concepts/licensing-module/license-token) (an ERC-721 NFT), which point to a particular set of conditions, known as [License Terms](/concepts/licensing-module/license-terms).

<Frame caption="Blue: contracts built into the protocol. White: contracts developed by the community or 3rd party vendor.">
  <img
    src="/images/concepts/licensing-module-diagram.png"
    alt="The contracts in blue are built into the protocol. The contracts in white can be developed by the community or 3rd party vendor."
  />
</Frame>

## LicensingModule

<CardGroup cols={1}>
  <Card
    title="LicensingModule.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/modules/licensing/LicensingModule.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the License Module.
  </Card>
</CardGroup>

The `LicensingModule.sol` contract is the main entry point for the licensing system. It is responsible for:

- Attaching License Terms to IP Assets
- Minting License Tokens
- Registering derivatives
- Setting License Configs

## Further Readings

The following document will walk through all of the major components of the Licensing Module as shown above:

- [License Template](/concepts/licensing-module/license-template)
- [License Terms](/concepts/licensing-module/license-terms)
- [License Token](/concepts/licensing-module/license-token)
- [License Registry](/concepts/registry/license-registry)
- [License Config](/concepts/licensing-module/license-config)


# License Registry

<CardGroup cols={1}>
  <Card
    title="LicenseRegistry.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/registries/LicenseRegistry.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the License Registry.
  </Card>
</CardGroup>

The License Registry stores all license-related states within the protocol, including managing global state like registering new License Templates like the [Programmable IP License (PIL💊)](/concepts/programmable-ip-license/overview), attaching licenses to individual [IP Assets](/concepts/ip-asset/overview), registering derivatives, and the like:

```solidity LicenseRegistry.sol
/// @dev Storage of the LicenseRegistry
/// @param defaultLicenseTemplate The default license template address
/// @param defaultLicenseTermsId The default license terms ID
/// @param registeredLicenseTemplates Registered license templates
/// @param registeredRoyaltyPolicies Registered royalty policies
/// @param registeredCurrencyTokens Registered currency tokens
/// @param parentIps Mapping of parent IPs to derivative IPs
/// @param parentLicenseTerms Mapping of parent IPs to license terms used to link to derivative IPs
/// @param childIps Mapping of derivative IPs to parent IPs
/// @param attachedLicenseTerms Mapping of attached license terms to IP IDs
/// @param licenseTemplates Mapping of license templates to IP IDs
/// @param expireTimes Mapping of IP IDs to expire times
/// @param licensingConfigs Mapping of minting license configs to a licenseTerms of an IP
/// @dev Storage structure for the LicenseRegistry
/// @custom:storage-location erc7201:story-protocol.LicenseRegistry
struct LicenseRegistryStorage {
  address defaultLicenseTemplate;
  uint256 defaultLicenseTermsId;
  mapping(address licenseTemplate => bool isRegistered) registeredLicenseTemplates;
  mapping(address childIpId => EnumerableSet.AddressSet parentIpIds) parentIps;
  mapping(address childIpId => mapping(address parentIpId => uint256 licenseTermsId)) parentLicenseTerms;
  mapping(address parentIpId => EnumerableSet.AddressSet childIpIds) childIps;
  mapping(address ipId => EnumerableSet.UintSet licenseTermsIds) attachedLicenseTerms;
  mapping(address ipId => address licenseTemplate) licenseTemplates;
  mapping(bytes32 ipLicenseHash => Licensing.LicensingConfig licensingConfig) licensingConfigs;
}
```

### Notable Functions

```solidity LicenseRegistry.sol
function attachLicenseTermsToIp(address ipId, address licenseTemplate, uint256 licenseTermsId) external onlyLicensingModule
```

This function allows you to attach License Terms to an IP Asset.

```solidity LicenseRegistry.sol
function registerDerivativeIp(address childIpId, address[] calldata parentIpIds, address licenseTemplate, uint256[] calldata licenseTermsIds, bool isUsingLicenseToken) external onlyLicensingModule
```

This function allows you to register an IP Asset as a derivative of another IP Asset, unlocking things like claimable royalty flows from the [💸 Royalty Module](/concepts/royalty-module/overview).


# IP Asset Registry

<CardGroup cols={1}>
  <Card
    title="IPAssetRegistry.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/registries/IPAssetRegistry.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the IP Asset Registry.
  </Card>
</CardGroup>

The IP Asset Registry is responsible for registering IPs into the protocol. It deploys a dedicated [IP Account](/concepts/ip-asset/ip-account) contract for each new IP Asset registered on the protocol (_NOTE: This registry inherits from the_ [IP Account Registry](https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/registries/IPAccountRegistry.sol))

### Notable Functions

```solidity IPAssetRegistry.sol
function register(uint256 chainid, address tokenContract, uint256 tokenId) external whenNotPaused returns (address id)
```

This function registers an ERC-721 NFT as a new IP Asset on Story.


# Group IP Asset Registry

<CardGroup cols={1}>
  <Card
    title="GroupIPAssetRegistry.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/registries/GroupIPAssetRegistry.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Group IP Asset Registry.
  </Card>
</CardGroup>

The Group IP Asset Registry is responsible for managing the registration and tracking of Group IP Assets, including the group members and reward pools.

The Group IP Asset Registry will maintain grouping relationship on-chain between the Group's IP Account and individual IP Accounts through a mapping:

```solidity GroupIPAssetRegistry.sol
mapping(address groupIpId => EnumerableSet.AddressSet memberIpIds) groups;
```

### Notable Functions

```solidity GroupIPAssetRegistry.sol
function registerGroup(address groupNft, uint256 groupNftId, address rewardPool) external onlyGroupingModule whenNotPaused returns (address groupId)
```

This function registers a new Group IPA on Story.

```solidity GroupIPAssetRegistry.sol
function addGroupMember(address groupId, address[] calldata ipIds) external onlyGroupingModule whenNotPaused
```

Adds already registered IPAs to an existing Group IPA.

```solidity GroupIPAssetRegistry.sol
function removeGroupMember(address groupId, address[] calldata ipIds) external onlyGroupingModule whenNotPaused
```

Removes registered IPAs from a Group IPA.


# Module Registry

<CardGroup cols={1}>
  <Card
    title="ModuleRegistry.sol"
    href="https://github.com/storyprotocol/protocol-core-v1/blob/main/contracts/registries/ModuleRegistry.sol"
    icon="scroll"
    color="#ccb092"
  >
    View the smart contract for the Module Registry.
  </Card>
</CardGroup>

The Module Registry maintains and updates the global list of modules and hooks registered permissionlessly on Story. It can enable/disable modules on a per-IP Account basis for granular control over each IP Account's interaction with modules and hooks.

**This module is likely not very important for you** unless you wish to dive into creating/reading modules.


# 🗂️ Registry

The various registries on Story function as a primary directory/storage for the global states of the protocol. Obviously, they also contain functions to update that storage.

Unlike [⚙️ IP Accounts](/concepts/ip-asset/ip-account), which manage the state of specific IPs, a **registry** oversees the broader states of the protocol.

# Types of Registries

Below are all of the registries on Story.

## [IP Asset Registry](/concepts/registry/ip-asset-registry)

Responsible for registering IPs into the protocol.

## [Group IP Asset Registry](/concepts/registry/group-ip-asset-registry)

Responsible for registering and maintaining Group IP Assets.

## [License Registry](/concepts/registry/license-registry)

Stores all license-related states within the protocol, like attaching License Terms to IP Assets, registering derivatives, creating new License Templates, etc.

## [Module Registry](/concepts/registry/module-registry)

Maintains and updates the global list of modules and hooks registered permissionlessly on Story


# License

## LicenseClient

### Methods

- attachLicenseTerms
- mintLicenseTokens
- registerPILTerms
- registerNonComSocialRemixingPIL
- registerCommercialUsePIL
- registerCommercialRemixPIL
- getLicenseTerms

### attachLicenseTerms

Attaches license terms to an IP.

| Method               | Type                                                                 |
| -------------------- | -------------------------------------------------------------------- |
| `attachLicenseTerms` | `(request: AttachLicenseTermsRequest) => AttachLicenseTermsResponse` |

Parameters:

- `request.ipId`: The address of the IP to which the license terms are attached.
- `request.licenseTemplate`: The address of the license template.
- `request.licenseTermsId`: The ID of the license terms.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const response = await client.license.attachLicenseTerms({
  licenseTermsId: "1",
  ipId: "0x4c1f8c1035a8cE379dd4ed666758Fb29696CF721",
  txOptions: { waitForTransaction: true },
});

if (response.success) {
  console.log(
    `Attached License Terms to IPA at transaction hash ${response.txHash}.`
  );
} else {
  console.log(`License Terms already attached to this IPA.`);
}
```

```python Python
response = story_client.License.attachLicenseTerms(
  ip_id="0x4c1f8c1035a8cE379dd4ed666758Fb29696CF721",
  license_template="0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316", # insert PILicenseTemplate from https://docs.story.foundation/docs/deployed-smart-contracts
  license_terms_id="1"
)
```

```typescript Request Type
export type AttachLicenseTermsRequest = {
  ipId: Address;
  licenseTermsId: string | number | bigint;
  licenseTemplate?: Address;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type AttachLicenseTermsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```

</CodeGroup>

### mintLicenseTokens

Mints [License Tokens](/concepts/licensing-module/license-token) that give permission to use the IP Asset based on [License Terms](/concepts/licensing-module/license-terms). The license tokens are minted to the `receiver`.

Note that a license token can only be minted if the `licenseTermsId` are already attached to the IP Asset, making it a publicly available license. The IP owner can, however, mint a [private license](/concepts/licensing-module/license-token#private-licenses) by minting a license token with a `licenseTermsId` that is not attached to the IP Asset.

<Warning>

It might require the caller pay a minting fee, depending on the license terms or configured by the IP owner. The minting fee is paid in the minting fee token specified in the license terms or configured by the IP owner. IP owners can configure the minting fee of their IPs or configure the minting fee module to determine the minting fee.

</Warning>

<Frame>
  <img
    src="/images/concepts/private-licenses.png"
    alt="A diagram showing how private licenses are minted."
  />
</Frame>

| Method              | Type                                                                        |
| ------------------- | --------------------------------------------------------------------------- |
| `mintLicenseTokens` | `(request: MintLicenseTokensRequest) => Promise<MintLicenseTokensResponse>` |

Parameters:

- `request.licensorIpId`: The licensor IP ID.
- `request.licenseTemplate`: The address of the license template.
- `request.licenseTermsId`: The ID of the license terms within the license template.
- `request.amount`: The amount of license tokens to mint.
- `request.receiver`: The address of the receiver.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const response = await client.license.mintLicenseTokens({
  licenseTermsId: "1",
  licensorIpId: "0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  receiver: "0x14dC79964da2C08b23698B3D3cc7Ca32193d9955", // optional
  amount: 1,
  maxMintingFee: BigInt(0), // disabled
  maxRevenueShare: 100, // default
  txOptions: { waitForTransaction: true },
});

console.log(
  `License Token minted at transaction hash ${response.txHash}, License IDs: ${response.licenseTokenIds}`
);
```

```python Python
response = client.License.mintLicenseTokens(
  licensor_ip_id="0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  license_template="0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316", # insert PILicenseTemplate from https://docs.story.foundation/docs/deployed-smart-contracts
  license_terms_id="1",
  amount=1,
  receiver="0x14dC79964da2C08b23698B3D3cc7Ca32193d9955", # optional
  max_minting_fee=0, # disabled
  max_revenue_share=100 # default
)
```

```typescript Request Type
export type MintLicenseTokensRequest = {
  licensorIpId: Address;
  licenseTermsId: string | number | bigint;
  licenseTemplate?: Address;
  maxMintingFee: bigint | string | number;
  maxRevenueShare: number | string;
  amount?: number | string | bigint;
  receiver?: Address;
} & WithTxOptions &
  WithWipOptions;
```

```typescript Response Type
export type MintLicenseTokensResponse = {
  licenseTokenIds?: bigint[];
  receipt?: TransactionReceipt;
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### registerPILTerms

Registers new license terms and return the ID of the newly registered license terms.

| Method             | Type                                                                 |
| ------------------ | -------------------------------------------------------------------- |
| `registerPILTerms` | `(request: RegisterPILTermsRequest) => Promise<RegisterPILResponse>` |

Parameters:

- Expected Parameters: Instead of listing all of the expected parameters here, please see `LicenseTerms` type in [this](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/resources/license.ts) file. They all come from the [PIL Terms](/concepts/programmable-ip-license/pil-terms).
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { LicenseTerms } from "@story-protocol/core-sdk";
import { zeroAddress } from "viem";

const licenseTerms: LicenseTerms = {
  transferable: false,
  royaltyPolicy: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  defaultMintingFee: 0n,
  expiration: 0n,
  commercialUse: false,
  commercialAttribution: false,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: "0x",
  commercialRevShare: 10, // 10%
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: false,
  derivativesApproval: false,
  derivativesReciprocal: false,
  derivativeRevCeiling: 0n,
  currency: "0x1514000000000000000000000000000000000000", // $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  uri: "",
};

const response = await client.license.registerPILTerms({
  ...licenseTerms,
  txOptions: { waitForTransaction: true },
});

console.log(
  `PIL Terms registered at transaction hash ${response.txHash}, License Terms ID: ${response.licenseTermsId}`
);
```

```python Python
response = story_client.License.registerPILTerms(
  transferable=False,
  royalty_policy="0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  default_minting_fee=0,
  expiration=0,
  commercial_use=False,
  commercial_attribution=False,
  commercializer_checker="0x0000000000000000000000000000000000000000",
  commercializer_checker_data="0x",
  commercial_rev_share=10, # 10%
  commercial_rev_ceiling=0,
  derivatives_allowed=True,
  derivatives_attribution=False,
  derivatives_approval=False,
  derivatives_reciprocal=False,
  derivative_rev_ceiling=0,
  currency="0x1514000000000000000000000000000000000000", # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  uri="",
)
```

```typescript Request Type
export type RegisterPILTermsRequest = Omit<
  LicenseTerms,
  | "defaultMintingFee"
  | "expiration"
  | "commercialRevCeiling"
  | "derivativeRevCeiling"
> & {
  defaultMintingFee: bigint | string | number;
  expiration: bigint | string | number;
  commercialRevCeiling: bigint | string | number;
  derivativeRevCeiling: bigint | string | number;
  txOptions?: TxOptions;
};

export type LicenseTerms = {
  /*Indicates whether the license is transferable or not.*/
  transferable: boolean;
  /*The address of the royalty policy contract which required to StoryProtocol in advance.*/
  royaltyPolicy: Address;
  /*The default minting fee to be paid when minting a license.*/
  defaultMintingFee: bigint;
  /*The expiration period of the license.*/
  expiration: bigint;
  /*Indicates whether the work can be used commercially or not.*/
  commercialUse: boolean;
  /*Whether attribution is required when reproducing the work commercially or not.*/
  commercialAttribution: boolean;
  /*Commercializers that are allowed to commercially exploit the work. If zero address, then no restrictions is enforced.*/
  commercializerChecker: Address;
  /*The data to be passed to the commercializer checker contract.*/
  commercializerCheckerData: Address;
  /**Percentage of revenue that must be shared with the licensor. Must be from 0-100.*/
  commercialRevShare: number;
  /*The maximum revenue that can be generated from the commercial use of the work.*/
  commercialRevCeiling: bigint;
  /*Indicates whether the licensee can create derivatives of his work or not.*/
  derivativesAllowed: boolean;
  /*Indicates whether attribution is required for derivatives of the work or not.*/
  derivativesAttribution: boolean;
  /*Indicates whether the licensor must approve derivatives of the work before they can be linked to the licensor IP ID or not.*/
  derivativesApproval: boolean;
  /*Indicates whether the licensee must license derivatives of the work under the same terms or not.*/
  derivativesReciprocal: boolean;
  /*The maximum revenue that can be generated from the derivative use of the work.*/
  derivativeRevCeiling: bigint;
  /*The ERC20 token to be used to pay the minting fee. the token must be registered in story protocol.*/
  currency: Address;
  /*The URI of the license terms, which can be used to fetch the offchain license terms.*/
  uri: string;
};
```

```typescript Response Type
export type RegisterPILResponse = {
  licenseTermsId?: bigint;
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### registerNonComSocialRemixingPIL

Convenient function to register a PIL non commercial social remix license to the registry.

<Warning>

No reason to call this function. Non-Commercial Social Remixing terms are already registered with `licenseTermdId = 1` in our protocol. There's no reason to register them again.

</Warning>

| Method                            | Type                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| `registerNonComSocialRemixingPIL` | `(request?: RegisterNonComSocialRemixingPILRequest) => Promise<RegisterPILResponse>` |

Parameters:

- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const response = await client.license.registerNonComSocialRemixingPIL({
  txOptions: { waitForTransaction: true },
});

console.log(
  `PIL Terms registered at transaction hash ${response.txHash}, License Terms ID: ${response.licenseTermsId}`
);
```

```python Python
response = story_client.License.registerNonComSocialRemixingPIL()
```

```typescript Request Type
export type RegisterNonComSocialRemixingPILRequest = {
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type RegisterPILResponse = {
  licenseTermsId?: bigint;
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### registerCommercialUsePIL

Convenient function to register a PIL commercial use license to the registry.

| Method                     | Type                                                                         |
| -------------------------- | ---------------------------------------------------------------------------- |
| `registerCommercialUsePIL` | `(request: RegisterCommercialUsePILRequest) => Promise<RegisterPILResponse>` |

Parameters:

- `request.defaultMintingFee`: The fee to be paid when minting a license.
- `request.currency`: The ERC20 token to be used to pay the minting fee and the token must be registered on Story's protocol.
- `request.royaltyPolicyAddress`: \[Optional] The address of the royalty policy contract, default value is LAP.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { parseEther } from "viem";

const commercialUseParams = {
  currency: "0x1514000000000000000000000000000000000000", // $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  defaultMintingFee: parseEther("1"), // 1 $WIP
  royaltyPolicyAddress: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
};

const response = await client.license.registerCommercialUsePIL({
  ...commercialUseParams,
  txOptions: { waitForTransaction: true },
});

console.log(
  `PIL Terms registered at transaction hash ${response.txHash}, License Terms ID: ${response.licenseTermsId}`
);
```

```python Python
response = story_client.License.registerCommercialUsePIL(
  currency='0x1514000000000000000000000000000000000000', # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  default_minting_fee=10, # 10 of the currency (using the above currency, 10 $WIP),
  royalty_policy="0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
)
```

```typescript Request Type
export type RegisterCommercialUsePILRequest = {
  defaultMintingFee: string | number | bigint;
  currency: Address;
  royaltyPolicyAddress?: Address;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type RegisterPILResponse = {
  licenseTermsId?: bigint;
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### registerCommercialRemixPIL

Convenient function to register a PIL commercial Remix license to the registry.

| Method                       | Type                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------ |
| `registerCommercialRemixPIL` | `(request: RegisterCommercialRemixPILRequest) => Promise<RegisterPILResponse>` |

Parameters:

- `request.defaultMintingFee`: The fee to be paid when minting a license.
- `request.commercialRevShare`: Percentage of revenue that must be shared with the licensor.
- `request.currency`: The ERC20 token to be used to pay the minting fee and the token must be registered on Story's protocol.
- `request.royaltyPolicyAddress`: \[Optional] The address of the royalty policy contract, default value is LAP.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { parseEther } from "viem";

const commercialRemixParams = {
  currency: "0x1514000000000000000000000000000000000000", // $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  defaultMintingFee: parseEther("1"), // 1 $WIP
  royaltyPolicyAddress: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  commercialRevShare: 10, // 10%
};

const response = await client.license.registerCommercialRemixPIL({
  ...commercialRemixParams,
  txOptions: { waitForTransaction: true },
});

console.log(
  `PIL Terms registered at transaction hash ${response.txHash}, License Terms ID: ${response.licenseTermsId}`
);
```

```python Python
response = story_client.License.registerCommercialRemixPIL(
  currency='0x1514000000000000000000000000000000000000', # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  default_minting_fee=10, # 10 of the currency (using the above currency, 10 $WIP)
  royalty_policy="0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  commercial_rev_share=10 # 10%
)
```

```typescript Request Type
export type RegisterCommercialRemixPILRequest = {
  defaultMintingFee: string | number | bigint;
  commercialRevShare: number;
  currency: Address;
  royaltyPolicyAddress?: Address;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type RegisterPILResponse = {
  licenseTermsId?: bigint;
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### getLicenseTerms

Gets License Terms of the given ID.

| Method            | Type                                 |           |                                                       |
| :---------------- | :----------------------------------- | :-------- | :---------------------------------------------------- |
| `getLicenseTerms` | \`(selectedLicenseTermsId: string \\ | number \\ | bigint) => PiLicenseTemplateGetLicenseTermsResponse\` |

Parameters:

- `selectedLicenseTermsId`: The ID of the license terms.

```typescript Response Type
export type PiLicenseTemplateGetLicenseTermsResponse = {
  terms: {
    transferable: boolean;
    royaltyPolicy: Address;
    defaultMintingFee: bigint;
    expiration: bigint;
    commercialUse: boolean;
    commercialAttribution: boolean;
    commercializerChecker: Address;
    commercializerCheckerData: Hex;
    commercialRevShare: number;
    commercialRevCeiling: bigint;
    derivativesAllowed: boolean;
    derivativesAttribution: boolean;
    derivativesApproval: boolean;
    derivativesReciprocal: boolean;
    derivativeRevCeiling: bigint;
    currency: Address;
    uri: string;
  };
};
```

### predictMintingLicenseFee

Pre-compute the minting license fee for the given IP and license terms. The function can be used to calculate the minting license fee before minting license tokens.

| Method                     | Type                                                                                            |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| `predictMintingLicenseFee` | `(request: PredictMintingLicenseFeeRequest) => LicensingModulePredictMintingLicenseFeeResponse` |

Parameters:

- `request.licensorIpId`: The IP ID of the licensor.
- `request.licenseTermsId`: The ID of the license terms.
- `request.amount`: The amount of license tokens to mint.
- `request.licenseTemplate`: \[Optional] The address of the license template, default value is Programmable IP License.
- `request.receiver`: \[Optional] The address of the receiver, default value is your wallet address.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type LicensingModulePredictMintingLicenseFeeResponse = {
  currencyToken: Address;
  tokenAmount: bigint;
};
```

### setLicensingConfig

Sets the licensing configuration for a specific license terms of an IP.

| Method               | Type                                                                 |
| -------------------- | -------------------------------------------------------------------- |
| `setLicensingConfig` | `(request: SetLicensingConfigRequest) => SetLicensingConfigResponse` |

Parameters:

- `request.ipId`: The address of the IP for which the configuration is being set.
- `request.licenseTermsId`: The ID of the license terms within the license template.
- `request.licenseTemplate`: The address of the license template used, If not specified, the configuration applies to all licenses.
- `request.licensingConfig`: The licensing configuration for the license.
  - `request.licensingConfig.isSet`: Whether the configuration is set or not.
  - `request.licensingConfig.mintingFee`: The minting fee to be paid when minting license tokens.
  - `request.licensingConfig.hookData`: The data to be used by the licensing hook.
  - `request.licensingConfig.licensingHook`: The hook contract address for the licensing module, or address(0) if none.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type SetLicensingConfigResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```


# Royalty

## RoyaltyClient

### Methods

- payRoyaltyOnBehalf
- claimableRevenue
- claimAllRevenue
- batchClaimAllRevenue
- getRoyaltyVaultAddress
- batchClaimAllRevenue
- transferToVault

### payRoyaltyOnBehalf

Allows the function caller to pay royalties to a receiver IP asset on behalf of the payer IP Asset.

| Method               | Type                                                                          |
| -------------------- | ----------------------------------------------------------------------------- |
| `payRoyaltyOnBehalf` | `(request: PayRoyaltyOnBehalfRequest) => Promise<PayRoyaltyOnBehalfResponse>` |

Parameters:

- `request.receiverIpId`: The ipId that receives the royalties.
- `request.payerIpId`: The ID of the IP asset that pays the royalties.
- `request.token`: The token to use to pay the royalties.
- `request.amount`: The amount to pay.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).
- `request.wipOptions`: \[Optional]
  - `request.wipOptions.useMulticallWhenPossible`: \[Optional] Use multicall to batch the WIP calls into one transaction when possible. **Default: true**
  - `request.wipOptions.enableAutoWrapIp`: \[Optional] By default IP is converted to WIP if the current WIP balance does not cover the fees. Set this to `false` to disable this behavior. **Default: true**
  - `request.wipOptions.enableAutoApprove`: \[Optional] Automatically approve WIP usage when WIP is needed but current allowance is not sufficient. Set this to `false` to disable this behavior. **Default: true**
- `request.erc20Options`: \[Optional]
  - `request.erc20Options.enableAutoApprove`: \[Optional] Automatically approve ERC20 usage when ERC20 is needed but current allowance is not sufficient. Set this to `false` to disable this behavior. **Default: true**

<CodeGroup>

```typescript TypeScript
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
import { parseEther, zeroAddress } from "viem";

// In this case, lets say there is a root IPA 'A' and a derivative IPA 'B'.
// Someone wants to pay 'B' for whatever reason (they bought it, they want to tip it, etc).
// Since the payer is not an IP Asset (rather an external user), the `payerIpId` can
// be a zeroAddress. And the receiver is, well, the receiver's ipId which is B.
//
// It's important to note that both 'B' and its parent 'A' will be able
// to claim revenue from this based on the negotiated license terms
const payRoyalty = await client.royalty.payRoyaltyOnBehalf({
  receiverIpId: "0x0b825D9E5FA196e6B563C0a446e8D9885057f9B1", // B's ipId
  payerIpId: zeroAddress,
  token: WIP_TOKEN_ADDRESS,
  amount: parseEther("2"), // 2 $WIP
  txOptions: { waitForTransaction: true },
});
console.log(`Paid royalty at transaction hash ${payRoyalty.txHash}`);

// In this case, lets say there is a root IPA 'A' and a derivative IPA 'B'.
// 'B' earns revenue off-chain, but must pay 'A' based on their negotiated license terms.
// So 'B' pays 'A' what they are due
const payRoyalty = await client.royalty.payRoyaltyOnBehalf({
  receiverIpId: "0x6B86B39F03558A8a4E9252d73F2bDeBfBedf5b68", // A's ipId
  payerIpId: "0x0b825D9E5FA196e6B563C0a446e8D9885057f9B1", // B's ipId
  token: WIP_TOKEN_ADDRESS,
  amount: parseEther("2"), // 2 $WIP
  txOptions: { waitForTransaction: true },
});
console.log(`Paid royalty at transaction hash ${payRoyalty.txHash}`);
```

```typescript Request Type
export type PayRoyaltyOnBehalfRequest = {
  receiverIpId: Address;
  payerIpId: Address;
  token: Address;
  amount: TokenAmountInput;
} & WithTxOptions &
  WithERC20Options &
  WithWipOptions;
```

```typescript Response Type
export type PayRoyaltyOnBehalfResponse = {
  txHash?: string;
  receipt?: TransactionReceipt;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### claimableRevenue

Get total amount of revenue token claimable by a royalty token holder.

| Method             | Type                                                                      |
| ------------------ | ------------------------------------------------------------------------- |
| `claimableRevenue` | `(request: ClaimableRevenueRequest) => Promise<ClaimableRevenueResponse>` |

Parameters:

- `request.royaltyVaultIpId`: The id of the royalty vault.
- `request.claimer`: The address of the royalty token holder.
- `request.token`: The revenue token to claim.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript Request Type
export type ClaimableRevenueRequest = {
  royaltyVaultIpId: Address;
  claimer: Address;
  token: Address;
};
```

```typescript Response Type
export type ClaimableRevenueResponse = bigint;
```

</CodeGroup>

### claimAllRevenue

Claims all revenue from child IP Assets and/or from your own IP Royalty Vault.

| Method            | Type                                                                    |
| ----------------- | ----------------------------------------------------------------------- |
| `claimAllRevenue` | `(request: ClaimAllRevenueRequest) => Promise<ClaimAllRevenueResponse>` |

Parameters:

- `request.ancestorIpId`: The address of the ancestor IP from which the revenue is being claimed.
- `request.claimer`: The address of the claimer of the currency (revenue) tokens. This is normally the ipId of the ancestor IP if the IP has all royalty tokens. Otherwise, this would be the address that is holding the ancestor IP royalty tokens.
- `request.childIpIds[]`: The addresses of the child IPs from which royalties are derived.
- `request.royaltyPolicies[]`: The addresses of the royalty policies, where royaltyPolicies\[i] governs the royalty flow for childIpIds\[i].
- `request.currencyTokens[]`: The addresses of the currency tokens in which royalties will be claimed.
- `request.claimOptions`: \[Optional]
  - `request.claimOptions.autoTransferAllClaimedTokensFromIp`: \[Optional] When enabled, all claimed tokens on the claimer are transferred to the wallet address if the wallet owns the IP. If the wallet is the claimer or if the claimer is not an IP owned by the wallet, then the tokens will not be transferred. Set to false to disable auto transferring claimed tokens from the claimer. **Default: true**
  - `request.claimOptions.autoUnwrapIpTokens`: \[Optional] By default all claimed WIP tokens are converted back to IP after they are transferred. Set this to false to disable this behavior. **Default: false**

<CodeGroup>

```typescript TypeScript
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";

const claimRevenue = await client.royalty.claimAllRevenue({
  // IP Asset 1's (parent) ipId
  ancestorIpId: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
  // whoever owns the royalty tokens associated with IP Royalty Vault 1
  // (most likely the associated ipId, which is IP Asset 1's ipId)
  claimer: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
  currencyTokens: [WIP_TOKEN_ADDRESS],
  // IP Asset 2's (child) ipId
  childIpIds: ["0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2"],
  // testnet address of RoyaltyPolicyLAP
  royaltyPolicies: ["0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E"],
});

console.log(`Claimed revenue: ${claimRevenue.claimedTokens}`);
```

```typescript Request Type
export type ClaimAllRevenueRequest = {
  ancestorIpId: Address;
  claimer: Address;
  childIpIds: Address[];
  royaltyPolicies: Address[];
  currencyTokens: Address[];
} & WithClaimOptions;

export type WithClaimOptions = {
  claimOptions?: {
    autoTransferAllClaimedTokensFromIp?: boolean;
    autoUnwrapIpTokens?: boolean;
  };
};
```

```typescript Response Type
export type ClaimAllRevenueResponse = {
  txHashes: Hash[];
  receipt?: TransactionReceipt;
  claimedTokens?: ClaimedToken[];
};

export type ClaimedToken = {
  token: Address;
  amount: bigint;
};
```

</CodeGroup>

### batchClaimAllRevenue

Automatically batch claims all revenue from the child IPs of multiple ancestor IPs. If multicall is disabled, it will call `claimAllRevenue` for each ancestor IP. Then transfer all claimed tokens to the wallet if the wallet owns the IP or is the claimer. If claimed token is WIP, it will also be converted back to IP.

| Method                 | Type                                                                              |
| ---------------------- | --------------------------------------------------------------------------------- |
| `batchClaimAllRevenue` | `(request: BatchClaimAllRevenueRequest) => Promise<BatchClaimAllRevenueResponse>` |

Parameters:

- `request.ancestorIps[]`: An array of ancestor IP information from which the revenue is being claimed.
  - `request.ancestorIps[].ipId`: The address of the ancestor IP from which the revenue is being claimed.
  - `request.ancestorIps[].claimer`: The address of the claimer of the currency (revenue) tokens. This is normally the ipId of the ancestor IP if the IP has all royalty tokens. Otherwise, this would be the address that is holding the ancestor IP royalty tokens.
  - `request.ancestorIps[].childIpIds[]`: The addresses of the child IPs from which royalties are derived.
  - `request.ancestorIps[].royaltyPolicies[]`: The addresses of the royalty policies, where royaltyPolicies\[i] governs the royalty flow for childIpIds\[i].
  - `request.ancestorIps[].currencyTokens[]`: The addresses of the currency tokens in which royalties will be claimed.
- `request.claimOptions`: \[Optional]
  - `request.claimOptions.autoTransferAllClaimedTokensFromIp`: \[Optional] When enabled, all claimed tokens on the claimer are transferred to the wallet address if the wallet owns the IP. If the wallet is the claimer or if the claimer is not an IP owned by the wallet, then the tokens will not be transferred. Set to false to disable auto transferring claimed tokens from the claimer. **Default: true**
  - `request.claimOptions.autoUnwrapIpTokens`: \[Optional] By default all claimed WIP tokens are converted back to IP after they are transferred. Set this to false to disable this behavior. **Default: false**
- `request.options`: \[Optional]
  - `request.options.useMulticallWhenPossible`: \[Optional] Use multicall to batch the calls `claimAllRevenue` into one transaction when possible. If only 1 ancestorIp is provided, multicall will not be used. **Default: true**

<CodeGroup>

```typescript TypeScript
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";

const claimRevenue = await client.royalty.batchClaimAllRevenue({
  ancestorIps: [
    {
      ipId: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
      claimer: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
      currencyTokens: [WIP_TOKEN_ADDRESS],
      childIpIds: ["0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2"],
      royaltyPolicies: ["0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E"],
    },
  ],
});

console.log(`Claimed revenue: ${claimRevenue.claimedTokens}`);
```

```typescript Request Type
export type BatchClaimAllRevenueRequest = WithClaimOptions & {
  ancestorIps: {
    ipId: Address;
    claimer: Address;
    childIpIds: Address[];
    royaltyPolicies: Address[];
    currencyTokens: Address[];
  }[];
  options?: {
    useMulticallWhenPossible?: boolean;
  };
};

export type WithClaimOptions = {
  claimOptions?: {
    autoTransferAllClaimedTokensFromIp?: boolean;
    autoUnwrapIpTokens?: boolean;
  };
};
```

```typescript Response Type
export type BatchClaimAllRevenueResponse = {
  txHashes: Hash[];
  receipts: TransactionReceipt[];
  claimedTokens?: IpRoyaltyVaultImplRevenueTokenClaimedEvent[];
};
```

</CodeGroup>

### getRoyaltyVaultAddress

Get the royalty vault proxy address of given royaltyVaultIpId.

| Method                   | Type                                          |
| ------------------------ | --------------------------------------------- |
| `getRoyaltyVaultAddress` | `(royaltyVaultIpId: Hex) => Promise<Address>` |

Parameters:

- `royaltyVaultIpId`: the `ipId` associated with the royalty vault.

### transferToVault

Transfers to vault an amount of revenue tokens claimable via a royalty policy.

| Method            | Type                                                                |
| ----------------- | ------------------------------------------------------------------- |
| `transferToVault` | `(request: TransferToVaultRequest) => Promise<TransactionResponse>` |

Parameters:

- `request.royaltyPolicy`: The royalty policy to use.
- `request.ipId`: The ID of the IP asset that pays the royalties.
- `request.ancestorIpId`: The ID of the ancestor IP asset.
- `request.token`: The token address to transfer.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript Request Type
export type TransferToVaultRequest = WithTxOptions & {
  royaltyPolicy: RoyaltyPolicyInput;
  ipId: Address;
  ancestorIpId: Address;
  token: Address;
};
```

```typescript Response Type
export type TransactionResponse = {
  txHash: Hex;

  /** Transaction receipt, only available if waitForTransaction is set to true */
  receipt?: TransactionReceipt;
};
```

</CodeGroup>


# Dispute

## DisputeClient

### Methods

- raiseDispute
- cancelDispute
- resolveDispute
- tagIfRelatedIpInfringed
- disputeAssertion
- disputeIdToAssertionId

### raiseDispute

Raises a dispute on a given ipId

| Method         | Type                                                              |
| -------------- | ----------------------------------------------------------------- |
| `raiseDispute` | `(request: RaiseDisputeRequest) => Promise<RaiseDisputeResponse>` |

Parameters:

- `request.targetIpId`: The IP ID that is the target of the dispute.
- `request.targetTag`: The target tag of the dispute. See [dispute tags](https://docs.story.foundation/docs/dispute-module#dispute-tags). **Example: "IMPROPER_REGISTRATION"**
- `request.cid`: Content Identifier (CID) for the dispute evidence. This should be obtained by uploading your dispute evidence (documents, images, etc.) to IPFS. **Example: "QmX4zdp8VpzqvtKuEqMo6gfZPdoUx9TeHXCgzKLcFfSUbk"**
- `request.liveness`: The liveness is the time window (in seconds) in which a counter dispute can be presented (30days).
- `request.bond`: [Optional] **If not specified, it defaults to the minimum bond value**. The amount of wrapper IP that the dispute initiator pays upfront into a pool. To counter that dispute the opposite party of the dispute has to place a bond of the same amount. The winner of the dispute gets the original bond back + 50% of the other party bond. The remaining 50% of the loser party bond goes to the reviewer.
- `request.wipOptions`: \[Optional]
  - `request.wipOptions.enableAutoWrapIp`: \[Optional]By default IP is converted to WIP if the current WIP balance does not cover the fees. Set this to `false` to disable this behavior. **Default: true**
  - `request.wipOptions.enableAutoApprove`: \[Optional]Automatically approve WIP usage when WIP is needed but current allowance is not sufficient. Set this to `false` to disable this behavior. **Default: true**
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { parseEther } from "viem";

const response = await client.dispute.raiseDispute({
  targetIpId: "0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  // NOTE: you must use your own CID here, because every time it is used,
  // the protocol does not allow you to use it again
  cid: "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",
  // you must pick from one of the whitelisted tags here:
  // https://docs.story.foundation/docs/dispute-module#dispute-tags
  targetTag: "IMPROPER_REGISTRATION",
  bond: parseEther("0.1"), // minimum of 0.1
  liveness: 2592000,
  txOptions: { waitForTransaction: true },
});
console.log(
  `Dispute raised at transaction hash ${disputeResponse.txHash}, Dispute ID: ${disputeResponse.disputeId}`
);
```

```typescript Request Type
export type RaiseDisputeRequest = WithTxOptions & {
  targetIpId: Address;
  cid: string;
  targetTag: string;
  liveness: bigint | number | string;
  bond?: bigint | number | string;
  wipOptions?: {
    enableAutoWrapIp?: boolean;
    enableAutoApprove?: boolean;
  };
};
```

```typescript Response Type
export type RaiseDisputeResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  disputeId?: bigint;
};
```

</CodeGroup>

### cancelDispute

Cancels an ongoing dispute

| Method          | Type                                                                |
| --------------- | ------------------------------------------------------------------- |
| `cancelDispute` | `(request: CancelDisputeRequest) => Promise<CancelDisputeResponse>` |

Parameters:

- `request.disputeId`: The ID of the dispute to be cancelled.
- `request.data`: \[Optional] Additional data used in the cancellation process. **Defaults to "0x"**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript
const response = await client.dispute.cancelDispute({
  disputeId: 1,
  txOptions: { waitForTransactions: true },
});
```

```typescript Request Type
export type CancelDisputeRequest = {
  disputeId: number | string | bigint;
  data?: Hex;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type CancelDisputeResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### resolveDispute

Resolves a dispute after it has been judged

| Method           | Type                                                                  |
| ---------------- | --------------------------------------------------------------------- |
| `resolveDispute` | `(request: ResolveDisputeRequest) => Promise<ResolveDisputeResponse>` |

Parameters:

- `request.disputeId`: The ID of the dispute to be resolved.
- `request.data`: \[Optional] The data to resolve the dispute. **Defaults to "0x"**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript
const response = await client.dispute.resolveDispute({
  disputeId: 1,
  data: "0x",
  txOptions: { waitForTransaction: true },
});
```

```typescript Request Type
export type ResolveDisputeRequest = {
  disputeId: number | string | bigint;
  data?: Hex;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type ResolveDisputeResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### tagIfRelatedIpInfringed

Tags a derivative if a parent has been tagged with an infringement tag or a group ip if a group member has been tagged with an infringement tag.

| Method                    | Type                                                                          |
| ------------------------- | ----------------------------------------------------------------------------- |
| `tagIfRelatedIpInfringed` | `(request: TagIfRelatedIpInfringedRequest) => Promise<TransactionResponse[]>` |

Parameters:

- `request.infringementTags[]`: An array of tags relating to the dispute
  - `request.infringementTags[].ipId`: The `ipId` to tag
  - `request.infringementTags[].disputeId`: The dispute id that tagged the related infringing parent IP
- `request.options`: \[Optional]
  - `request.options.useMulticallWhenPossible`: \[Optional] Use multicall to batch the calls into one transaction when possible. If only 1 infringementTag is provided, multicall will not be used. **Default: true**
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript
const response = await client.dispute.tagIfRelatedIpInfringed({
  infringementTags: [
    {
      ipId: "0xa1BaAA464716eC76A285Ef873d27f97645fE0366",
      disputeId: 1,
    },
  ],
  txOptions: { waitForTransaction: true },
});
```

```typescript Request Type
export type TagIfRelatedIpInfringedRequest = {
  infringementTags: {
    ipId: Address;
    disputeId: number | string | bigint;
  }[];
  options?: {
    useMulticallWhenPossible?: boolean;
  };
} & WithTxOptions;
```

```typescript Response Type
export type TransactionResponse = {
  txHash: Hex;

  /** Transaction receipt, only available if waitForTransaction is set to true */
  receipt?: TransactionReceipt;
};
```

</CodeGroup>

### disputeAssertion

Counters a dispute that was raised by another party on an IP using counter evidence.

This method can only be called by the IP's owner to counter a dispute by providing counter evidence. The counter evidence (e.g., documents, images) should be uploaded to IPFS, and its corresponding CID is converted to a hash for the request.

If you only have a `disputeId`, call `disputeIdToAssertionId` to get the `assertionId` needed here.

| Method             | Type                                                                 |
| ------------------ | -------------------------------------------------------------------- |
| `disputeAssertion` | `(request: DisputeAssertionRequest) => Promise<TransactionResponse>` |

Parameters:

- `request.ipId`: The IP ID that is the target of the dispute.
- `request.assertionId`: The identifier of the assertion that was disputed. You can get this from the `disputeId` by calling `dispute.disputeIdToAssertionId`.
- `request.counterEvidenceCID`: Content Identifier (CID) for the counter evidence. This should be obtained by uploading your dispute evidence (documents, images, etc.) to IPFS. **Example: "QmX4zdp8VpzqvtKuEqMo6gfZPdoUx9TeHXCgzKLcFfSUbk"**
- `request.wipOptions`: \[Optional]
  - `request.wipOptions.enableAutoWrapIp`: \[Optional]By default IP is converted to WIP if the current WIP balance does not cover the fees. Set this to `false` to disable this behavior. **Default: true**
  - `request.wipOptions.enableAutoApprove`: \[Optional]Automatically approve WIP usage when WIP is needed but current allowance is not sufficient. Set this to `false` to disable this behavior. **Default: true**
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript
const assertionId = await client.dispute.disputeIdToAssertionId(1);

const result = await client.dispute.disputeAssertion({
  ipId: "0xa1BaAA464716eC76A285Ef873d27f97645fE0366",
  assertionId: assertionId,
  counterEvidenceCID: "QmX4zdp8VpzqvtKuEqMo6gfZPdoUx9TeHXCgzKLcFfSUbk",
  txOptions: { waitForTransaction: true },
});
```

```typescript Request Type
export type DisputeAssertionRequest = {
  ipId: Address;
  assertionId: Hex;
  counterEvidenceCID: string;
  wipOptions?: {
    enableAutoWrapIp?: boolean;
    enableAutoApprove?: boolean;
  };
} & WithTxOptions;
```

```typescript Response Type
export type TransactionResponse = {
  txHash: Hex;

  /** Transaction receipt, only available if waitForTransaction is set to true */
  receipt?: TransactionReceipt;
};
```

</CodeGroup>

### disputeIdToAssertionId

Maps a dispute id to an assertion id

| Method                   | Type                                  |
| ------------------------ | ------------------------------------- |
| `disputeIdToAssertionId` | `(disputeId: number) => Promise<Hex>` |

Parameters:

- `request.disputeId`: The dispute ID.

```typescript
const result = await client.dispute.disputeIdToAssertionId(1);
```


# IP Asset

## IPAssetClient

### Methods

- register
- registerDerivative
- registerDerivativeWithLicenseTokens
- mintAndRegisterIpAssetWithPilTerms
- registerIpAndAttachPilTerms
- registerDerivativeIp
- mintAndRegisterIpAndMakeDerivative
- mintAndRegisterIp
- registerPilTermsAndAttach
- mintAndRegisterIpAndMakeDerivativeWithLicenseTokens
- registerIpAndMakeDerivativeWithLicenseTokens

### Navigating Around the IPAssetClient

Because there are a lot of functions to interact with the [📜 Licensing Module](/concepts/licensing-module), we have broken them down into a helpful chart so you can identify what you're looking for, and then find the associated docs.

| **Function**                                                                                | **Mint an NFT** | **Register IPA** | **Create License Terms** | **Attach License Terms** | **Mint License Token** | **Register as Derivative** |
| ------------------------------------------------------------------------------------------- | :-------------: | :--------------: | :----------------------: | :----------------------: | :--------------------: | :------------------------: |
| <span style={{color: "#e03130"}}>register</span>                                            |                 |        ✓         |                          |                          |                        |                            |
| <span style={{color: "#e03130"}}>mintAndRegisterIp</span>                                   |        ✓        |        ✓         |                          |                          |                        |                            |
| <span style={{color: "#e03130"}}>registerIpAndAttachPilTerms</span>                         |                 |        ✓         |            ✓             |            ✓             |                        |                            |
| <span style={{color: "#e03130"}}>mintAndRegisterIpAssetWithPilTerms</span>                  |        ✓        |        ✓         |            ✓             |            ✓             |                        |                            |
| <span style={{color: "#e03130"}}>registerDerivativeIp</span>                                |                 |        ✓         |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>mintAndRegisterIpAndMakeDerivativeWithLicenseTokens</span> |        ✓        |        ✓         |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>registerIpAndMakeDerivativeWithLicenseTokens</span>        |                 |        ✓         |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>mintAndRegisterIpAndMakeDerivative</span>                  |        ✓        |        ✓         |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>registerDerivative</span>                                  |                 |                  |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>registerDerivativeWithLicenseTokens</span>                 |                 |                  |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>registerPilTermsAndAttach</span>                           |                 |                  |            ✓             |            ✓             |                        |                            |
| <span style={{color: "#1971c2"}}>registerPILTerms</span>                                    |                 |                  |            ✓             |                          |                        |                            |
| <span style={{color: "#1971c2"}}>attachLicenseTerms</span>                                  |                 |                  |                          |            ✓             |                        |                            |
| <span style={{color: "#1971c2"}}>mintLicenseTokens</span>                                   |                 |                  |                          |                          |           ✓            |                            |

- <span style={{ color: "#e03130" }}>Red</span>: IPAssetClient (this page)
- <span style={{ color: "#1971c2" }}>Blue</span>:
  [LicenseClient](/sdk-reference/license)

## register

Registers an NFT as IP, creating a corresponding [🧩 IP Asset](/concepts/ip-asset). If the given NFT was already registered, this function will return the existing `ipId`.

<Note title="NFT Metadata">
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method     | Type                                                        |
| ---------- | ----------------------------------------------------------- |
| `register` | `(request: RegisterRequest) => Promise<RegisterIpResponse>` |

Parameters:

- `request.nftContract`: The address of the NFT.
- `request.tokenId`: The token identifier of the NFT.
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds. **Defaults to 1000**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { toHex } from "viem";

const response = await client.ipAsset.register({
  nftContract: "0x041B4F29183317Fd352AE57e331154b73F8a1D73",
  tokenId: "12",
  ipMetadata: {
    ipMetadataURI: "test-uri",
    ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
    nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
    nftMetadataURI: "test-nft-uri",
  },
  txOptions: { waitForTransaction: true },
});

console.log(
  `Root IPA created at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
);
```

```typescript Request Type
export type RegisterRequest = {
  nftContract: Address;
  tokenId: string | number | bigint;
  deadline?: string | number | bigint;
} & IpMetadataAndTxOptions;
```

```typescript Response Type
export type RegisterIpResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  ipId?: Address;
};
```

</CodeGroup>

## batchRegister

Batch registers an NFT as IP, creating a corresponding IP record.

| Method          | Type                                                                |
| --------------- | ------------------------------------------------------------------- |
| `batchRegister` | `(request: BatchRegisterRequest) => Promise<BatchRegisterResponse>` |

## registerDerivative

Registers a derivative directly with parent IP's license terms, without needing license tokens, and attaches the license terms of the parent IPs to the derivative IP.

The license terms must be attached to the parent IP before calling this function.

All IPs attached default license terms by default.

The derivative IP owner must be the caller or an authorized operator.

| Method               | Type                                                                          |
| -------------------- | ----------------------------------------------------------------------------- |
| `registerDerivative` | `(request: RegisterDerivativeRequest) => Promise<RegisterDerivativeResponse>` |

Parameters:

- `request.childIpId`: The derivative IP ID.
- `request.licenseTermsIds`: Array of license term IDs that authorize the creation of this derivative IP. Each ID must correspond positionally to a parent IP in the `parentIpIds` array, creating a one-to-one mapping. Story verifies on-chain that each specified license term permits derivative registration for its corresponding parent IP. Transaction fails if arrays don't match in length or if terms don't permit derivative creation.
- `request.parentIpIds`: Array of parent IP IDs from which this derivative is created. Each parent IP must have corresponding license terms specified at the same index in the `licenseTermsIds` array that authorize the derivative relationship.
- `request.licenseTemplate`: \[Optional] The address of the license template to be used for the linking. For now, this can only be the [PIL](/concepts/programmable-ip-license)
- `request.maxMintingFee`: \[Optional] The maximum minting fee that the caller is willing to pay. If set to 0, then there is no no limit. **Default: 0**
- `request.maxRevenueShare`: \[Optional] The maximum revenue share percentage agreed upon between a child and parent when a child is registering as derivative. Must be between 0 and 100. **Default: 100**
- `request.maxRts`: \[Optional] The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Default: 100_000_000**
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const response = await client.ipAsset.registerDerivative({
  childIpId: "0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  parentIpIds: ["0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba"],
  licenseTermsIds: ["5"],
  txOptions: { waitForTransaction: true },
});

console.log(
  `Derivative IPA linked to parent at transaction hash ${response.txHash}`
);
```

```typescript Request Type
export type RegisterDerivativeRequest = {
  txOptions?: TxOptions;
  childIpId: Address;
} & DerivativeData &
  WithWipOptions;

export type DerivativeData = {
  parentIpIds: Address[];
  licenseTermsIds: bigint[] | string[] | number[];
  maxMintingFee: bigint | string | number;
  maxRts: number | string;
  maxRevenueShare: number | string;
  licenseTemplate?: Address;
};
```

```typescript Response Type
export type RegisterDerivativeResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

## registerDerivativeWithLicenseTokens

Registers a derivative with license tokens.

The derivative IP is registered with license tokens minted from the parent IP's license terms.

The license terms of the parent IPs issued with license tokens are attached to the derivative IP.

The caller must be the derivative IP owner or an authorized operator.

| Method                                | Type                                                                                                            |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `registerDerivativeWithLicenseTokens` | `(request: RegisterDerivativeWithLicenseTokensRequest) => Promise<RegisterDerivativeWithLicenseTokensResponse>` |

Parameters:

- `request.childIpId`: The derivative IP ID.
- `request.licenseTokenIds`: The IDs of the license tokens.
- `request.maxRts`: The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Recommended for simplicity: 100_000_000**
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const response = await client.ipAsset.registerDerivativeWithLicenseTokens({
  childIpId: "0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  licenseTokenIds: ["5"], // array of license ids relevant to the creation of the derivative, minted from the parent IPA
  txOptions: { waitForTransaction: true },
});

console.log(
  `Derivative IPA linked to parent at transaction hash ${response.txHash}`
);
```

```typescript Request Type
export type RegisterDerivativeWithLicenseTokensRequest = {
  childIpId: Address;
  licenseTokenIds: string[] | bigint[] | number[];
  maxRts: number | string;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type RegisterDerivativeWithLicenseTokensResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

## mintAndRegisterIpAssetWithPilTerms

Mint an NFT from a collection, register it as an IP, attach metadata to the IP, and attach License Terms to the IP all in one function.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                               | Type                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `mintAndRegisterIpAssetWithPilTerms` | `(request: MintAndRegisterIpAssetWithPilTermsRequest) => Promise<MintAndRegisterIpAssetWithPilTermsResponse>` |

Parameters:

- `request.spgNftContract`: The address of the NFT collection.
- `request.allowDuplicates`: \[Optional] Set to true to allow minting IPs with the same NFT metadata. **Default: true**
- `request.licenseTermsData[]`: The array of license terms to be attached. ⚠️ **This function will fail if you pass in an empty array.**
  - `request.licenseTermsData.terms`: See the [LicenseTerms type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/resources/license.ts#L26).
  - `request.licenseTermsData.licensingConfig`: \[Optional] See the [LicensingConfig type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/common.ts#L15). If none provided, it will default to the one shown [here](https://github.com/storyprotocol/sdk/blob/dev/packages/core-sdk/src/utils/validateLicenseConfig.ts).
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI`: \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash`: \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI`: \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash`: \[Optional] The hash of the metadata for the IP NFT.
- `request.recipient`: \[Optional] The address of the recipient of the minted NFT.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { LicenseTerms } from "@story-protocol/core-sdk";
import { zeroAddress } from "viem";

const commercialRemixTerms: LicenseTerms = {
  transferable: true,
  royaltyPolicy: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  defaultMintingFee: 0n,
  expiration: 0n,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: zeroAddress,
  commercialRevShare: 50, // can claim 50% of derivative revenue
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0n,
  currency: "0x1514000000000000000000000000000000000000", // $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  uri: "",
};

const response = await client.ipAsset.mintAndRegisterIpAssetWithPilTerms({
  spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc",
  licenseTermsData: [{ terms: commercialRemixTerms }],
  // https://docs.story.foundation/docs/ip-asset#adding-nft--ip-metadata-to-ip-asset
  ipMetadata: {
    ipMetadataURI: "test-uri",
    ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
    nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
    nftMetadataURI: "test-nft-uri",
  },
  txOptions: { waitForTransaction: true },
});

console.log(`
  Token ID: ${response.tokenId}, 
  IPA ID: ${response.ipId}, 
  License Terms ID: ${response.licenseTermsId}
`);
```

```typescript Request Type
export type MintAndRegisterIpAssetWithPilTermsRequest = {
  spgNftContract: Address;
  allowDuplicates: boolean;
  licenseTermsData: LicenseTermsData<
    RegisterPILTermsRequest,
    LicensingConfig
  >[];
  recipient?: Address;
  royaltyPolicyAddress?: Address;
} & IpMetadataAndTxOptions &
  WithWipOptions;
```

```typescript Response Type
export type MintAndRegisterIpAssetWithPilTermsResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
  ipId?: Address;
  tokenId?: bigint;
  receipt?: TransactionReceipt;
  licenseTermsIds?: bigint[];
};
```

</CodeGroup>

## batchMintAndRegisterIpAssetWithPilTerms

Batch mint an NFT from a collection and register it as an IP.

| Method                                    | Type                                                                                                                    |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `batchMintAndRegisterIpAssetWithPilTerms` | `(request: BatchMintAndRegisterIpAssetWithPilTermsRequest) => Promise<BatchMintAndRegisterIpAssetWithPilTermsResponse>` |

## registerIpAndAttachPilTerms

Register a given NFT as an IP, attach metadata to the IP, and attach License Terms to the IP all in one function.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                        | Type                                                                                            |
| ----------------------------- | ----------------------------------------------------------------------------------------------- |
| `registerIpAndAttachPilTerms` | `(request: RegisterIpAndAttachPilTermsRequest) => Promise<RegisterIpAndAttachPilTermsResponse>` |

Parameters:

- `request.nftContract`: The address of the NFT collection.
- `request.tokenId`: The ID of the NFT.
- `request.licenseTermsData[]`: The array of license terms to be attached. ⚠️ **This function will fail if you pass in an empty array.**
  - `request.licenseTermsData.terms`: See the [LicenseTerms type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/resources/license.ts#L26).
  - `request.licenseTermsData.licensingConfig`: \[Optional] See the [LicensingConfig type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/common.ts#L15). If none provided, it will default to the one shown [here](https://github.com/storyprotocol/sdk/blob/dev/packages/core-sdk/src/utils/validateLicenseConfig.ts).
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI`: \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash`: \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI`: \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash`: \[Optional] The hash of the metadata for the IP NFT.
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds. **Defaults to 1000**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { LicenseTerms } from "@story-protocol/core-sdk";
import { toHex, zeroAddress } from "viem";

const commercialRemixTerms: LicenseTerms = {
  transferable: true,
  royaltyPolicy: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  defaultMintingFee: 0n,
  expiration: 0n,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: zeroAddress,
  commercialRevShare: 50, // can claim 50% of derivative revenue
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0n,
  currency: "0x1514000000000000000000000000000000000000", // $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  uri: "",
};

const response = await client.ipAsset.registerIpAndAttachPilTerms({
  nftContract: "0x041B4F29183317Fd352AE57e331154b73F8a1D73",
  tokenId: "12",
  licenseTermsData: [{ terms: commercialRemixTerms }],
  ipMetadata: {
    ipMetadataURI: "test-uri",
    ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
    nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
    nftMetadataURI: "test-nft-uri",
  },
  txOptions: { waitForTransaction: true },
});
console.log(
  `Root IPA created at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
);
```

```typescript Request Type
export type RegisterIpAndAttachPilTermsRequest = {
  nftContract: Address;
  tokenId: bigint | string | number;
  licenseTermsData: LicenseTermsData<
    RegisterPILTermsRequest,
    LicensingConfig
  >[];
  deadline?: bigint | number | string;
} & IpMetadataAndTxOptions;
```

```typescript Response Type
export type RegisterIpAndAttachPilTermsResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
  ipId?: Address;
  licenseTermsIds?: bigint[];
  tokenId?: bigint;
};
```

</CodeGroup>

## registerDerivativeIp

Register an NFT as IP and then link it as a derivative of another IP Asset without using license tokens.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                 | Type                                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| `registerDerivativeIp` | `(request: RegisterIpAndMakeDerivativeRequest) => Promise<RegisterIpAndMakeDerivativeResponse>` |

Parameters:

- `request.nftContract`: The address of the NFT collection.
- `request.tokenId`: The ID of the NFT.
- `request.derivData`: The derivative data to be used for registerDerivative.
  - `request.derivData.parentIpIds`: The IDs of the parent IPs to link the registered derivative IP.
  - `request.derivData.licenseTermsIds`: The IDs of the license terms to be used for the linking.
  - `request.derivData.maxMintingFee`: \[Optional] The maximum minting fee that the caller is willing to pay. If set to 0, then there is no no limit. **Default: 0**
  - `request.derivData.maxRevenueShare`: \[Optional] The maximum revenue share percentage agreed upon between a child and parent when a child is registering as derivative. Must be between 0 and 100. **Default: 100**
  - `request.derivData.maxRts`: \[Optional]The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Default: 100_000_000**
  - `request.derivData.licenseTemplate`: \[Optional] The address of the license template to be used for the linking. For now, this can only be the [PIL](/concepts/programmable-ip-license)
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds. **Defaults to 1000**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { toHex } from "viem";

const response = await client.ipAsset.registerDerivativeIp({
  nftContract: "0x041B4F29183317Fd352AE57e331154b73F8a1D73", // your NFT contract address
  tokenId: "127",
  derivData: {
    parentIpIds: ["0xd142822Dc1674154EaF4DDF38bbF7EF8f0D8ECe4"],
    licenseTermsIds: ["1"],
  },
  // https://docs.story.foundation/docs/ip-asset#adding-nft--ip-metadata-to-ip-asset
  ipMetadata: {
    ipMetadataURI: "test-uri",
    ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
    nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
    nftMetadataURI: "test-nft-uri",
  },
  txOptions: { waitForTransaction: true },
});

console.log(
  `Completed at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
);
```

```typescript Request Type
export type RegisterIpAndMakeDerivativeRequest = {
  nftContract: Address;
  tokenId: string | number | bigint;
  deadline?: string | number | bigint;
  derivData: DerivativeData;
} & IpMetadataAndTxOptions &
  WithWipOptions;

export type DerivativeData = {
  parentIpIds: Address[];
  licenseTermsIds: bigint[] | string[] | number[];
  /**
   * The maximum minting fee that the caller is willing to pay. if set to 0 then no limit.
   * @default 0
   */
  maxMintingFee?: bigint | string | number;
  /**
   * The maximum number of royalty tokens that can be distributed to the external royalty policies (max: 100,000,000).
   * @default 100_000_000
   */
  maxRts?: number | string;
  /**
   * The maximum revenue share percentage allowed for minting the License Tokens. Must be between 0 and 100 (where 100% represents 100_000_000).
   * @default 100
   */
  maxRevenueShare?: number | string;
  licenseTemplate?: Address;
};
```

```typescript Response Type
export type RegisterIpAndMakeDerivativeResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
  ipId?: Address;
  tokenId?: bigint;
  receipt?: TransactionReceipt;
};
```

</CodeGroup>

## batchRegisterDerivative

Batch registers a derivative directly with parent IP's license terms.

| Method                    | Type                                                                                    |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `batchRegisterDerivative` | `(request: BatchRegisterDerivativeRequest) => Promise<BatchRegisterDerivativeResponse>` |

## mintAndRegisterIpAndMakeDerivative

Mint an NFT from a collection and register it as a derivative IP without license tokens.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                               | Type                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `mintAndRegisterIpAndMakeDerivative` | `(request: MintAndRegisterIpAndMakeDerivativeRequest) => Promise<MintAndRegisterIpAndMakeDerivativeResponse>` |

Parameters:

- `request.spgNftContract`: The address of the NFT collection.
- `request.allowDuplicates`: \[Optional] Set to true to allow minting IPs with the same NFT metadata. **Default: true**
- `request.derivData`: The derivative data to be used for registerDerivative.
  - `request.derivData.parentIpIds`: The IDs of the parent IPs to link the registered derivative IP.
  - `request.derivData.licenseTermsIds`: The IDs of the license terms to be used for the linking.
  - `request.derivData.maxMintingFee`: \[Optional] The maximum minting fee that the caller is willing to pay. If set to 0, then there is no no limit. **Default: 0**
  - `request.derivData.maxRevenueShare`: \[Optional] The maximum revenue share percentage agreed upon between a child and parent when a child is registering as derivative. Must be between 0 and 100. **Default: 100**
  - `request.derivData.maxRts`: \[Optional] The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Default: 100_000_000**
  - `request.derivData.licenseTemplate`: \[Optional] The address of the license template to be used for the linking. For now, this can only be the [PIL](/concepts/programmable-ip-license)
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.recipient`: \[Optional] The address of the recipient of the minted NFT, default value is your wallet address.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { toHex } from "viem";

const response = await client.ipAsset.mintAndRegisterIpAndMakeDerivative({
  // an NFT contract address created by the SPG
  spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc",
  derivData: {
    parentIpIds: ["0xd142822Dc1674154EaF4DDF38bbF7EF8f0D8ECe4"],
    licenseTermsIds: ["1"],
  },
  // https://docs.story.foundation/docs/ip-asset#adding-nft--ip-metadata-to-ip-asset
  ipMetadata: {
    ipMetadataURI: "test-uri",
    ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
    nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
    nftMetadataURI: "test-nft-uri",
  },
  txOptions: { waitForTransaction: true },
});

console.log(
  `Completed at transaction hash ${response.txHash}, IPA ID: ${response.ipId}, Token ID: ${response.tokenId}`
);
```

```typescript Request Type
export type MintAndRegisterIpAndMakeDerivativeRequest = {
  spgNftContract: Address;
  derivData: DerivativeData;
  recipient?: Address;
  allowDuplicates: boolean;
} & IpMetadataAndTxOptions &
  WithWipOptions;

export type DerivativeData = {
  parentIpIds: Address[];
  licenseTermsIds: bigint[] | string[] | number[];
  /**
   * The maximum minting fee that the caller is willing to pay. if set to 0 then no limit.
   * @default 0
   */
  maxMintingFee?: bigint | string | number;
  /**
   * The maximum number of royalty tokens that can be distributed to the external royalty policies (max: 100,000,000).
   * @default 100_000_000
   */
  maxRts?: number | string;
  /**
   * The maximum revenue share percentage allowed for minting the License Tokens. Must be between 0 and 100 (where 100% represents 100_000_000).
   * @default 100
   */
  maxRevenueShare?: number | string;
  licenseTemplate?: Address;
};
```

```typescript Response Type
export type MintAndRegisterIpAndMakeDerivativeResponse = {
  encodedTxData?: EncodedTxData;
} & CommonRegistrationResponse;

export type CommonRegistrationResponse = {
  txHash?: Hex;
  ipId?: Address;
  tokenId?: bigint;
  receipt?: TransactionReceipt;
};
```

</CodeGroup>

## batchMintAndRegisterIpAndMakeDerivative

Batch mint an NFT from a collection and register it as a derivative IP without license tokens.

| Method                                    | Type                                                                                                                    |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `batchMintAndRegisterIpAndMakeDerivative` | `(request: BatchMintAndRegisterIpAndMakeDerivativeRequest) => Promise<BatchMintAndRegisterIpAndMakeDerivativeResponse>` |

## mintAndRegisterIp

Mint an NFT from an SPGNFT collection and register it with metadata as an IP.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method              | Type                                                                 |
| ------------------- | -------------------------------------------------------------------- |
| `mintAndRegisterIp` | `(request: MintAndRegisterIpRequest) => Promise<RegisterIpResponse>` |

Parameters:

- `request.spgNftContract`: The address of the NFT collection.
- `request.allowDuplicates`: \[Optional] Set to true to allow minting IPs with the same NFT metadata. **Default: true**
- `request.recipient`: \[Optional] The address of the recipient of the minted NFT, default value is your wallet address.
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { toHex, Address, zeroAddress } from "viem";

const response = await client.ipAsset.mintAndRegisterIp({
  // an NFT contract address created by the SPG
  spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc",
  // https://docs.story.foundation/docs/ip-asset#adding-nft--ip-metadata-to-ip-asset
  ipMetadata: {
    ipMetadataURI: "test-uri",
    ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
    nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
    nftMetadataURI: "test-nft-uri",
  },
  txOptions: { waitForTransaction: true },
});

console.log(
  `Completed at transaction hash ${response.txHash}, NFT Token ID: ${response.tokenId}, IPA ID: ${response.ipId}, License Terms ID: ${response.licenseTermsId}`
);
```

```typescript Request Type
export type MintAndRegisterIpRequest = {
  spgNftContract: Address;
  recipient?: Address;
  allowDuplicates: boolean;
} & IpMetadataAndTxOptions &
  WithWipOptions;
```

```typescript Response Type
export type RegisterIpResponse = {
  encodedTxData?: EncodedTxData;
} & CommonRegistrationResponse;

export type CommonRegistrationResponse = {
  txHash?: Hex;
  ipId?: Address;
  tokenId?: bigint;
  receipt?: TransactionReceipt;
};
```

</CodeGroup>

## registerPilTermsAndAttach

Register Programmable IP License Terms (if unregistered) and attach it to IP.

| Method                      | Type                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| `registerPilTermsAndAttach` | `(request: RegisterPilTermsAndAttachRequest) => Promise<RegisterPilTermsAndAttachResponse>` |

Parameters:

- `request.ipId`: The ID of the IP.
- `request.licenseTermsData[]`: The array of license terms to be attached.
  - `request.licenseTermsData.terms`: See the [LicenseTerms type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/resources/license.ts#L26).
  - `request.licenseTermsData.licensingConfig`: \[Optional] See the [LicensingConfig type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/common.ts#L15). If none provided, it will default to the one shown [here](https://github.com/storyprotocol/sdk/blob/dev/packages/core-sdk/src/utils/validateLicenseConfig.ts).
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds. **Defaults to 1000**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { LicenseTerms } from "@story-protocol/core-sdk";
import { zeroAddress } from "viem";

const commercialRemixTerms: LicenseTerms = {
  transferable: true,
  royaltyPolicy: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  defaultMintingFee: 0n,
  expiration: 0n,
  commercialUse: true,
  commercialAttribution: true,
  commercializerChecker: zeroAddress,
  commercializerCheckerData: zeroAddress,
  commercialRevShare: 50, // can claim 50% of derivative revenue
  commercialRevCeiling: 0n,
  derivativesAllowed: true,
  derivativesAttribution: true,
  derivativesApproval: false,
  derivativesReciprocal: true,
  derivativeRevCeiling: 0n,
  currency: "0x1514000000000000000000000000000000000000", // $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  uri: "",
};

const response = await client.ipAsset.registerPilTermsAndAttach({
  ipId: "0x4c1f8c1035a8cE379dd4ed666758Fb29696CF721",
  licenseTermsData: [{ terms: commercialRemixTerms }],
  txOptions: { waitForTransaction: true },
});
console.log(`License Terms ${response.licenseTermsId} attached to IP Asset.`);
```

```typescript Request Type
export type RegisterPilTermsAndAttachRequest = {
  ipId: Address;
  licenseTermsData: LicenseTermsData<
    RegisterPILTermsRequest,
    LicensingConfig
  >[];
  deadline?: string | number | bigint;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type RegisterPilTermsAndAttachResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
  licenseTermsIds?: bigint[];
};
```

</CodeGroup>

## mintAndRegisterIpAndMakeDerivativeWithLicenseTokens

Mint an NFT from a collection and register it as a derivative IP using license tokens

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                                                | Type                                                                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `mintAndRegisterIpAndMakeDerivativeWithLicenseTokens` | `(request: MintAndRegisterIpAndMakeDerivativeWithLicenseTokensRequest) => Promise<RegisterIpResponse>` |

Parameters:

- `request.spgNftContract`: The address of the NFT collection.
- `request.allowDuplicates`: \[Optional] Set to true to allow minting IPs with the same NFT metadata. **Default: true**
- `request.maxRts`: The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Recommended for simplicity: 100_000_000**
- `request.licenseTokenIds`: The IDs of the license tokens to be burned for linking the IP to parent IPs.
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.recipient`: \[Optional] The address to receive the minted NFT, default value is your wallet address.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { toHex } from "viem";

const response =
  await client.ipAsset.mintAndRegisterIpAndMakeDerivativeWithLicenseTokens({
    spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc", // your SPG NFT contract address
    licenseTokenIds: ["10"],
    // https://docs.story.foundation/docs/ip-asset#adding-nft--ip-metadata-to-ip-asset
    ipMetadata: {
      ipMetadataURI: "test-uri",
      ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
      nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      nftMetadataURI: "test-nft-uri",
    },
    maxRts: 100_000_000, // default
    txOptions: { waitForTransaction: true },
  });

console.log(
  `Completed at transaction hash ${response.txHash}, IPA ID: ${response.ipId}, Token ID: ${response.tokenId}`
);
```

```typescript Request Type
export type MintAndRegisterIpAndMakeDerivativeWithLicenseTokensRequest = {
  spgNftContract: Address;
  licenseTokenIds: string[] | bigint[] | number[];
  recipient?: Address;
  maxRts: number | string;
  allowDuplicates: boolean;
} & IpMetadataAndTxOptions &
  WithWipOptions;
```

```typescript Response Type
export type RegisterIpResponse = {
  encodedTxData?: EncodedTxData;
} & CommonRegistrationResponse;

export type CommonRegistrationResponse = {
  txHash?: Hex;
  ipId?: Address;
  tokenId?: bigint;
  receipt?: TransactionReceipt;
};
```

</CodeGroup>

## registerIpAndMakeDerivativeWithLicenseTokens

Register the given NFT as a derivative IP using license tokens.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                                         | Type                                                                                            |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `registerIpAndMakeDerivativeWithLicenseTokens` | `(request: RegisterIpAndMakeDerivativeWithLicenseTokensRequest) => Promise<RegisterIpResponse>` |

Parameters:

- `request.nftContract`: The address of the NFT collection.
- `request.tokenId`: The ID of the NFT.
- `request.maxRts`: The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Recommended for simplicity: 100_000_000**
- `request.licenseTokenIds`: The IDs of the license tokens to be burned for linking the IP to parent IPs.
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds. **Default is 1000**.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { toHex } from "viem";

const response =
  await client.ipAsset.registerIpAndMakeDerivativeWithLicenseTokens({
    nftContract: "0x041B4F29183317Fd352AE57e331154b73F8a1D73", // your NFT contract address
    tokenId: "127",
    licenseTokenIds: ["10"],
    // https://docs.story.foundation/docs/ip-asset#adding-nft--ip-metadata-to-ip-asset
    ipMetadata: {
      ipMetadataURI: "test-uri",
      ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
      nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      nftMetadataURI: "test-nft-uri",
    },
    txOptions: { waitForTransaction: true },
  });

console.log(
  `Completed at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
);
```

```typescript Request Type
export type RegisterIpAndMakeDerivativeWithLicenseTokensRequest = {
  nftContract: Address;
  tokenId: string | number | bigint;
  licenseTokenIds: string[] | bigint[] | number[];
  deadline?: string | number | bigint;
  maxRts: number | string;
} & IpMetadataAndTxOptions &
  WithWipOptions;
```

```typescript Response Type
export type RegisterIpResponse = {
  encodedTxData?: EncodedTxData;
} & CommonRegistrationResponse;

export type CommonRegistrationResponse = {
  txHash?: Hex;
  ipId?: Address;
  tokenId?: bigint;
  receipt?: TransactionReceipt;
};
```

</CodeGroup>


# License

## License

### Methods

- attachLicenseTerms
- mintLicenseTokens
- registerPILTerms
- registerNonComSocialRemixingPIL
- registerCommercialUsePIL
- registerCommercialRemixPIL

### attachLicenseTerms

Attaches license terms to an IP.

| Method               |
| -------------------- |
| `attachLicenseTerms` |

Parameters:

- `ip_id`: The address of the IP to which the license terms are attached.
- `license_template`: The address of the license template.
- `license_terms_id`: The ID of the license terms.
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.License.attachLicenseTerms(
  ip_id="0x4c1f8c1035a8cE379dd4ed666758Fb29696CF721",
  license_template="0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316", # insert PILicenseTemplate from https://docs.story.foundation/docs/deployed-smart-contracts
  license_terms_id="1"
)
```

```python Request Parameters
ip_id: str  # The address of the IP to which the license terms are attached
license_template: str  # The address of the license template
license_terms_id: int  # The ID of the license terms
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str
}
```

</CodeGroup>

### mintLicenseTokens

Mints license tokens for the license terms attached to an IP.

The license tokens are minted to the receiver.

The license terms must be attached to the IP before calling this function.

IP owners can mint license tokens for their IPs for arbitrary license terms without attaching the license terms to IP.

It might require the caller pay the minting fee, depending on the license terms or configured by the iP owner. The minting fee is paid in the minting fee token specified in the license terms or configured by the IP owner. IP owners can configure the minting fee of their IPs or configure the minting fee module to determine the minting fee.

| Method              |
| ------------------- |
| `mintLicenseTokens` |

Parameters:

- `licensor_ip_id`: The licensor IP ID.
- `license_template`: The address of the license template.
- `license_terms_id`: The ID of the license terms within the license template.
- `amount`: The amount of license tokens to mint.
- `receiver`: The address of the receiver.
- `max_minting_fee`: [Optional] The maximum minting fee to pay.
- `max_revenue_share`: [Optional] The maximum revenue share percentage.
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = client.License.mintLicenseTokens(
  licensor_ip_id="0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  license_template="0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316", # insert PILicenseTemplate from https://docs.story.foundation/docs/deployed-smart-contracts
  license_terms_id="1",
  amount=1,
  receiver="0x14dC79964da2C08b23698B3D3cc7Ca32193d9955", # optional
  max_minting_fee=0, # disabled
  max_revenue_share=100 # default
)
```

```python Request Parameters
licensor_ip_id: str  # The licensor IP ID
license_template: str  # The address of the license template
license_terms_id: int  # The ID of the license terms
amount: int   # The amount of license tokens to mint
receiver: str  # The address of the receiver
max_minting_fee: int = 0  # Optional: The maximum minting fee to pay
max_revenue_share: int = 0  # Optional: The maximum revenue share percentage
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "licenseTokenIds": list,  # List of license token IDs
  "txHash": str,  # The transaction hash
}
```

</CodeGroup>

### registerPILTerms

Registers new license terms and return the ID of the newly registered license terms.

| Method             |
| ------------------ |
| `registerPILTerms` |

Parameters:

- See the Python code example below for all the parameters. They all come from the [PIL Terms](/concepts/programmable-ip-license/pil-terms).
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.License.registerPILTerms(
  transferable=False,
  royalty_policy="0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  default_minting_fee=0,
  expiration=0,
  commercial_use=False,
  commercial_attribution=False,
  commercializer_checker="0x0000000000000000000000000000000000000000",
  commercializer_checker_data="0x",
  commercial_rev_share=10, # 10%
  commercial_rev_ceiling=0,
  derivatives_allowed=True,
  derivatives_attribution=False,
  derivatives_approval=False,
  derivatives_reciprocal=False,
  derivative_rev_ceiling=0,
  currency="0x1514000000000000000000000000000000000000", # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  uri="",
)
```

```python Request Parameters
transferable: bool  # Indicates whether the license is transferable or not
royalty_policy: str  # The address of the royalty policy contract
default_minting_fee: int  # The default minting fee to be paid when minting a license
expiration: int  # The expiration period of the license
commercial_use: bool  # Indicates whether the work can be used commercially or not
commercial_attribution: bool  # Whether attribution is required when reproducing the work commercially
commercializer_checker: str  # Commercializers that are allowed to commercially exploit the work
commercializer_checker_data: str  # The data to be passed to the commercializer checker contract
commercial_rev_share: int  # Percentage of revenue that must be shared with the licensor (0-100)
commercial_rev_ceiling: int  # The maximum revenue that can be generated from commercial use
derivatives_allowed: bool  # Indicates whether the licensee can create derivatives of the work
derivatives_attribution: bool  # Whether attribution is required for derivatives of the work
derivatives_approval: bool  # Whether the licensor must approve derivatives before they can be linked
derivatives_reciprocal: bool  # Whether derivatives must be licensed under the same terms
derivative_rev_ceiling: int  # The maximum revenue that can be generated from derivative use
currency: str  # The ERC20 token to be used to pay the minting fee
uri: str  # The URI of the license terms
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "licenseTermsId": int,
  "txHash": str
}
```

</CodeGroup>

### registerNonComSocialRemixingPIL

Convenient function to register a PIL non commercial social remix license to the registry.

<Warning>

No reason to call this function. Non-Commercial Social Remixing terms are already registered with `licenseTermdId = 1` in our protocol. There's no reason to register them again.

</Warning>

| Method                            |
| --------------------------------- |
| `registerNonComSocialRemixingPIL` |

Parameters:

- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.License.registerNonComSocialRemixingPIL()
```

```python Request Parameters
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "licenseTermsId": int,  # The ID of the registered license terms
  "txHash": str,  # The transaction hash
}
```

</CodeGroup>

### registerCommercialUsePIL

Convenient function to register a PIL commercial use license to the registry.

| Method                     |
| -------------------------- |
| `registerCommercialUsePIL` |

Parameters:

- `default_minting_fee`: The fee to be paid when minting a license.
- `currency`: The ERC20 token to be used to pay the minting fee and the token must be registered on Story's protocol.
- `royalty_policy`: [Optional] The address of the royalty policy contract, default value is LAP.
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.License.registerCommercialUsePIL(
  currency='0x1514000000000000000000000000000000000000', # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  default_minting_fee=10, # 10 of the currency (using the above currency, 10 $WIP),
  royalty_policy="0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
)
```

```python Request Parameters
default_minting_fee: int  # The fee to be paid when minting a license
currency: str  # The ERC20 token to be used to pay the minting fee
royalty_policy: str = None  # Optional: The address of the royalty policy contract
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "licenseTermsId": int,  # The ID of the registered license terms
  "txHash": str,  # The transaction hash
}
```

</CodeGroup>

### registerCommercialRemixPIL

Convenient function to register a PIL commercial Remix license to the registry.

| Method                       |
| ---------------------------- |
| `registerCommercialRemixPIL` |

Parameters:

- `default_minting_fee`: The fee to be paid when minting a license.
- `commercial_rev_share`: Percentage of revenue that must be shared with the licensor.
- `currency`: The ERC20 token to be used to pay the minting fee and the token must be registered on Story's protocol.
- `royalty_policy`: The address of the royalty policy contract, default value is LAP.
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.License.registerCommercialRemixPIL(
  currency='0x1514000000000000000000000000000000000000', # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  default_minting_fee=10, # 10 of the currency (using the above currency, 10 $WIP)
  royalty_policy="0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  commercial_rev_share=10 # 10%
)
```

```python Request Parameters
default_minting_fee: int  # The fee to be paid when minting a license
currency: str  # The ERC20 token to be used to pay the minting fee
commercial_rev_share: int  # Percentage of revenue that must be shared with the licensor
royalty_policy: str  # The address of the royalty policy contract
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "licenseTermsId": int,  # The ID of the registered license terms
  "txHash": str,  # The transaction hash
}
```

</CodeGroup>


# IP Asset

## IPAsset

### Methods

- register
- registerDerivative
- registerDerivativeWithLicenseTokens
- mintAndRegisterIpAssetWithPilTerms

### Navigating Around the IPAssetClient

Because there are a lot of functions to interact with the [📜 Licensing Module](/concepts/licensing-module), we have broken them down into a helpful chart so you can identify what you're looking for, and then find the associated docs.

| **Function**                                                                | **Mint an NFT** | **Register IPA** | **Create License Terms** | **Attach License Terms** | **Mint License Token** | **Register as Derivative** |
| --------------------------------------------------------------------------- | :-------------: | :--------------: | :----------------------: | :----------------------: | :--------------------: | :------------------------: |
| <span style={{color: "#e03130"}}>register</span>                            |                 |        ✓         |                          |                          |                        |                            |
| <span style={{color: "#e03130"}}>mintAndRegisterIpAssetWithPilTerms</span>  |        ✓        |        ✓         |            ✓             |            ✓             |                        |                            |
| <span style={{color: "#e03130"}}>registerDerivative</span>                  |                 |                  |                          |                          |                        |             ✓              |
| <span style={{color: "#e03130"}}>registerDerivativeWithLicenseTokens</span> |                 |                  |                          |                          |                        |             ✓              |
| <span style={{color: "#1971c2"}}>registerPILTerms</span>                    |                 |                  |            ✓             |                          |                        |                            |
| <span style={{color: "#1971c2"}}>attachLicenseTerms</span>                  |                 |                  |                          |            ✓             |                        |                            |
| <span style={{color: "#1971c2"}}>mintLicenseTokens</span>                   |                 |                  |                          |                          |           ✓            |                            |

- <span style={{ color: "#e03130" }}>Red</span>: IPAssetClient (this page)
- <span style={{ color: "#1971c2" }}>Blue</span>:
  [LicenseClient](/sdk-reference/python/license)

## register

Registers an NFT as IP, creating a corresponding [🧩 IP Asset](/concepts/ip-asset). If the given NFT was already registered, this function will return the existing `ipId`.

<Note title="NFT Metadata">
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method     |
| ---------- |
| `register` |

Parameters:

- `nft_contract`: The address of the NFT.
- `token_id`: The token identifier of the NFT.
- `ip_metadata`: [Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `ip_metadata['ip_metadata_uri']`: [Optional] The URI of the metadata for the IP.
  - `ip_metadata['ip_metadata_hash']`: [Optional] The hash of the metadata for the IP.
  - `ip_metadata['nft_metadata_uri']`: [Optional] The URI of the metadata for the NFT.
  - `ip_metadata['nft_metadata_hash']`: [Optional] The hash of the metadata for the IP NFT.
- `deadline`: [Optional] The deadline for the signature in milliseconds.
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
metadata = {
  'ip_metadata_uri': "test-uri",
  'ip_metadata_hash': web3.to_hex(web3.keccak(text="test-ip-metadata-hash")),
  'nft_metadata_uri': "test-uri",
  'nft_metadata_hash': web3.to_hex(web3.keccak(text="test-nft-metadata-hash"))
}

response = story_client.IPAsset.register(
  nft_contract="0x041B4F29183317Fd352AE57e331154b73F8a1D73",
  token_id="12",
  ip_metadata=metadata
)
```

```python Request Parameters
nft_contract: str  # The address of the NFT
token_id: str  # The token identifier of the NFT
ip_metadata: dict = None  # Optional: Metadata for the NFT and IP
deadline: int = None  # Optional: The deadline for the signature in milliseconds
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "ipId": str,  # The IP ID of the registered IP
  "txHash": str  # The transaction hash
}
```

</CodeGroup>

## registerDerivative

Registers a derivative directly with parent IP's license terms, without needing license tokens, and attaches the license terms of the parent IPs to the derivative IP.

The license terms must be attached to the parent IP before calling this function.

All IPs attached default license terms by default.

The derivative IP owner must be the caller or an authorized operator.

| Method               |
| -------------------- |
| `registerDerivative` |

Parameters:

- `child_ip_id`: The derivative IP ID.
- `parent_ip_ids`: The parent IP IDs.
- `license_terms_ids`: The IDs of the license terms that the parent IP supports.
- `max_minting_fee`: [Optional] The maximum minting fee that the caller is willing to pay. If set to 0, then there is no limit. **Default: 0**
- `max_revenue_share`: [Optional] The maximum revenue share percentage agreed upon between a child and parent when a child is registering as derivative. Must be between 0 and 100. **Default: 100**
- `max_rts`: [Optional] The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Default: 100_000_000**
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.IPAsset.registerDerivative(
  child_ip_id="0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  parent_ip_ids=["0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba"],
  license_terms_ids=["5"],
  max_minting_fee=0, # disabled
  max_rts=100_000_000, # default
  max_revenue_share=100 # default
)
```

```python Request Parameters
child_ip_id: str  # The derivative IP ID
parent_ip_ids: list  # The parent IP IDs
license_terms_ids: list  # The IDs of the license terms that the parent IP supports
max_minting_fee: int = 0  # Optional: The maximum minting fee the caller is willing to pay
max_rts: int = 0  # Optional: The maximum number of royalty tokens
max_revenue_share: int = 0  # Optional: The maximum revenue share percentage
license_template: str = None  # Optional: The address of the license template
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str  # The transaction hash
}
```

</CodeGroup>

## registerDerivativeWithLicenseTokens

Registers a derivative with license tokens.

The derivative IP is registered with license tokens minted from the parent IP's license terms.

The license terms of the parent IPs issued with license tokens are attached to the derivative IP.

The caller must be the derivative IP owner or an authorized operator.

| Method                                |
| ------------------------------------- |
| `registerDerivativeWithLicenseTokens` |

Parameters:

- `child_ip_id`: The derivative IP ID.
- `license_token_ids`: The IDs of the license tokens.
- `max_rts`: The maximum number of royalty tokens that can be distributed to the external royalty policies. Must be between 0 and 100,000,000. **Recommended for simplicity: 100_000_000**
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.IPAsset.registerDerivativeWithLicenseTokens(
  child_ip_id="0xC92EC2f4c86458AFee7DD9EB5d8c57920BfCD0Ba",
  license_token_ids=["5"],
  max_rts=100_000_000 # default
)
```

```python Request Parameters
child_ip_id: str  # The derivative IP ID
license_token_ids: list  # The IDs of the license tokens
max_rts: int = 0  # Optional: The maximum number of royalty tokens
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str  # The transaction hash
}
```

</CodeGroup>

## mintAndRegisterIpAssetWithPilTerms

Mint an NFT from a collection, register it as an IP, attach metadata to the IP, and attach License Terms to the IP all in one function.

<Note>
  Note that this function will also set the underlying NFT's `tokenUri` to
  whatever is passed under `ipMetadata.nftMetadataURI`.
</Note>

| Method                               |
| ------------------------------------ |
| `mintAndRegisterIpAssetWithPilTerms` |

Parameters:

- `spg_nft_contract`: The address of the NFT collection.
- `terms`: The array of license terms to be attached. ⚠️ **This function will fail if you pass in an empty array.**
  - `terms[].terms`: The license terms data. See the Python example below for the structure.
  - `terms[].licensing_config`: [Optional] The licensing configuration. See the Python example below for the structure.
- `allow_duplicates`: [Optional] Set to true to allow minting IPs with the same NFT metadata. **Default: True**
- `ip_metadata`: [Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `ip_metadata['ip_metadata_uri']`: [Optional] The URI of the metadata for the IP.
  - `ip_metadata['ip_metadata_hash']`: [Optional] The hash of the metadata for the IP.
  - `ip_metadata['nft_metadata_uri']`: [Optional] The URI of the metadata for the NFT.
  - `ip_metadata['nft_metadata_hash']`: [Optional] The hash of the metadata for the IP NFT.
- `recipient`: [Optional] The address of the recipient of the minted NFT.
- `tx_options`: [Optional] Transaction options dictionary.

<CodeGroup>

```python Python
commercial_remix_terms = {
  "transferable": True,
  "royalty_policy": "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", # RoyaltyPolicyLAP address from https://docs.story.foundation/docs/deployed-smart-contracts
  "default_minting_fee": 0,
  "expiration": 0,
  "commercial_use": True,
  "commercial_attribution": True,
  "commercializer_checker": "0x0000000000000000000000000000000000000000",
  "commercializer_checker_data": "0x0000000000000000000000000000000000000000",
  "commercial_rev_share": 50,
  "commercial_rev_ceiling": 0,
  "derivatives_allowed": True,
  "derivatives_attribution": True,
  "derivatives_approval": False,
  "derivatives_reciprocal": True,
  "derivative_rev_ceiling": 0,
  "currency": "0x1514000000000000000000000000000000000000", # $WIP address from https://docs.story.foundation/docs/deployed-smart-contracts
  "uri": "",
}

licensing_config = {
  "is_set": False,
  "minting_fee": 0,
  "licensing_hook": "0x0000000000000000000000000000000000000000",
  "hook_data": "0x0000000000000000000000000000000000000000",
  "commercial_rev_share": 0,
  "disabled": False,
  "expect_minimum_group_reward_share": 0,
  "expect_group_reward_pool": "0x0000000000000000000000000000000000000000",
}

metadata = {
  'ip_metadata_uri': "test-uri",
  'ip_metadata_hash': web3.to_hex(web3.keccak(text="test-ip-metadata-hash")),
  'nft_metadata_uri': "test-uri",
  'nft_metadata_hash': web3.to_hex(web3.keccak(text="test-nft-metadata-hash"))
}

response = story_client.IPAsset.mintAndRegisterIpAssetWithPilTerms(
  spg_nft_contract="0xfE265a91dBe911db06999019228a678b86C04959",
  terms=[{
    "terms": commercial_remix_terms,
    "licensing_config": licensing_config
  }],
  allow_duplicates=True,
  ip_metadata=metadata
)
```

```python Request Parameters
spg_nft_contract: str  # The address of the NFT collection
terms: list  # The array of license terms to be attached
ip_metadata: dict = None  # Optional: Metadata for the NFT and IP
recipient: str = None  # Optional: The address of the recipient of the minted NFT
allow_duplicates: bool = False  # Optional: Allow minting IPs with the same NFT metadata
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "ipId": str,  # The IP ID of the registered IP
  "tokenId": int,  # The token ID of the minted NFT
  "txHash": str,  # The transaction hash
  "licenseTermsIds": list  # The IDs of the registered license terms
}
```

</CodeGroup>


# IP Account

## IPAccountClient

### Methods

- setIpMetadata
- execute
- executeWithSig
- transferErc20

### setIpMetadata

Sets the metadataURI for an IP asset.

| Method          |
| --------------- |
| `setIpMetadata` |

Parameters:

- `ip_id`: The IP to set the metadata for.
- `metadata_uri`: The metadataURI to set for the IP asset. Should be a URL pointing to metadata that fits the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard).
- `metadata_hash`: The hash of metadata at metadataURI.
- `tx_options`: \[Optional] Transaction options dictionary.

<CodeGroup>

```python Python
tx_hash = story_client.IPAccount.setIpMetadata(
  ip_id="0x01",
  metadata_uri="https://ipfs.io/ipfs/bafkreiardkgvkejqnnkdqp4pamkx2e5bs4lzus5trrw3hgmoa7dlbb6foe",
  # example hash (not accurate)
  metadata_hash="0x129f7dd802200f096221dd89d5b086e4bd3ad6eafb378a0c75e3b04fc375f997",
)
```

```python Request Parameters
ip_id: str  # The IP to set the metadata for
metadata_uri: str  # The metadataURI to set for the IP asset. Should be a URL pointing to metadata that fits the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard)
metadata_hash: str  # The hash of metadata at metadataURI
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str  # The transaction hash
}
```

</CodeGroup>

### execute

Executes a transaction from the IP Account.

| Method    |
| --------- |
| `execute` |

Parameters:

- `ip_id`: The IP Id to get ip account.
- `to`: The recipient of the transaction.
- `value`: The amount of Ether to send.
- `data`: The data to send along with the transaction.
- `tx_options`: \[Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.IPAccount.execute(
  ip_id="0x01",
  to="0x1234567890123456789012345678901234567890",
  value=1000000000000000000,  # 1 ETH
  data="0x1234567890123456789012345678901234567890",
)
```

```python Request Parameters
ip_id: str  # The IP to set the metadata for
to: str  # The recipient of the transaction
value: int  # The amount of Ether to send
data: str  # The data to send along with the transaction
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str  # The transaction hash
}
```

</CodeGroup>

### executeWithSig

Executes a transaction from the IP Account.

| Method           |
| ---------------- |
| `executeWithSig` |

Parameters:

- `ip_id`: The IP to set the metadata for.
- `to`: The recipient of the transaction.
- `data`: The data to send along with the transaction.
- `signer`: The signer of the transaction.
- `deadline`: The deadline of the transaction signature.
- `signature`: The signature of the transaction, EIP-712 encoded.
- `value`: \[Optional] The amount of Ether to send. **Default: 0**
- `tx_options`: \[Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.IPAccount.executeWithSig(
  ip_id="0x01",
  to="0x1234567890123456789012345678901234567890",
  data="0x1234567890123456789012345678901234567890",
  signer="0x1234567890123456789012345678901234567890",
  deadline=1000000000000000000,
  signature="0x1234567890123456789012345678901234567890",
  value=1000000000000000000,  # 1 ETH
)
```

```python Request Parameters
ip_id: str  # The IP to set the metadata for
to: str  # The recipient of the transaction
data: str  # The data to send along with the transaction
signer: str  # The signer of the transaction
deadline: int  # The deadline of the transaction signature
signature: str  # The signature of the transaction, EIP-712 encoded
value: int = 0  # Optional: The amount of Ether to send
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str  # The transaction hash
}
```

</CodeGroup>

### transferErc20

Transfers an ERC20 token from the IP Account.

| Method          |
| --------------- |
| `transferErc20` |

Parameters:

- `ip_id`: The `ipId` of the account
- `tokens`: The token info to transfer
  - `tokens.address`: The address of the ERC20 token including WIP and standard ERC20.
  - `tokens.amount`: The amount of tokens to transfer
  - `tokens.target`: The address of the recipient.
- `tx_options`: \[Optional] Transaction options dictionary.

<CodeGroup>

```python Python
response = story_client.IPAccount.transferERC20(
  ip_id="0x01",
  tokens=[
    {
        "address": "0x1514000000000000000000000000000000000000", # $WIP
        "target": "0x02",
        "amount": 1000000  # Equivalent to 0.001 ether
    }
  ]
)
```

```python Request Parameters
ip_id: str  # The IP to set the metadata for
tokens: list  # The token info to transfer
tx_options: dict = None  # Optional: Transaction options
```

```python Response
{
  "txHash": str, # The transaction hash
}
```

</CodeGroup>


# "SDK Reference Overview"

This section provides a detailed description of every function in our Python SDK.

| Package                                                        | Compatibility                                                 | Package                                                                                                 | GitHub                                                                                                             |                          |
| -------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| <Icon icon="screwdriver-wrench" iconType="solid" /> TypeScript | <Icon icon="check" iconType="solid" /> Full                   | <Icon icon="box-open" iconType="solid" /> [npm](https://www.npmjs.com/package/@story-protocol/core-sdk) | <Icon icon="arrow-up-right-from-square" iconType="solid" /> [Code](https://github.com/storyprotocol/sdk/tree/main) | [SWITCH](/sdk-reference) |
| <Icon icon="python" iconType="solid" /> Python                 | <Icon icon="triangle-exclamation" iconType="solid" /> Partial | <Icon icon="box-open" iconType="solid" /> [PyPi](https://pypi.org/project/story-protocol-python-sdk)    | <Icon icon="arrow-up-right-from-square" iconType="solid" /> [Code](https://github.com/storyprotocol/python-sdk)    |                          |

---

## Licensing Module

<CardGroup cols={2}>

<Card
  title="Register an IP Asset"
  icon="house"
  href="/sdk-reference/python/ipasset"
>
  Learn how to register an IP asset using the Python SDK.
</Card>

<Card
  title="Mint & Attach License Terms"
  icon="house"
  href="/sdk-reference/python/license"
>
  Learn how to mint and attach license terms using the Python SDK.
</Card>

</CardGroup>


# WIP Client

## WipClient

### Methods

- deposit
- withdraw
- approve
- balanceOf
- transfer
- transferFrom

### deposit

Wraps the selected amount of IP to WIP. The WIP will be deposited to the wallet that transferred the IP.

| Method    | Type                        |
| --------- | --------------------------- |
| `deposit` | `(request: DepositRequest)` |

Parameters:

- `request.amount`: The amount to deposit.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Request Type
export type DepositRequest = WithTxOptions & {
  amount: TokenAmountInput;
};
```

### withdraw

Unwraps the selected amount of WIP to IP.

| Method     | Type                         |
| ---------- | ---------------------------- |
| `withdraw` | `(request: WithdrawRequest)` |

Parameters:

- `request.amount`: The amount to withdraw.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Request Type
export type WithdrawRequest = WithTxOptions & {
  amount: TokenAmountInput;
};
```

### approve

Approve a spender to use the wallet's WIP balance.

| Method    | Type                        |
| --------- | --------------------------- |
| `approve` | `(request: ApproveRequest)` |

Parameters:

- `request.amount`: The amount of WIP tokens to approve.
- `request.spender`: The address that will use the WIP tokens
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Request Type
export type ApproveRequest = WithTxOptions & {
  spender: Address;
  amount: TokenAmountInput;
};
```

### balanceOf

Returns the balance of WIP for an address.

| Method      | Type                                 |
| ----------- | ------------------------------------ |
| `balanceOf` | `(addr: Address) => Promise<bigint>` |

Parameters:

- `addr`: The address you want to check the baalnce for.

### transfer

Transfers `amount` of WIP to a recipient `to`.

| Method     | Type                         |
| ---------- | ---------------------------- |
| `transfer` | `(request: TransferRequest)` |

Parameters:

- `request.to`: Who you're transferring to.
- `request.amount`: The amount to transfer.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Request Type
export type TransferRequest = WithTxOptions & {
  to: Address;
  amount: TokenAmountInput;
};
```

### transferFrom

Transfers `amount` of WIP from `from` to a recipient `to`.

| Method         | Type                             |
| -------------- | -------------------------------- |
| `transferFrom` | `(request: TransferFromRequest)` |

Parameters:

- `request.to`: Who you're transferring to.
- `request.amount`: The amount to transfer.
- `request.from`: The address to transfer from.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Request Type
export type TransferFromRequest = WithTxOptions & {
  to: Address;
  amount: TokenAmountInput;
  from: Address;
};
```


# IP Account

## IPAccountClient

### Methods

- setIpMetadata
- execute
- executeWithSig
- transferErc20

### setIpMetadata

Sets the metadataURI for an IP asset.

| Method          | Type                                    |
| --------------- | --------------------------------------- |
| `setIpMetadata` | `(SetIpMetadataRequest) => Promis<Hex>` |

Parameters:

- `request.ipId`: The IP to set the metadata for.
- `request.metadataURI`: The metadataURI to set for the IP asset. Should be a URL pointing to metadata that fits the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard).
- `request.metadataHash`: The hash of metadata at metadataURI.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const txHash = await client.ipAccount.setIpMetadata({
  ipId: "0x01",
  metadataURI:
    "https://ipfs.io/ipfs/bafkreiardkgvkejqnnkdqp4pamkx2e5bs4lzus5trrw3hgmoa7dlbb6foe",
  // example hash (not accurate)
  metadataHash:
    "0x129f7dd802200f096221dd89d5b086e4bd3ad6eafb378a0c75e3b04fc375f997",
});
```

```typescript Request Type
export type SetIpMetadataRequest = {
  ipId: Address;
  metadataURI: string;
  metadataHash: Hex;
  txOptions?: Omit<TxOptions, "encodedTxDataOnly">;
};
```

</CodeGroup>

### execute

Executes a transaction from the IP Account.

| Method    | Type                                                            |
| --------- | --------------------------------------------------------------- |
| `execute` | `(IPAccountExecuteRequest) => Promis<IPAccountExecuteResponse>` |

Parameters:

- `request.ipId`: The Ip Id to get ip account.
- `request.to`: The recipient of the transaction.
- `request.value`: The amount of Ether to send.
- `request.data`: The data to send along with the transaction.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript Request Type
export type IPAccountExecuteRequest = {
  ipId: Address;
  to: Address;
  value: number;
  data: Hex;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type IPAccountExecuteResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### executeWithSig

Executes a transaction from the IP Account.

| Method           | Type                                                            |
| ---------------- | --------------------------------------------------------------- |
| `executeWithSig` | `(IPAccountExecuteRequest) => Promis<IPAccountExecuteResponse>` |

Parameters:

- `request.ipId`: The Ip Id to get ip account.
- `request.to`: The recipient of the transaction.
- `request.data`: The data to send along with the transaction.
- `request.signer`: The signer of the transaction.
- `request.deadline`: The deadline of the transaction signature.
- `request.signature`: The signature of the transaction, EIP-712 encoded.
- `request.value`: \[Optional] The amount of Ether to send.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript Request Type
export type IPAccountExecuteWithSigRequest = {
  ipId: Address;
  to: Address;
  data: Hex;
  signer: Address;
  deadline: number | bigint | string;
  signature: Address;
  value?: number | bigint | string;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type IPAccountExecuteWithSigResponse = {
  txHash?: Hex;
  encodedTxData?: EncodedTxData;
};
```

</CodeGroup>

### transferErc20

Transfers an ERC20 token from the IP Account.

| Method          | Type                                                              |
| --------------- | ----------------------------------------------------------------- |
| `transferErc20` | `(request: TransferErc20Request) => Promise<TransactionResponse>` |

Parameters:

- `request.ipId`: The `ipId` of the account
- `request.tokens`: The token info to transfer
  - `request.tokens.address`: The address of the ERC20 token including WIP and standard ERC20.
  - `request.tokens.amount`: The amount of tokens to transfer
  - `request.tokens.target`: The address of the recipient.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript Request Type
export type TransferErc20Request = {
  ipId: Address;
  tokens: {
    address: Address;
    amount: bigint | number;
    target: Address;
  }[];
  txOptions?: Omit<TxOptions, "encodedTxDataOnly">;
};
```

```typescript Response Type
export type TransactionResponse = {
  txHash: Hex;

  /** Transaction receipt, only available if waitForTransaction is set to true */
  receipt?: TransactionReceipt;
};
```

</CodeGroup>


# Group

## GroupClient

### Methods

- registerGroup
- mintAndRegisterIpAndAttachLicenseAndAddToGroup
- registerIpAndAttachLicenseAndAddToGroup
- registerGroupAndAttachLicense
- registerGroupAndAttachLicenseAndAddIps
- collectAndDistributeGroupRoyalties

### registerGroup

Registers a Group IPA.

| Method          | Type                                                                |
| --------------- | ------------------------------------------------------------------- |
| `registerGroup` | `(request: RegisterGroupRequest) => Promise<RegisterGroupResponse>` |

Parameters:

- `request.groupPool`: The address specifying how royalty will be split amongst the pool of IPs in the group.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type RegisterGroupResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  groupId?: Address;
};
```

### mintAndRegisterIpAndAttachLicenseAndAddToGroup

Mint an NFT from a SPGNFT collection, register it with metadata as an IP, attach license terms to the registered IP, and add it to a group IP.

| Method                                           | Type                                                                                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| `mintAndRegisterIpAndAttachLicenseAndAddToGroup` | `(request: MintAndRegisterIpAndAttachLicenseAndAddToGroupRequest) => Promise<MintAndRegisterIpAndAttachLicenseAndAddToGroupResponse>` |

Parameters:

- `request.nftContract`: The address of the NFT collection.
- `request.groupId`: The ID of the group IP to add the newly registered IP.
- `request.licenseTermsId`: The ID of the registered license terms that will be attached to the new IP.
- `request.recipient`: \[Optional] The address of the recipient of the minted NFT,default value is your wallet address.
- `request.licenseTemplate`: \[Optional] The address of the license template to be attached to the new group IP,default value is Programmable IP License.
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds,default value is 1000ms.
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type MintAndRegisterIpAndAttachLicenseAndAddToGroupResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  ipId?: Address;
  tokenId?: bigint;
};
```

### registerIpAndAttachLicenseAndAddToGroup

Register an NFT as IP with metadata, attach license terms to the registered IP, and add it to a group IP.

| Method                                    | Type                                                                                                                    |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `registerIpAndAttachLicenseAndAddToGroup` | `(request: RegisterIpAndAttachLicenseAndAddToGroupRequest) => Promise<RegisterIpAndAttachLicenseAndAddToGroupResponse>` |

Parameters:

- `request.spgNftContract`: The address of the NFT collection.
- `request.tokenId`: The ID of the NFT.
- `request.groupId`: The ID of the group IP to add the newly registered IP.
- `request.licenseTermsId`: The ID of the registered license terms that will be attached to the new IP.
- `request.licenseTemplate`: \[Optional] The address of the license template to be attached to the new group IP, default value is Programmable IP License.
- `request.deadline`: \[Optional] The deadline for the signature in milliseconds, default is 1000ms.
- `request.ipMetadata`: \[Optional] The desired metadata for the newly minted NFT and newly registered IP.
  - `request.ipMetadata.ipMetadataURI` \[Optional] The URI of the metadata for the IP.
  - `request.ipMetadata.ipMetadataHash` \[Optional] The hash of the metadata for the IP.
  - `request.ipMetadata.nftMetadataURI` \[Optional] The URI of the metadata for the NFT.
  - `request.ipMetadata.nftMetadataHash` \[Optional] The hash of the metadata for the IP NFT.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type RegisterIpAndAttachLicenseAndAddToGroupResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  ipId?: Address;
  tokenId?: bigint;
};
```

### registerGroupAndAttachLicense

Register a group IP with a group reward pool and attach license terms to the group IP.

| Method                          | Type                                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------------------- |
| `registerGroupAndAttachLicense` | `(request: RegisterGroupAndAttachLicenseRequest) => Promise<RegisterGroupAndAttachLicenseResponse>` |

Parameters:

- `request.groupPool`: The address specifying how royalty will be split amongst the pool of IPs in the group.
- `request.licenseTermsId`: The ID of the registered license terms that will be attached to the new group IP.
- `request.licenseTemplate`: \[Optional] The address of the license template to be attached to the new group IP, default value is Programmable IP License.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type RegisterGroupAndAttachLicenseResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  groupId?: Address;
};
```

### registerGroupAndAttachLicenseAndAddIps

Register a group IP with a group reward pool, attach license terms to the group IP, and add individual IPs to the group IP.

| Method                                   | Type                                                                                                                  |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `registerGroupAndAttachLicenseAndAddIps` | `(request: RegisterGroupAndAttachLicenseAndAddIpsRequest) => Promise<RegisterGroupAndAttachLicenseAndAddIpsResponse>` |

Parameters:

- `request.ipIds`: The IP IDs of the IPs to be added to the group.
- `request.groupPool`: The address specifying how royalty will be split amongst the pool of IPs in the group.
- `request.maxAllowedRevShare`: The maximum reward share percentage that can be allocated to each member IP.
- `request.licenseData`: The data of the license and its configuration to be attached to the new group IP.
  - `request.licenseData.licenseTermsId`: The ID of the registered license terms that will be attached to the new group IP.
  - `request.licenseData.licensingConfig`: \[Optional] See the [LicensingConfig type](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/common.ts#L15). If none provided, it will default to the one shown [here](https://github.com/storyprotocol/sdk/blob/dev/packages/core-sdk/src/utils/validateLicenseConfig.ts).
  - `request.licenseData.licenseTemplate`: \[Optional] The address of the license template to be attached to the new group IP, default value is Programmable IP License.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
const response =
  await client.groupClient.registerGroupAndAttachLicenseAndAddIps({
    groupPool: "0xf96f2c30b41Cb6e0290de43C8528ae83d4f33F89", // EvenSplitGroupPool from https://docs.story.foundation/docs/deployed-smart-contracts
    maxAllowedRewardShare: 5,
    ipIds: ["0x01"],
    licenseData: {
      licenseTermsId: "5",
    },
    txOptions: { waitForTransaction: true },
  });
```

```typescript Request Type
export type RegisterGroupAndAttachLicenseAndAddIpsRequest = {
  groupPool: Address;
  ipIds: Address[];
  licenseData: LicenseData;
  maxAllowedRewardShare: number | string;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type RegisterGroupAndAttachLicenseAndAddIpsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  groupId?: Address;
};
```

</CodeGroup>

### collectAndDistributeGroupRoyalties

Collect royalties for the entire group and distribute the rewards to each member IP's royalty vault.

| Method                               | Type                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `collectAndDistributeGroupRoyalties` | `(request: CollectAndDistributeGroupRoyaltiesRequest) => Promise<CollectAndDistributeGroupRoyaltiesResponse>` |

Parameters:

- `request.groupIpId`: The IP ID of the group.
- `request.currencyTokens`: The addresses of the currency (revenue) tokens to claim.
- `request.memberIpIds`: The IDs of the member IPs to distribute the rewards to.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";

const response = await client.groupClient.collectAndDistributeGroupRoyalties({
  groupIpId: "0x01",
  currencyTokens: [WIP_TOKEN_ADDRESS],
  memberIpIds: ["0x02"],
  txOptions: { waitForTransaction: true },
});
```

```typescript Request Type
export type CollectAndDistributeGroupRoyaltiesRequest = {
  groupIpId: Address;
  currencyTokens: Address[];
  memberIpIds: Address[];
  txOptions?: Omit<TxOptions, "encodedTxDataOnly">;
};
```

```typescript Response Type
export type CollectAndDistributeGroupRoyaltiesResponse = {
  txHash: Hash;
  receipts?: TransactionReceipt[];
  collectedRoyalties?: Omit<
    GroupingModuleCollectedRoyaltiesToGroupPoolEvent,
    "pool"
  >[];
  royaltiesDistributed?: {
    ipId: Address;
    amount: bigint;
    token: Address;
    /**
     * Amount after the fee to the royalty module treasury.
     */
    amountAfterFee: bigint;
  }[];
};
```

</CodeGroup>


# NFT Client

## NftClient

### Methods

- createNFTCollection

### createNFTCollection

Creates a new SPG NFT Collection.

| Method                | Type                                                                            |
| --------------------- | ------------------------------------------------------------------------------- |
| `createNFTCollection` | `(request: CreateNFTCollectionRequest) => Promise<CreateNFTCollectionResponse>` |

Parameters:

- `request.name`: The name of the collection.
- `request.symbol`: The symbol of the collection.
- `request.isPublicMinting`: If true, anyone can mint from the collection. If false, only the addresses with the minter role can mint.
- `request.mintOpen`: Whether the collection is open for minting on creation.
- `request.mintFeeRecipient`: The address to receive mint fees.
- `request.contractURI`: The contract URI for the collection. Follows ERC-7572 standard. See [here](https://eips.ethereum.org/EIPS/eip-7572).
- `request.baseURI`: \[Optional] The base URI for the collection. If baseURI is not empty, tokenURI will be either baseURI + token ID (if nftMetadataURI is empty) or baseURI + nftMetadataURI.
- `request.maxSupply`: \[Optional] The maximum supply of the collection.
- `request.mintFee`: \[Optional] The cost to mint a token.
- `request.mintFeeToken`: \[Optional] The token to mint.
- `request.owner`: \[Optional] The owner of the collection.
- `request.txOptions`: \[Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

<CodeGroup>

```typescript TypeScript
import { zeroAddress } from "viem";

// Create a new SPG NFT collection
//
// NOTE: Use this code to create a new SPG NFT collection. You can then use the
// `newCollection.spgNftContract` address as the `spgNftContract` argument in
// functions like `mintAndRegisterIpAssetWithPilTerms` in the
// `simpleMintAndRegisterSpg.ts` file.
//
// You will mostly only have to do this once. Once you get your nft contract address,
// you can use it in SPG functions.
//
const newCollection = await client.nftClient.createNFTCollection({
  name: "Test NFT",
  symbol: "TEST",
  isPublicMinting: true,
  mintOpen: true,
  mintFeeRecipient: zeroAddress,
  contractURI: "",
  txOptions: { waitForTransaction: true },
});

console.log(
  `New SPG NFT collection created at transaction hash ${newCollection.txHash}`
);
console.log(`NFT contract address: ${newCollection.spgNftContract}`);
```

```typescript Request Type
export type CreateNFTCollectionRequest = {
  name: string;
  symbol: string;
  isPublicMinting: boolean;
  mintOpen: boolean;
  mintFeeRecipient: Address;
  contractURI: string;
  baseURI?: string;
  maxSupply?: number;
  mintFee?: bigint;
  mintFeeToken?: Hex;
  owner?: Hex;
  txOptions?: TxOptions;
};
```

```typescript Response Type
export type CreateNFTCollectionResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  spgNftContract?: Address; // the address of the newly created contract
};
```

</CodeGroup>


# "SDK Reference Overview"

This section provides a detailed description of every function in our TypeScript SDK.

| Package                                                        | Compatibility                                                 | Package                                                                                                 | GitHub                                                                                                             |                                 |
| -------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| <Icon icon="screwdriver-wrench" iconType="solid" /> TypeScript | <Icon icon="check" iconType="solid" /> Full                   | <Icon icon="box-open" iconType="solid" /> [npm](https://www.npmjs.com/package/@story-protocol/core-sdk) | <Icon icon="arrow-up-right-from-square" iconType="solid" /> [Code](https://github.com/storyprotocol/sdk/tree/main) |
| <Icon icon="python" iconType="solid" /> Python                 | <Icon icon="triangle-exclamation" iconType="solid" /> Partial | <Icon icon="box-open" iconType="solid" /> [PyPi](https://pypi.org/project/story-protocol-python-sdk)    | <Icon icon="arrow-up-right-from-square" iconType="solid" /> [Code](https://github.com/storyprotocol/python-sdk)    | [SWITCH](/sdk-reference/python) |

---

<Card title="Step-by-Step Guide" icon="house" href="/developers/typescript-sdk">
  Learn our SDK through a series of tutorials with the TypeScript SDK Guide.
</Card>

## Licensing Module

<CardGroup cols={2}>

<Card title="Register an IP Asset" icon="house" href="/sdk-reference/ipasset">
  Learn how to register an IP asset using the SDK.
</Card>

<Card
  title="Mint & Attach License Terms"
  icon="house"
  href="/sdk-reference/license"
>
  Learn how to mint and attach license terms using the SDK.
</Card>

</CardGroup>

## Royalty Module

<CardGroup cols={2}>

<Card title="Pay & Claim Royalty" icon="house" href="/sdk-reference/royalty">
  Learn how to pay and claim royalty using the SDK.
</Card>

</CardGroup>

## Dispute Module

<CardGroup cols={2}>

<Card title="Raise a Dispute" icon="house" href="/sdk-reference/dispute">
  Learn how to raise a dispute using the SDK.
</Card>

</CardGroup>

## Grouping Module

<CardGroup cols={2}>

<Card title="Manage Groups" icon="house" href="/sdk-reference/group">
  Learn how to manage groups using the SDK.
</Card>

</CardGroup>

## Utility Clients

Additional utility and extra clients:

<CardGroup cols={2}>

<Card title="Set Permissions" icon="house" href="/sdk-reference/permissions">
  Learn how to set permissions using the SDK.
</Card>

<Card title="NFT Client" icon="house" href="/sdk-reference/nftclient">
  Learn how to interact with NFTs using the SDK.
</Card>

<Card title="WIP Client" icon="house" href="/sdk-reference/wip-client">
  Learn how to use the WIP client using the SDK.
</Card>

</CardGroup>


# Permissions

## PermissionClient

### Methods

- setPermission
- createSetPermissionSignature
- setAllPermissions
- setBatchPermissions
- createBatchPermissionSignature

### setPermission

Sets the permission for a specific function call.

Each policy is represented as a mapping from an IP account address to a signer address to a recipient\
address to a function selector to a permission level. The permission level can be 0 (ABSTAIN), 1 (ALLOW), or\
2 (DENY).

By default, all policies are set to 0 (ABSTAIN), which means that the permission is not set. The owner of IP Account by default has all permission.

| Method          | Type                                                                  |
| --------------- | --------------------------------------------------------------------- |
| `setPermission` | `(request: SetPermissionsRequest) => Promise<SetPermissionsResponse>` |

Parameters:

- `request.ipId`: The IP ID that grants the permission for `signer`.
- `request.signer`: The address that can call `to` on behalf of the `ipAccount`.
- `request.to`: The address that can be called by the `signer` (currently only modules can be `to`)
- `request.permission`: The new permission level.
- `request.func`: [Optional] The function selector string of `to` that can be called by the `signer` on behalf of the `ipAccount`. By default, it allows all functions.
- `request.txOptions`: [Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type SetPermissionsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```

### createSetPermissionSignature

Specific permission overrides wildcard permission with signature.

| Method                         | Type                                                                                |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `createSetPermissionSignature` | `(request: CreateSetPermissionSignatureRequest) => Promise<SetPermissionsResponse>` |

Parameters:

- `request.ipId`: The IP ID that grants the permission for `signer`.
- `request.signer`: The address that can call `to` on behalf of the `ipAccount`.
- `request.to`: The address that can be called by the `signer` (currently only modules can be `to`)
- `request.permission`: The new permission level.
- `request.func`: [Optional] The function selector string of `to` that can be called by the `signer` on behalf of the `ipAccount`. By default, it allows all functions.
- `request.deadline`: [Optional] The deadline for the signature in milliseconds, default is 1000ms.
- `request.txOptions`: [Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type SetPermissionsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```

### setAllPermissions

Sets permission to a signer for all functions across all modules.

| Method              | Type                                                                     |
| ------------------- | ------------------------------------------------------------------------ |
| `setAllPermissions` | `(request: SetAllPermissionsRequest) => Promise<SetPermissionsResponse>` |

Parameters:

- `request.ipId`: The IP ID that grants the permission for `signer`.
- `request.signer`: The address of the signer receiving the permissions.
- `request.permission`: The new permission.
- `request.txOptions`: [Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type SetPermissionsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```

### setBatchPermissions

Sets a batch of permissions in a single transaction.

| Method                | Type                                                                       |
| --------------------- | -------------------------------------------------------------------------- |
| `setBatchPermissions` | `(request: SetBatchPermissionsRequest) => Promise<SetPermissionsResponse>` |

Parameters:

- `request.permissions[]`: An array of `Permission` structure, each representing the permission to be set.
  - `request.permissions[].ipId`: The IP ID that grants the permission for `signer`.
  - `request.permissions[].signer`: The address that can call `to` on behalf of the `ipAccount`.
  - `request.permissions[].to`: The address that can be called by the `signer` (currently only modules can be `to`)
  - `request.permissions[].permission`: The new permission level.
  - `request.permissions[].func`: [Optional] The function selector string of `to` that can be called by the `signer` on behalf of the `ipAccount`. By default, it allows all functions.
- `request.deadline`: [Optional] The deadline for the signature in milliseconds, default is 1000ms.
- `request.txOptions`: [Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type SetPermissionsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```

### createBatchPermissionSignature

Sets a batch of permissions in a single transaction with signature.

| Method                           | Type                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `createBatchPermissionSignature` | `(request: CreateBatchPermissionSignatureRequest) => Promise<SetPermissionsResponse>` |

Parameters:

- `request.ipId`: The IP ID that grants the permission for `signer`
- `request.permissions[]` - An array of `Permission` structure, each representing the permission to be set.
  - `request.permissions[].ipId`: The IP ID that grants the permission for `signer`.
  - `request.permissions[].signer`: The address that can call `to` on behalf of the `ipAccount`.
  - `request.permissions[].to`: The address that can be called by the `signer` (currently only modules can be `to`)
  - `request.permissions[].permission`: The new permission level.
  - `request.permissions[].func`: [Optional] The function selector string of `to` that can be called by the `signer` on behalf of the `ipAccount`. By default, it allows all functions.
- `request.txOptions`: [Optional] The transaction [options](https://github.com/storyprotocol/sdk/blob/main/packages/core-sdk/src/types/options.ts).

```typescript Response Type
export type SetPermissionsResponse = {
  txHash?: string;
  encodedTxData?: EncodedTxData;
  success?: boolean;
};
```


# Governance

As the steward of the Story ecosystem, the Story Foundation works in close alignment with $IP Tokenholders and the broader ecosystem. The Story Foundation supports the Story DAO by providing operational support, executing tokenholder governance decisions, and overseeing strategic development and growth of the overall ecosystem. This relationship is designed to empower decentralized governance while preserving efficiency and stability throughout the Story ecosystem.

## Story DAO's Constitution

<CardGroup cols={1}>
  <Card
    title="Story DAO Constitution"
    href="https://story.foundation/constitution.pdf"
    icon="scroll"
    color="#ccb092"
  >
    Read the entire Story DAO constitution.
  </Card>
</CardGroup>

## Story Foundation’s Role in Governance

<Accordion title="Strategic Grants" icon="money-check-dollar">
  Provide **strategic grants** to align with innovation via partner projects
  including, but not limited to, infrastructure providers, application
  developers, artists, creators, brand partnerships, creative studios, and
  strategic growth partners.
</Accordion>

<Accordion title="Network Security" icon="file-shield">
  **Promote network security** by creating a security council and appointing
  members to serve on this council.
</Accordion>

<Accordion title="Implement Proposals" icon="scroll">
  Developing the ecosystem and protocol by **implementing proposals** of the
  Story DAO that are approved in accordance with the process outlined in the
  Story DAO Constitution and engaging parties to build apps. This may include
  funding research, public education, and establishing grant programs.
</Accordion>

<Accordion title="Educational Initiatives / Events" icon="book">
  Organizing **educational initiatives and hosting events** to increase
  awareness of and promote the Story Network, Story Protocol and ecosystem.
</Accordion>

<Accordion title="Decentralization" icon="globe">
  Advocating for and **supporting increased autonomy and decentralization** of
  the Story DAO.
</Accordion>

<Accordion title="Treasury Management" icon="piggy-bank">
  **Treasury management** and oversight to foster long-term ecosystem growth and
  support the Foundation’s ongoing mission.
</Accordion>


# Using an Example

<CardGroup cols={2}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/src/Example.sol"
    icon="thumbs-up"
    
  >
    See the completed code.
  </Card>

  <Card
    title="Video Walkthrough"
    href="https://www.youtube.com/watch?v=X421IuZENqM"
    icon="video"
    
  >
    Check out a video walkthrough of this tutorial!
  </Card>
</CardGroup>

# Writing the Smart Contract

Now that we have walked through each of the individual steps, let's try to write, deploy, and verify our own smart contract.

## Register IPA, Register License Terms, and Attach to IPA

In this first section, we will combine a few of the tutorials into one. We will create a function named `mintAndRegisterAndCreateTermsAndAttach` that allows you to mint & register a new IP Asset, register new License Terms, and attach those terms to an IP Asset. It will also accept a `receiver` field to be the owner of the new IP Asset.

### Prerequisites

- Complete [Register an IP Asset](/developers/smart-contracts-guide/register-ip-asset)
- Complete [Register License Terms](/developers/smart-contracts-guide/register-terms)
- Complete [Attach Terms to an IPA](/developers/smart-contracts-guide/attach-terms)

### Writing our Contract

Create a new file under `./src/Example.sol` and paste the following:

<Note>
**Contract Addresses**

In order to get the contract addresses to pass in the constructor, go to [Deployed Smart Contracts](/developers/deployed-smart-contracts).

</Note>

```solidity src/Example.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";
import { ILicensingModule } from "@storyprotocol/core/interfaces/modules/licensing/ILicensingModule.sol";
import { IPILicenseTemplate } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";
import { PILFlavors } from "@storyprotocol/core/lib/PILFlavors.sol";

import { SimpleNFT } from "./mocks/SimpleNFT.sol";

import { ERC721Holder } from "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";

/// @notice An example contract that demonstrates how to mint an NFT, register it as an IP Asset,
/// attach license terms to it, mint a license token from it, and register it as a derivative of the parent.
contract Example is ERC721Holder {
  IIPAssetRegistry public immutable IP_ASSET_REGISTRY;
  ILicensingModule public immutable LICENSING_MODULE;
  IPILicenseTemplate public immutable PIL_TEMPLATE;
  address public immutable ROYALTY_POLICY_LAP;
  address public immutable WIP;
  SimpleNFT public immutable SIMPLE_NFT;

  constructor(
    address ipAssetRegistry,
    address licensingModule,
    address pilTemplate,
    address royaltyPolicyLAP,
    address wip
  ) {
    IP_ASSET_REGISTRY = IIPAssetRegistry(ipAssetRegistry);
    LICENSING_MODULE = ILicensingModule(licensingModule);
    PIL_TEMPLATE = IPILicenseTemplate(pilTemplate);
    ROYALTY_POLICY_LAP = royaltyPolicyLAP;
    WIP = wip;
    // Create a new Simple NFT collection
    SIMPLE_NFT = new SimpleNFT("Simple IP NFT", "SIM");
  }

  /// @notice Mint an NFT, register it as an IP Asset, and attach License Terms to it.
  /// @param receiver The address that will receive the NFT/IPA.
  /// @return tokenId The token ID of the NFT representing ownership of the IPA.
  /// @return ipId The address of the IP Account.
  /// @return licenseTermsId The ID of the license terms.
  function mintAndRegisterAndCreateTermsAndAttach(
    address receiver
  ) external returns (uint256 tokenId, address ipId, uint256 licenseTermsId) {
    // We mint to this contract so that it has permissions
    // to attach license terms to the IP Asset.
    // We will later transfer it to the intended `receiver`
    tokenId = SIMPLE_NFT.mint(address(this));
    ipId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), tokenId);

    // register license terms so we can attach them later
    licenseTermsId = PIL_TEMPLATE.registerLicenseTerms(
      PILFlavors.commercialRemix({
        mintingFee: 0,
        commercialRevShare: 10 * 10 ** 6, // 10%
        royaltyPolicy: ROYALTY_POLICY_LAP,
        currencyToken: WIP
      })
    );

    // attach the license terms to the IP Asset
    LICENSING_MODULE.attachLicenseTerms(ipId, address(PIL_TEMPLATE), licenseTermsId);

    // transfer the NFT to the receiver so it owns the IPA
    SIMPLE_NFT.transferFrom(address(this), receiver, tokenId);
  }
}
```

## Mint a License Token and Register as Derivative

In this next section, we will combine a few of the later tutorials into one. We will create a function named `mintLicenseTokenAndRegisterDerivative` that allows a potentially different user to register their own "child" (derivative) IP Asset, mint a License Token from the "parent" (root) IP Asset, and register their child IPA as a derivative of the parent IPA. It will accept a few parameters:

1. `parentIpId`: the `ipId` of the parent IPA
2. `licenseTermsId`: the id of the License Terms you want to mint a License Token for
3. `receiver`: the owner of the child IPA

### Prerequisites

- Complete [Mint a License Token](/developers/smart-contracts-guide/mint-license)
- Complete [Register a Derivative](/developers/smart-contracts-guide/register-derivative)

### Writing our Contract

In your `Example.sol` contract, add the following function at the bottom:

```solidity src/Example.sol
/// @notice Mint and register a new child IPA, mint a License Token
/// from the parent, and register it as a derivative of the parent.
/// @param parentIpId The ipId of the parent IPA.
/// @param licenseTermsId The ID of the license terms you will
/// mint a license token from.
/// @param receiver The address that will receive the NFT/IPA.
/// @return childTokenId The token ID of the NFT representing ownership of the child IPA.
/// @return childIpId The address of the child IPA.
function mintLicenseTokenAndRegisterDerivative(
  address parentIpId,
  uint256 licenseTermsId,
  address receiver
) external returns (uint256 childTokenId, address childIpId) {
  // We mint to this contract so that it has permissions
  // to register itself as a derivative of another
  // IP Asset.
  // We will later transfer it to the intended `receiver`
  childTokenId = SIMPLE_NFT.mint(address(this));
  childIpId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), childTokenId);

  // mint a license token from the parent
  uint256 licenseTokenId = LICENSING_MODULE.mintLicenseTokens({
    licensorIpId: parentIpId,
    licenseTemplate: address(PIL_TEMPLATE),
    licenseTermsId: licenseTermsId,
    amount: 1,
    // mint the license token to this contract so it can
    // use it to register as a derivative of the parent
    receiver: address(this),
    royaltyContext: "", // for PIL, royaltyContext is empty string
    maxMintingFee: 0,
    maxRevenueShare: 0
  });

  uint256[] memory licenseTokenIds = new uint256[](1);
  licenseTokenIds[0] = licenseTokenId;

  // register the new child IPA as a derivative
  // of the parent
  LICENSING_MODULE.registerDerivativeWithLicenseTokens({
    childIpId: childIpId,
    licenseTokenIds: licenseTokenIds,
    royaltyContext: "", // empty for PIL
    maxRts: 0
  });

  // transfer the NFT to the receiver so it owns the child IPA
  SIMPLE_NFT.transferFrom(address(this), receiver, childTokenId);
}
```

# Testing our Contract

Create another new file under `test/Example.t.sol` and paste the following:

```solidity test/Example.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
// for testing purposes only
import { MockIPGraph } from "@storyprotocol/test/mocks/MockIPGraph.sol";
import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";
import { ILicenseRegistry } from "@storyprotocol/core/interfaces/registries/ILicenseRegistry.sol";

import { Example } from "../src/Example.sol";
import { SimpleNFT } from "../src/mocks/SimpleNFT.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/Example.t.sol
contract ExampleTest is Test {
  address internal alice = address(0xa11ce);
  address internal bob = address(0xb0b);

  // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
  // Protocol Core - IPAssetRegistry
  address internal ipAssetRegistry = 0x77319B4031e6eF1250907aa00018B8B1c67a244b;
  // Protocol Core - LicenseRegistry
  address internal licenseRegistry = 0x529a750E02d8E2f15649c13D69a465286a780e24;
  // Protocol Core - LicensingModule
  address internal licensingModule = 0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f;
  // Protocol Core - PILicenseTemplate
  address internal pilTemplate = 0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316;
  // Protocol Core - RoyaltyPolicyLAP
  address internal royaltyPolicyLAP = 0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E;
  // Revenue Token - WIP
  address internal wip = 0x1514000000000000000000000000000000000000;

  SimpleNFT public SIMPLE_NFT;
  Example public EXAMPLE;

  function setUp() public {
    // this is only for testing purposes
    // due to our IPGraph precompile not being
    // deployed on the fork
    vm.etch(address(0x0101), address(new MockIPGraph()).code);

    EXAMPLE = new Example(ipAssetRegistry, licensingModule, pilTemplate, royaltyPolicyLAP, wip);
    SIMPLE_NFT = SimpleNFT(EXAMPLE.SIMPLE_NFT());
  }

  function test_mintAndRegisterAndCreateTermsAndAttach() public {
    ILicenseRegistry LICENSE_REGISTRY = ILicenseRegistry(licenseRegistry);
    IIPAssetRegistry IP_ASSET_REGISTRY = IIPAssetRegistry(ipAssetRegistry);

    uint256 expectedTokenId = SIMPLE_NFT.nextTokenId();
    address expectedIpId = IP_ASSET_REGISTRY.ipId(block.chainid, address(SIMPLE_NFT), expectedTokenId);

    (uint256 tokenId, address ipId, uint256 licenseTermsId) = EXAMPLE.mintAndRegisterAndCreateTermsAndAttach(alice);

    assertEq(tokenId, expectedTokenId);
    assertEq(ipId, expectedIpId);
    assertEq(SIMPLE_NFT.ownerOf(tokenId), alice);

    assertTrue(LICENSE_REGISTRY.hasIpAttachedLicenseTerms(ipId, pilTemplate, licenseTermsId));
    assertEq(LICENSE_REGISTRY.getAttachedLicenseTermsCount(ipId), 1);
    (address licenseTemplate, uint256 attachedLicenseTermsId) = LICENSE_REGISTRY.getAttachedLicenseTerms({
      ipId: ipId,
      index: 0
    });
    assertEq(licenseTemplate, pilTemplate);
    assertEq(attachedLicenseTermsId, licenseTermsId);
  }

  function test_mintLicenseTokenAndRegisterDerivative() public {
    ILicenseRegistry LICENSE_REGISTRY = ILicenseRegistry(licenseRegistry);
    IIPAssetRegistry IP_ASSET_REGISTRY = IIPAssetRegistry(ipAssetRegistry);

    (uint256 parentTokenId, address parentIpId, uint256 licenseTermsId) = EXAMPLE
    .mintAndRegisterAndCreateTermsAndAttach(alice);

    (uint256 childTokenId, address childIpId) = EXAMPLE.mintLicenseTokenAndRegisterDerivative(
      parentIpId,
      licenseTermsId,
      bob
    );

    assertTrue(LICENSE_REGISTRY.hasDerivativeIps(parentIpId));
    assertTrue(LICENSE_REGISTRY.isParentIp(parentIpId, childIpId));
    assertTrue(LICENSE_REGISTRY.isDerivativeIp(childIpId));
    assertEq(LICENSE_REGISTRY.getDerivativeIpCount(parentIpId), 1);
    assertEq(LICENSE_REGISTRY.getParentIpCount(childIpId), 1);
    assertEq(LICENSE_REGISTRY.getParentIp({ childIpId: childIpId, index: 0 }), parentIpId);
    assertEq(LICENSE_REGISTRY.getDerivativeIp({ parentIpId: parentIpId, index: 0 }), childIpId);
  }
}
```

Run `forge build`. If everything is successful, the command should successfully compile.

To test this out, simply run the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/Example.t.sol
```

# Deploy & Verify the Example Contract

The `--constructor-args` come from [Deployed Smart Contracts](/developers/deployed-smart-contracts).

```bash
forge create \
  --rpc-url https://aeneid.storyrpc.io/ \
  --private-key $PRIVATE_KEY \
  ./src/Example.sol:Example \
  --verify \
  --verifier blockscout \
  --verifier-url https://aeneid.storyscan.io/api/ \
  --constructor-args 0x77319B4031e6eF1250907aa00018B8B1c67a244b 0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f 0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316 0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E 0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E
```

If everything worked correctly, you should see something like `Deployed to: 0xfb0923D531C1ca54AB9ee10CB8364b23d0C7F47d` in the console. Paste that address into [the explorer](https://aeneid.storyscan.io/) and see your verified contract!

# Great job! :)

<CardGroup cols={2}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/src/Example.sol"
    icon="thumbs-up"
    
  >
    See the completed code.
  </Card>

  <Card
    title="Video Walkthrough"
    href="https://www.youtube.com/watch?v=X421IuZENqM"
    icon="video"
    
  >
    Check out a video walkthrough of this tutorial!
  </Card>
</CardGroup>


# Mint a License Token

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/3_LicenseToken.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

This section demonstrates how to mint a [License Token](/concepts/licensing-module/license-token) from an [IP Asset](/concepts/ip-asset/overview). You can only mint a License Token from an IP Asset if the IP Asset has [License Terms](/concepts/licensing-module/license-terms) attached to it. A License Token is minted as an ERC-721.

There are two reasons you'd mint a License Token:

1. To hold the license and be able to use the underlying IP Asset as the license described (for ex. "Can use commercially as long as you provide proper attribution and share 5% of your revenue)
2. Use the license token to link another IP Asset as a derivative of it. _Note though that, as you'll see later, some SDK functions don't require you to explicitly mint a license token first in order to register a derivative, and will actually handle it for you behind the scenes._

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)
2. An IP Asset has License Terms attached to it. You can learn how to do that [here](/developers/smart-contracts-guide/attach-terms)

## Mint License

Let's say that IP Asset (`ipId = 0x01`) has License Terms (`licenseTermdId = 10`) attached to it. We want to mint 2 License Tokens with those terms to a specific wallet address (`0x02`).

<Warning>
**Paid Licenses**

Be mindful that some IP Assets may have license terms attached that require the user minting the license to pay a `mintingFee`.

</Warning>

Let's create a test file under `test/3_LicenseToken.t.sol` to see it work and verify the results:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

</Note>

```solidity test/3_LicenseToken.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
// for testing purposes only
import { MockIPGraph } from "@storyprotocol/test/mocks/MockIPGraph.sol";
import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";
import { IPILicenseTemplate } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";
import { ILicensingModule } from "@storyprotocol/core/interfaces/modules/licensing/ILicensingModule.sol";
import { ILicenseToken } from "@storyprotocol/core/interfaces/ILicenseToken.sol";
import { RoyaltyPolicyLAP } from "@storyprotocol/core/modules/royalty/policies/LAP/RoyaltyPolicyLAP.sol";
import { PILFlavors } from "@storyprotocol/core/lib/PILFlavors.sol";
import { PILTerms } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";

import { SimpleNFT } from "../src/mocks/SimpleNFT.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/3_LicenseToken.t.sol
contract LicenseTokenTest is Test {
    address internal alice = address(0xa11ce);
    address internal bob = address(0xb0b);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - IPAssetRegistry
    IIPAssetRegistry internal IP_ASSET_REGISTRY = IIPAssetRegistry(0x77319B4031e6eF1250907aa00018B8B1c67a244b);
    // Protocol Core - LicensingModule
    ILicensingModule internal LICENSING_MODULE = ILicensingModule(0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f);
    // Protocol Core - PILicenseTemplate
    IPILicenseTemplate internal PIL_TEMPLATE = IPILicenseTemplate(0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316);
    // Protocol Core - RoyaltyPolicyLAP
    address internal ROYALTY_POLICY_LAP = 0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E;
    // Protocol Core - LicenseToken
    ILicenseToken internal LICENSE_TOKEN = ILicenseToken(0xFe3838BFb30B34170F00030B52eA4893d8aAC6bC);
    // Revenue Token - MERC20
    address internal MERC20 = 0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E;

    SimpleNFT public SIMPLE_NFT;
    uint256 public tokenId;
    address public ipId;
    uint256 public licenseTermsId;

    function setUp() public {
        // this is only for testing purposes
        // due to our IPGraph precompile not being
        // deployed on the fork
        vm.etch(address(0x0101), address(new MockIPGraph()).code);

        SIMPLE_NFT = new SimpleNFT("Simple IP NFT", "SIM");
        tokenId = SIMPLE_NFT.mint(alice);
        ipId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), tokenId);

        licenseTermsId = PIL_TEMPLATE.registerLicenseTerms(
            PILFlavors.commercialRemix({
                mintingFee: 0,
                commercialRevShare: 10 * 10 ** 6, // 10%
                royaltyPolicy: ROYALTY_POLICY_LAP,
                currencyToken: MERC20
            })
        );

        vm.prank(alice);
        LICENSING_MODULE.attachLicenseTerms(ipId, address(PIL_TEMPLATE), licenseTermsId);
    }

    /// @notice Mints license tokens for an IP Asset.
    /// Anyone can mint a license token.
    function test_mintLicenseToken() public {
        uint256 startLicenseTokenId = LICENSING_MODULE.mintLicenseTokens({
            licensorIpId: ipId,
            licenseTemplate: address(PIL_TEMPLATE),
            licenseTermsId: licenseTermsId,
            amount: 2,
            receiver: bob,
            royaltyContext: "", // for PIL, royaltyContext is empty string
            maxMintingFee: 0,
            maxRevenueShare: 0
        });

        assertEq(LICENSE_TOKEN.ownerOf(startLicenseTokenId), bob);
        assertEq(LICENSE_TOKEN.ownerOf(startLicenseTokenId + 1), bob);
    }
}
```

## Test Your Code!

Run `forge build`. If everything is successful, the command should successfully compile.

Now run the test by executing the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/3_LicenseToken.t.sol
```

## Register a Derivative

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/3_LicenseToken.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

Now that we have minted a License Token, we can hold it or use it to link an IP Asset as a derivative. We will go over that on the next page.


# Pay & Claim Revenue

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/5_Royalty.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

This section demonstrates how to pay an IP Asset. There are a few reasons you would do this:

1. You simply want to "tip" an IP
2. You have to because your license terms with an ancestor IP require you to forward a certain % of payment

In either scenario, you would use the below `payRoyaltyOnBehalf` function. When this happens, the [Royalty Module](/concepts/royalty-module/overview) automatically handles the different payment flows such that parent IP Assets who have negotiated a certain `commercialRevShare` with the IPA being paid can claim their due share.

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)
2. Have a basic understanding of the [Royalty Module](/concepts/royalty-module/overview)
3. A child IPA and a parent IPA, for which their license terms have a commercial revenue share to make this example work

## Before We Start

You can pay an IP Asset using the `payRoyaltyOnBehalf` function from the [Royalty Module](/concepts/royalty-module/overview).

You will be paying the IP Asset with [MockERC20](https://aeneid.storyscan.io/address/0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E). Usually you would pay with $WIP, but because we need to mint some tokens to test, we will use MockERC20.

To help with the following scenarios, let's say we have a parent IP Asset that has negotiated a 50% `commercialRevShare` with its child IP Asset.

### Whitelisted Revenue Tokens

Only tokens that are whitelisted by our protocol can be used as payment ("revenue") tokens. MockERC20 is one of those tokens. To see that list, go [here](/developers/deployed-smart-contracts#whitelisted-revenue-tokens).

## Paying an IP Asset

We can pay an IP Asset like so:

```solidity Solidity
ROYALTY_MODULE.payRoyaltyOnBehalf(childIpId, address(0), address(MERC20), 10);
```

This will send 10 $MERC20 to the `childIpId`'s [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault). From there, the child can claim revenue. In the next section, you'll see a working version of this.

<Warning>
**Important: Approving the Royalty Module**

Before you call `payRoyaltyOnBehalf`, you have to approve the royalty module to spend the tokens for you. In the section below, you will see that we call `MERC20.approve(address(ROYALTY_MODULE), 10);` or else it will not work.

</Warning>

## Claim Revenue

When payments are made, they eventually end up in an IP Asset's [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault). From here, they are claimed/transferred to whoever owns the Royalty Tokens associated with it, which represent a % of revenue share for a given IP Asset's IP Royalty Vault.

The IP Account (the smart contract that represents the [IP Asset](/concepts/ip-asset/overview)) is what holds 100% of the Royalty Tokens when it's first registered. So usually, it indeed holds most of the Royalty Tokens.

Let's create a test file under `test/5_Royalty.t.sol` to see it work and verify the results:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

</Note>

```solidity test/5_Royalty.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
// for testing purposes only
import { MockIPGraph } from "@storyprotocol/test/mocks/MockIPGraph.sol";
import { IPAssetRegistry } from "@storyprotocol/core/registries/IPAssetRegistry.sol";
import { LicenseRegistry } from "@storyprotocol/core/registries/LicenseRegistry.sol";
import { PILicenseTemplate } from "@storyprotocol/core/modules/licensing/PILicenseTemplate.sol";
import { RoyaltyPolicyLAP } from "@storyprotocol/core/modules/royalty/policies/LAP/RoyaltyPolicyLAP.sol";
import { PILFlavors } from "@storyprotocol/core/lib/PILFlavors.sol";
import { PILTerms } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";
import { LicensingModule } from "@storyprotocol/core/modules/licensing/LicensingModule.sol";
import { LicenseToken } from "@storyprotocol/core/LicenseToken.sol";
import { RoyaltyWorkflows } from "@storyprotocol/periphery/workflows/RoyaltyWorkflows.sol";
import { RoyaltyModule } from "@storyprotocol/core/modules/royalty/RoyaltyModule.sol";
import { MockERC20 } from "@storyprotocol/test/mocks/token/MockERC20.sol";

import { SimpleNFT } from "../src/mocks/SimpleNFT.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/5_Royalty.t.sol
contract RoyaltyTest is Test {
    address internal alice = address(0xa11ce);
    address internal bob = address(0xb0b);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - IPAssetRegistry
    IPAssetRegistry internal IP_ASSET_REGISTRY = IPAssetRegistry(0x77319B4031e6eF1250907aa00018B8B1c67a244b);
    // Protocol Core - LicenseRegistry
    LicenseRegistry internal LICENSE_REGISTRY = LicenseRegistry(0x529a750E02d8E2f15649c13D69a465286a780e24);
    // Protocol Core - LicensingModule
    LicensingModule internal LICENSING_MODULE = LicensingModule(0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f);
    // Protocol Core - PILicenseTemplate
    PILicenseTemplate internal PIL_TEMPLATE = PILicenseTemplate(0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316);
    // Protocol Core - RoyaltyPolicyLAP
    RoyaltyPolicyLAP internal ROYALTY_POLICY_LAP = RoyaltyPolicyLAP(0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E);
    // Protocol Core - LicenseToken
    LicenseToken internal LICENSE_TOKEN = LicenseToken(0xFe3838BFb30B34170F00030B52eA4893d8aAC6bC);
    // Protocol Core - RoyaltyModule
    RoyaltyModule internal ROYALTY_MODULE = RoyaltyModule(0xD2f60c40fEbccf6311f8B47c4f2Ec6b040400086);
    // Protocol Periphery - RoyaltyWorkflows
    RoyaltyWorkflows internal ROYALTY_WORKFLOWS = RoyaltyWorkflows(0x9515faE61E0c0447C6AC6dEe5628A2097aFE1890);
    // Mock - MERC20
    MockERC20 internal MERC20 = MockERC20(0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E);

    SimpleNFT public SIMPLE_NFT;
    uint256 public tokenId;
    address public ipId;
    uint256 public licenseTermsId;
    uint256 public startLicenseTokenId;
    address public childIpId;

    function setUp() public {
        // this is only for testing purposes
        // due to our IPGraph precompile not being
        // deployed on the fork
        vm.etch(address(0x0101), address(new MockIPGraph()).code);

        SIMPLE_NFT = new SimpleNFT("Simple IP NFT", "SIM");
        tokenId = SIMPLE_NFT.mint(alice);
        ipId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), tokenId);

        licenseTermsId = PIL_TEMPLATE.registerLicenseTerms(
            PILFlavors.commercialRemix({
                mintingFee: 0,
                commercialRevShare: 10 * 10 ** 6, // 10%
                royaltyPolicy: address(ROYALTY_POLICY_LAP),
                currencyToken: address(MERC20)
            })
        );

        vm.prank(alice);
        LICENSING_MODULE.attachLicenseTerms(ipId, address(PIL_TEMPLATE), licenseTermsId);
        startLicenseTokenId = LICENSING_MODULE.mintLicenseTokens({
            licensorIpId: ipId,
            licenseTemplate: address(PIL_TEMPLATE),
            licenseTermsId: licenseTermsId,
            amount: 2,
            receiver: bob,
            royaltyContext: "", // for PIL, royaltyContext is empty string
            maxMintingFee: 0,
            maxRevenueShare: 0
        });

        // Registers a child IP (owned by Bob) as a derivative of Alice's IP.
        uint256 childTokenId = SIMPLE_NFT.mint(bob);
        childIpId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), childTokenId);

        uint256[] memory licenseTokenIds = new uint256[](1);
        licenseTokenIds[0] = startLicenseTokenId;

        vm.prank(bob);
        LICENSING_MODULE.registerDerivativeWithLicenseTokens({
            childIpId: childIpId,
            licenseTokenIds: licenseTokenIds,
            royaltyContext: "", // empty for PIL
            maxRts: 0
        });
    }

    /// @notice Pays MERC20 to Bob's IP. Some of this MERC20 is then claimable
    /// by Alice's IP.
    /// @dev In this case, this contract will act as the 3rd party paying MERC20
    /// to Bob (the child IP).
    function test_claimAllRevenue() public {
        // ADMIN SETUP
        // We mint 100 MERC20 to this contract so it has some money to pay.
        MERC20.mint(address(this), 100);
        // We have to approve the Royalty Module to spend MERC20 on our behalf, which
        // it will do using `payRoyaltyOnBehalf`.
        MERC20.approve(address(ROYALTY_MODULE), 10);

        // This contract pays 10 MERC20 to Bob's IP.
        ROYALTY_MODULE.payRoyaltyOnBehalf(childIpId, address(0), address(MERC20), 10);

        // Now that Bob's IP has been paid, Alice can claim her share (1 MERC20, which
        // is 10% as specified in the license terms)
        address[] memory childIpIds = new address[](1);
        address[] memory royaltyPolicies = new address[](1);
        address[] memory currencyTokens = new address[](1);
        childIpIds[0] = childIpId;
        royaltyPolicies[0] = address(ROYALTY_POLICY_LAP);
        currencyTokens[0] = address(MERC20);

        uint256[] memory amountsClaimed = ROYALTY_WORKFLOWS.claimAllRevenue({
            ancestorIpId: ipId,
            claimer: ipId,
            childIpIds: childIpIds,
            royaltyPolicies: royaltyPolicies,
            currencyTokens: currencyTokens
        });

        // Check that 1 MERC20 was claimed by Alice's IP Account
        assertEq(amountsClaimed[0], 1);
        // Check that Alice's IP Account now has 1 MERC20 in its balance.
        assertEq(MERC20.balanceOf(ipId), 1);
        // Check that Bob's IP now has 9 MERC20 in its Royalty Vault, which it
        // can claim to its IP Account at a later point if he wants.
        assertEq(MERC20.balanceOf(ROYALTY_MODULE.ipRoyaltyVaults(childIpId)), 9);
    }
}
```

## Test Your Code!

Run `forge build`. If everything is successful, the command should successfully compile.

Now run the test by executing the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/5_Royalty.t.sol
```

## Dispute an IP

Congratulations, you claimed revenue using the [Royalty Module](/concepts/royalty-module/overview)!

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/5_Royalty.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

Now what happens if an IP Asset doesn't pay their due share? We can dispute the IP on-chain, which we will cover on the next page.

<Warning>Coming soon!</Warning>


# Register an IP Asset

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/0_IPARegistrar.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

Let's say you have some off-chain IP (ex. a book, a character, a drawing, etc). In order to register that IP on Story, you first need to mint an NFT. This NFT is the **ownership** over the IP. Then you **register** that NFT on Story, turning it into an [IP Asset](/concepts/ip-asset/overview). The below tutorial will walk you through how to do this.

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)

## Before We Start

There are two scenarios:

1. You already have a **custom** ERC-721 NFT contract and can mint from it
2. You want to create an [SPG (Periphery)](/concepts/spg/overview) NFT contract to do minting for you

## Scenario #1: You already have a custom ERC-721 NFT contract and can mint from it

If you already have an NFT minted, or you want to register IP using a custom-built ERC-721 contract, this is the section for you.

As you can see below, the registration process is relatively straightforward. We use `SimpleNFT` as an example, but you can replace it with your own ERC-721 contract.

All you have to do is call `register` on the [IP Asset Registry](/concepts/registry/ip-asset-registry) with:

- `chainid` - you can simply use `block.chainid`
- `tokenContract` - the address of your NFT collection
- `tokenId` - your NFT's ID

Let's create a test file under `test/0_IPARegistrar.t.sol` to see it work and verify the results:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

You can view the `SimpleNFT` contract we're using to test [here](https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/src/mocks/SimpleNFT.sol).

</Note>

<Info>

You can view the `SimpleNFT` contract we're using to test [here](https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/src/mocks/SimpleNFT.sol).

</Info>

```solidity test/0_IPARegistrar.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";

// your own ERC-721 NFT contract
import { SimpleNFT } from "../src/mocks/SimpleNFT.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/0_IPARegistrar.t.sol
contract IPARegistrarTest is Test {
    address internal alice = address(0xa11ce);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - IPAssetRegistry
    IIPAssetRegistry internal IP_ASSET_REGISTRY = IIPAssetRegistry(0x77319B4031e6eF1250907aa00018B8B1c67a244b);

    SimpleNFT public SIMPLE_NFT;

    function setUp() public {
        // Create a new Simple NFT collection
        SIMPLE_NFT = new SimpleNFT("Simple IP NFT", "SIM");
    }

    /// @notice Mint an NFT and then register it as an IP Asset.
    function test_register() public {
        uint256 expectedTokenId = SIMPLE_NFT.nextTokenId();
        address expectedIpId = IP_ASSET_REGISTRY.ipId(block.chainid, address(SIMPLE_NFT), expectedTokenId);

        uint256 tokenId = SIMPLE_NFT.mint(alice);
        address ipId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), tokenId);

        assertEq(tokenId, expectedTokenId);
        assertEq(ipId, expectedIpId);
        assertEq(SIMPLE_NFT.ownerOf(tokenId), alice);
    }
}
```

## Scenario #2: You want to create an SPG NFT contract to do minting for you

If you don't have your own custom NFT contract, this is the section for you.

To achieve this, we will be using the [SPG](/concepts/spg/overview), which is a utility contract that allows us to combine multiple transactions into one. In this case, we'll be using the SPG's `mintAndRegisterIp` function which combines both minting an NFT and registering it as an IP Asset.

In order to use `mintAndRegisterIp`, we first have to create a new `SPGNFT` collection. We can do this simply by calling `createCollection` on the `StoryProtocolGateway` contract. Or, if you want to create your own `SPGNFT` for some reason, you can implement the [ISPGNFT](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/interfaces/ISPGNFT.sol) contract interface. Follow the example below to see example parameters you can use to initialize a new SPGNFT.

Once you have your own SPGNFT, all you have to do is call `mintAndRegisterIp` with:

- `spgNftContract` - the address of your SPGNFT contract
- `recipient` - the address of who will receive the NFT and thus be the owner of the newly registered IP. _Note: remember that registering IP on Story is permissionless, so you can register an IP for someone else (by paying for the transaction) yet they can still be the owner of that IP Asset._
- `ipMetadata` - the metadata associated with your NFT & IP. See [this](/concepts/ip-asset/overview#nft-vs-ip-metadata) section to better understand setting NFT & IP metadata.

1. Run `touch test/0_IPARegistrar.t.sol` to create a test file under `test/0_IPARegistrar.t.sol`. Then, paste in the following code:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

</Note>

```solidity test/0_IPARegistrar.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";
import { ISPGNFT } from "@storyprotocol/periphery/interfaces/ISPGNFT.sol";
import { IRegistrationWorkflows } from "@storyprotocol/periphery/interfaces/workflows/IRegistrationWorkflows.sol";
import { WorkflowStructs } from "@storyprotocol/periphery/lib/WorkflowStructs.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/0_IPARegistrar.t.sol
contract IPARegistrarTest is Test {
    address internal alice = address(0xa11ce);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - IPAssetRegistry
    IIPAssetRegistry internal IP_ASSET_REGISTRY = IIPAssetRegistry(0x77319B4031e6eF1250907aa00018B8B1c67a244b);
    // Protocol Periphery - RegistrationWorkflows
    IRegistrationWorkflows internal REGISTRATION_WORKFLOWS =
        IRegistrationWorkflows(0xbe39E1C756e921BD25DF86e7AAa31106d1eb0424);

    ISPGNFT public SPG_NFT;

    function setUp() public {
        // Create a new NFT collection via SPG
        SPG_NFT = ISPGNFT(
            REGISTRATION_WORKFLOWS.createCollection(
                ISPGNFT.InitParams({
                    name: "Test Collection",
                    symbol: "TEST",
                    baseURI: "",
                    contractURI: "",
                    maxSupply: 100,
                    mintFee: 0,
                    mintFeeToken: address(0),
                    mintFeeRecipient: address(this),
                    owner: address(this),
                    mintOpen: true,
                    isPublicMinting: false
                })
            )
        );
    }

    /// @notice Mint an NFT and register it in the same call via the Story Protocol Gateway.
    /// @dev Requires the collection address that is passed into the `mintAndRegisterIp` function
    /// to be created via SPG (createCollection), as done above. Or, a contract that
    /// implements the `ISPGNFT` interface.
    function test_mintAndRegisterIp() public {
        uint256 expectedTokenId = SPG_NFT.totalSupply() + 1;
        address expectedIpId = IP_ASSET_REGISTRY.ipId(block.chainid, address(SPG_NFT), expectedTokenId);

        // Note: The caller of this function must be the owner of the SPG NFT Collection.
        // In this case, the owner of the SPG NFT Collection is the contract itself
        // because it deployed it in the `setup` function.
        // We can make `alice` the recipient of the NFT though, which makes her the
        // owner of not only the NFT, but therefore the IP Asset.
        (address ipId, uint256 tokenId) = REGISTRATION_WORKFLOWS.mintAndRegisterIp(
            address(SPG_NFT),
            alice,
            WorkflowStructs.IPMetadata({
                ipMetadataURI: "https://ipfs.io/ipfs/QmZHfQdFA2cb3ASdmeGS5K6rZjz65osUddYMURDx21bT73",
                ipMetadataHash: keccak256(
                    abi.encodePacked(
                        "{'title':'My IP Asset','description':'This is a test IP asset','createdAt':'','creators':[]}"
                    )
                ),
                nftMetadataURI: "https://ipfs.io/ipfs/QmRL5PcK66J1mbtTZSw1nwVqrGxt98onStx6LgeHTDbEey",
                nftMetadataHash: keccak256(
                    abi.encodePacked(
                        "{'name':'Test NFT','description':'This is a test NFT','image':'https://picsum.photos/200'}"
                    )
                )
            }),
            true
        );

        assertEq(ipId, expectedIpId);
        assertEq(tokenId, expectedTokenId);
        assertEq(SPG_NFT.ownerOf(tokenId), alice);
    }
}
```

## Run the Test and Verify the Results

2. Run `forge build`. If everything is successful, the command should successfully compile.

3. Now run the test by executing the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/0_IPARegistrar.t.sol
```

## Add License Terms to IP

Congratulations, you registered an IP!

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/0_IPARegistrar.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

Now that your IP is registered, you can create and attach [License Terms](/concepts/licensing-module/license-terms) to it. This will allow others to mint a license and use your IP, restricted by the terms.

We will go over this on the next page.


# Setup

In this guide, we will show you how to setup the Story smart contract development environment in just a few minutes.

## Prerequisites

- [Install Foundry](https://book.getfoundry.sh/getting-started/installation)
- [Install yarn](https://classic.yarnpkg.com/lang/en/docs/install/)

## Creating a Project

1. Run `foundryup` to automatically install the latest stable version of the precompiled binaries: forge, cast, anvil, and chisel
2. Run the following command in a new directory: `forge init`. This will create a `foundry.toml` and example project files in the project root. By default, forge init will also initialize a new git repository.
3. Initialize a new yarn project: `yarn init`. Alternatively, you can use `npm init` or `pnpm init`.
4. Open up your `foundry.toml` file and replace it with this:

```toml
[profile.default]
out = 'out'
libs = ['node_modules', 'lib']
cache_path  = 'forge-cache'
gas_reports = ["*"]
optimizer = true
optimizer_runs = 20000
test = 'test'
solc = '0.8.26'
fs_permissions = [{ access = 'read', path = './out' }, { access = 'read-write', path = './deploy-out' }]
evm_version = 'cancun'
remappings = [
    '@openzeppelin/=node_modules/@openzeppelin/',
    '@storyprotocol/core/=node_modules/@story-protocol/protocol-core/contracts/',
    '@storyprotocol/periphery/=node_modules/@story-protocol/protocol-periphery/contracts/',
    'erc6551/=node_modules/erc6551/',
    'forge-std/=node_modules/forge-std/src/',
    'ds-test/=node_modules/ds-test/src/',
    '@storyprotocol/test/=node_modules/@story-protocol/protocol-core/test/foundry/',
    '@solady/=node_modules/solady/'
]
```

5. Remove the example contract files: `rm src/Counter.sol script/Counter.s.sol test/Counter.t.sol`

## Installing Dependencies

Now, we are ready to start installing our dependencies. To incorporate the Story Protocol core and periphery modules, run the following to have them added to your `package.json`. We will also install `openzeppelin` and `erc6551` as a dependency for the contract and test.

```bash
# note: you can run them one-by-one, or all at once
yarn add @story-protocol/protocol-core@https://github.com/storyprotocol/protocol-core-v1
yarn add @story-protocol/protocol-periphery@https://github.com/storyprotocol/protocol-periphery-v1
yarn add @openzeppelin/contracts
yarn add @openzeppelin/contracts-upgradeable
yarn add erc6551
yarn add solady
```

Additionally, for working with Foundry's test kit, we also recommend adding the following `devDependencies`:

```bash
yarn add -D https://github.com/dapphub/ds-test
yarn add -D github:foundry-rs/forge-std#v1.7.6
```

Now we are ready to build a simple test registration contract!


# Register a Derivative

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/4_IPARemix.t.sol"
  icon="thumbs-up"
>
  All of this page is covered in this working code example.
</Card>

Once a [License Token](/concepts/licensing-module/license-token) has been minted from an IP Asset, the owner of that token (an ERC-721 NFT) can burn it to register their own IP Asset as a derivative of the IP Asset associated with the License Token.

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)
2. Have a minted License Token. You can learn how to do that [here](/developers/smart-contracts-guide/mint-license)

## Register as Derivative

Let's create a test file under `test/4_IPARemix.t.sol` to see it work and verify the results:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

</Note>

```solidity test/4_IPARemix.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
// for testing purposes only
import { MockIPGraph } from "@storyprotocol/test/mocks/MockIPGraph.sol";
import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";
import { ILicenseRegistry } from "@storyprotocol/core/interfaces/registries/ILicenseRegistry.sol";
import { IPILicenseTemplate } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";
import { ILicensingModule } from "@storyprotocol/core/interfaces/modules/licensing/ILicensingModule.sol";
import { PILFlavors } from "@storyprotocol/core/lib/PILFlavors.sol";
import { PILTerms } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";

import { SimpleNFT } from "../src/mocks/SimpleNFT.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/4_IPARemix.t.sol
contract IPARemixTest is Test {
    address internal alice = address(0xa11ce);
    address internal bob = address(0xb0b);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - IPAssetRegistry
    IIPAssetRegistry internal IP_ASSET_REGISTRY = IIPAssetRegistry(0x77319B4031e6eF1250907aa00018B8B1c67a244b);
    // Protocol Core - LicenseRegistry
    ILicenseRegistry internal LICENSE_REGISTRY = ILicenseRegistry(0x529a750E02d8E2f15649c13D69a465286a780e24);
    // Protocol Core - LicensingModule
    ILicensingModule internal LICENSING_MODULE = ILicensingModule(0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f);
    // Protocol Core - PILicenseTemplate
    IPILicenseTemplate internal PIL_TEMPLATE = IPILicenseTemplate(0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316);
    // Protocol Core - RoyaltyPolicyLAP
    address internal ROYALTY_POLICY_LAP = 0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E;
    // Revenue Token - MERC20
    address internal MERC20 = 0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E;

    SimpleNFT public SIMPLE_NFT;
    uint256 public tokenId;
    address public ipId;
    uint256 public licenseTermsId;
    uint256 public startLicenseTokenId;

    function setUp() public {
        // this is only for testing purposes
        // due to our IPGraph precompile not being
        // deployed on the fork
        vm.etch(address(0x0101), address(new MockIPGraph()).code);

        SIMPLE_NFT = new SimpleNFT("Simple IP NFT", "SIM");
        tokenId = SIMPLE_NFT.mint(alice);
        ipId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), tokenId);

        licenseTermsId = PIL_TEMPLATE.registerLicenseTerms(
            PILFlavors.commercialRemix({
                mintingFee: 0,
                commercialRevShare: 10 * 10 ** 6, // 10%
                royaltyPolicy: ROYALTY_POLICY_LAP,
                currencyToken: MERC20
            })
        );

        vm.prank(alice);
        LICENSING_MODULE.attachLicenseTerms(ipId, address(PIL_TEMPLATE), licenseTermsId);
        startLicenseTokenId = LICENSING_MODULE.mintLicenseTokens({
            licensorIpId: ipId,
            licenseTemplate: address(PIL_TEMPLATE),
            licenseTermsId: licenseTermsId,
            amount: 2,
            receiver: bob,
            royaltyContext: "", // for PIL, royaltyContext is empty string
            maxMintingFee: 0,
            maxRevenueShare: 0
        });
    }

    /// @notice Mints an NFT to be registered as IP, and then
    /// linked as a derivative of alice's asset using the
    /// minted license token.
    function test_registerDerivativeWithLicenseTokens() public {
        // First we mint an NFT and register it as an IP Asset,
        // owned by Bob.
        uint256 childTokenId = SIMPLE_NFT.mint(bob);
        address childIpId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), childTokenId);

        uint256[] memory licenseTokenIds = new uint256[](1);
        licenseTokenIds[0] = startLicenseTokenId;

        // Bob uses the License Token he has from Alice's IP
        // to register his IP as a derivative of Alice's IP.
        vm.prank(bob);
        LICENSING_MODULE.registerDerivativeWithLicenseTokens({
            childIpId: childIpId,
            licenseTokenIds: licenseTokenIds,
            royaltyContext: "", // empty for PIL
            maxRts: 0
        });

        assertTrue(LICENSE_REGISTRY.hasDerivativeIps(ipId));
        assertTrue(LICENSE_REGISTRY.isParentIp(ipId, childIpId));
        assertTrue(LICENSE_REGISTRY.isDerivativeIp(childIpId));
        assertEq(LICENSE_REGISTRY.getParentIpCount(childIpId), 1);
        assertEq(LICENSE_REGISTRY.getDerivativeIpCount(ipId), 1);
        assertEq(LICENSE_REGISTRY.getParentIp({ childIpId: childIpId, index: 0 }), ipId);
        assertEq(LICENSE_REGISTRY.getDerivativeIp({ parentIpId: ipId, index: 0 }), childIpId);
    }
}
```

## Test Your Code!

Run `forge build`. If everything is successful, the command should successfully compile.

Now run the test by executing the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/4_IPARemix.t.sol
```

## Paying and Claiming Revenue

Congratulations, you registered a derivative IP Asset!

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/4_IPARemix.t.sol"
  icon="thumbs-up"
>
  All of this page is covered in this working code example.
</Card>

Now that we have established parent-child IP relationships, we can begin to explore payments and automated revenue share based on the license terms. We'll cover that in the upcoming pages.


# Register License Terms

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/1_LicenseTerms.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

[License Terms](/concepts/licensing-module/license-terms) are a configurable set of values that define restrictions on licenses minted from your IP that have those terms. For example, "If you mint this license, you must share 50% of your revenue with me." You can view the full set of terms in [PIL Terms](/concepts/programmable-ip-license/pil-terms).

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)

## Before We Start

It's important to know that if **License Terms already exist for the identical set of parameters you intend to create, it is unnecessary to create it again**. License Terms are protocol-wide, so you can use existing License Terms by its `licenseTermsId`.

## Register License Terms

You can view the full set of terms in [PIL Terms](/concepts/programmable-ip-license/pil-terms).

Let's create a test file under `test/1_LicenseTerms.t.sol` to see it work and verify the results:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

</Note>

```solidity test/1_LicenseTerms.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
import { IPILicenseTemplate } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";
import { PILTerms } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/1_LicenseTerms.t.sol
contract LicenseTermsTest is Test {
    address internal alice = address(0xa11ce);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - PILicenseTemplate
    IPILicenseTemplate internal PIL_TEMPLATE = IPILicenseTemplate(0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316);
    // Protocol Core - RoyaltyPolicyLAP
    address internal ROYALTY_POLICY_LAP = 0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E;
    // Revenue Token - MERC20
    address internal MERC20 = 0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E;

    function setUp() public {}

    /// @notice Registers new PIL Terms. Anyone can register PIL Terms.
    function test_registerPILTerms() public {
        PILTerms memory pilTerms = PILTerms({
            transferable: true,
            royaltyPolicy: ROYALTY_POLICY_LAP,
            defaultMintingFee: 0,
            expiration: 0,
            commercialUse: true,
            commercialAttribution: true,
            commercializerChecker: address(0),
            commercializerCheckerData: "",
            commercialRevShare: 0,
            commercialRevCeiling: 0,
            derivativesAllowed: true,
            derivativesAttribution: true,
            derivativesApproval: true,
            derivativesReciprocal: true,
            derivativeRevCeiling: 0,
            currency: MERC20,
            uri: ""
        });
        uint256 licenseTermsId = PIL_TEMPLATE.registerLicenseTerms(pilTerms);

        uint256 selectedLicenseTermsId = PIL_TEMPLATE.getLicenseTermsId(pilTerms);
        assertEq(licenseTermsId, selectedLicenseTermsId);
    }
}
```

### PIL Flavors

As you see above, you have to choose between a lot of terms.

We have convenience functions to help you register new terms. We have created [PIL Flavors](/concepts/programmable-ip-license/pil-flavors), which are pre-configured popular combinations of License Terms to help you decide what terms to use. You can view those PIL Flavors and then register terms using the following convenience functions:

<CardGroup cols={2}>

<Card
  title="Non-Commercial Social Remixing"
  href="/concepts/programmable-ip-license/pil-flavors#flavor-%231%3A-non-commercial-social-remixing"
  icon="file"
>
  Free remixing with attribution. No commercialization.
</Card>

<Card
  title="Commercial Use"
  href="/concepts/programmable-ip-license/pil-flavors#flavor-%232%3A-commercial-use"
  icon="file"
>
  Pay to use the license with attribution, but don't have to share revenue.
</Card>

<Card
  title="Commercial Remix"
  href="/concepts/programmable-ip-license/pil-flavors#flavor-%233%3A-commercial-remix"
  icon="file"
>
  Pay to use the license with attribution and pay % of revenue earned.
</Card>

<Card
  title="Creative Commons Attribution"
  href="/concepts/programmable-ip-license/pil-flavors#flavor-%234%3A-creative-commons-attribution"
  icon="file"
>
  Free remixing and commercial use with attribution.
</Card>

</CardGroup>

For example:

```solidity Solidity
import { PILFlavors } from "@storyprotocol/core/lib/PILFlavors.sol";

PILTerms memory pilTerms = PILFlavors.commercialRemix({
  mintingFee: 0,
  commercialRevShare: 5 * 10 ** 6, // 5% rev share
  royaltyPolicy: ROYALTY_POLICY_LAP,
  currencyToken: MERC20
});
```

## Test Your Code!

Run `forge build`. If everything is successful, the command should successfully compile.

Now run the test by executing the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/1_LicenseTerms.t.sol
```

## Attach Terms to Your IP

Congratulations, you created new license terms!

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/1_LicenseTerms.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

Now that you have registered new license terms, we can attach them to an IP Asset. This will allow others to mint a license and use your IP, restricted by the terms.

We will go over this on the next page.


# Attach Terms to an IPA

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/2_AttachTerms.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

This section demonstrates how to attach [License Terms](/concepts/licensing-module/license-terms) to an [IP Asset](/concepts/ip-asset/overview). By attaching terms, users can publicly mint [License Tokens](/concepts/licensing-module/license-token) (the on-chain "license") with those terms from the IP.

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)
2. Create License Terms and have a `licenseTermsId`. You can do that by following the [previous page](/developers/smart-contracts-guide/register-terms).

## Attach License Terms

Now that we have created terms and have the associated `licenseTermsId`, we can attach them to an existing IP Asset.

Let's create a test file under `test/2_AttachTerms.t.sol` to see it work and verify the results:

<Note>
**Contract Addresses**

We have filled in the addresses from the Story contracts for you. However you can also find the addresses for them here: [Deployed Smart Contracts](/developers/deployed-smart-contracts)

</Note>

```solidity test/2_AttachTerms.t.sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;

import { Test } from "forge-std/Test.sol";
// for testing purposes only
import { MockIPGraph } from "@storyprotocol/test/mocks/MockIPGraph.sol";
import { IIPAssetRegistry } from "@storyprotocol/core/interfaces/registries/IIPAssetRegistry.sol";
import { ILicenseRegistry } from "@storyprotocol/core/interfaces/registries/ILicenseRegistry.sol";
import { IPILicenseTemplate } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";
import { ILicensingModule } from "@storyprotocol/core/interfaces/modules/licensing/ILicensingModule.sol";
import { PILFlavors } from "@storyprotocol/core/lib/PILFlavors.sol";
import { PILTerms } from "@storyprotocol/core/interfaces/modules/licensing/IPILicenseTemplate.sol";

import { SimpleNFT } from "../src/mocks/SimpleNFT.sol";

// Run this test:
// forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/2_AttachTerms.t.sol
contract AttachTermsTest is Test {
    address internal alice = address(0xa11ce);

    // For addresses, see https://docs.story.foundation/developers/deployed-smart-contracts
    // Protocol Core - IPAssetRegistry
    IIPAssetRegistry internal IP_ASSET_REGISTRY = IIPAssetRegistry(0x77319B4031e6eF1250907aa00018B8B1c67a244b);
    // Protocol Core - LicenseRegistry
    ILicenseRegistry internal LICENSE_REGISTRY = ILicenseRegistry(0x529a750E02d8E2f15649c13D69a465286a780e24);
    // Protocol Core - LicensingModule
    ILicensingModule internal LICENSING_MODULE = ILicensingModule(0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f);
    // Protocol Core - PILicenseTemplate
    IPILicenseTemplate internal PIL_TEMPLATE = IPILicenseTemplate(0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316);
    // Protocol Core - RoyaltyPolicyLAP
    address internal ROYALTY_POLICY_LAP = 0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E;
    // Revenue Token - MERC20
    address internal MERC20 = 0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E;

    SimpleNFT public SIMPLE_NFT;
    uint256 public tokenId;
    address public ipId;
    uint256 public licenseTermsId;

    function setUp() public {
        // this is only for testing purposes
        // due to our IPGraph precompile not being
        // deployed on the fork
        vm.etch(address(0x0101), address(new MockIPGraph()).code);

        SIMPLE_NFT = new SimpleNFT("Simple IP NFT", "SIM");
        tokenId = SIMPLE_NFT.mint(alice);
        ipId = IP_ASSET_REGISTRY.register(block.chainid, address(SIMPLE_NFT), tokenId);

        // Register random Commercial Remix terms so we can attach them later
        licenseTermsId = PIL_TEMPLATE.registerLicenseTerms(
            PILFlavors.commercialRemix({
                mintingFee: 0,
                commercialRevShare: 10 * 10 ** 6, // 10%
                royaltyPolicy: ROYALTY_POLICY_LAP,
                currencyToken: MERC20
            })
        );
    }

    /// @notice Attaches license terms to an IP Asset.
    /// @dev Only the owner of an IP Asset can attach license terms to it.
    /// So in this case, alice has to be the caller of the function because
    /// she owns the NFT associated with the IP Asset.
    function test_attachLicenseTerms() public {
        vm.prank(alice);
        LICENSING_MODULE.attachLicenseTerms(ipId, address(PIL_TEMPLATE), licenseTermsId);

        assertTrue(LICENSE_REGISTRY.hasIpAttachedLicenseTerms(ipId, address(PIL_TEMPLATE), licenseTermsId));
        assertEq(LICENSE_REGISTRY.getAttachedLicenseTermsCount(ipId), 1);
        (address licenseTemplate, uint256 attachedLicenseTermsId) = LICENSE_REGISTRY.getAttachedLicenseTerms({
            ipId: ipId,
            index: 0
        });
        assertEq(licenseTemplate, address(PIL_TEMPLATE));
        assertEq(attachedLicenseTermsId, licenseTermsId);
    }
}
```

## Test Your Code!

Run `forge build`. If everything is successful, the command should successfully compile.

Now run the test by executing the following command:

```bash
forge test --fork-url https://aeneid.storyrpc.io/ --match-path test/2_AttachTerms.t.sol
```

## Mint a License

Congratulations, you attached terms to an IPA!

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate/blob/main/test/2_AttachTerms.t.sol"
  icon="thumbs-up"
>
  Follow the completed code all the way through.
</Card>

Now that we have attached License Terms to our IP, the next step is minting a License Token, which we'll go over on the next page.


# Smart Contract Guide

In this section, we will briefly go over the protocol contracts and then guide you through how to start building on top of the protocol. If you haven't yet familiarized yourself with the overall architecture, we recommend first going over the [Architecture Overview](/concepts/overview) section.

## Smart Contract Tutorial

<Card
  title="Completed Code"
  href="https://github.com/storyprotocol/story-protocol-boilerplate"
  icon="thumbs-up"
>
  Skip the tutorial and view the completed code. Follow the README instructions
  to run the tests, or go to the `/test` folder to view all of the example
  contracts.
</Card>

**If you want to set things up from scratch**, then continue with the following tutorials, starting with the [Setup Your Own Project](/developers/smart-contracts-guide/setup) step.

## Our Smart Contracts

As of the current version, our Proof-of-Creativity Protocol is compatible with all EVM chains and is written as a set of Smart Contracts in Solidity. There are two repositories that you may interact with as a developer:

- [Story Protocol Core](https://github.com/storyprotocol/protocol-core-v1) - This repository contains the core protocol logic, consisting of a thin IP registry (the [IP Asset Registry](/concepts/registry/ip-asset-registry)), a set of [Modules](/concepts/modules/overview) defining logic around [Licensing](/concepts/licensing-module/overview), [Royalty](/concepts/royalty-module/overview), [Dispute](/concepts/dispute-module/overview), metadata, and a module manager for administering module and user access control.
- [Story Protocol Periphery](https://github.com/storyprotocol/protocol-periphery-v1)- Whereas the core contracts deal with the underlying protocol logic, the periphery contracts deal with protocol extensions that greatly increase UX and simplify IPA management. This is mostly handled through the [SPG](/concepts/spg/overview).

## Deploy & Verify Contracts on Story

<Note>
  The approach to deploy & verify contracts comes from the [Blockscout official
  documentation](https://docs.blockscout.com/developer-support/verifying-a-smart-contract/foundry-verification).
</Note>

Verify a contract with Blockscout right after deployment (make sure you add "/api/" to the end of the Blockscout homepage explorer URL):

```shell
forge create \
  --rpc-url <rpc_https_endpoint> \
  --private-key $PRIVATE_KEY \
  <contract_file>:<contract_name> \
  --verify \
  --verifier blockscout \
  --verifier-url <blockscout_homepage_explorer_url>/api/
```

Or if using foundry scripts:

```shell
forge script <script_file> \
  --rpc-url <rpc_https_endpoint> \
  --private-key $PRIVATE_KEY \
  --broadcast \
  --verify \
  --verifier blockscout \
  --verifier-url <blockscout_homepage_explorer_url>/api/
```

<Warning>

Do not use RANDAO for pseudo-randomness, instead use onchain VRF (Pyth or Gelato). Currently, RANDAO value is set as the parent block hash and thus is not random for X-1 block.

</Warning>


# Deployed Smart Contracts

## Core Protocol Contracts

- View contracts on our GitHub [here](https://github.com/storyprotocol/protocol-core-v1/tree/main)

<CodeGroup>
```json Aeneid Testnet
{
  "AccessController": "0xcCF37d0a503Ee1D4C11208672e622ed3DFB2275a",
  "ArbitrationPolicyUMA": "0xfFD98c3877B8789124f02C7E8239A4b0Ef11E936",
  "CoreMetadataModule": "0x6E81a25C99C6e8430aeC7353325EB138aFE5DC16",
  "CoreMetadataViewModule": "0xB3F88038A983CeA5753E11D144228Ebb5eACdE20",
  "DisputeModule": "0x9b7A9c70AFF961C799110954fc06F3093aeb94C5",
  "EvenSplitGroupPool": "0xf96f2c30b41Cb6e0290de43C8528ae83d4f33F89",
  "GroupNFT": "0x4709798FeA84C84ae2475fF0c25344115eE1529f",
  "GroupingModule": "0x69D3a7aa9edb72Bc226E745A7cCdd50D947b69Ac",
  "IPAccountImplBeacon": "0x9825cc7A398D9C3dDD66232A8Ec76d5b05422581",
  "IPAccountImplBeaconProxy": "0x00b800138e4D82D1eea48b414d2a2A8Aee9A33b1",
  "IPAccountImplCode": "0x6ccAd5718a27fB6a09EAdb737D889A2007838b77",
  "IPAssetRegistry": "0x77319B4031e6eF1250907aa00018B8B1c67a244b",
  "IPGraphACL": "0x1640A22a8A086747cD377b73954545e2Dfcc9Cad",
  "IpRoyaltyVaultBeacon": "0x6928ba25Aa5c410dd855dFE7e95713d83e402AA6",
  "IpRoyaltyVaultImpl": "0x73e2D097F71e5103824abB6562362106A8955AEc",
  "LicenseRegistry": "0x529a750E02d8E2f15649c13D69a465286a780e24",
  "LicenseToken": "0xFe3838BFb30B34170F00030B52eA4893d8aAC6bC",
  "LicensingModule": "0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f",
  "ModuleRegistry": "0x022DBAAeA5D8fB31a0Ad793335e39Ced5D631fa5",
  "PILicenseTemplate": "0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316",
  "ProtocolAccessManager": "0xFdece7b8a2f55ceC33b53fd28936B4B1e3153d53",
  "ProtocolPauseAdmin": "0xdd661f55128A80437A0c0BDA6E13F214A3B2EB24",
  "RoyaltyModule": "0xD2f60c40fEbccf6311f8B47c4f2Ec6b040400086",
  "RoyaltyPolicyLAP": "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E",
  "RoyaltyPolicyLRP": "0x9156e603C949481883B1d3355c6f1132D191fC41"
}
```

```json Mainnet
{
  "AccessController": "0xcCF37d0a503Ee1D4C11208672e622ed3DFB2275a",
  "ArbitrationPolicyUMA": "0xfFD98c3877B8789124f02C7E8239A4b0Ef11E936",
  "CoreMetadataModule": "0x6E81a25C99C6e8430aeC7353325EB138aFE5DC16",
  "CoreMetadataViewModule": "0xB3F88038A983CeA5753E11D144228Ebb5eACdE20",
  "DisputeModule": "0x9b7A9c70AFF961C799110954fc06F3093aeb94C5",
  "EvenSplitGroupPool": "0xf96f2c30b41Cb6e0290de43C8528ae83d4f33F89",
  "GroupNFT": "0x4709798FeA84C84ae2475fF0c25344115eE1529f",
  "GroupingModule": "0x69D3a7aa9edb72Bc226E745A7cCdd50D947b69Ac",
  "IPAccountImplBeacon": "0x9825cc7A398D9C3dDD66232A8Ec76d5b05422581",
  "IPAccountImplBeaconProxy": "0x00b800138e4D82D1eea48b414d2a2A8Aee9A33b1",
  "IPAccountImplCode": "0x7343646585443F1c3F64E4F08b708788527e1C77",
  "IPAssetRegistry": "0x77319B4031e6eF1250907aa00018B8B1c67a244b",
  "IPGraphACL": "0x1640A22a8A086747cD377b73954545e2Dfcc9Cad",
  "IpRoyaltyVaultBeacon": "0x6928ba25Aa5c410dd855dFE7e95713d83e402AA6",
  "IpRoyaltyVaultImpl": "0x63cC7611316880213f3A4Ba9bD72b0EaA2010298",
  "LicenseRegistry": "0x529a750E02d8E2f15649c13D69a465286a780e24",
  "LicenseToken": "0xFe3838BFb30B34170F00030B52eA4893d8aAC6bC",
  "LicensingModule": "0x04fbd8a2e56dd85CFD5500A4A4DfA955B9f1dE6f",
  "ModuleRegistry": "0x022DBAAeA5D8fB31a0Ad793335e39Ced5D631fa5",
  "PILicenseTemplate": "0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316",
  "ProtocolAccessManager": "0xFdece7b8a2f55ceC33b53fd28936B4B1e3153d53",
  "ProtocolPauseAdmin": "0xdd661f55128A80437A0c0BDA6E13F214A3B2EB24",
  "RoyaltyModule": "0xD2f60c40fEbccf6311f8B47c4f2Ec6b040400086",
  "RoyaltyPolicyLAP": "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E",
  "RoyaltyPolicyLRP": "0x9156e603C949481883B1d3355c6f1132D191fC41"
}
```

</CodeGroup>

## Periphery Contracts

- View contracts on our GitHub [here](https://github.com/storyprotocol/protocol-periphery-v1)

<CodeGroup>
```json Aeneid Testnet
{
  "DerivativeWorkflows": "0x9e2d496f72C547C2C535B167e06ED8729B374a4f",
  "GroupingWorkflows": "0xD7c0beb3aa4DCD4723465f1ecAd045676c24CDCd",
  "LicenseAttachmentWorkflows": "0xcC2E862bCee5B6036Db0de6E06Ae87e524a79fd8",
  "OwnableERC20Beacon": "0x9a81C447C0b4C47d41d94177AEea3511965d3Bc9",
  "OwnableERC20Template": "0x37DbEbcFe991901C4F255E7a3C4F7D3B45EAEDe9",
  "RegistrationWorkflows": "0xbe39E1C756e921BD25DF86e7AAa31106d1eb0424",
  "RoyaltyTokenDistributionWorkflows": "0xa38f42B8d33809917f23997B8423054aAB97322C",
  "RoyaltyWorkflows": "0x9515faE61E0c0447C6AC6dEe5628A2097aFE1890",
  "SPGNFTBeacon": "0xD2926B9ecaE85fF59B6FB0ff02f568a680c01218",
  "SPGNFTImpl": "0xc09e3788Fdfbd3dd8CDaa2aa481B52CcFAb74a42",
  "TokenizerModule": "0x7e14cD9833E8A0c649bCF4AB6768f62D57febbd3"
}
```

```json Mainnet
{
  "DerivativeWorkflows": "0x9e2d496f72C547C2C535B167e06ED8729B374a4f",
  "GroupingWorkflows": "0xD7c0beb3aa4DCD4723465f1ecAd045676c24CDCd",
  "LicenseAttachmentWorkflows": "0xcC2E862bCee5B6036Db0de6E06Ae87e524a79fd8",
  "OwnableERC20Beacon": "0x9a81C447C0b4C47d41d94177AEea3511965d3Bc9",
  "OwnableERC20Template": "0xE6505ffc5A7C19B68cEc2311Cc35BC02d8f7e0B1",
  "RegistrationWorkflows": "0xbe39E1C756e921BD25DF86e7AAa31106d1eb0424",
  "RoyaltyTokenDistributionWorkflows": "0xa38f42B8d33809917f23997B8423054aAB97322C",
  "RoyaltyWorkflows": "0x9515faE61E0c0447C6AC6dEe5628A2097aFE1890",
  "SPGNFTBeacon": "0xD2926B9ecaE85fF59B6FB0ff02f568a680c01218",
  "SPGNFTImpl": "0x6Cfa03Bc64B1a76206d0Ea10baDed31D520449F5",
  "TokenizerModule": "0xAC937CeEf893986A026f701580144D9289adAC4C"
}
```

</CodeGroup>

## License Hooks

- View contracts on our GitHub [here](https://github.com/storyprotocol/protocol-periphery-v1/tree/main/contracts/hooks)

<CodeGroup>
```json Aeneid Testnet
{
  "LockLicenseHook": "0x5D874d4813c4A8A9FB2AB55F30cED9720AEC0222",
  "TotalLicenseTokenLimitHook": "0xba8E30d9EB784Badc2aF610F56d99d212BC2A90c"
}
```

```json Mainnet
{
  "LockLicenseHook": "0x5D874d4813c4A8A9FB2AB55F30cED9720AEC0222",
  "TotalLicenseTokenLimitHook": "0xB72C9812114a0Fc74D49e01385bd266A75960Cda"
}
```

</CodeGroup>

## Whitelisted Revenue Tokens

The below list contains the whitelisted revenue tokens that can be used in the Royalty Module. Learn more about Revenue Tokens [here](/concepts/royalty-module/ip-royalty-vault).

<Tabs>
  <Tab title="Aeneid Testnet">
    | Token  | Contract Address                             | Explorer                                                                                                                   | Mint                                                                                                                                                |
    | :----- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
    | WIP    | `0x1514000000000000000000000000000000000000` | [View here ↗️](https://aeneid.storyscan.io/address/0x1514000000000000000000000000000000000000) | N/A                                                                                                                                                 |
    | MERC20 | `0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E` | [View here ↗️](https://aeneid.storyscan.io/address/0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E) | [Mint ↗️](https://aeneid.storyscan.io/address/0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E?tab=write_contract#0x40c10f19) |
  </Tab>

  <Tab title="Mainnet">
    | Token | Contract Address                             | Explorer                                                                                                                   | Mint |
    | :---- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :--- |
    | WIP   | `0x1514000000000000000000000000000000000000` | [View here ↗️](https://aeneid.storyscan.io/address/0x1514000000000000000000000000000000000000) | N/A  |
  </Tab>
</Tabs>

## Misc

- **Multicall3**: 0xcA11bde05977b3631167028862bE2a173976CA11
- **Default License Terms ID** (Non-Commercial Social Remixing): 1

## Ecosystem Official Contracts

The below is a list of official ecosystem contracts.

### Story ENS

<CodeGroup>
```json Aeneid Testnet
{
  "SidRegistry": "0x5dC881dDA4e4a8d312be3544AD13118D1a04Cb17",
  "PublicResolver": "0x6D3B3F99177FB2A5de7F9E928a9BD807bF7b5BAD"
}
```

```json Mainnet
{
  "SidRegistry": "0x5dC881dDA4e4a8d312be3544AD13118D1a04Cb17",
  "PublicResolver": "0x6D3B3F99177FB2A5de7F9E928a9BD807bF7b5BAD"
}
```

</CodeGroup>


# "Case Study: Registering a Derivative of Ippy"

[PiPi](https://pfp3.io/pipi/mint) is a free generative pfp project on Story that lets you mint derivative artworks of [Ippy](https://explorer.story.foundation/ipa/0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42), Story's official mascot. Ippy has [Non-Commercial Social Remixing (NCSR)](/concepts/programmable-ip-license/pil-flavors#flavor-%231%3A-non-commercial-social-remixing) terms attached, which means anyone can use it or create derivative works as long as it's not used commercially and proper attribution is shown.

<CardGroup cols={3}>
  <Card
    title="Original Ippy"
    href="https://explorer.story.foundation/ipa/0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42"
    icon="house"
    
    
  >
    View the original Ippy mascot on our explorer.
  </Card>

{" "}

<Card
  title="PiPi Derivative"
  href="https://explorer.story.foundation/ipa/0xBB42BF2713ee736284C45B1b549a03625cc97e51"
  icon="house"
>
  View a derviative PiPi on our explorer.
</Card>

  <Card
    title="View PiPi Contract"
    href="https://www.storyscan.io/address/0x5C6b236A100d09f8A625dB87E11122749A9B71A6?tab=contract"
    icon="scroll"
    
    
  >
    View the PiPi contract source code.
  </Card>
</CardGroup>

When a PiPi is linked as a derivative of Ippy, it automatically inherits the same license terms (NCSR) and is linked in its ancestry graph, which you can see directly on our explorer:

<Frame caption="In the bottom right, you can see Ippy is the root IP of this PiPi.">
  <img
    src="/images/tutorials/pippy-explorer.png"
    alt="In the bottom right, you can see Ippy is the root IP of this PiPi."
  />
</Frame>

In the following tutorial, you will learn how exactly these PiPi images were properly registered as derivatives of the official Ippy IP.

## Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [Setup Your Own Project](/developers/smart-contracts-guide/setup)

## 1. Setup Metadata

Before we register our new PiPi IP, we need to set up its metadata. There are two types of metadata:

1. NFT Metadata
2. IP Metadata

<CardGroup cols={1}>
  <Card
    title="NFT vs. IP Metadata"
    href="/concepts/ip-asset/overview#nft-vs-ip-metadata"
    icon="house"
  >
    Learn how to properly set up NFT and IP Metadata.
  </Card>
</CardGroup>

Using [this PiPi](https://explorer.story.foundation/ipa/0xBB42BF2713ee736284C45B1b549a03625cc97e51) as an example, here is what the NFT & IP metadata should be:

<CodeGroup>

```json NFT Metadata
{
  "name": "PiPi NFT #1103",
  "image": "https://ipfs.io/ipfs/bafybeigsv4cgacndijwy6b7qhxbseonrybrcpbh47zrlm64gsjm4mlpb2q/nft_1103.jpeg",
  "attributes": [
    {
      "trait_type": "Bg",
      "value": "Orange"
    },
    {
      "trait_type": "Body",
      "value": "Pink"
    },
    {
      "trait_type": "Eyes",
      "value": "Cute"
    },
    {
      "trait_type": "Cloth",
      "value": "Blue"
    },
    {
      "trait_type": "Glasses",
      "value": "Neo"
    },
    {
      "trait_type": "Hat",
      "value": "Duck"
    }
  ],
  "description": "Pipi - The first Derivative IP Asset NFT collection on Story Protocol. Limited 2222 generative PFPs inspired by the Ippy, official Story mascot."
}
```

```json IP Metadata
{
  "title": "PiPi NFT",
  "description": "Pipi - The first Derivative IP Asset NFT collection on Story Protocol. Limited 2222 generative PFPs inspired by the Ippy, official Story mascot.",
  "image": "https://ipfs.io/ipfs/bafybeigsv4cgacndijwy6b7qhxbseonrybrcpbh47zrlm64gsjm4mlpb2q/nft_1103.jpeg",
  "imageHash": "0xb930f3ba19350bddbcd8c180a3127086f6e454d29cd5b3db613c70bae2848329",
  "mediaUrl": "https://ipfs.io/ipfs/bafybeigsv4cgacndijwy6b7qhxbseonrybrcpbh47zrlm64gsjm4mlpb2q/nft_1103.jpeg",
  "mediaHash": "0xb930f3ba19350bddbcd8c180a3127086f6e454d29cd5b3db613c70bae2848329",
  "mediaType": "image/jpeg",
  "creators": [
    {
      "name": "PFP3",
      "address": "0xF91510A17392Be6B3b6F620427051168A1e56A72",
      "description": "PFP Generator",
      "image": "https://utfs.io/f/XyGBmmuHQK18FodS0WDuqCo1LVerXR7sgm8vJnESazWcM5yB",
      "socialMedia": [
        {
          "platform": "twitter",
          "url": "https://x.com/pfp3_"
        },
        {
          "platform": "website",
          "url": "https://pfp3.io"
        },
        {
          "platform": "discord",
          "url": "https://discord.gg/pfp3"
        }
      ],
      "role": "creator",
      "contributionPercent": 100
    }
  ],
  "tags": ["PiPi", "Derivative IPA", "NFT", "PF3", "PFP"],
  "ipType": "NFT"
}
```

</CodeGroup>

Once you have metadata written, you can upload them to IPFS and will later set it when minting our NFT.

## 2. Minting an NFT

When you want to register an IP on Story, you must first mint an NFT. This NFT represents the **ownership** over the [IP Asset](/concepts/ip-asset).

<CardGroup cols={1}>
  <Card
    title="View PiPi Contract"
    href="https://www.storyscan.io/address/0x5C6b236A100d09f8A625dB87E11122749A9B71A6?tab=contract"
    icon="scroll"
  >
    View the PiPi contract source code.
  </Card>
</CardGroup>

Here is part of the `_mintNFT` function in the `PiPi.sol` contract:

```sol PiPi.sol
contract PiPi is ERC721, Ownable, IERC721Receiver {

  // ... some code here ...

  function whitelistMint() external payable returns (string memory, address) {
    require(whitelistMintEnabled, "Whitelist mint is not active");
    require(whitelist[msg.sender], "Address not whitelisted");
    require(mintedCount[msg.sender] < WHITELIST_MAX_P_WALLET, "Whitelist mint limit reached");
    require(_totalSupply < MAX_SUPPLY, "Max supply reached");

    return _mintNFT(msg.sender);
  }

  function _mintNFT(address recipient) internal returns (string memory, address) {
    uint256 newTokenId = _totalSupply + 1;
    _safeMint(address(this), newTokenId);

    address ipId = _registerAsIPAsset(newTokenId);

    string memory nftUri = tokenURI(newTokenId);
    bytes32 metadataHash = keccak256(abi.encodePacked(nftUri));
    CORE_METADATA_MODULE.setAll(ipId, nftUri, metadataHash, metadataHash);

    registerDerivativeForToken(ipId);

    _safeTransfer(address(this), recipient, newTokenId, "");

    // ... more code here ...

    return (nftUri, ipId);
  }
}
```

As you can see, the user calls `whitelistMint` which then calls `_mintNFT` after checking if the user is on a whitelist. On line 16, we are then minting a new NFT to the contract.

<Note>
**Why do we mint an NFT to the contract and not the user?**

We later have to register the IP as a derivative of Ippy. Only the owner (the address holding the NFT) can register an IP as a derivative of another. So, we will mint the NFT to the contract => contract registers NFT as IP and then later as a derivative of Ippy => transfer NFT to the user.

</Note>

## 3. Registering NFT as IP

Once we have minted a new NFT, we can register it as IP. On line 18 above, it calls a `_registerAsIPAsset` function:

```sol PiPi.sol
function _registerAsIPAsset(uint256 tokenId) internal returns (address) {
  try IP_ASSET_REGISTRY.register(block.chainid, address(this), tokenId) returns (address ipId) {
    require(ipId != address(0), "IP Asset registration failed");
    return ipId;
  } catch Error(string memory reason) {
    revert(reason);
  } catch {
    revert("IP Asset registration failed");
  }
}
```

All this is doing is calling the `register` function on the [IP Asset Registry](/concepts/registry/ip-asset-registry), which creates a new [IP Asset](/concepts/ip-asset) in our protocol, and returns an `ipId`.

## 4. Set Metadata on IP

Now that we have registered a new IP Asset, we can take our metadata from before and set it on the NFT & IP with the `CoreMetadataModule.sol`. As described [here](/concepts/ip-asset/overview#adding-nft-%26-ip-metadata-to-ip-asset), we need to set 4 params:

1. `nftMetadataHash`
2. `nftMetadataURI`
3. `ipMetadataHash`
4. `ipMetadataURI`

```sol PiPi.sol
// handles the NFT's `nftMetadataHash`
// handles the IP's `ipMetadataURI` and `ipMetadataHash`
function _mintNFT(address recipient) internal returns (string memory, address) {

  // ... some code here ...

  string memory nftUri = tokenURI(newTokenId);
  bytes32 metadataHash = keccak256(abi.encodePacked(nftUri));
  CORE_METADATA_MODULE.setAll(ipId, nftUri, metadataHash, metadataHash);

  // ... some code here ...

}

// handles the NFT's `nftMetadataURI`
function tokenURI(uint256 tokenId) public view override returns (string memory) {
  return string(abi.encodePacked(_baseUri, StringUtils.uint2str(tokenId), ".json"));
}
```

## 5. Register as Derivative

Now that we have minted an NFT, registered it as IP, and set proper metadata, we can register it as a derivative of Ippy. The `PiPi.sol` contract uses `registerDerivativeForToken` to handle this:

```sol PiPi.sol
function registerDerivativeForToken(address ipId) internal {
  address[] memory parentIpIds = new address[](1);
  parentIpIds[0] = 0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42;

  uint256[] memory licenseTermsIds = new uint256[](1);
  licenseTermsIds[0] = 1;

  address licenseTemplate = 0x2E896b0b2Fdb7457499B56AAaA4AE55BCB4Cd316;
  bytes memory royaltyContext = hex"0000000000000000000000000000000000000000";
  uint256 maxMintingFee = 0;
  uint32 maxRts = 0;
  uint32 maxRevenueShare = 0;

  LICENSING_MODULE.registerDerivative(
    ipId,
    parentIpIds,
    licenseTermsIds,
    licenseTemplate,
    royaltyContext,
    maxMintingFee,
    maxRts,
    maxRevenueShare
  );
}
```

This function calls `registerDerivative` in the [Licensing Module](/concepts/licensing-module), with:

- `ipId`: the new `ipId` we got in step 3
- `parentIpIds`: an array that contains Ippy's `ipId`, which is `0xB1D831271A68Db5c18c8F0B69327446f7C8D0A42`
- `licenseTermsIds`: an array containing `1`, which is the license term ID of [Non-Commercial Social Remixing (NCSR)](/concepts/programmable-ip-license/pil-flavors#flavor-%231%3A-non-commercial-social-remixing). This means the derivative can use Ippy for free but not commercialize it
- `licenseTemplate`: the address of `PILicenseTemplate`, found in [Deployed Smart Contracts](/developers/deployed-smart-contracts)
- `royaltyContext`: just set to zero address
- `maxMintingFee`, `maxRts`, and `maxRevenueShare` can be set to 0. They don't do anything because the license terms are non-commercial.

## 6. Transfer NFT

Now that the contract has handled registering the IP as a derivative, it transfers the NFT to the user to have ownership over the PiPi IP:

```sol PiPi.sol
function _mintNFT(address recipient) internal returns (string memory, address) {
  // ... some code here ...
  _safeTransfer(address(this), recipient, newTokenId, "");
  // ... some code here ...
}
```

## 7. Done!

Congratulations, you registered a derivative of the official Ippy IP!

<CardGroup cols={2}>
  <Card
    title="View on Explorer"
    href="https://explorer.story.foundation/ipa/0xBB42BF2713ee736284C45B1b549a03625cc97e51"
    icon="house"
  >
    View a derviative PiPi on our explorer.
  </Card>
  <Card title="Learn More" href="/developers/tutorials" icon="book-open">
    Explore more tutorials in our documentation
  </Card>
</CardGroup>


# Email Login & Sponsored Transactions with Privy

<Card
  title="Completed Code"
  href="https://github.com/jacob-tucker/story-privy-tutorial"
  icon="thumbs-up"
  color="#51af51"
>
  View the completed code for this tutorial.
</Card>

You are reading this tutorial because you probably want to do one or both of these things:

1. Enable users who don't have a wallet to login with email to your app ("Embedded Wallets")
2. Sponsor transactions for your users so they don't have to pay gas ("Smart Wallets")

Here is how Privy describes both of these things:

> Embedded wallets are self-custodial wallets provisioned by Privy itself for a wallet experience that is directly embedded in your application. Embedded wallets do not require a separate wallet client, like a browser extension or a mobile app, and can be accessed directly from your product. These are primarily designed for users of your app who may not already have an external wallet, or don't want to connect their external wallet.
>
> Smart wallets are programmable, onchain accounts that incorporate the features of account abstraction. With just a few lines of code, you can create smart wallets for your users to sponsor gas payments, send batched transactions, and more.

We will be implementing both using [Privy](https://www.privy.io/) + [Pimlico](https://www.pimlico.io/).

### ⚠️ Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Create a new project on [Privy's Dashboard](https://dashboard.privy.io)
2. Copy your **"App ID"** under **"App settings > API keys"**. In your local project, make a `.env` file and add your App ID:

```Text .env
NEXT_PUBLIC_PRIVY_APP_ID=
```

3. On your project dashboard, enable Smart Wallets under "**Wallet Configuration > Smart wallets**" and select "**Kernel (ZeroDev)**" as shown below:

<Frame>

<img src="/images/tutorials/privy-tutorial-1.png" alt="Privy Dashboard" />

</Frame>

4. Once you enable Smart wallets, right underneath make sure to put a "Custom chain" with the following values:
   1. Name: `Story Aeneid Testnet`
   2. ID number: `1315`
   3. RPC URL: `https://aeneid.storyrpc.io`
   4. For the Bundler URL and Paymaster URL, go to [Pimlico's Dashboard](https://dashboard.pimlico.io) and create a new app. Then click on "API Keys", create a new API Key, click "RPC URLs" as shown below, and then select "Story Aeneid Testnet" as the network:

<Warning>

This is for testing. In a real scenario, you would have to set up proper sponsorship policies and billing info on Pimlico to automatically sponsor the transactions on behalf of your app. We don't have to do this on testnet.

</Warning>
<Frame>

<img src="/images/tutorials/pimlico-dashboard.png" alt="Pimlico Dashboard" />

</Frame>

5. Install the dependencies:

```Text Terminal
npm install @story-protocol/core-sdk permissionless viem @privy-io/react-auth
```

## 1. Set up Embedded Wallets

<CardGroup cols={1}>
  <Card
    title="Official Privy Tutoral"
    href="https://docs.privy.io/guide/react/wallets/smart-wallets/usage#setup"
    icon="house"
  >
    Follow Privy's official tutorial for setup instead of reading this step.
  </Card>
</CardGroup>

<Note>
  You can read Privy's tutorial
  [here](https://docs.privy.io/guide/react/wallets/embedded/creation) that
  describes setting up Embedded Wallets, which is a fancy way of saying email
  login for your users. In the below example, we simply create an embedded
  wallet for every user, but you may want more customization by reading their
  tutorial.
</Note>

You must wrap any component that will be using embedded/smart wallets with the `PrivyProvider` and `SmartWalletsProvider`. In a `providers.tsx` (or whatever you want to call it) file, add the following code:

```jsx providers.tsx
"use client";

import { PrivyProvider } from "@privy-io/react-auth";
import { SmartWalletsProvider } from "@privy-io/react-auth/smart-wallets";
import { aeneid } from "@story-protocol/core-sdk";

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <PrivyProvider
      appId={process.env.NEXT_PUBLIC_PRIVY_APP_ID as string}
      config={{
        // Customize Privy's appearance in your app
        appearance: {
          theme: "light",
          accentColor: "#676FFF",
          logo: "/story-logo.jpg",
        },
        // Create embedded wallets for users who don't have a wallet
        // when they sign in with email
        embeddedWallets: {
          createOnLogin: "all-users",
        },
        defaultChain: aeneid,
        supportedChains: [aeneid],
      }}
    >
      <SmartWalletsProvider>{children}</SmartWalletsProvider>
    </PrivyProvider>
  );
}
```

Then you can simply add it to your`layout.tsx` like so:

```jsx layout.tsx
import Providers from "@/providers/providers";

/* other code here... */

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode,
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
```

## 2. Login & Logout

You can add email login to your app like so:

```jsx page.tsx
import { usePrivy } from "@privy-io/react-auth";

export default function Home() {
  const { login, logout, user } = usePrivy();

  useEffect(() => {
    if (user) {
      const smartWallet = user.linkedAccounts.find(
        (account) => account.type === "smart_wallet"
      );
      // Logs the smart wallet's address
      console.log(smartWallet.address);
      // Logs the smart wallet type (e.g. 'safe', 'kernel', 'light_account', 'biconomy', 'thirdweb', 'coinbase_smart_wallet')
      console.log(smartWallet.type);
    }
  }, [user]);

  return (
    <div>
      <button onClick={user ? logout : login}>
        {user ? "Logout" : "Login with Privy"}
      </button>
    </div>
  );
}
```

## 3. Sign a Message with Privy

<CardGroup cols={1}>

  <Card
    title="Official Privy Tutoral"
    href="https://docs.privy.io/guide/react/wallets/smart-wallets/usage#signing-messages"
    icon="house"
  >
    Follow Privy's official tutorial for signing messages instead of reading
    this step.
  </Card>
  
</CardGroup>

We can use the generated smart wallet to sign messages:

```jsx page.tsx
import { useSmartWallets } from "@privy-io/react-auth/smart-wallets";

export default function Home() {
  const { client: smartWalletClient } = useSmartWallets();

  /* previous code here */

  async function sign() {
    const uiOptions = {
      title: "Example Sign",
      description: "This is an example for a user to sign.",
      buttonText: "Sign",
    };
    const request = {
      message: "IP is cool",
    };
    const signature = await smartWalletClient?.signMessage(request, {
      uiOptions,
    });
  }

  return (
    <div>
      {/* previous code here */}
      <button onClick={sign}>Sign</button>
    </div>
  );
}
```

## 4. Send an Arbitrary Transaction

<CardGroup cols={1}>
  <Card
    title="Official Privy Tutoral"
    href="https://docs.privy.io/guide/react/wallets/smart-wallets/usage#sending-transactions"
    icon="house"
  >
    Follow Privy's official tutorial for sending transactions instead of reading
    this step.
  </Card>
</CardGroup>

We can also use the generated smart wallet to sponsor transactions for our users:

<CodeGroup>

```jsx page.tsx
import { useSmartWallets } from "@privy-io/react-auth/smart-wallets";
import { encodeFunctionData } from "viem";
import { defaultNftContractAbi } from "./defaultNftContractAbi";

export default function Home() {
  const { client: smartWalletClient } = useSmartWallets();

  /* previous code here */

  async function mintNFT() {
    const uiOptions = {
      title: "Mint NFT",
      description: "This is an example transaction that mints an NFT.",
      buttonText: "Mint",
    };

    const transactionRequest = {
      to: "0x937bef10ba6fb941ed84b8d249abc76031429a9a", // example nft contract
      data: encodeFunctionData({
        abi: defaultNftContractAbi, // abi from another file
        functionName: "mintNFT",
        args: ["0x6B86B39F03558A8a4E9252d73F2bDeBfBedf5b68", "test-uri"],
      }),
    } as const;

    const txHash = await smartWalletClient?.sendTransaction(
      transactionRequest,
      { uiOptions }
    );
    console.log(`View Tx: https://aeneid.storyscan.io/tx/${txHash}`);
  }

  return (
    <div>
      {/* previous code here */}
      <button onClick={mintNFT}>Mint NFT</button>
    </div>
  )
}
```

```Text defaultNftContractAbi.ts
export const defaultNftContractAbi = [
  {
    inputs: [],
    stateMutability: "nonpayable",
    type: "constructor",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "recipient",
        type: "address",
      },
      {
        internalType: "string",
        name: "tokenURI",
        type: "string",
      },
    ],
    name: "mintNFT",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "tokenId",
        type: "uint256",
      },
    ],
    name: "tokenURI",
    outputs: [
      {
        internalType: "string",
        name: "",
        type: "string",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "tokenId",
        type: "uint256",
      },
    ],
    name: "ownerOf",
    outputs: [
      {
        internalType: "address",
        name: "",
        type: "address",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "symbol",
    outputs: [
      {
        internalType: "string",
        name: "",
        type: "string",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "name",
    outputs: [
      {
        internalType: "string",
        name: "",
        type: "string",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "totalSupply",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
];

```

</CodeGroup>

## 5. Send a Transaction from Story SDK

We can also use the generated smart wallet to send transactions from the [🛠️ TypeScript SDK](/developers/typescript-sdk). Some of the functions have an option to return the `encodedTxData`, which we can use to pass into Privy's smart wallet. You can see which functions support this in the [SDK Reference](/sdk-reference).

```jsx page.tsx
import { useSmartWallets } from "@privy-io/react-auth/smart-wallets";
import {
  EncodedTxData,
  StoryClient,
  StoryConfig,
} from "@story-protocol/core-sdk";
import { http } from "viem";

export default function Home() {
  const { client: smartWalletClient } = useSmartWallets();

  /* previous code here */

  async function setupStoryClient() {
    const config: StoryConfig = {
      account: smartWalletClient!.account,
      transport: http("https://aeneid.storyrpc.io"),
      chainId: "aeneid",
    };
    const client = StoryClient.newClient(config);
    return client;
  }

  async function registerIp() {
    const storyClient = await setupStoryClient();

    const response = await storyClient.ipAsset.mintAndRegisterIp({
      spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc", // public spg contract for testing
      txOptions: { encodedTxDataOnly: true },
    });

    const uiOptions = {
      title: "Register IP",
      description: "This is an example transaction that registers an IP.",
      buttonText: "Register",
    };

    const txHash = await smartWalletClient?.sendTransaction(
      response.encodedTxData as EncodedTxData,
      { uiOptions }
    );
    console.log(`View Tx: https://aeneid.storyscan.io/tx/${txHash}`);
  }

  return (
    <div>
      {/* previous code here */}
      <button onClick={registerIp}>Register IP</button>
    </div>
  );
}
```

## 6. Done!

<CardGroup cols={2}>
  <Card
    title="Completed Code"
    href="https://github.com/jacob-tucker/story-privy-tutorial"
    icon="thumbs-up"
    iconColor="#51af51"
  >
    View the completed code for this tutorial.
  </Card>
  <Card title="Learn More" href="/developers/tutorials" icon="book-open">
    Explore more tutorials in our documentation
  </Card>
</CardGroup>


# Register & Monetize Stability Images

In this tutorial, you will learn how to:

1. Generate an image with Stability AI
2. Upload your image to Pinata IPFS
3. Register your image as IP on Story
4. Attach License Terms to your IP

## The Explanation

Let's say you generate an image using Stability AI. Without adding a proper license to your image, others could use it freely. In this tutorial, you will learn how to add a license to your Stability AI-Generated image so that if others want to use it, they must properly license it from you.

## 0. Before you Start

There are a few steps you have to complete before you can start the tutorial.

1. You will need to install [Node.js](https://nodejs.org/en/download) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). If you've coded before, you likely have these.
2. Add your Story Network Testnet wallet's private key to `.env` file:

```yaml .env
WALLET_PRIVATE_KEY=
```

3. Go to [the Pinata dashboard](https://app.pinata.cloud/developers/api-keys) and create a new API key and a gateway. Add the JWT along with the gateway to your `.env` file:

```yaml .env
PINATA_JWT=
PINATA_GATEWAY=
```

4. Go to [Stability](https://platform.stability.ai/account/keys) and create a new API key. Add the new key to your `.env` file:

<Warning>
**Stability Credits**

In order to generate an image, you'll need Stability credits. If you just created an account, you will probably have a free trial that will give you a few credits to start with.

</Warning>

```yaml .env
STABILITY_API_KEY=
```

5. Add your preferred RPC URL to your `.env` file. You can just use the public default one we provide:

```yaml .env
RPC_PROVIDER_URL=https://aeneid.storyrpc.io
```

6. Install the dependencies:

```bash Terminal
npm install @story-protocol/core-sdk pinata-web3 viem axios sharp form-data
```

## 1. Generate an Image

You can follow the [Stability API Reference](https://platform.stability.ai/docs/api-reference) to use the model of your choice. For this tutorial, we'll be using Stability's **Stable Image Core** generate endpoint to generate an image. The below is taken directly from their documentation.

Create a `main.ts` file and add the following code:

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";

async function main() {
  const payload = {
    prompt: "Lighthouse on a cliff overlooking the ocean",
    output_format: "png",
  };

  const response = await axios.postForm(
    `https://api.stability.ai/v2beta/stable-image/generate/core`,
    axios.toFormData(payload, new FormData()),
    {
      validateStatus: undefined,
      responseType: "arraybuffer",
      headers: {
        Authorization: `Bearer ${process.env.STABILITY_API_KEY}`,
        Accept: "image/*",
      },
    }
  );
}

main();
```

## 1.5. (Optional) Condense the Image

Stability generates images that are heavy in size, and therefore expensive to store. Optionally, we can condense the produced image for faster loading speeds and less expensive storage costs.

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";

async function main() {
  // previous code here ...

  const condensedImgBuffer = await sharp(response.data)
    .png({ quality: 10 }) // Adjust the quality value as needed (between 0 and 100)
    .toBuffer();
}

main();
```

## 2. Store Image in IPFS

Now that we have our image, we need to store it on IPFS so we can get a URL back to access it. In this tutorial we'll be using [Pinata](https://pinata.cloud/), a decentralized storage solution that makes storing images easy.

In a separate file `uploadToIpfs.ts`, create a function `uploadBlobToIPFS` that uploads our buffer to IPFS:

```typescript uploadToIpfs.ts
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
  // you can put your pinata gateway here, or leave it empty
  pinataGateway: process.env.PINATA_GATEWAY,
});

// upload our image to ipfs by putting it in a public group
export async function uploadBlobToIPFS(
  blob: Blob,
  fileName: string
): Promise<string> {
  const file = new File([blob], fileName, { type: "image/png" });
  const { IpfsHash } = await pinata.upload.file(file);
  return IpfsHash;
}
```

Back in the main file, call the `uploadBlobToIPFS` function to store our image:

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";
import { uploadBlobToIPFS } from "./uploadToIpfs.ts";

async function main() {
  // previous code here ...

  // convert the buffer to a blob
  const blob = new Blob([condensedImgBuffer], { type: "image/png" });
  // store the blob on ipfs
  const imageCid = await uploadBlobToIPFS(blob, "lighthouse.png");
}

main();
```

## 3. Set up your Story Config

Now that we have generated and stored our image, we can register the image as IP on Story. First, let's set up our config. In a `utils.ts` file, add the following code:

<Info>
  Associated docs: [TypeScript SDK Setup](/developers/typescript-sdk/setup)
</Info>

```typescript utils.ts
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";
import { http } from "viem";
import { privateKeyToAccount, Address, Account } from "viem/accounts";

const privateKey: Address = `0x${process.env.WALLET_PRIVATE_KEY}`;
export const account: Account = privateKeyToAccount(privateKey);

const config: StoryConfig = {
  account: account,
  transport: http(process.env.RPC_PROVIDER_URL),
  chainId: "aeneid",
};
export const client = StoryClient.newClient(config);
```

## 4. Set up your IP Metadata

View the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard) and construct the metadata for your IP. Properly format your metadata as shown below:

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";
import { uploadBlobToIPFS } from "./uploadToIpfs.ts";
import { client, account } from "./utils";

async function main() {
  // previous code here ...

  const ipMetadata = {
    title: "Lighthouse",
    description: "A generated picture of a lighthouse.",
    createdAt: "1728401700",
    image: process.env.PINATA_GATEWAY + "/files/" + imageCid,
    imageHash: "0x...", // a hash of the image
    mediaUrl: process.env.PINATA_GATEWAY + "/files/" + imageCid,
    mediaHash: "0x...", // a hash of the image
    mediaType: "image/png",
    creators: [
      {
        name: "Jacob Tucker",
        address: "0x67ee74EE04A0E6d14Ca6C27428B27F3EFd5CD084",
        description: "A cool dev rel person.",
        contributionPercent: 100,
        socialMedia: [
          {
            platform: "Twitter",
            url: "https://x.com/jacobmtucker",
          },
        ],
      },
    ],
  };
}

main();
```

## 5. Set up your NFT Metadata

The NFT Metadata follows the [ERC-721 Metadata Standard](https://eips.ethereum.org/EIPS/eip-721).

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";
import { uploadBlobToIPFS } from "./uploadToIpfs.ts";
import { client, account } from "./utils";

async function main() {
  // previous code here ...

  const nftMetadata = {
    name: "Ownership NFT",
    description:
      "This NFT represents ownership of the image generated by Stability",
    image: process.env.PINATA_GATEWAY + "/files/" + imageCid,
    attributes: [
      {
        key: "Model",
        value: "Stability",
      },
      {
        key: "Service",
        value: "Stable Image Core",
      },
      {
        key: "Prompt",
        value: "Lighthouse on a cliff overlooking the ocean",
      },
    ],
  };
}

main();
```

## 6. Upload your IP and NFT Metadata to IPFS

In the `uploadToIpfs.ts` file, create a function to upload your IP & NFT Metadata objects to IPFS:

```typescript uploadToIpfs.ts
// previous code here ...

export async function uploadJSONToIPFS(jsonMetadata: any): Promise<string> {
  const { IpfsHash } = await pinata.upload.json(jsonMetadata);
  return IpfsHash;
}
```

You can then use that function to upload your metadata, as shown below:

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";
import { uploadBlobToIPFS, uploadJSONToIPFS } from "./uploadToIpfs.ts";
import { client, account } from "./utils";
import { createHash } from "crypto";

async function main() {
  // previous code here ...

  const ipIpfsHash = await uploadJSONToIPFS(ipMetadata);
  const ipHash = createHash("sha256")
    .update(JSON.stringify(ipMetadata))
    .digest("hex");
  const nftIpfsHash = await uploadJSONToIPFS(nftMetadata);
  const nftHash = createHash("sha256")
    .update(JSON.stringify(nftMetadata))
    .digest("hex");
}

main();
```

## 7. Create License Terms

When registering your image on Story, you can attach [License Terms](/concepts/licensing-module/license-terms) to the IP. These are real, legally binding terms enforced on-chain by the [Licensing Module](/concepts/licensing-module), disputable by the [Dispute Module](/concepts/dispute-module), and in the worst case, able to be enforced off-chain in court through traditional means.

Let's say we want to monetize our image such that every time someone wants to use it (on merch, advertisement, or whatever) they have to pay an initial minting fee of 10 $WIP. Additionally, every time they earn revenue on derivative work, they owe 5% revenue back as royalty.

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";
import { uploadBlobToIPFS, uploadJSONToIPFS } from "./uploadToIpfs.ts";
import { client, account } from "./utils";
import { createHash } from "crypto";
import { LicenseTerms, WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
import { zeroAddress, parseEther } from "viem";

async function main() {
  // previous code here ...

  const commercialRemixTerms: LicenseTerms = {
    transferable: true,
    royaltyPolicy: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E", // RoyaltyPolicyLAP address from https://docs.story.foundation/developers/deployed-smart-contracts
    defaultMintingFee: parseEther("1"), // 1 $WIP
    expiration: BigInt(0),
    commercialUse: true,
    commercialAttribution: true, // must give us attribution
    commercializerChecker: zeroAddress,
    commercializerCheckerData: zeroAddress,
    commercialRevShare: 5, // can claim 50% of derivative revenue
    commercialRevCeiling: BigInt(0),
    derivativesAllowed: true,
    derivativesAttribution: true,
    derivativesApproval: false,
    derivativesReciprocal: true,
    derivativeRevCeiling: BigInt(0),
    currency: WIP_TOKEN_ADDRESS,
    uri: "",
  };
}

main();
```

## 8. Register an NFT as an IP Asset

Next we will mint an NFT, register it as an [IP Asset](/concepts/ip-asset), set [License Terms](/concepts/licensing-module/license-terms) on the IP, and then set both NFT & IP metadata.

Luckily, we can use the `mintAndRegisterIp` function to mint an NFT and register it as an IP Asset in the same transaction.

This function needs an SPG NFT Contract to mint from. For simplicity, you can use a public collection we have created for you on Aeneid testnet: `0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc`.

<Accordion title="Creating your own custom ERC-721 collection" icon="pen-circle">
  Using the public collection we provide for you is fine, but when you do this for real, you should make your own NFT Collection for your IPs. You can do this in 2 ways:

1. Deploy a contract that implements the [ISPGNFT](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/interfaces/ISPGNFT.sol) interface, or use the SDK's [createNFTCollection](/sdk-reference/nftclient#createnftcollection) function (shown below) to do it for you. This will give you your own SPG NFT Collection that only you can mint from.

```typescript createSpgNftCollection.ts
import { zeroAddress } from "viem";
import { client } from "./utils";

async function createSpgNftCollection() {
  const newCollection = await client.nftClient.createNFTCollection({
    name: "Test NFTs",
    symbol: "TEST",
    isPublicMinting: false,
    mintOpen: true,
    mintFeeRecipient: zeroAddress,
    contractURI: "",
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `New SPG NFT collection created at transaction hash ${newCollection.txHash}`
  );
  console.log(`NFT contract address: ${newCollection.spgNftContract}`);
}

createSpgNftCollection();
```

2. Create a custom ERC-721 NFT collection on your own and use the [register](/sdk-reference/ipasset#register) function - providing an `nftContract` and `tokenId` - _instead of_ using the `mintAndRegisterIp` function. See a working code example [here](https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/registration/registerCustom.ts). This is helpful if you **already have a custom NFT contract that has your own custom logic, or if your IPs themselves are NFTs.**

</Accordion>

<Info>
  Associated Docs:
  [ipAsset.mintAndRegisterIp](/sdk-reference/ipasset#mintandregisterip)
</Info>

```typescript main.ts
import fs from "fs";
import axios from "axios";
import FormData from "form-data";
import { uploadBlobToIPFS, uploadJSONToIPFS } from "./uploadToIpfs.ts";
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
import { client, account } from "./utils";
import { createHash } from "crypto";
import { LicenseTerms } from "@story-protocol/core-sdk";
import { zeroAddress, parseEther, Address } from "viem";

async function main() {
  // previous code here ...

  const response = await client.ipAsset.mintAndRegisterIpAssetWithPilTerms({
    spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc",
    // the terms we created in the previous step
    licenseTermsData: [{ terms: commercialRemixTerms }],
    ipMetadata: {
      ipMetadataURI: process.env.PINATA_GATEWAY + "/files/" + ipIpfsHash,
      ipMetadataHash: `0x${ipHash}`,
      nftMetadataURI: process.env.PINATA_GATEWAY + "/files/" + nftIpfsHash,
      nftMetadataHash: `0x${nftHash}`,
    },
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `Root IPA created at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
  );
  console.log(
    `View on the explorer: https://aeneid.explorer.story.foundation/ipa/${response.ipId}`
  );
}

main();
```

## 9. Done!

Congratulations! Now your image is registered on Story with commercial license terms.

<CardGroup cols={1}>
  <Card title="Learn More" href="/developers/tutorials" icon="book-open">
    Explore more tutorials in our documentation
  </Card>
</CardGroup>


# How to Register IP on Story

<CardGroup cols={2}>
  <Card
    title="Using the SDK"
    href="/developers/typescript-sdk/register-ip-asset"
    icon="house"
  >
    Learn how to register an IP using the SDK.
  </Card>

  <Card
    title="Using a Smart Contract"
    href="/developers/smart-contracts-guide/register-ip-asset"
    icon="house"
  >
    Learn how to register an IP using the Smart Contracts.
  </Card>
</CardGroup>


# How to Register Music on Story

In this tutorial, you will learn how to properly register music as IP on Story using the TypeScript SDK. At the end, you will be able to listen to your song directly on our explorer.

<CardGroup cols={2}>
  <Card
    title="Example Final Result"
    href="https://aeneid.explorer.story.foundation/ipa/0x70920EaC7F9748Ac5A71C82310f1ac1C7eD11f02"
    icon="house"
    
    
  >
    View an example result after following this tutorial.
  </Card>

  <Card
    title="Justin Bieber is coming to Story!"
    href="https://x.com/StoryProtocol/status/1881713146274156951"
    icon="megaphone"
    
    
  >
    "Peaches" by Justin Bieber is one of the first RWAs coming to Story. Check out the announcement!
  </Card>
</CardGroup>

## 1. Create a Song

Before we register music on Story, you'll obviously need some music! If you already have music, make sure you have a link to the music file directly. For example, `https://cdn1.suno.ai/dcd3076f-3aa5-400b-ba5d-87d30f27c311.mp3`. If you don't already have this, you can upload your music file to IPFS:

If you want to create a test song, go to [Suno](https://suno.com), which is an awesome platform for AI-generated music. We can get a test song by:

1. Inputting a prompt to create a song
2. Click on the final result, which should take you to a URL like `https://suno.com/song/dcd3076f-3aa5-400b-ba5d-87d30f27c311`
3. Copy the the `SONG_ID` in the URL (`dcd3076f-3aa5-400b-ba5d-87d30f27c311`)
4. Copy the following URL: `https://cdn1.suno.ai/${SONG_ID}.mp3`, making sure to replace `SONG_ID` with your own.

This is the URL we'll use in step 2.

## 2. Complete the "How to Register IP" Tutorial

Most of what we need to do is already covered in [Register an IP Asset](/developers/typescript-sdk/register-ip-asset). Complete that tutorial first, and then come back here.

## 3. Change Metadata

The only difference is how you set your metadata. Here is an example:

- `image.*` is used to display a cover image when your song is registered
- `media.*` is used for the audio file. Also note that the fields passed into `media.*` are checked for infringement by the [Story Attestation Service](/concepts/story-attestation-service).

```typescript main.ts
const ipMetadata = {
  title: "Midnight Marriage",
  description: "This is a house-style song generated on suno.",
  createdAt: "1740005219",
  creators: [
    {
      name: "Jacob Tucker",
      address: "0xA2f9Cf1E40D7b03aB81e34BC50f0A8c67B4e9112",
      contributionPercent: 100,
    },
  ],
  image:
    "https://cdn2.suno.ai/image_large_8bcba6bc-3f60-4921-b148-f32a59086a4c.jpeg",
  imageHash:
    "0xc404730cdcdf7e5e54e8f16bc6687f97c6578a296f4a21b452d8a6ecabd61bcc",
  mediaUrl: "https://cdn1.suno.ai/dcd3076f-3aa5-400b-ba5d-87d30f27c311.mp3",
  mediaHash:
    "0xb52a44f53b2485ba772bd4857a443e1fb942cf5dda73c870e2d2238ecd607aee",
  mediaType: "audio/mpeg",
};
```

After you've done that, you can set your NFT metadata like so:

- `image` for the cover image
- `animation_url` is used for the audio file
- `attributes` for any extra attributes you want to include

```typescript main.ts
const nftMetadata = {
  name: "Midnight Marriage",
  description:
    "This is a house-style song generated on suno. This NFT represents ownership of the IP Asset.",
  image:
    "https://cdn2.suno.ai/image_large_8bcba6bc-3f60-4921-b148-f32a59086a4c.jpeg",
  animation_url:
    "https://cdn1.suno.ai/dcd3076f-3aa5-400b-ba5d-87d30f27c311.mp3",
  attributes: [
    {
      key: "Suno Artist",
      value: "amazedneurofunk956",
    },
    {
      key: "Artist ID",
      value: "4123743b-8ba6-4028-a965-75b79a3ad424",
    },
    {
      key: "Source",
      value: "Suno.com",
    },
  ],
};
```

## 4. Done!

When you run the script, you will register an IP Asset and it will look something like [this](https://aeneid.explorer.story.foundation/ipa/0x70920EaC7F9748Ac5A71C82310f1ac1C7eD11f02) on our explorer.

You can see the explorer recognizes the metadata format, and you can play the song directly on the page!

<CardGroup cols={1}>
  <Card title="Learn More" href="/developers/tutorials" icon="book-open">
    Explore more tutorials in our documentation
  </Card>
</CardGroup>


# Finetune Images on Story

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/jacob-tucker/finetune-story-flux"
    icon="thumbs-up"
  >
    View the completed code for this tutorial.
  </Card>
</CardGroup>

In this tutorial, you will use the FLUX Finetuning API to take a bunch of images of Story's mascot "Ippy" and finetune an AI model to create similar images along with a prompt. Then you will monetize and protect the output IP on Story.

<Note>
**This Tutorial is in TypeScript**

Steps 1-3 of this tutorial are based on the [FLUX Finetuning Beta Guide](https://docs.bfl.ml/finetuning/), which contains examples for calling their API in Python, however I have rewritten them in TypeScript.

</Note>

## The Explanation

Generative text-to-image models often do not fully capture a creator's unique vision, and have insufficient knowledge about specific objects, brands or visual styles. With the FLUX Pro Finetuning API, creators can use existing images to finetune an AI to create similar images, along with a prompt.

When an image is created, we will register it as IP on Story in order to grow, monetize, and protect the IP.

## 0. Before you Start

There are a few steps you have to complete before you can start the tutorial.

1. You will need to install [Node.js](https://nodejs.org/en/download) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). If you've coded before, you likely have these.
2. Add your Story Network Testnet wallet's private key to `.env` file:

```yaml .env
WALLET_PRIVATE_KEY=
```

3. Go to [Pinata](https://pinata.cloud/) and create a new API key. Add the JWT to your `.env` file:

```yaml .env
PINATA_JWT=
```

4. Go to [BFL](https://api.us1.bfl.ai/auth/profile) and create a new API key. Add the new key to your `.env` file:

<Warning>
**BFL Credits**

In order to generate an image, you'll need BFL credits. If you just created an account, you will need to purchase credits [here](https://api.us1.bfl.ai/auth/profile).

You can also see the pricing for each of the API endpoints [here](https://docs.bfl.ml/pricing/).

</Warning>

```yaml .env
BFL_API_KEY=
```

5. Add your preferred Story RPC URL to your `.env` file. You can just use the public default one we provide:

```yaml .env
RPC_PROVIDER_URL=https://aeneid.storyrpc.io
```

6. Install the dependencies:

```bash Terminal
npm install @story-protocol/core-sdk axios pinata-web3 viem
```

## 1. Compile the Training Data

In order to create a finetune, we'll need the input training data!

1. Create a folder in your project called `images`. In that folder, add a bunch of images that you want your finetune to train on. _Supported formats: JPG, JPEG, PNG, and WebP. Also recommended to use more than 5 images._
2. Add Text Descriptions (Optional): In the same folder, create text files with descriptions for your images. Text files should share the same name as their corresponding images. _Example: if your image is "sample.jpg", create "sample.txt"_
3. Compress your folder into a ZIP file. It should be named `images.zip`

## 2. Create a Finetune

In order to generate an image using a similar style as input images, we need to create a **finetune**. Think of a finetune as an AI that knows all of your input images and can then start producing new ones.

Let's make a function that calls FLUX's `/v1/finetune` API route. Create a `flux` folder, and inside that folder add a file named `requestFinetuning.ts` and add the following code:

<Note>
**Official Docs**

In order to learn what each of the parameters in the payload are, see the official `/v1/finetune` API docs [here](https://api.us1.bfl.ai/scalar#tag/tasks/POST/v1/finetune).

</Note>

```typescript flux/requestFinetuning.ts
import axios from "axios";
import fs from "fs";

interface FinetunePayload {
  finetune_comment: string;
  trigger_word: string;
  file_data: string;
  iterations: number;
  mode: string;
  learning_rate: number;
  captioning: boolean;
  priority: string;
  lora_rank: number;
  finetune_type: string;
}

export async function requestFinetuning(
  zipPath: string,
  finetuneComment: string,
  triggerWord = "TOK",
  mode = "general",
  iterations = 300,
  learningRate = 0.00001,
  captioning = true,
  priority = "quality",
  finetuneType = "full",
  loraRank = 32
) {
  if (!fs.existsSync(zipPath)) {
    throw new Error(`ZIP file not found at ${zipPath}`);
  }

  const modes = ["character", "product", "style", "general"];
  if (!modes.includes(mode)) {
    throw new Error(`Invalid mode. Must be one of: ${modes.join(", ")}`);
  }

  const fileData = fs.readFileSync(zipPath);
  const encodedZip = Buffer.from(fileData).toString("base64");

  const url = "https://api.us1.bfl.ai/v1/finetune";
  const headers = {
    "Content-Type": "application/json",
    "X-Key": process.env.BFL_API_KEY,
  };

  const payload: FinetunePayload = {
    finetune_comment: finetuneComment,
    trigger_word: triggerWord,
    file_data: encodedZip,
    iterations,
    mode,
    learning_rate: learningRate,
    captioning,
    priority,
    lora_rank: loraRank,
    finetune_type: finetuneType,
  };

  try {
    const response = await axios.post(url, payload, { headers });
    return response.data;
  } catch (error) {
    throw new Error(`Finetune request failed: ${error}`);
  }
}
```

Next, create a file named `train.ts` and call the `requestFinetuning` function we just made:

<Warning>
**Warning: This is expensive!**

Creating a new finetune is expensive, ranging from $2-$6 at the time of me writing this tutorial. Please review the "FLUX PRO FINETUNE: TRAINING" section on the [pricing page](https://docs.bfl.ml/pricing/).

</Warning>

```typescript train.ts
import { requestFinetuning } from "./flux/requestFinetuning";

async function main() {
  const response = await requestFinetuning("./images.zip", "ippy-finetune");
  console.log(response);
}

main();
```

This will log something that looks like:

```json
{
  "finetune_id": "6fc5e628-6f56-48ec-93cb-c6a6b22bf5a"
}
```

This is your `finetune_id`, and will be used to create images in the following steps.

## 3. Wait for Finetune

Before we can generate images with our finetuned model, we have to wait for FLUX to finish training!

In our `flux` folder, create a file named `finetune-progress.ts` and add the following code:

<Note>
**Official Docs**

In order to learn what each of the parameters in the payload are, see the official `/v1/get_result` API docs [here](https://api.us1.bfl.ai/scalar#tag/utility/GET/v1/get_result).

</Note>

```typescript flux/finetuneProgress.ts
import axios from "axios";

export async function finetuneProgress(finetuneId: string) {
  const url = "https://api.us1.bfl.ai/v1/get_result";
  const headers = {
    "Content-Type": "application/json",
    "X-Key": process.env.BFL_API_KEY,
  };
  try {
    const response = await axios.get(url, {
      headers,
      params: { id: finetuneId },
    });
    return response.data;
  } catch (error) {
    throw new Error(`Finetune progress failed: ${error}`);
  }
}
```

Next, create a file named `finetune-progress.ts` and call the `finetuneProgress` function we just made:

```typescript finetune-progress.ts
import { finetuneProgress } from "./flux/finetuneProgress";

// input your finetune_id here
const FINETUNE_ID = "";

async function main() {
  const progress = await finetuneProgress(FINETUNE_ID);
  console.log(progress);
}

main();
```

This will log something that looks like:

```json
{
  "id": "023a1507-369e-46e0-bd6d-1f3446d7d5f2",
  "status": "Pending",
  "result": null,
  "progress": null
}
```

As you can see, the status is still pending. We must wait until the training is 'Ready' before we can move on to the next step.

## 4. Run Inference

<Warning>
**Warning: This costs money.**

Although very cheap, running an inference does cost money, ranging from $0.06-0.07 at the time of me writing this tutorial. Please review the "FLUX PRO FINETUNE: INFERENCE" section on the [pricing page](https://docs.bfl.ml/pricing/).

</Warning>

Now that we have trained a finetune, we will use the model to create images. "Running an inference" simply means using our new model (identified by its `finetune_id`), which is trained on our images, to create new images.

There are several different inference endpoints we can use, each with [their own pricing](https://docs.bfl.ml/pricing/) (found at the bottom of the page). For this tutorial, I'll be using the `/v1/flux-pro-1.1-ultra-finetuned` endpoint, which is documented [here](https://api.us1.bfl.ai/scalar#tag/tasks/POST/v1/flux-pro-1.1-ultra-finetuned).

In our `flux` folder, create a `finetuneInference.ts` file and add the following code:

<Note>
**Official Docs**

In order to learn what each of the parameters in the payload are, see the official `/v1/flux-pro-1.1-ultra-finetuned` API docs [here](https://api.us1.bfl.ai/scalar#tag/tasks/POST/v1/flux-pro-1.1-ultra-finetuned).

</Note>

```typescript flux/finetineInference.ts
import axios from "axios";

export async function finetuneInference(
  finetuneId: string,
  prompt: string,
  finetuneStrength = 1.2,
  endpoint = "flux-pro-1.1-ultra-finetuned",
  additionalParams: Record<string, any> = {}
) {
  const url = `https://api.us1.bfl.ai/v1/${endpoint}`;
  const headers = {
    "Content-Type": "application/json",
    "X-Key": process.env.BFL_API_KEY,
  };

  const payload = {
    finetune_id: finetuneId,
    finetune_strength: finetuneStrength,
    prompt,
    ...additionalParams,
  };

  try {
    const response = await axios.post(url, payload, { headers });
    return response.data;
  } catch (error) {
    throw new Error(`Finetune inference failed: ${error}`);
  }
}
```

Next, create a file named `inference.ts` and call the `finetuneInference` function we just made. The first parameter should be the `finetune_id` we got from running the script above, and the second parameter is a prompt to generate a new image.

```typescript inference.ts
import { finetuneInference } from "./flux/finetuneInference";

// input your finetune_id here
const FINETUNE_ID = "";
// add your prompt here
const PROMPT = "A picture of Ippy being really happy.";

async function main() {
  const inference = await finetuneInference(FINETUNE_ID, PROMPT);
  console.log(inference);
}

main();
```

This will log something that looks like:

```json
{
  "id": "023a1507-369e-46e0-bd6d-1f3446d7d5f2",
  "status": "Pending",
  "result": null,
  "progress": null
}
```

As you can see, the status is still pending. We must wait until the generation is ready to view our image. To do this, we will need a function to fetch our new inference to see if its ready and view the details about it.

In our `flux` folder, create a file named `getInference.ts` and add the following code:

<Note>
**Official Docs**

In order to learn what each of the parameters in the payload are, see the official `/v1/get_result` API docs [here](https://api.us1.bfl.ai/scalar#tag/utility/GET/v1/get_result).

</Note>

```typescript flux/getInference.ts
import axios from "axios";

export async function getInference(id: string) {
  const url = "https://api.us1.bfl.ai/v1/get_result";
  const headers = {
    "Content-Type": "application/json",
    "X-Key": process.env.BFL_API_KEY,
  };

  try {
    const response = await axios.get(url, { headers, params: { id } });
    return response.data;
  } catch (error) {
    throw new Error(`Inference retrieval failed: ${error}`);
  }
}
```

Back in our `inference.ts` file, lets add a loop that continuously fetches the inference until it's ready. When it's ready, we will view the new image.

```typescript inference.ts
import { finetuneInference } from "./flux/finetuneInference";
import { getInference } from "./flux/getInference";

// input your finetune_id here
const FINETUNE_ID = "";
// add your prompt here
const PROMPT = "A picture of Ippy being really happy.";

async function main() {
  const inference = await finetuneInference(FINETUNE_ID, PROMPT);

  let inferenceData = await getInference(inference.id);
  while (inferenceData.status != "Ready") {
    console.log("Waiting for inference to complete...");
    // wait 5 seconds
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // fetch the inference again
    inferenceData = await getInference(inference.id);
  }
  // now the inference data is ready
  console.log(inferenceData);
}

main();
```

Once the loop completed, the final log will look like:

```json
{
  "id": "023a1507-369e-46e0-bd6d-1f3446d7d5f2",
  "status": "Ready",
  "result": {
    "sample": "https://delivery-us1.bfl.ai/results/746585f8d1b341f3a8735ababa563ac1/sample.jpeg?se=2025-01-16T19%3A50%3A11Z&sp=r&sv=2024-11-04&sr=b&rsct=image/jpeg&sig=pPtWnntLqc49hfNnGPgTf4BzS6MZcBgHayrYkKe%2BZIc%3D",
    "prompt": "A picture of Ippy being really happy."
  },
  "progress": null
}
```

You can paste the `sample` into your browser and see the final result! Make sure to save this image as it will disappear eventually.

## 5. Set up your Story Config

Next we will register this image on Story as an [IP Asset](/concepts/ip-asset) in order to monetize and license the IP. Create a `story` folder and add a `utils.ts` file. In there, add the following code to set up your Story Config:

<Info>
  Associated docs: [TypeScript SDK Setup](/developers/typescript-sdk/setup)
</Info>

```typescript story/utils.ts
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";
import { http } from "viem";
import { privateKeyToAccount, Address, Account } from "viem/accounts";

const privateKey: Address = `0x${process.env.WALLET_PRIVATE_KEY}`;
export const account: Account = privateKeyToAccount(privateKey);

const config: StoryConfig = {
  account: account,
  transport: http(process.env.RPC_PROVIDER_URL),
  chainId: "aeneid",
};
export const client = StoryClient.newClient(config);
```

## 6. Upload Inference to IPFS

Now that we have made a new inference, we'll have to store the image `sample` file ourselves on IPFS because the sample is only temporary.

In a new `pinata` folder, create a `uploadToIpfs.ts` file and create a function to upload our image and get details about it:

```typescript pinata/uploadToIpfs.ts
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
});

export async function uploadImageAndGetDetails(
  imageUrl: string
): Promise<{ ipfsCid: string; contentType: string; contentHash: string }> {
  try {
    const response = await axios.get(imageUrl, {
      responseType: "arraybuffer",
      validateStatus: (status) => status === 200,
    });

    const contentType = response.headers["content-type"];
    if (!contentType?.startsWith("image/")) {
      throw new Error("URL does not point to an image");
    }

    const extension = contentType.split("/")[1];
    const filename = `${Date.now()}-${Math.random()
      .toString(36)
      .slice(2)}.${extension}`;

    const buffer = Buffer.from(response.data);
    const contentHash =
      "0x" + createHash("sha256").update(buffer).digest("hex");
    const file = new File([buffer], filename, { type: contentType });

    const { IpfsHash } = await pinata.upload.file(file);
    return { ipfsCid: IpfsHash, contentType, contentHash };
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(`Failed to fetch image: ${error.message}`);
    }
    throw error;
  }
}
```

We will now use this function in the following step.

## 7. Set up your IP Metadata

In your `story` folder, create a `registerIp.ts` file.

View the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard) and construct the metadata for your IP as shown below:

```typescript story/registerIp.ts
import { client, account } from "./utils";
import { uploadImageAndGetDetails } from "../pinata/uploadToIpfs";

export async function registerIp(inference) {
  const { ipfsCid, contentType, contentHash } = await uploadImageAndGetDetails(
    inference.result.sample
  );

  // Docs: https://docs.story.foundation/concepts/ip-asset/ipa-metadata-standard
  const ipMetadata = {
    title: "Happy Ippy",
    description:
      "An image of Ippy being really happy, generated by FLUX's 1.1 [pro] ultra Finetune",
    image: `https://ipfs.io/ipfs/${ipfsCid}`,
    imageHash: contentHash,
    mediaUrl: `https://ipfs.io/ipfs/${ipfsCid}`,
    mediaHash: contentHash,
    mediaType: contentType,
    creators: [
      {
        name: "Jacob Tucker",
        contributionPercent: 100,
        address: account.address,
      },
    ],
  };
}
```

## 8. Set up your NFT Metadata

In the `registerIp.ts` file, configure your NFT Metadata, which follows the [OpenSea ERC-721 Standard](https://docs.opensea.io/docs/metadata-standards).

```typescript story/registerIp.ts
import { client, account } from "./utils";
import { uploadImageAndGetDetails } from "../pinata/uploadToIpfs";

export async function registerIp(inference) {
  // previous code here...

  // Docs: https://docs.opensea.io/docs/metadata-standards
  const nftMetadata = {
    name: "Ippy Ownership NFT",
    description:
      "This NFT represents ownership of the Happy Ippy image generated by FLUX's 1.1 [pro] ultra Finetune",
    image: `https://ipfs.io/ipfs/${ipfsCid}`,
    attributes: [
      {
        key: "Model",
        value: "FLUX 1.1 [pro] ultra Finetune",
      },
      {
        key: "Prompt",
        value: "A picture of Ippy being really happy.",
      },
    ],
  };
}
```

## 9. Upload your IP and NFT Metadata to IPFS

In the `pinata` folder, create a function to upload your IP & NFT Metadata objects to IPFS:

```typescript pinata/uploadToIpfs.ts
// previous code here ...

export async function uploadJSONToIPFS(jsonMetadata: any): Promise<string> {
  const { IpfsHash } = await pinata.upload.json(jsonMetadata);
  return IpfsHash;
}
```

You can then use that function to upload your metadata, as shown below:

```typescript story/registerIp.ts
import { client, account } from "./utils";
import {
  uploadImageAndGetDetails,
  uploadJSONToIPFS,
} from "../pinata/uploadToIpfs";
import { createHash } from "crypto";

export async function registerIp(inference) {
  // previous code here...

  const ipIpfsHash = await uploadJSONToIPFS(ipMetadata);
  const ipHash = createHash("sha256")
    .update(JSON.stringify(ipMetadata))
    .digest("hex");
  const nftIpfsHash = await uploadJSONToIPFS(nftMetadata);
  const nftHash = createHash("sha256")
    .update(JSON.stringify(nftMetadata))
    .digest("hex");
}
```

## 10. Register the NFT as an IP Asset

Next we will mint an NFT, register it as an [IP Asset](/concepts/ip-asset), set [License Terms](/concepts/licensing-module/license-terms) on the IP, and then set both NFT & IP metadata.

Luckily, we can use the `mintAndRegisterIp` function to mint an NFT and register it as an IP Asset in the same transaction.

This function needs an SPG NFT Contract to mint from. For simplicity, you can use a public collection we have created for you on Aeneid testnet: `0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc`.

<Accordion title="Creating your own custom ERC-721 collection" icon="pen-circle">
  Using the public collection we provide for you is fine, but when you do this for real, you should make your own NFT Collection for your IPs. You can do this in 2 ways:

1. Deploy a contract that implements the [ISPGNFT](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/interfaces/ISPGNFT.sol) interface, or use the SDK's [createNFTCollection](/sdk-reference/nftclient#createnftcollection) function (shown below) to do it for you. This will give you your own SPG NFT Collection that only you can mint from.

   ```typescript createSpgNftCollection.ts
   import { zeroAddress } from "viem";
   import { client } from "./utils";

   async function createSpgNftCollection() {
     const newCollection = await client.nftClient.createNFTCollection({
       name: "Test NFTs",
       symbol: "TEST",
       isPublicMinting: false,
       mintOpen: true,
       mintFeeRecipient: zeroAddress,
       contractURI: "",
       txOptions: { waitForTransaction: true },
     });

     console.log(
       `New SPG NFT collection created at transaction hash ${newCollection.txHash}`
     );
     console.log(`NFT contract address: ${newCollection.spgNftContract}`);
   }

   createSpgNftCollection();
   ```

2. Create a custom ERC-721 NFT collection on your own and use the [register](/sdk-reference/ipasset#register) function - providing an `nftContract` and `tokenId` - _instead of_ using the `mintAndRegisterIp` function. See a working code example [here](https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/registration/registerCustom.ts). This is helpful if you **already have a custom NFT contract that has your own custom logic, or if your IPs themselves are NFTs.**

</Accordion>

<Info>
  Associated Docs:
  [ipAsset.mintAndRegisterIp](/sdk-reference/ipasset#mintandregisterip)
</Info>

```typescript story/registerIp.ts
import { client, account } from "./utils";
import {
  uploadImageAndGetDetails,
  uploadJSONToIPFS,
} from "../pinata/uploadToIpfs";
import { createHash } from "crypto";
import { Address } from "viem";

export async function registerIp(inference) {
  // previous code here ...

  const response = await client.ipAsset.mintAndRegisterIp({
    spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc",
    ipMetadata: {
      ipMetadataURI: `https://ipfs.io/ipfs/${ipIpfsHash}`,
      ipMetadataHash: `0x${ipHash}`,
      nftMetadataURI: `https://ipfs.io/ipfs/${nftIpfsHash}`,
      nftMetadataHash: `0x${nftHash}`,
    },
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `Root IPA created at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
  );
  console.log(
    `View on the explorer: https://aeneid.explorer.story.foundation/ipa/${response.ipId}`
  );
}
```

## 11. Register our Inference

Now that we have completed our `registerIp` function, let's add it to our `inference.ts` file:

```typescript inference.ts
import { finetuneInference } from "./flux/finetuneInference";
import { getInference } from "./flux/getInference";
import { registerIp } from "./story/registerIp";

const FINETUNE_ID = "";
const PROMPT = "A picture of Ippy being really happy.";

async function main() {
  const inference = await finetuneInference(FINETUNE_ID, PROMPT);

  let inferenceData = await getInference(inference.id);
  while (inferenceData.status != "Ready") {
    console.log("Waiting for inference to complete...");
    await new Promise((resolve) => setTimeout(resolve, 5000));
    inferenceData = await getInference(inference.id);
  }
  // now the inference data is ready
  console.log(inferenceData);

  // add the function here
  await registerIp(inferenceData);
}

main();
```

## 12. Done!

<CardGroup cols={2}>
  <Card
    title="Completed Code"
    href="https://github.com/jacob-tucker/finetune-story-flux"
    icon="thumbs-up"
  >
    View the completed code for this tutorial.
  </Card>
  <Card title="Learn More" href="/developers/tutorials" icon="book-open">
    Explore more tutorials in our documentation
  </Card>
</CardGroup>


# How to Tip an IP

- [Use the SDK](#using-the-sdk)
- [Use a Smart Contract](#using-a-smart-contract)

# Using the SDK

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercialCustom.ts"
    icon="thumbs-up"
  >
    See a completed, working example of setting up a simple derivative chain and
    then tipping the child IP Asset.
  </Card>
</CardGroup>

In this tutorial, you will learn how to send money ("tip") an IP Asset using the TypeScript SDK.

## The Explanation

In this scenario, let's say there is a parent IP Asset that represents Mickey Mouse. Someone else draws a hat on that Mickey Mouse and registers it as a derivative (or "child") IP Asset. The License Terms specify that the child must share 50% of all commercial revenue (`commercialRevShare = 50`) with the parent. Someone else (a 3rd party user) comes along and wants to send the derivative 2 $WIP for being really cool.

For the purposes of this example, we will assume the child is already registered as a derivative IP Asset. If you want help learning this, check out [Register a Derivative](/developers/typescript-sdk/register-derivative).

- Parent IP ID: `0x42595dA29B541770D9F9f298a014bF912655E183`
- Child IP ID: `0xeaa4Eed346373805B377F5a4fe1daeFeFB3D182a`

## 0. Before you Start

There are a few steps you have to complete before you can start the tutorial.

1. You will need to install [Node.js](https://nodejs.org/en/download) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). If you've coded before, you likely have these.
2. Add your Story Network Testnet wallet's private key to `.env` file:

```text env
WALLET_PRIVATE_KEY=<YOUR_WALLET_PRIVATE_KEY>
```

3. Add your preferred RPC URL to your `.env` file. You can just use the public default one we provide:

```text env
RPC_PROVIDER_URL=https://aeneid.storyrpc.io
```

4. Install the dependencies:

```bash Terminal
npm install @story-protocol/core-sdk viem
```

## 1. Set up your Story Config

In a `utils.ts` file, add the following code to set up your Story Config:

- Associated docs: [TypeScript SDK Setup](/developers/typescript-sdk/setup)

```typescript utils.ts
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";
import { http } from "viem";
import { privateKeyToAccount, Address, Account } from "viem/accounts";

const privateKey: Address = `0x${process.env.WALLET_PRIVATE_KEY}`;
export const account: Account = privateKeyToAccount(privateKey);

const config: StoryConfig = {
  account: account,
  transport: http(process.env.RPC_PROVIDER_URL),
  chainId: "aeneid",
};
export const client = StoryClient.newClient(config);
```

## 2. Tipping the Derivative IP Asset

Now create a `main.ts` file. We will use the `payRoyaltyOnBehalf` function to pay the derivative asset.

You will be paying the IP Asset with [$WIP](https://aeneid.storyscan.io/address/0x1514000000000000000000000000000000000000). **Note that if you don't have enough $WIP, the function will auto wrap an equivalent amount of $IP into $WIP for you.** If you don't have enough of either, it will fail.

<Note>
**Whitelisted Revenue Tokens**

Only tokens that are whitelisted by our protocol can be used as payment ("revenue") tokens. $WIP is one of those tokens. To see that list, go [here](/developers/deployed-smart-contracts).

</Note>

Now we can call the `payRoyaltyOnBehalf` function. In this case:

1. `receiverIpId` is the `ipId` of the derivative (child) asset
2. `payerIpId` is `zeroAddress` because the payer is a 3rd party (someone that thinks Mickey Mouse with a hat on him is cool), and not necessarily another IP Asset
3. `token` is the address of $WIP, which can be found [here](/concepts/royalty-module/ip-royalty-vault#whitelisted-revenue-tokens)
4. `amount` is 2, since the person tipping wants to send 2 $WIP

```typescript main.ts
import { client } from "./utils";
import { zeroAddress, parseEther } from "viem";
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";

async function main() {
  const response = await client.royalty.payRoyaltyOnBehalf({
    receiverIpId: "0xeaa4Eed346373805B377F5a4fe1daeFeFB3D182a",
    payerIpId: zeroAddress,
    token: WIP_TOKEN_ADDRESS,
    amount: parseEther("2"), // 2 $WIP
    txOptions: { waitForTransaction: true },
  });
  console.log(`Paid royalty at transaction hash ${response.txHash}`);
}

main();
```

## 3. Child Claiming Due Revenue

At this point we have already finished the tutorial: we learned how to tip an IP Asset. But what if the child and parent want to claim their due revenue?

The child has been paid 2 $WIP. But remember, it shares 50% of its revenue with the parent IP because of the `commercialRevenue = 50` in the license terms.

The child IP can claim its 1 $WIP by calling the `claimAllRevenue` function:

- `ancestorIpId` is the `ipId` of the IP Asset thats associated with the royalty vault that has the funds in it (more simply, this is just the child's `ipId`)
- `currencyTokens` is an array that contains the address of $WIP, which can be found [here](/concepts/royalty-module/ip-royalty-vault#whitelisted-revenue-tokens)
- `claimer` is the address that holds the royalty tokens associated with the child's [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault). By default, they are in the IP Account, which is just the `ipId` of the child asset

```typescript main.ts
import { client } from "./utils";
import { zeroAddress, parseEther } from "viem";
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";

async function main() {
  // previous code here ...
  const response = await client.royalty.claimAllRevenue({
    ancestorIpId: "0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2",
    claimer: "0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2",
    currencyTokens: [WIP_TOKEN_ADDRESS],
    childIpIds: [],
    royaltyPolicies: [],
  });

  console.log(`Claimed revenue: ${response.claimedTokens}`);
}

main();
```

## 4. Parent Claiming Due Revenue

Continuing, the parent should be able to claim its revenue as well. In this example, the parent should be able to claim 1 $WIP since the child earned 2 $WIP and the `commercialRevShare = 50` in the license terms.

We will use the `claimAllRevenue` function to claim the due revenue tokens.

1. `ancestorIpId` is the `ipId` of the parent ("ancestor") asset
2. `claimer` is the address that holds the royalty tokens associated with the parent's [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault). By default, they are in the IP Account, which is just the `ipId` of the parent asset
3. `childIpIds` will have the `ipId` of the child asset
4. `royaltyPolicies` will contain the address of the royalty policy. As explained in [Royalty Module](/concepts/royalty-module), this is either `RoyaltyPolicyLAP` or `RoyaltyPolicyLRP`, depending on the license terms. In this case, let's assume the license terms specify a `RoyaltyPolicyLAP`. Simply go to [Deployed Smart Contracts](/developers/deployed-smart-contracts) and find the correct address.
5. `currencyTokens` is an array that contains the address of $WIP, which can be found [here](/concepts/royalty-module/ip-royalty-vault#whitelisted-revenue-tokens)

```typescript main.ts
import { client } from "./utils";
import { zeroAddress, parseEther } from "viem";
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";

async function main() {
  // previous code here ...

  const response = await client.royalty.claimAllRevenue({
    ancestorIpId: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
    claimer: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
    currencyTokens: [WIP_TOKEN_ADDRESS],
    childIpIds: ["0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2"],
    royaltyPolicies: ["0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E"],
  });

  console.log(`Claimed revenue: ${response.claimedTokens}`);
}

main();
```

## 5. Done!

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercialCustom.ts"
    icon="thumbs-up"
  >
    See a completed, working example of setting up a simple derivative chain and
    then tipping the child IP Asset.
  </Card>
</CardGroup>

# Using a Smart Contract

<CardGroup cols={1}>
  <Card
    title="Go to Smart Contract Tutorial"
    href="/developers/smart-contracts-guide/claim-revenue"
    icon="house"
  >
    View the tutorial here!
  </Card>
</CardGroup>


# Protect DALL·E AI-Generated Images

In this tutorial, you will learn how to license and protect DALL·E 2 AI-Generated images by registering it on Story.

## The Explanation

Let's say you generate an image using AI. Without adding a proper license to your image, others could use it freely. In this tutorial, you will learn how to add a license to your DALL·E 2 AI-Generated image so that if others want to use it, they must properly license it from you.

In order to register that IP on Story, you first need to mint an NFT to represent that IP, and then register that NFT on Story, turning it into an [IP Asset](/concepts/ip-asset).

## 0. Before you Start

There are a few steps you have to complete before you can start the tutorial.

1. You will need to install [Node.js](https://nodejs.org/en/download) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). If you've coded before, you likely have these.
2. Add your Story Network Testnet wallet's private key to `.env` file:

```yaml .env
WALLET_PRIVATE_KEY=
```

3. Go to [Pinata](https://pinata.cloud/) and create a new API key. Add the JWT to your `.env` file:

```yaml .env
PINATA_JWT=
```

4. Go to [OpenAI](https://platform.openai.com/settings/organization/api-keys) and create a new API key. Add the new key to your `.env` file:

<Warning>
**OpenAI Credits**

In order to generate an image, you'll need OpenAI credits. If you just created an account, you will probably have a free trial that will give you a few credits to start with.

</Warning>

```yaml .env
OPENAI_API_KEY=
```

5. Add your preferred RPC URL to your `.env` file. You can just use the public default one we provide:

```yaml .env
RPC_PROVIDER_URL=https://aeneid.storyrpc.io
```

6. Install the dependencies:

```bash Terminal
npm install @story-protocol/core-sdk pinata-web3 viem openai
```

## 1. Generate an Image

In a `main.ts` file, add the following code to generate an image:

```typescript main.ts
import OpenAI from "openai";

async function main() {
  const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

  const image = await openai.images.generate({
    model: "dall-e-2",
    prompt: "A cute baby sea otter",
  });

  console.log(image.data[0].url); // the url to the newly created image
}

main();
```

## 2. Set up your Story Config

In a `utils.ts` file, add the following code to set up your Story Config:

<Info>
  Associated docs: [TypeScript SDK Setup](/developers/typescript-sdk/setup)
</Info>

```typescript utils.ts
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";
import { http } from "viem";
import { privateKeyToAccount, Address, Account } from "viem/accounts";

const privateKey: Address = `0x${process.env.WALLET_PRIVATE_KEY}`;
export const account: Account = privateKeyToAccount(privateKey);

const config: StoryConfig = {
  account: account,
  transport: http(process.env.RPC_PROVIDER_URL),
  chainId: "aeneid",
};
export const client = StoryClient.newClient(config);
```

## 3. Set up your IP Metadata

View the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard) and construct your metadata for your IP. Back in the `main.ts` file, properly format your metadata as shown below:

```typescript main.ts
import OpenAI from "openai";
import { client, account } from "./utils";

async function main() {
  // previous code here ...

  const ipMetadata = {
    title: "Baby Sea Otter",
    description: "A baby sea otter generated with DALL·E.",
    createdAt: "1728401700",
    image: image.data[0].url,
    imageHash: "0x...", // a hash of the image
    mediaUrl: image.data[0].url,
    mediaHash: "0x...", // a hash of the image
    mediaType: "image/png",
    creators: [
      {
        name: "Jacob Tucker",
        address: "0x67ee74EE04A0E6d14Ca6C27428B27F3EFd5CD084",
        description: "A cool dev rel person.",
        contributionPercent: 100,
        socialMedia: [
          {
            platform: "Twitter",
            url: "https://x.com/jacobmtucker",
          },
        ],
      },
    ],
  };
}

main();
```

## 4. Set up your NFT Metadata

The NFT Metadata follows the [ERC-721 Metadata Standard](https://eips.ethereum.org/EIPS/eip-721).

```typescript main.ts
import OpenAI from "openai";
import { client, account } from "./utils";

async function main() {
  // previous code here ...

  const nftMetadata = {
    name: "Image Ownership NFT",
    description:
      "This NFT represents ownership of the image generated by Dall-E 2",
    image: image.data[0].url,
    attributes: [
      {
        key: "Model",
        value: "dall-e-2",
      },
      {
        key: "Prompt",
        value: "A cute baby sea otter",
      },
    ],
  };
}

main();
```

## 5. Upload & Register IP

Now that we have all of our metadata set up, you can easily complete this tutorial by going to [Register an IP Asset](/developers/typescript-sdk/register-ip-asset#3-%5Boptional%5D-upload-your-ip-and-nft-metadata-to-ipfs) and **completing steps 3 (Upload your IP and NFT Metadata to IPFS) & 4 (Register an NFT as an IP Asset)**.

Once you have done that, you should see a console log with a link to our IP-explorer that shows your registered AI generated image.

## 6. Done!

<CardGroup cols={1}>
  <Card title="Learn More" href="/developers/tutorials" icon="book-open">
    Explore more tutorials in our documentation
  </Card>
</CardGroup>


# Overview

## Registration

- [How to Register IP on Story](/developers/tutorials/how-to-register-ip-on-story)
- [How to Register Music on Story](/developers/tutorials/how-to-register-music-on-story)
- [Case Study: Registering a Derivative of Ippy](/developers/tutorials/case-study-register-derivative-ippy)

## Royalty

- [How to Tip an IP](/developers/tutorials/how-to-tip-an-ip)

## AI-Themed

- [Protect DALL·E AI-Generated Images](/developers/tutorials/protect-dalle-ai-generated-images)
- [Register & Monetize Stability Images](/developers/tutorials/register-stability-images)
- [Finetune Images on Story](/developers/tutorials/finetune-images)

## Wallet-less / Onboarding

- [Email Login & Sponsored Transactions with Privy](/developers/tutorials/privy-tutorial)


# Releases

<CardGroup cols={1}>
  <Card
    title="SDK"
    href="https://github.com/storyprotocol/sdk/releases"
    icon="github"
    arrow={true}
  />

{" "}
<Card
  title="Deployed Smart Contract Addresses"
  href="/developers/deployed-smart-contracts"
  icon="file-contract"
/>

{" "}
<Card
  title="Protocol Core"
  href="https://github.com/storyprotocol/protocol-core-v1/releases"
  icon="github"
  arrow={true}
/>

{" "}
<Card
  title="Protocol Periphery"
  href="https://github.com/storyprotocol/protocol-periphery-v1/releases"
  icon="github"
  arrow={true}
/>

{" "}
<Card
  title="Story - Consensus Implementation"
  href="https://github.com/piplabs/story/releases"
  icon="github"
  arrow={true}
/>

  <Card
    title="Story Geth - Execution Layer Implementation"
    href="https://github.com/piplabs/story-geth/releases"
    icon="github"
    arrow={true}
  />
</CardGroup>


# Using the SDK in React

Once you have the SDK set up in React, you can use it just as we describe in the [TypeScript SDK Guide](/developers/typescript-sdk/overview).

<CardGroup cols={2}>
  <Card
    title="Working Code Example"
    href="https://github.com/jacob-tucker/story-developer-sandbox"
    icon="thumbs-up"
    
    
  >
    A working code example that shows setting up & calling TypeScript SDK functions in Next.js
  </Card>

  <Card
    title="SDK Reference"
    href="/sdk-reference"
    icon="books"
    
    
  >
    View the whole SDK reference, which shows examples and types for every function in our SDK.
  </Card>
</CardGroup>

## Prerequisites

1. Complete the [SDK setup in React](/developers/react-guide/setup)

## Example

Here is an example of calling an SDK function in React, which will look the same for any function you use:

```jsx TestComponent.tsx
import { custom, toHex } from 'viem';
import { useWalletClient } from "wagmi";
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";

// example of how you would now use the fully setup sdk

export default function TestComponent() {
  const { data: wallet } = useWalletClient();

  async function setupStoryClient(): Promise<StoryClient> {
    const config: StoryConfig = {
      wallet: wallet,
      transport: custom(wallet!.transport),
      chainId: "aeneid",
    };
    const client = StoryClient.newClient(config);
    return client;
  }

  async function registerIp() {
    const client = await setupStoryClient();
    const response = await client.ipAsset.mintAndRegisterIp({
      spgNftContract: '0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc',
      ipMetadata: {
        ipMetadataURI: "test-metadata-uri",
        ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
        nftMetadataURI: "test-nft-metadata-uri",
        nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      },
      txOptions: { waitForTransaction: true }
    });
    console.log(
      `Root IPA created at tx hash ${response.txHash}, IPA ID: ${response.ipId}`
    );
  }

  return (
    {/* */}
  )
}
```


# Tomo Setup

<Note>
**Optional: Official TomoEVMKit Docs**

Check out the official Wagmi + TomoEVMKit installation docs [here](https://docs.tomo.inc/tomo-sdk/tomoevmkit/quick-start).

</Note>

## Install the Dependencies

<CodeGroup>

```bash npm
npm install --save @story-protocol/core-sdk @tomo-inc/tomo-evm-kit wagmi viem @tanstack/react-query
```

```bash pnpm
pnpm install @story-protocol/core-sdk viem
```

```bash yarn
yarn add @story-protocol/core-sdk viem
```

</CodeGroup>

## Setup

Before diving into the example, make sure you have two things setup:

1. Make sure to have `NEXT_PUBLIC_RPC_PROVIDER_URL` set up in your `.env` file.
   - You can use the public default one (`https://aeneid.storyrpc.io`) or any other RPC [here](/network/network-info/aeneid#rpcs).
2. Make sure to have `NEXT_PUBLIC_TOMO_CLIENT_ID` set up in your `.env` file. Do this by logging into the [Tomo Dashboard](https://dashboard.tomo.inc/) and creating a project.
3. Make sure to have `NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID` set up in your `.env` file. Do this by logging into [Reown (prev. WalletConnect)](https://reown.com/) and creating a project.

<CodeGroup>

```jsx Web3Providers.tsx
"use client";
import '@tomo-inc/tomo-evm-kit/styles.css';
import { getDefaultConfig, TomoEVMKitProvider } from "@tomo-inc/tomo-evm-kit";
import { WagmiProvider } from "wagmi";
import { QueryClientProvider, QueryClient } from "@tanstack/react-query";
import { PropsWithChildren } from "react";
import { aeneid } from "@story-protocol/core-sdk";

const config = getDefaultConfig({
  appName: "Test Story App",
  clientId: process.env.NEXT_PUBLIC_TOMO_CLIENT_ID as string,
  projectId: process.env.NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID as string,
  chains: [aeneid],
  ssr: true, // If your dApp uses server side rendering (SSR)
});

const queryClient = new QueryClient();

export default function Web3Providers({ children }: PropsWithChildren) {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <TomoEVMKitProvider>
          {children}
        </TomoEVMKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

```jsx layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { PropsWithChildren } from "react";
import Web3Providers from "./Web3Providers";
import { useConnectModal } from "@tomo-inc/tomo-evm-kit";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Example",
  description: "This is an Example DApp",
};

export default function RootLayout({ children }: PropsWithChildren) {
  const { openConnectModal } = useConnectModal();

  return (
    <html lang="en">
      <body>
        <Web3Providers>
          <button onClick={openConnectModal}>Connect Wallet</button>
          {children}
        </Web3Providers>
      </body>
    </html>
  );
}
```

```jsx TestComponent.tsx
import { custom, toHex } from 'viem';
import { useWalletClient } from "wagmi";
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";

// example of how you would now use the fully setup sdk

export default function TestComponent() {
  const { data: wallet } = useWalletClient();

  async function setupStoryClient(): Promise<StoryClient> {
    const config: StoryConfig = {
      wallet: wallet,
      transport: custom(wallet!.transport),
      chainId: "aeneid",
    };
    const client = StoryClient.newClient(config);
    return client;
  }

  async function registerIp() {
    const client = await setupStoryClient();
    const response = await client.ipAsset.register({
      nftContract: '0x01...',
      tokenId: '1',
      ipMetadata: {
        ipMetadataURI: "test-metadata-uri",
        ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
        nftMetadataURI: "test-nft-metadata-uri",
        nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      },
      txOptions: { waitForTransaction: true },
    });
    console.log(
      `Root IPA created at tx hash ${response.txHash}, IPA ID: ${response.ipId}`
    );
  }

  return (
    {/* */}
  )
}
```

</CodeGroup>


# Reown (WalletConnect) Setup

<Note>
**Optional: Official WalletConnect Docs**

Check out the official Wagmi + Reown installation docs [here](https://docs.walletconnect.com/appkit/next/core/installation).

</Note>

## Install the Dependencies

<CodeGroup>

```bash npm
npm install --save @story-protocol/core-sdk @reown/appkit @reown/appkit-adapter-wagmi wagmi viem @tanstack/react-query
```

```bash pnpm
pnpm install @story-protocol/core-sdk viem
```

```bash yarn
yarn add @story-protocol/core-sdk viem
```

</CodeGroup>

## Setup

Before diving into the example, make sure you have two things setup:

1. Make sure to have `NEXT_PUBLIC_RPC_PROVIDER_URL` set up in your `.env` file.
   - You can use the public default one (`https://aeneid.storyrpc.io`) or any other RPC [here](/network/network-info/aeneid#rpcs).
2. Make sure to have `NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID` set up in your `.env` file. Do this by logging into [Reown (prev. WalletConnect)](https://reown.com/) and creating a project.

<CodeGroup>

```jsx config/index.tsx
import { cookieStorage, createStorage, http } from "@wagmi/core";
import { WagmiAdapter } from "@reown/appkit-adapter-wagmi";
import { mainnet, arbitrum } from "@reown/appkit/networks";
import { aeneid } from "@story-protocol/core-sdk";

// Get projectId from https://cloud.reown.com
export const projectId = process.env.NEXT_PUBLIC_PROJECT_ID;

if (!projectId) {
  throw new Error("Project ID is not defined");
}

export const networks = [aeneid];

//Set up the Wagmi Adapter (Config)
export const wagmiAdapter = new WagmiAdapter({
  storage: createStorage({
    storage: cookieStorage,
  }),
  ssr: true,
  projectId,
  networks,
});

export const config = wagmiAdapter.wagmiConfig;
```

```jsx context/index.tsx
'use client'

import { wagmiAdapter, projectId } from '@/config'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { createAppKit } from '@reown/appkit/react'
import { mainnet, arbitrum } from '@reown/appkit/networks'
import React, { type ReactNode } from 'react'
import { cookieToInitialState, WagmiProvider, type Config } from 'wagmi'

// Set up queryClient
const queryClient = new QueryClient()

if (!projectId) {
  throw new Error('Project ID is not defined')
}

// Set up metadata
const metadata = {
  name: 'appkit-example',
  description: 'AppKit Example',
  url: 'https://appkitexampleapp.com', // origin must match your domain & subdomain
  icons: ['https://avatars.githubusercontent.com/u/179229932']
}

// Create the modal
const modal = createAppKit({
  adapters: [wagmiAdapter],
  projectId,
  networks: [mainnet, arbitrum],
  defaultNetwork: mainnet,
  metadata: metadata,
  features: {
    analytics: true // Optional - defaults to your Cloud configuration
  }
})

function ContextProvider({ children, cookies }: { children: ReactNode; cookies: string | null }) {
  const initialState = cookieToInitialState(wagmiAdapter.wagmiConfig as Config, cookies)

  return (
    <WagmiProvider config={wagmiAdapter.wagmiConfig as Config} initialState={initialState}>
      <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
    </WagmiProvider>
  )
}

export default ContextProvider
```

```jsx app/layout.tsx
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

import { headers } from 'next/headers' // added
import ContextProvider from '@/context'

export const metadata: Metadata = {
  title: 'AppKit Example App',
  description: 'Powered by Reown'
}

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode
}>) {

  const headersObj = await headers();
  const cookies = headersObj.get('cookie')

  return (
    <html lang="en">
      <body className={inter.className}>
        <ContextProvider cookies={cookies}>
          <appkit-button />
          {children}
        </ContextProvider>
      </body>
    </html>
  )
}
```

```jsx TestComponent.tsx
import { custom, toHex } from 'viem';
import { useWalletClient } from "wagmi";
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";

// example of how you would now use the fully setup sdk

export default function TestComponent() {
  const { data: wallet } = useWalletClient();

  async function setupStoryClient(): Promise<StoryClient> {
    const config: StoryConfig = {
      wallet: wallet,
      transport: custom(wallet!.transport),
      chainId: "aeneid",
    };
    const client = StoryClient.newClient(config);
    return client;
  }

  async function registerIp() {
    const client = await setupStoryClient();
    const response = await client.ipAsset.register({
      nftContract: '0x01...',
      tokenId: '1',
      ipMetadata: {
        ipMetadataURI: "test-metadata-uri",
        ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
        nftMetadataURI: "test-nft-metadata-uri",
        nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      },
      txOptions: { waitForTransaction: true },
    });
    console.log(
      `Root IPA created at tx hash ${response.txHash}, IPA ID: ${response.ipId}`
    );
  }

  return (
    {/* */}
  )
}
```

</CodeGroup>


# RainbowKit Setup

<Note>
**Optional: Official RainbowKit Docs**

Check out the official Wagmi + RainbowKit installation docs [here](https://www.rainbowkit.com/docs/installation).

</Note>

## Install the Dependencies

<CodeGroup>

```bash npm
npm install --save @story-protocol/core-sdk @rainbow-me/rainbowkit wagmi viem @tanstack/react-query
```

```bash pnpm
pnpm install @story-protocol/core-sdk viem
```

```bash yarn
yarn add @story-protocol/core-sdk viem
```

</CodeGroup>

## Setup

Before diving into the example, make sure you have two things setup:

1. Make sure to have `NEXT_PUBLIC_RPC_PROVIDER_URL` set up in your `.env` file.
   - You can use the public default one (`https://aeneid.storyrpc.io`) or any other RPC [here](/network/network-info/aeneid#rpcs).
2. Make sure to have `NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID` set up in your `.env` file. Do this by logging into [Reown (prev. WalletConnect)](https://reown.com/) and creating a project.

<CodeGroup>

```jsx Web3Providers.tsx
"use client";
import "@rainbow-me/rainbowkit/styles.css";
import { getDefaultConfig, RainbowKitProvider } from "@rainbow-me/rainbowkit";
import { WagmiProvider } from "wagmi";
import { QueryClientProvider, QueryClient } from "@tanstack/react-query";
import { PropsWithChildren } from "react";
import { aeneid } from "@story-protocol/core-sdk";

const config = getDefaultConfig({
  appName: "Test Story App",
  projectId: process.env.NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID as string,
  chains: [aeneid],
  ssr: true, // If your dApp uses server side rendering (SSR)
});

const queryClient = new QueryClient();

export default function Web3Providers({ children }: PropsWithChildren) {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <RainbowKitProvider>
          {children}
        </RainbowKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

```jsx layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { PropsWithChildren } from "react";
import Web3Providers from "./Web3Providers";
import { ConnectButton } from "@rainbow-me/rainbowkit";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Example",
  description: "This is an Example DApp",
};

export default function RootLayout({ children }: PropsWithChildren) {
  return (
    <html lang="en">
      <body>
        <Web3Providers>
          <ConnectButton />
          {children}
        </Web3Providers>
      </body>
    </html>
  );
}
```

```jsx TestComponent.tsx
import { custom, toHex } from 'viem';
import { useWalletClient } from "wagmi";
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";

// example of how you would now use the fully setup sdk

export default function TestComponent() {
  const { data: wallet } = useWalletClient();

  async function setupStoryClient(): Promise<StoryClient> {
    const config: StoryConfig = {
      wallet: wallet,
      transport: custom(wallet!.transport),
      chainId: "aeneid",
    };
    const client = StoryClient.newClient(config);
    return client;
  }

  async function registerIp() {
    const client = await setupStoryClient();
    const response = await client.ipAsset.register({
      nftContract: '0x01...',
      tokenId: '1',
      ipMetadata: {
        ipMetadataURI: "test-metadata-uri",
        ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
        nftMetadataURI: "test-nft-metadata-uri",
        nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      },
      txOptions: { waitForTransaction: true },
    });
    console.log(
      `Root IPA created at tx hash ${response.txHash}, IPA ID: ${response.ipId}`
    );
  }

  return (
    {/* */}
  )
}
```

</CodeGroup>


# Dynamic Setup

<Note>
**Optional: Official Dynamic Docs**

Check out the official Wagmi + Dynamic installation docs [here](https://docs.dynamic.xyz/react-sdk/using-wagmi).

</Note>

## Install the Dependencies

<CodeGroup>

```bash npm
npm install --save @story-protocol/core-sdk viem wagmi @dynamic-labs/sdk-react-core @dynamic-labs/wagmi-connector @dynamic-labs/ethereum @tanstack/react-query
```

```bash pnpm
pnpm install @story-protocol/core-sdk viem
```

```bash yarn
yarn add @story-protocol/core-sdk viem
```

</CodeGroup>

## Setup

Before diving into the example, make sure you have two things setup:

1. Make sure to have `NEXT_PUBLIC_RPC_PROVIDER_URL` set up in your `.env` file.
   - You can use the public default one (`https://aeneid.storyrpc.io`) or any other RPC [here](/network/network-info/aeneid#rpcs).
2. Make sure to have `NEXT_PUBLIC_DYNAMIC_ENV_ID` set up in your `.env` file. Do this by logging into [Dynamic](https://app.dynamic.xyz/) and creating a project.

<CodeGroup>

```jsx Web3Providers.tsx
"use client";
import { createConfig, WagmiProvider } from "wagmi";
import { http } from 'viem';
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { DynamicContextProvider } from "@dynamic-labs/sdk-react-core";
import { DynamicWagmiConnector } from "@dynamic-labs/wagmi-connector";
import { EthereumWalletConnectors } from "@dynamic-labs/ethereum";
import { PropsWithChildren } from "react";
import { aeneid } from "@story-protocol/core-sdk";

// setup wagmi
const config = createConfig({
  chains: [aeneid],
  multiInjectedProviderDiscovery: false,
  transports: {
    [aeneid.id]: http(),
  },
});
const queryClient = new QueryClient();

export default function Web3Providers({ children }: PropsWithChildren) {
  return (
    // setup dynamic
    <DynamicContextProvider
      settings={{
        // Find your environment id at https://app.dynamic.xyz/dashboard/developer
        environmentId: process.env.NEXT_PUBLIC_DYNAMIC_ENV_ID as string,
        walletConnectors: [EthereumWalletConnectors],
      }}
    >
      <WagmiProvider config={config}>
        <QueryClientProvider client={queryClient}>
          <DynamicWagmiConnector>
            {children}
          </DynamicWagmiConnector>
        </QueryClientProvider>
      </WagmiProvider>
    </DynamicContextProvider>
  );
}
```

```jsx layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { PropsWithChildren } from "react";
import Web3Providers from "./Web3Providers";
import { DynamicWidget } from "@dynamic-labs/sdk-react-core";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Example",
  description: "This is an Example DApp",
};

export default function RootLayout({ children }: PropsWithChildren) {
  return (
    <html lang="en">
      <body>
        <Web3Providers>
          <DynamicWidget />
          {children}
        </Web3Providers>
      </body>
    </html>
  );
}
```

```jsx TestComponent.tsx
import { custom, toHex } from 'viem';
import { useWalletClient } from "wagmi";
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";

// example of how you would now use the fully setup sdk

export default function TestComponent() {
  const { data: wallet } = useWalletClient();

  async function setupStoryClient(): Promise<StoryClient> {
    const config: StoryConfig = {
      wallet: wallet,
      transport: custom(wallet!.transport),
      chainId: "aeneid",
    };
    const client = StoryClient.newClient(config);
    return client;
  }

  async function registerIp() {
    const client = await setupStoryClient();
    const response = await client.ipAsset.register({
      nftContract: '0x01...',
      tokenId: '1',
      ipMetadata: {
        ipMetadataURI: "test-metadata-uri",
        ipMetadataHash: toHex("test-metadata-hash", { size: 32 }),
        nftMetadataURI: "test-nft-metadata-uri",
        nftMetadataHash: toHex("test-nft-metadata-hash", { size: 32 }),
      },
      txOptions: { waitForTransaction: true },
    });
    console.log(
      `Root IPA created at tx hash ${response.txHash}, IPA ID: ${response.ipId}`
    );
  }

  return (
    {/* */}
  )
}
```

</CodeGroup>


# React Setup

We do not have a specific React SDK, however **we can use the TypeScript SDK in React** all the same, to delay signing & sending transactions to a JSON-RPC account like Metamask.

We recommend using [wagmi](https://wagmi.sh/) as a Web3 provider and then installing a wallet provider like Dynamic or RainbowKit. We provide examples for all of the following:

- [Dynamic Setup](/developers/react-guide/wallet-providers/dynamic-setup)
- [RainbowKit Setup](/developers/react-guide/wallet-providers/rainbowkit-setup)
- [Reown (WalletConnect) Setup](/developers/react-guide/wallet-providers/reown-setup)
- [Tomo Setup](/developers/react-guide/wallet-providers/tomo-setup)


# React Guide

The best way to get started is to get your hands dirty and start building.

<CardGroup cols={3}>

<Card
  title="Working Code Example"
  href="https://github.com/jacob-tucker/story-developer-sandbox"
  icon="thumbs-up"
>
  Clone our "developer sandbox" locally to see a working code example that shows
  setting up & calling TypeScript SDK functions in Next.js
</Card>

<Card
  title="Live Sandbox"
  href="https://sandbox.story.foundation"
  icon="umbrella-beach"
>
  Play around with a live version of our developer sandbox to get an
  introductory walkthrough of our SDK.
</Card>

<Card
  title="SDK Reference"
  href="/sdk-reference"
  icon="books"
  
  
>
  View the whole SDK reference, which shows examples and types for every function in our SDK.
</Card>
  
</CardGroup>

In the following series of tutorials, you will learn how to setup the TypeScript SDK in React.


# Raise a Dispute

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/dispute/disputeIp.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

This section demonstrates how to dispute an IP on Story. There are many instances where you may want to dispute an IP - whether that IP is or is not owned by you. Disputing IP on Story is easy thanks to our [Dispute Module](/concepts/dispute-module) and the [UMA Arbitration Policy](/concepts/dispute-module/uma-arbitration-policy).

Let's say you register a drawing, and then someone else registers that drawing with 1 pixel off. You can dispute it along a `IMPROPER_REGISTRATION` tag, which communicates potential plagiarism.

In this tutorial, you will simply learn how to flag an IP as being disputed.

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)
2. Have a basic understanding of the [Dispute Module](/concepts/dispute-module)

## 1. Dispute an IP

To dispute an IP Asset, you will need:

- The `targetIpId` of the IP Asset you are disputing (we use a test one below)
- The `targetTag` that you are applying to the dispute. Only [whitelisted tags](/concepts/dispute-module/overview#dispute-tags) can be applied.
- A `cid` (Content Identifier) is a unique identifier in IPFS that represents the dispute evidence you must provide, as described [here](/concepts/dispute-module/uma-arbitration-policy#dispute-evidence-submission-guidelines) (we use a test one below).

<Warning>
  **Note you can only provide a CID one time.** After it is used, it can't be
  used as evidence again.
</Warning>

Create a `main.ts` file and add the code below:

```typescript main.ts
import { client } from "./utils";
import { parseEther } from "viem";

async function main() {
  const disputeResponse = await client.dispute.raiseDispute({
    targetIpId: "0x6b42d065aDCDA6fA83B59ad731841360dC5321fB",
    // NOTE: you must use your own CID here, because every time it is used,
    // the protocol does not allow you to use it again
    cid: "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",
    // you must pick from one of the whitelisted tags here: https://docs.story.foundation/concepts/dispute-module#dispute-tags
    targetTag: "IMPROPER_REGISTRATION",
    bond: parseEther("0.1"), // minimum of 0.1
    liveness: 2592000,
    txOptions: { waitForTransaction: true },
  });
  console.log(
    `Dispute raised at transaction hash ${disputeResponse.txHash}, Dispute ID: ${disputeResponse.disputeId}`
  );
}

main();
```

## 2. View Completed Code

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/dispute/disputeIp.ts"
    icon="thumbs-up"
  >
    See a completed, working example disputing an IP.
  </Card>
</CardGroup>


# Mint a License Token

This section demonstrates how to mint a [License Token](/concepts/licensing-module/license-token) from an [IP Asset](/concepts/ip-asset). You can only mint a License Token from an IP Asset if the IP Asset has [License Terms](/concepts/licensing-module/license-terms) attached to it. A License Token is minted as an ERC-721.

There are two reasons you'd mint a License Token:

1. To hold the license and be able to use the underlying IP Asset as the license described (for ex. "Can use commercially as long as you provide proper attribution and share 5% of your revenue)
2. Use the license token to link another IP Asset as a derivative of it. _Note though that, as you'll see later, some SDK functions don't require you to explicitly mint a license token first in order to register a derivative, and will actually handle it for you behind the scenes._

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)
2. An IP Asset that has License Terms added. Learn how to add License Terms to an IPA [here](/developers/typescript-sdk/attach-terms).

## 1. Mint License

Let's say that IP Asset (`ipId = 0x01`) has License Terms (`licenseTermdId = 10`) attached to it. We want to mint 2 License Tokens with those terms to a specific wallet address (`0x02`).

<Warning>

Be mindful that some IP Assets may have license terms attached that require the user minting the license to pay a `defaultMintingFee`. You can see an example of that in the [TypeScript Tutorial](https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercialCustom.ts).

</Warning>

<Note>
 
  Note that a license token can only be minted if the `licenseTermsId` are already attached to the IP Asset, making it a publicly available license. The IP owner can, however, mint a [private license](/concepts/licensing-module/license-token#private-licenses) by minting a license token with a `licenseTermsId` that is not attached to the IP Asset.

</Note>

<Info>
  Associated Docs:
  [license.mintLicenseTokens](/sdk-reference/license#mintlicensetokens)
</Info>

```typescript main.ts
// you should already have a client set up (prerequisite)
import { client } from "./client";

async function main() {
  const response = await client.license.mintLicenseTokens({
    licenseTermsId: "10",
    licensorIpId: "0x641E638e8FCA4d4844F509630B34c9D524d40BE5",
    receiver: "0x641E638e8FCA4d4844F509630B34c9D524d40BE5", // optional. if not provided, it will go to the tx sender
    amount: 2,
    maxMintingFee: BigInt(0), // disabled
    maxRevenueShare: 100, // default
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `License Token minted at transaction hash ${response.txHash}, License IDs: ${response.licenseTokenIds}`
  );
}

main();
```

### 1a. Setting Restrictions on Minting License Token

This is a note for owners of an IP Asset who want to set restrictions on who or how their license tokens are minted. You can:

- Set a max number of licenses that can be minted
- Charge dynamic fees based on who / how many are minted
- Whitelisted certain wallets to mint the tokens

... and more. Learn more by checking out the [License Config](/concepts/licensing-module/license-config) section of our documentation.

## 2. Register a Derivative

Now that we have minted a License Token, we can hold it or use it to link an IP Asset as a derivative. We will go over that on the next page.

_Note though that, as you'll see later, some SDK functions don't require you to explicitly mint a license token first in order to register a derivative, and will actually handle it for you behind the scenes._

### 2a. Why would I ever use a License Token if it's not needed?

There are a few times when **you would need** a License Token to register a derivative:

- The License Token contains private license terms, so you would only be able to register as a derivative if you had the License Token that was manually minted by the owner. More on that [here](/concepts/licensing-module/license-token#private-licenses).
- The License Token (which is an NFT) costs a `mintingFee` to mint, and you were able to buy it on a marketplace for a cheaper price. Then it makes more sense to simply register with the License Token then have to pay the more expensive `defaultMintingFee`.


# Claim Revenue

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercial.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

This section demonstrates how to claim due revenue from an IP Asset.

There are two main ways revenue can be claimed:

1. **Scenario #1**: Someone pays my IP Asset directly, and I claim that revenue.
2. **Scenario #2**: Someone pays a derivative IP Asset of my IP, and I have the right to a % of their revenue based on the `commercialRevShare` in the license terms.

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)
2. Have a basic understanding of the [Royalty Module](/concepts/royalty-module)
3. Obviously, there must be a payment to be claimed. Read [Pay an IPA](/developers/typescript-sdk/pay-ipa)

## Before We Start

When payments are made, they eventually end up in an IP Asset's [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault). From here, they are claimed/transferred to whoever owns the Royalty Tokens associated with it, which represent a % of revenue share for a given IP Asset's IP Royalty Vault.

The IP Account (the smart contract that represents the [IP Asset](/concepts/ip-asset)) is what holds 100% of the Royalty Tokens when it's first registered. So usually, it indeed holds most of the Royalty Tokens.

<Note>
**Quick Note**. The below scenarios and examples use a [Liquid Absolute Percentage](/concepts/royalty-module/liquid-absolute-percentage) royalty policy. This is currently one of two royalty policies you can use.

</Note>

## Scenario #1

In this scenario, I own IP Asset 3. Someone pays my IP Asset 3 directly, and I claim that revenue. Let's view this in steps:

1. As we can see in the below diagram, when IP Asset 4 (it doesn't have to be an IP Asset, it can be any address) pays IP Asset 3 1M \$WIP, 850k \$WIP automatically gets deposited into IP Royalty Vault 3.

   <Frame>
     <img
       src="/images/concepts/lap-1.png"
       alt="Payment flow to IP Royalty Vault"
     />
   </Frame>

2. Now, IP Asset 3 wants to claim its revenue sitting in the IP Royalty Vault 3. It will look like this:

   <Frame>
     <img
       src="/images/concepts/lap-3.png"
       alt="Claiming revenue from IP Royalty Vault"
     />
   </Frame>

Below is how IP Asset 3 would claim their revenue, as shown in the image above, with the SDK:

<Info>
  Associated Docs:
  [royalty.claimAllRevenue](/sdk-reference/royalty#claimallrevenue)
</Info>

```typescript main.ts
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
// you should already have a client set up (prerequisite)
import { client } from "./client";

async function main() {
  const claimRevenue = await client.royalty.claimAllRevenue({
    // IP Asset 3's ipId
    ancestorIpId: "0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2",
    // whoever owns the royalty tokens associated with IP Royalty Vault 3
    // (most likely the associated ipId, which is IP Asset 3's ipId)
    claimer: "0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2",
    currencyTokens: [WIP_TOKEN_ADDRESS],
    childIpIds: [],
    royaltyPolicies: [],
    claimOptions: {
      // If the wallet claiming the revenue is the owner of the
      // IP Account/IP Asset (in other words, the owner of the
      // IP's underlying NFT), `claimAllRevenue` will transfer all
      // earnings to the user's external wallet holding the NFT
      // instead of the IP Account, for convenience. You can disable it here.
      autoTransferAllClaimedTokensFromIp: true,
      // Unwraps the claimed $WIP to $IP for you
      autoUnwrapIpTokens: true,
    },
  });

  console.log(`Claimed revenue: ${claimRevenue.claimedTokens}`);
}

main();
```

## Scenario #2

In this scenario, I own IP Asset 1. Someone pays a derivative IP Asset 3, and I have the right to a % of their revenue based on the `commercialRevShare` in the license terms. This is exactly the same as Scenario #1, except one extra step is added. Let's view this in steps:

1. As we can see in the below diagram, when IP Asset 4 (it doesn't have to be an IP Asset, it can be any address) pays IP Asset 3 1M \$WIP, 150k \$WIP automatically gets deposited to the LAP royalty policy contract to be distributed to ancestors.

   <Frame>
     <img
       src="/images/concepts/lap-1.png"
       alt="Revenue distribution to royalty policy contract"
     />
   </Frame>

2. Then, in a second step, the tokens are transferred to the ancestors' [IP Royalty Vault](/concepts/royalty-module/ip-royalty-vault) based on the negotiated `commercialRevShare` in the license terms.

   <Frame>
     <img
       src="/images/concepts/lap-2.png"
       alt="Revenue distribution to ancestors"
     />
   </Frame>

3. Lastly, IP Asset 1 & 2 want to claim their revenue sitting in their associated IP Royalty Vaults. It will look like this:

   <Frame>
     <img
       src="/images/concepts/lap-3.png"
       alt="Claiming revenue from ancestor IP Royalty Vaults"
     />
   </Frame>

Below is how IP Asset 1 (or 2) would claim their revenue, as shown in the image above, with the SDK:

<Info>
  Associated Docs:
  [royalty.claimAllRevenue](/sdk-reference/royalty#claimallrevenue)
</Info>

```typescript main.ts
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
// you should already have a client set up (prerequisite)
import { client } from "./client";

async function main() {
  const claimRevenue = await client.royalty.claimAllRevenue({
    // IP Asset 1's ipId
    ancestorIpId: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
    // whoever owns the royalty tokens associated with IP Royalty Vault 1
    // (most likely the associated ipId, which is IP Asset 1's ipId)
    claimer: "0x089d75C9b7E441dA3115AF93FF9A855BDdbfe384",
    currencyTokens: [WIP_TOKEN_ADDRESS],
    // IP Asset 3's ipId
    childIpIds: ["0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2"],
    // Aeneid testnet address of RoyaltyPolicyLAP
    royaltyPolicies: ["0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E"],
    claimOptions: {
      // If the wallet claiming the revenue is the owner of the
      // IP Account/IP Asset (in other words, the owner of the
      // IP's underlying NFT), `claimAllRevenue` will transfer all
      // earnings to the user's external wallet holding the NFT
      // instead of the IP Account, for convenience. You can disable it here.
      autoTransferAllClaimedTokensFromIp: true,
      // Unwraps the claimed $WIP to $IP for you
      autoUnwrapIpTokens: true,
    },
  });

  console.log(`Claimed revenue: ${claimRevenue.claimedTokens}`);
}

main();
```

## View Completed Code

Congratulations, you claimed revenue using the [Royalty Module](/concepts/royalty-module)!

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercial.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

## Dispute an IP

Now what happens if an IP Asset doesn't pay their due share? We can dispute the IP on-chain, which we will cover on the next page.


# Register an IP Asset

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/registration/register.ts"
    icon="thumbs-up"
  >
    Follow the completed code all the way through.
  </Card>
</CardGroup>

Let's say you have some off-chain IP (ex. a book, a character, a drawing, etc). In order to register that IP on Story, you first need to mint an NFT. This NFT is the **ownership** over the IP. Then you **register** that NFT on Story, turning it into an [IP Asset](/concepts/ip-asset). The below tutorial will walk you through how to do this.

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)
2. \[OPTIONAL] Go to [Pinata](https://pinata.cloud/) and create a new API key. Add the JWT to your `.env` file:

```text .env
PINATA_JWT=<YOUR_PINATA_JWT>
```

3. \[OPTIONAL] Install the `pinata-web3` dependency:

```bash Terminal
npm install pinata-web3
```

## 1. \[OPTIONAL] Set up your IP Metadata

We can set metadata on our NFT & IP, _but you don't have to_. To do this, view the [IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard) and construct your metadata for both your NFT & IP.

```typescript main.ts
// you should already have a client set up (prerequisite)
import { client } from "./utils";

async function main() {
  const ipMetadata = {
    title: "Ippy",
    description: "Official mascot of Story.",
    image:
      "https://ipfs.io/ipfs/QmSamy4zqP91X42k6wS7kLJQVzuYJuW2EN94couPaq82A8",
    imageHash:
      "0x21937ba9d821cb0306c7f1a1a2cc5a257509f228ea6abccc9af1a67dd754af6e",
    mediaUrl:
      "https://ipfs.io/ipfs/QmSamy4zqP91X42k6wS7kLJQVzuYJuW2EN94couPaq82A8",
    mediaHash:
      "0x21937ba9d821cb0306c7f1a1a2cc5a257509f228ea6abccc9af1a67dd754af6e",
    mediaType: "image/png",
    creators: [
      {
        name: "Story Foundation",
        address: "0x67ee74EE04A0E6d14Ca6C27428B27F3EFd5CD084",
        description: "The World's IP Blockchain",
        contributionPercent: 100,
        socialMedia: [
          {
            platform: "Twitter",
            url: "https://twitter.com/storyprotocol",
          },
          {
            platform: "Website",
            url: "https://story.foundation",
          },
        ],
      },
    ],
  };
}

main();
```

## 2. \[OPTIONAL] Set up your NFT Metadata

The NFT Metadata follows the [ERC-721 Metadata Standard](https://eips.ethereum.org/EIPS/eip-721).

```typescript main.ts
import { IpMetadata } from "@story-protocol/core-sdk";
import { client } from "./utils";

async function main() {
  // previous code here ...

  const nftMetadata = {
    name: "Ownership NFT",
    description: "This is an NFT representing owernship of our IP Asset.",
    image: "https://picsum.photos/200",
  };
}

main();
```

## 3. \[OPTIONAL] Upload your IP and NFT Metadata to IPFS

In a separate `uploadToIpfs` file, create a function to upload your IP & NFT Metadata objects to IPFS:

```typescript uploadToIpfs.ts
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
});

export async function uploadJSONToIPFS(jsonMetadata: any): Promise<string> {
  const { IpfsHash } = await pinata.upload.json(jsonMetadata);
  return IpfsHash;
}
```

You can then use that function to upload your metadata, as shown below:

```typescript main.ts
import { IpMetadata } from "@story-protocol/core-sdk";
import { client } from "./utils";
import { uploadJSONToIPFS } from "./uploadToIpfs";
import { createHash } from "crypto";

async function main() {
  // previous code here ...

  const ipIpfsHash = await uploadJSONToIPFS(ipMetadata);
  const ipHash = createHash("sha256")
    .update(JSON.stringify(ipMetadata))
    .digest("hex");
  const nftIpfsHash = await uploadJSONToIPFS(nftMetadata);
  const nftHash = createHash("sha256")
    .update(JSON.stringify(nftMetadata))
    .digest("hex");
}

main();
```

## 4. Register an NFT as an IP Asset

Remember that in order to register a new IP, we first have to mint an NFT, which will represent the underlying ownership of the IP. This NFT then gets "registered" and becomes an [IP Asset](/concepts/ip-asset).

Luckily, we can use the `mintAndRegisterIp` function to mint an NFT and register it as an IP Asset in the same transaction.

This function needs an SPG NFT Contract to mint from.

### 4a. What SPG NFT contract address should I use?

For simplicity, you can use a public collection we have created for you on Aeneid testnet: `0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc`. On Mainnet, or even when testing a real scenario on Aeneid, you should **create your own** contract as described in the "Using a custom ERC-721 contract" section below.

<Accordion title="Using a custom ERC-721 contract" icon="info">
  Using a public collection we provide for you is fine, but when you do this for real, you should make your own NFT Collection for your IPs. You can do this in 2 ways:

1. Deploy a contract that implements the [ISPGNFT](https://github.com/storyprotocol/protocol-periphery-v1/blob/main/contracts/interfaces/ISPGNFT.sol) interface, or use the SDK's [createNFTCollection](/sdk-reference/nftclient#createnftcollection) function (shown below) to do it for you. This will give you your own SPG NFT Collection that only you can mint from.

```typescript createSpgNftCollection.ts
import { zeroAddress } from "viem";
import { client } from "./utils";

async function createSpgNftCollection() {
  const newCollection = await client.nftClient.createNFTCollection({
    name: "Test NFTs",
    symbol: "TEST",
    isPublicMinting: false,
    mintOpen: true,
    mintFeeRecipient: zeroAddress,
    contractURI: "",
    txOptions: { waitForTransaction: true },
  });

  console.log("New collection created:", {
    "SPG NFT Contract Address": newCollection.spgNftContract,
    "Transaction Hash": newCollection.txHash,
  });
}

createSpgNftCollection();
```

2. Create a custom ERC-721 NFT collection on your own and use the [register](/sdk-reference/ipasset#register) function - providing an `nftContract` and `tokenId` - _instead of_ using the `mintAndRegisterIp` function. See a working code example [here](https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/registration/registerCustom.ts). This is helpful if you **already have a custom NFT contract that has your own custom logic, or if your IPs themselves are NFTs.**

</Accordion>

Here is the code to register an IP:

<Info>
  Associated Docs:
  [ipAsset.mintAndRegisterIp](/sdk-reference/ipasset#mintandregisterip)
</Info>

```typescript main.ts
import { IpMetadata } from "@story-protocol/core-sdk";
import { client } from "./utils";
import { uploadJSONToIPFS } from "./uploadToIpfs";
import { createHash } from "crypto";
import { Address } from "viem";

async function main() {
  // previous code here ...

  const response = await client.ipAsset.mintAndRegisterIp({
    spgNftContract: "0xc32A8a0FF3beDDDa58393d022aF433e78739FAbc",
    ipMetadata: {
      ipMetadataURI: `https://ipfs.io/ipfs/${ipIpfsHash}`,
      ipMetadataHash: `0x${ipHash}`,
      nftMetadataURI: `https://ipfs.io/ipfs/${nftIpfsHash}`,
      nftMetadataHash: `0x${nftHash}`,
    },
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `Root IPA created at transaction hash ${response.txHash}, IPA ID: ${response.ipId}`
  );
  console.log(
    `View on the explorer: https://aeneid.explorer.story.foundation/ipa/${response.ipId}`
  );
}

main();
```

## 5. View Completed Code

Congratulations, you registered an IP!

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/registration/register.ts"
    icon="thumbs-up"
  >
    Follow the completed code all the way through.
  </Card>
</CardGroup>

## 6. Add License Terms to IP

Now that your IP is registered, you can create and attach [License Terms](/concepts/licensing-module/license-terms) to it. This will allow others to mint a license and use your IP, restricted by the terms.

We will go over this in the next section, but it's worth mentioning that instead of using the `mintAndRegisterIp` function, you can **register IP + create terms + attach terms** all in the same step with the following functions:

- [mintAndRegisterIpAssetWithPilTerms](/sdk-reference/ipasset#mintandregisteripassetwithpilterms)
- [registerIpAndAttachPilTerms](/sdk-reference/ipasset#registeripandattachpilterms)


# Setup

### Prerequisites

We require node version 18 or later version and npm version 8 to be installed in your environment. To install node and npm, we recommend you go to the [Node.js official website](https://nodejs.org) and download the latest LTS (Long Term Support) version.

### Install the Dependencies

Install the [Story SDK](https://www.npmjs.com/package/@story-protocol/core-sdk) node package, as well as [viem](https://www.npmjs.com/package/viem).

<CodeGroup>

```bash npm
npm install --save @story-protocol/core-sdk viem
```

```bash pnpm
pnpm install @story-protocol/core-sdk viem
```

```bash yarn
yarn add @story-protocol/core-sdk viem
```

</CodeGroup>

## Initiate SDK Client

Next we can initiate the SDK Client. There are two ways to do this:

1. Using a private key (preferable for some backend admin)
2. JSON-RPC account like Metamask where users sign their own transactions

### Set Up Private Key Account

<CardGroup cols={1}>
  <Card
    title="Working Example"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/utils/config.ts"
    icon="thumbs-up"
  >
    Check out the TypeScript Tutorial for a working example of how to set up the
    Story SDK Client.
  </Card>
</CardGroup>

Before continuing with the code below:

1. Make sure to have `WALLET_PRIVATE_KEY` set up in your `.env` file.
2. Make sure to have `RPC_PROVIDER_URL` set up in your `.env` file.
   - You can use the public default one (`https://aeneid.storyrpc.io`) or check out the other RPCs [here](/network/network-info/aeneid#rpcs).

```typescript utils.ts
import { http } from "viem";
import { Account, privateKeyToAccount, Address } from "viem/accounts";
import { StoryClient, StoryConfig } from "@story-protocol/core-sdk";

const privateKey: Address = `0x${process.env.WALLET_PRIVATE_KEY}`;
const account: Account = privateKeyToAccount(privateKey);

const config: StoryConfig = {
  account: account, // the account object from above
  transport: http(process.env.RPC_PROVIDER_URL),
  chainId: "aeneid",
};
export const client = StoryClient.newClient(config);
```

### Setup for React (ex. Metamask)

The [React Setup Guide](/developers/react-guide/setup) shows how we can also use the TypeScript SDK to delay signing & sending transactions to a JSON-RPC account like Metamask.


# Register a Derivative

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercial.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

This section demonstrates how to register an IP Asset as a derivative of another.

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)

## 1. Before We Start

There are a lot of ways to register an IP Asset as a derivative of another. Below, we will help you figure out what function you should use.

<Note>

**Have no idea?** It is best to figure out which SDK function to use based on what is easiest for you. But if you have no idea, simply continue to the next section.

</Note>

<Tip>
By the way we recognize this is confusing and are releasing an update to our SDK soon to combine all of these into 1 simple function. :\)

</Tip>

Do you already have a [License Token](/concepts/licensing-module/license-token) you can use?

- ✅ Yes: Is the derivative IP Asset already registered?
  - ✅ Yes: Use [registerDerivativeWithLicenseTokens](/sdk-reference/ipasset#registerderivativewithlicensetokens)
  - ❌ No: Do you have your own NFT contract, or an already minted NFT?
    - ✅ Yes: Use [registerIpAndMakeDerivativeWithLicenseTokens](/sdk-reference/ipasset#registeripandmakederivativewithlicensetokens)
    - ❌ No: Use [mintAndRegisterIpAndMakeDerivativeWithLicenseTokens](/sdk-reference/ipasset#mintandregisteripandmakederivativewithlicensetokens)
- ❌ No: Is the derivative IP Asset already registered?
  - ✅ Yes: Use [registerDerivative](/sdk-reference/ipasset#registerderivative)
  - ❌ No: Do you have your own NFT contract, or an already minted NFT?
    - ✅ Yes: Use [registerDerivativeIp](/sdk-reference/ipasset#registerderivativeip)
    - ❌ No: Use [mintAndRegisterIpAndMakeDerivative](/sdk-reference/ipasset#mintandregisteripandmakederivative)

### 1a. Why would I ever use a License Token if it's not needed?

There are a few times when **you would need** a License Token to register a derivative:

- The License Token contains private license terms, so you would only be able to register as a derivative if you had the License Token that was manually minted by the owner. More on that [here](/concepts/licensing-module/license-token#private-licenses).
- The License Token (which is an NFT) costs a `mintingFee` to mint, and you were able to buy it on a marketplace for a cheaper price. Then it makes more sense to simply register with the License Token then have to pay the more expensive `defaultMintingFee`.

## 2. Register Derivative

<Note>
**This is just an example**. You are encouraged to figure out the best derivative function to use based on the survey above. However, if you don't know and want to be walked through one solution, this next part is for you.

</Note>

We're going to assume you have ❌ no license tokens, ❌ the derivative IP is not yet registered, and ❌ you don't have your own NFT contract or an already minted NFT.

**Follow steps 1-4 of** [Register an IP Asset](/developers/typescript-sdk/register-ip-asset). Note you can skip step 4 if you already have an SPG NFT Collection. Then, come back here.

Modify your code such that...

1. Instead of using `mintAndRegisterIp`, use `mintAndRegisterIpAndMakeDerivative`
2. Add a `derivData` field, where:
   - `parentIpIds` is the `ipIds` of the parents you want to become a derivative of. **NOTE: Once you become a derivative, you cannot add more parents**
   - `licenseTermIds` is an array of license terms you want to register under. These are the terms your derivative must abide by

Now we can call the function like so:

<Info>
  Associated Docs:
  [ipAsset.mintAndRegisterIpAndMakeDerivative](/sdk-reference/ipasset#mintandregisteripandmakederivative)
</Info>

```typescript main.ts
import { IpMetadata, DerivativeData } from "@story-protocol/core-sdk";
import { client } from "./utils";
import { uploadJSONToIPFS } from "./uploadToIpfs";
import { createHash } from "crypto";
import { Address } from "viem";

async function main() {
  // previous code here ...

  const derivData: DerivativeData = {
    // TODO: insert the parent's ipId
    parentIpIds: [PARENT_IP_ID],
    // TODO: insert the licenseTermsId attached to parent IpId
    licenseTermsIds: [LICENSE_TERMS_ID],
  };

  const response = await client.ipAsset.mintAndRegisterIpAndMakeDerivative({
    // TODO: insert your NFT contract address created by the SPG
    spgNftContract: SPG_NFT_CONTRACT_ADDRESS as Address,
    derivData,
    ipMetadata: {
      ipMetadataURI: `https://ipfs.io/ipfs/${ipIpfsHash}`,
      ipMetadataHash: `0x${ipHash}`,
      nftMetadataURI: `https://ipfs.io/ipfs/${nftIpfsHash}`,
      nftMetadataHash: `0x${nftHash}`,
    },
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `Completed at transaction hash ${response.txHash}, IPA ID: ${response.ipId}, Token ID: ${response.tokenId}`
  );
}
```

## 3. View Completed Code

Congratulations, you registered a derivative IP Asset!

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercial.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

## 4. Paying and Claiming Revenue

Now that we have established parent-child IP relationships, we can begin to explore payments and automated revenue share based on the license terms. We'll cover that in the upcoming pages.


# Pay an IPA

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercial.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

This section demonstrates how to pay an IP Asset. There are a few reasons you would do this:

1. You simply want to "tip" an IP
2. You have to because your license terms with an ancestor IP require you to forward a certain % of payment

In either scenario, you would use the below `payRoyaltyOnBehalf` function. When this happens, the [Royalty Module](/concepts/royalty-module) automatically handles the different payment flows such that parent IP Assets who have negotiated a certain `commercialRevShare` with the IPA being paid can claim their due share.

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)
2. Have a basic understanding of the [Royalty Module](/concepts/royalty-module)

## Before We Start

You can pay an IP Asset using the `payRoyaltyOnBehalf` function.

You will be paying the IP Asset with [\$WIP](https://aeneid.storyscan.io/address/0x1514000000000000000000000000000000000000). **Note that if you don't have enough \$WIP, the function will auto wrap an equivalent amount of \$IP into \$WIP for you.** If you don't have enough of either, it will fail.

To help with the following scenarios, let's say we have a parent IP Asset that has negotiated a 50% `commercialRevShare` with its child IP Asset.

### Whitelisted Revenue Tokens

Only tokens that are whitelisted by our protocol can be used as payment ("revenue") tokens. \$WIP is one of those tokens. To see that list, go [here](/developers/deployed-smart-contracts#whitelisted-revenue-tokens).

<Tip>

If you want to test paying IP Assets, you'll probably want a whitelisted revenue token you can mint freely for testing. We have provided [MockERC20](https://aeneid.storyscan.io/address/0xF2104833d386a2734a4eB3B8ad6FC6812F29E38E?tab=write_contract#0x40c10f19) on Aeneid testnet which you can mint and pay with. Then when you're ready, you should use \$WIP.

</Tip>

## Scenario #1: Tipping an IP Asset

In this scenario, you're an external 3rd-party user who wants to pay an IP Asset 2 \$WIP for being cool. When you call the function below, you should make `payerIpId` a zero address because you are not paying on behalf of an IP Asset. Additionally, you would set `amount` to 2.

<Info>
  Associated Docs:
  [royalty.payRoyaltyOnBehalf](/sdk-reference/royalty#payroyaltyonbehalf)
</Info>

```typescript main.ts
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
// you should already have a client set up (prerequisite)
import { client } from "./utils";
import { zeroAddress, parseEther } from "viem";

async function main() {
  const payRoyalty = await client.royalty.payRoyaltyOnBehalf({
    receiverIpId: "0x0b825D9E5FA196e6B563C0a446e8D9885057f9B1", // the ip you're paying
    payerIpId: zeroAddress,
    token: WIP_TOKEN_ADDRESS,
    amount: parseEther("2"), // 2 $WIP
    txOptions: { waitForTransaction: true },
  });

  console.log(`Paid royalty at transaction hash ${payRoyalty.txHash}`);
}

main();
```

Let's say the IP Asset you're paying is a derivative. And due to existing license terms with a parent that specify 50% `commercialRevShare`, 50% of the revenue (2\*0.5 = 1) would automatically be claimable by the parent thanks to the [Royalty Module](/concepts/royalty-module), such that both the parent and child IP Assets earn 1 \$WIP. We'll go over this on the next page.

## Scenario #2: Paying Due Share

In this scenario, lets say a derivative IP Asset earned 2 USD off-chain. Because the derivative owes the parent IP Asset 50% of its revenue, it could give the parent 1 USD off-chain and be ok. Or, it can send 1 \$USD equivalent to the parent on-chain _(for this example, let's just assume 1 \$WIP = 1 USD)_.

<Info>
  Associated Docs:
  [royalty.payRoyaltyOnBehalf](/sdk-reference/royalty#payroyaltyonbehalf)
</Info>

```typescript main.ts
import { WIP_TOKEN_ADDRESS } from "@story-protocol/core-sdk";
// you should already have a client set up (prerequisite)
import { client } from "./utils";
import { parseEther } from "viem";

async function main() {
  const payRoyalty = await client.royalty.payRoyaltyOnBehalf({
    receiverIpId: "0xDa03c4B278AD44f5a669e9b73580F91AeDE0E3B2", // parentIpId
    payerIpId: "0x0b825D9E5FA196e6B563C0a446e8D9885057f9B1", // childIpId
    token: WIP_TOKEN_ADDRESS,
    amount: parseEther("1"), // 1 $WIP
    txOptions: { waitForTransaction: true },
  });

  console.log(`Paid royalty at transaction hash ${payRoyalty.txHash}`);
}

main();
```

### Complex Royalty Graphs

Let's say the child earned 1,000 USD off-chain, and is linked to a huge ancestor tree where each parent has a different set of complex license terms. In this scenario, you won't be able to individually calculate each payment to each parent. Instead, you would just pay _yourself_ the amount you earned, and the [Royalty Module](/concepts/royalty-module) will automate the payment, such that each ancestor gets their due share.

## View Completed Code

Congratulations, you paid an IP Asset on-chain!

<CardGroup cols={1}>
  <Card
    title="Completed Code"
    href="https://github.com/storyprotocol/typescript-tutorial/blob/main/scripts/derivative/registerDerivativeCommercial.ts"
    icon="thumbs-up"
  >
    All of this page is covered in this working code example.
  </Card>
</CardGroup>

## Claiming Revenue

Now that we have paid revenue, we need to learn how to claim it! We will cover that on the next page.


# Attach Terms to an IPA

This section demonstrates how to attach [License Terms](/concepts/licensing-module/license-terms) to an [IP Asset](/concepts/ip-asset). By attaching terms, users can publicly mint [License Tokens](/concepts/licensing-module/license-token) (the on-chain "license") with those terms from the IP.

### Prerequisites

There are a few steps you have to complete before you can start the tutorial.

1. Complete the [TypeScript SDK Setup](/developers/typescript-sdk/setup)

## 1. Before We Start

We should mention that you do not need an existing IP Asset to attach terms to it. There are two functions you can use that allow you to **register IP + create terms + attach terms** in the same function:

- [mintAndRegisterIpAssetWithPilTerms](/sdk-reference/ipasset#mintandregisteripassetwithpilterms)
- [registerIpAndAttachPilTerms](/sdk-reference/ipasset#registeripandattachpilterms)

## 2. Register License Terms

In order to attach terms to an IP Asset, let's first create them!

[License Terms](/concepts/licensing-module/license-terms) are a configurable set of values that define restrictions on licenses minted from your IP that have those terms. For example, "If you mint this license, you must share 50% of your revenue with me." You can view the full set of terms in [PIL Terms](/concepts/programmable-ip-license/pil-terms).

<Note>

If License Terms already exist on our protocol for the identical set of parameters you intend to create, it is unnecessary to create it again and the function will simply return the existing `licenseTermsId` and an undefined `txHash`. License Terms are protocol-wide, so you can use existing License Terms by its `licenseTermsId`.

</Note>

Below is a code example showing how to create new terms:

<Info>
  Associated Docs:
  [license.registerPILTerms](/sdk-reference/license#registerpilterms)
</Info>

```typescript main.ts
import { LicenseTerms } from "@story-protocol/core-sdk";
import { zeroAddress } from "viem";
// you should already have a client set up (prerequisite)
import { client } from "./utils";

async function main() {
  const licenseTerms: LicenseTerms = {
    defaultMintingFee: 0n,
    // must be a whitelisted revenue token from https://docs.story.foundation/developers/deployed-smart-contracts
    // in this case, we use $WIP
    currency: "0x1514000000000000000000000000000000000000",
    // RoyaltyPolicyLAP address from https://docs.story.foundation/developers/deployed-smart-contracts
    royaltyPolicy: "0xBe54FB168b3c982b7AaE60dB6CF75Bd8447b390E",
    transferable: false,
    expiration: 0n,
    commercialUse: false,
    commercialAttribution: false,
    commercializerChecker: zeroAddress,
    commercializerCheckerData: "0x",
    commercialRevShare: 0,
    commercialRevCeiling: 0n,
    derivativesAllowed: false,
    derivativesAttribution: false,
    derivativesApproval: false,
    derivativesReciprocal: false,
    derivativeRevCeiling: 0n,
    uri: "",
  };

  const response = await client.license.registerPILTerms({
    ...licenseTerms,
    txOptions: { waitForTransaction: true },
  });

  console.log(
    `PIL Terms registered at transaction hash ${response.txHash}, License Terms ID: ${response.licenseTermsId}`
  );
}

main();
```

### 2a. PIL Flavors

As you see above, you have to choose between a lot of terms.

We have convenience functions to help you register new terms. We have created [PIL Flavors](/concepts/programmable-ip-license/pil-flavors), which are pre-configured popular combinations of License Terms to help you decide what terms to use. You can view those PIL Flavors and then register terms using the following convenience functions:

<CardGroup cols={4}>
  <Card
    title="Non-Commercial Social Remixing"
    href="/concepts/programmable-ip-license/pil-flavors#flavor-%231%3A-non-commercial-social-remixing"
    icon="file"
    
    
  >
    Free remixing with attribution. No commercialization.
  </Card>

{" "}

<Card
  title="Commercial Use"
  href="/concepts/programmable-ip-license/pil-flavors#flavor-%232%3A-commercial-use"
  icon="file"
>
  Pay to use the license with attribution, but don't have to share revenue.
</Card>

{" "}

<Card
  title="Commercial Remix"
  href="/concepts/programmable-ip-license/pil-flavors#flavor-%233%3A-commercial-remix"
  icon="file"
>
  Pay to use the license with attribution and pay % of revenue earned.
</Card>

  <Card
    title="Creative Commons Attribution"
    href="/concepts/programmable-ip-license/pil-flavors#flavor-%234%3A-creative-commons-attribution"
    icon="file"
    
    
  >
    Free remixing and commercial use with attribution.
  </Card>
</CardGroup>

## 3. Attach License Terms

Now that we have created terms and have the associated `licenseTermsId`, we can attach them to an existing IP Asset like so:

<Info>
  Associated Docs:
  [license.attachLicenseTerms](/sdk-reference/license#attachlicenseterms)
</Info>

```typescript main.ts
import { LicenseTerms } from "@story-protocol/core-sdk";
import { zeroAddress } from "viem";
// you should already have a client set up (prerequisite)
import { client } from "./utils";

async function main() {
  // previous code here ...

  const response = await client.license.attachLicenseTerms({
    // insert your newly created license terms id here
    licenseTermsId: LICENSE_TERMS_ID,
    // insert the ipId you want to attach terms to here
    ipId: "0x4c1f8c1035a8cE379dd4ed666758Fb29696CF721",
    txOptions: { waitForTransaction: true },
  });

  if (response.success) {
    console.log(
      `Attached License Terms to IPA at transaction hash ${response.txHash}.`
    );
  } else {
    console.log(`License Terms already attached to this IPA.`);
  }
}

main();
```

### 3a. Create Terms + Attach

It's worth mentioning that you can **create terms + attach terms** all in the same step with the the [registerPilTermsAndAttach](/sdk-reference/ipasset#registerpiltermsandattach) function. Whatever is easiest for you!

And, like we mentioned at the beginning, there are two functions you can use that allow you to **register IP + create terms + attach terms** in the same function:

- [mintAndRegisterIpAssetWithPilTerms](/sdk-reference/ipasset#mintandregisteripassetwithpilterms)
- [registerIpAndAttachPilTerms](/sdk-reference/ipasset#registeripandattachpilterms)

## 4. Mint a License

Now that we have attached License Terms to our IP, the next step is minting a License Token, which we'll go over on the next page.


# Overview

The best way to get started is to get your hands dirty and start building.

<CardGroup cols={2}>
  <Card
    title="Working Code Examples"
    href="https://github.com/storyprotocol/typescript-tutorial"
    icon="thumbs-up"
    
    
  >
    Extremely easy & straightforward working code examples for all of the following tutorials.
  </Card>

  <Card
    title="SDK Reference"
    href="/sdk-reference"
    icon="books"
    
    
  >
    View the whole SDK reference, which shows examples and types for every function in our SDK.
  </Card>
</CardGroup>

In the following series of tutorials, you will learn how to build IP applications with the Story SDK along with the concepts we mentioned in the [Architecture Overview](/concepts/overview).


# Dev Overview

If you're a developer, here is everything you need:

<Tip>

Can't find something? Ask the writer of our docs for help in our [Builder Discord](https://discord.gg/storybuilders).

</Tip>

<CardGroup cols={3}>

<Card
  title="Testnet Block Explorer"
  href="https://aeneid.storyscan.io"
  icon="house"
>
  View all testnet block & transaction data on Story.
</Card>

<Card
  title="IP-related Explorer"
  href="https://aeneid.explorer.story.foundation"
  icon="user"
>
  View testnet transaction data specifically related to IP interactions like
  registering, licensing, etc.
</Card>

<Card
  title="Quickstart"
  href="/quickstart"
  icon="truck-fast"
  
>
  Start building on Story quickly.
</Card>
  
</CardGroup>

## SDK

Check out the following resources to learn the SDK:

- [SDK Reference](/sdk-reference) - view the entire SDK reference with detailed **explanations and examples** for each function **_(includes working code so you can jump right to coding)_**
- [TypeScript SDK Guide](/developers/typescript-sdk/overview) - a detailed, step-by-step walkthrough of how to set up and implement the most popular uses of the SDK (register IP, attach terms, register derivative, etc) **_(includes working code so you can jump right to coding)_**
- [Tutorials](/developers/tutorials/overview) - more specific, external topics/tutorials that may be popular questions, like "How do I register music on Story?", "How do I implement wallet-less onboarding with the SDK?", etc **_(includes working code so you can jump right to coding)_**

## Smart Contracts

Check out the following resources to learn the protocol:

- [Smart Contract Guide](/developers/smart-contracts-guide/overview) - a walkthrough of how to set up and implement the most popular uses of the protocol **_(includes working code so you can jump right to coding)_**
- [Deployed Smart Contracts](/developers/deployed-smart-contracts) - all the deployed protocol addresses
- [Tutorials](/developers/tutorials/overview) - includes tutorials that cover more specific topics, like registering music, registering AI-generated images, etc **_(includes working code so you can jump right to coding)_**

<Warning>
  Do not use `RANDAO` for pseudo-randomness, instead use onchain VRF (Pyth or
  Gelato). Currently, `RANDAO` value is set as the parent block hash and thus is
  not random for X-1 block.
</Warning>

## API

View our [API Reference](/api-reference).


# "Implementing ATCP/IP"

<Warning>
Still new!

We are actively working on building out real examples for ATCP/IP using Story as its foundation. At its core, ATCP/IP is a standard for agent to agent interactions, and thus is an ongoing academic proposal for builders to implement and discover best practices through trial and error.

</Warning>

Below are details on how to actually implement the **_2. An ATCP/IP Transaction_** section of the whitepaper below.

<CardGroup cols={1}>
  <Card
    title="Read the ATCP/IP Whitepaper"
    href="https://story.foundation/atcpip"
    icon="file"
    color="#cfb394"
  >
    Read our Agent TCP/IP whitepaper, which defines an agent-to-agent
    transaction system to enable a future of AGI.
  </Card>
</CardGroup>

## Performing Each Step

Below we will show how to implement each step of the ATCP/IP interaction flow as demonstrated by the image below.

<Frame>
  <img src="/images/ai-agents/atcpip-diagram.jpeg" />
</Frame>

### Registering your Agent's Outputs

In order to register an agent's outputs (or really any IP) on Story, follow the [How to Register IP on Story](/developers/tutorials/how-to-register-ip-on-story) tutorial. The only difference is how you structure your IP Metadata, which should always follow the [📝 IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard).

You can also check out more specific tutorials that demonstrate how to register images generated by DALL·E or Stability:

- [Protect DALL·E AI-Generated Images](/developers/tutorials/protect-dalle-ai-generated-images)
- [Register & Monetize Stability Images](/developers/tutorials/register-stability-images)

Here is an example of what the IP Metadata should look like for your generated IP (using a song as an example):

```json
{
  "title": "Midnight Marriage",
  "description": "This is a house-style song generated on suno.",
  "createdAt": "1740005219",
  "creators": [
    {
      "name": "Jacob Tucker",
      "address": "0xA2f9Cf1E40D7b03aB81e34BC50f0A8c67B4e9112",
      "contributionPercent": 100
    }
  ],
  "image": "https://cdn2.suno.ai/image_large_8bcba6bc-3f60-4921-b148-f32a59086a4c.jpeg",
  "imageHash": "0xc404730cdcdf7e5e54e8f16bc6687f97c6578a296f4a21b452d8a6ecabd61bcc",
  "mediaUrl": "https://cdn1.suno.ai/dcd3076f-3aa5-400b-ba5d-87d30f27c311.mp3",
  "mediaHash": "0xb52a44f53b2485ba772bd4857a443e1fb942cf5dda73c870e2d2238ecd607aee",
  "mediaType": "audio/mpeg"
}
```

### Creating Agreement Terms

As described in the [Whitepaper](https://story.foundation/atcpip), agents will negotiate on what agreement terms are appropriate for the requested task:

<Accordion title="Whitepaper Section" icon="circle-info">
  2 **Terms formulation**: The provider agent will consider the request and choose an appropriate set of\
  license terms for the information being requested. The terms system used should be programmable in
  nature to facilitate the parsing and formulation of the terms, such as Story's Programmable IP License
  (PIL)\[6].

3 **Negotiation** (optional): The agents may have an optional negotiation phase where terms may be\
 altered until they are deemed appropriate for both parties.

- **Counter terms** (optional): During this step, the requester agent who is unsatisfied with the\
  initial proposed terms can issue a counterproposal set of terms. Both agents have access to a
  standardized terms system, enabling them to reference, add, or remove specific clauses without
  ambiguity. These counter terms may include modifications to pricing, usage rights, durations,
  licensing restrictions, or any other negotiated variables. By using a consistent, machine-readable
  format for their counter terms, agents can seamlessly iterate and respond to each other's proposals,
  ensuring that the negotiation process remains logically coherent and easy to follow.
- **Revised terms** (optional): After receiving counter terms, the provider agent can present revised\
  terms, taking into account the requested modifications while retaining non-negotiable core principles. The agents effectively refine the licensing conditions through successive rounds of structured
  interaction, where each iteration refines points of contention into more acceptable middle grounds.
  Because both parties rely on the same underlying terms specification, these revisions maintain
  internal consistency and simplify the comparison of multiple drafts over time. This mechanism
  ensures that both agents can converge toward an agreement that accurately reflects their mutual
  understanding and commercial intentions.
- _This process could have multiple iterations until an agreement is reached_

</Accordion>

Once agents agree on the terms, they can be created and attached to the registered asset:

<CardGroup cols={2}>
  <Card title="Using the SDK" href="/developers/typescript-sdk/attach-terms" icon="house">
    Learn how to attach terms to your IP using the SDK.
  </Card>

  <Card title="Using the Smart Contracts" href="/developers/smart-contracts-guide/attach-terms" icon="house" >
    Learn how to attach terms to your IP using the Smart Contracts.
  </Card>
</CardGroup>

### Mint a License

As stated in the [Whitepaper](https://story.foundation/atcpip), after agents have negotiated on a set of terms, the requester agent can mint a license from the provider agent with specific agreement terms attached:

<Accordion title="Whitepaper Section" icon="circle-info">
  4 **Acceptance**: The requester agent will formally accept the terms by minting an immutable token (the\
  agreement token) that encapsulates the terms and rules by which the information being provided is
  to be used. Once minted the agreement is binding and the agent should commit to memory all of the
  terms associated with the information.

- **Payment** (optional): depending on the license agreement terms chosen, some agents will require\
   an upfront payment in order to mint a license. Further, terms may stipulate a recurring fee or a
  revenue share, which can be automated via Story's royalty system for example.

</Accordion>

Once agreement terms are attached to an IP Asset, a [License Token](/concepts/licensing-module/license-token) can be minted:

<CardGroup cols={2}>
  <Card title="Using the SDK" href="/developers/typescript-sdk/mint-license" icon="house">
    Learn how to mint a License Token using the SDK.
  </Card>

  <Card title="Using the Smart Contracts" href="/developers/smart-contracts-guide/mint-license" icon="house">
    Learn how to mint a License Token using the Smart Contracts.
  </Card>
</CardGroup>

Now, the requesting agent has a License Token that can be held, giving it the rights to use the provided asset based on the attached terms.

### Claim Revenue

Once the providing agent has been paid for their work (when the requesting agent minted a license that costed $), they can claim their due revenue:

<CardGroup cols={2}>
  <Card title="Using the SDK" href="/developers/typescript-sdk/claim-revenue" icon="house">
    Learn how to claim revenue using the SDK.
  </Card>

  <Card title="Using the Smart Contracts" href="/developers/smart-contracts-guide/claim-revenue" icon="house">
    Learn how to claim revenue using the Smart Contracts.
  </Card>
</CardGroup>

## Example Integration with MCP

We have implemented a Model Context Protocol (MCP) server that provides tools for interacting with Story's protocol using [the MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk), and an AI Agent that uses those tools.

<CardGroup cols={2}>
  <Card title="Story MCP Server" href="https://github.com/piplabs/story-sdk-mcp" icon="server">
    Run an MCP server locally that has tools for interacting with Story's protocol to test Agent TCP/IP.
  </Card>

  <Card title="LangGraph AI Agent" href="https://github.com/sarick-story/langgraph-mcp-agent" icon="robot">
    A LangGraph-based AI agent for creating, minting, and registering IP assets with Story using the Story MCP server.
  </Card>
</CardGroup>

1. You can clone the Story MCP server to play around with tools that interact with Story's protocol, like minting + registering IP and minting [License Tokens](/concepts/licensing-module/license-token).
2. Then, run the LangGraph AI Agent that generates images upon user request, negotiates license terms with the user, and then uses the Story MCP server to mint + register IP on Story and mint a [License Token](/concepts/licensing-module/license-token) so the requesting user can use the work legally.

Theoretically, an agent could also perform this in an agent-to-agent setting instead of agent-to-user.

### What is MCP?

> "MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools."

Check out the [Model Context Protocol (MCP) website](https://modelcontextprotocol.io/introduction) to learn more.


# "Using Cursor with Story"

[Cursor](https://www.cursor.com/) is an AI code editor that makes it easy to write code while building Story apps. Let's walk through how to setup Cursor for the best possible results with Story.

## Add Story Docs

Adding Story docs lets you interact with our docs directly and get the most accurate answers to your questions.

1. Go to Cursor Settings > Features > Docs and click "+ Add new doc"

<Frame>
  <img src="/images/ai-agents/add-cursor.png" />
</Frame>

2. Paste the URL `https://raw.githubusercontent.com/storyprotocol/docs/refs/heads/main/combined.md`

<Note>
  This is our entire documentation combined into a single `.md` file, **which is
  automatically updated every single time our docs have changes.**
</Note>

3. Change the name to Story, and leave everything else the same

<Frame>
  <img src="/images/ai-agents/add-cursor-2.png" />
</Frame>

## Using the Docs

You can then reference the Story docs in your prompt with the `@Story` symbol.

<Frame>
  <img src="/images/ai-agents/add-cursor-3.png" />
</Frame>


# "For AI Agents"

This page is all about AI Agents. We have prepared a way for you to use our documentation as training data which can be seen below, or continue to learn about developing AI Agents on Story.

<CardGroup cols={2}>
  <Card title="Train on Our Docs" href="https://github.com/storyprotocol/docs/blob/main/combined.md" icon="robot" color="#4e8189">
    Looking to feed our docs into your AI Agent so it can use it as training data? Check out this file, which contains all of our docs in one combined `.md` file.
  </Card>

  <Card title="Read the ATCP/IP Whitepaper" href="https://story.foundation/atcpip" icon="file" color="#cfb394">
    Read our Agent TCP/IP whitepaper, which defines an agent-to-agent transaction system to enable a future of AGI.
  </Card>
</CardGroup>

Below you will find two sections:

1. **Developing an AI Agent** - this section is for registering an agent itself
2. **Implementing ATCP/IP** - this section is for implementing the **_2. An ATCP/IP Transaction_** section of the [Whitepaper](https://story.foundation/whitepaper.pdf).

## Developing an Agent

Below are details on how to:

- Register an AI Agent as IP
- Add License Terms to your AI Agent

### Registering an Agent

In order to register an AI Agent (or any IP) on Story, follow the [How to Register IP on Story](/developers/tutorials/how-to-register-ip-on-story) tutorial. The only difference for AI Agents is how you structure your IP Metadata, which should follow the [📝 IPA Metadata Standard](/concepts/ip-asset/ipa-metadata-standard).

Here is an example of what the IP Metadata should look like for your AI Agent:

```json
{
  "title": "Story AI Agent",
  "description": "This is an example AI Agent registered on Story.",
  "createdAt": "1740005219",
  "creators": [
    {
      "name": "Jacob Tucker",
      "address": "0xA2f9Cf1E40D7b03aB81e34BC50f0A8c67B4e9112",
      "contributionPercent": 100
    }
  ],
  "image": "https://ipfs.io/ipfs/bafybeigi3k77t5h5aefwpzvx3uiomuavdvqwn5rb5uhd7i7xcq466wvute",
  "imageHash": "0x64ccc40de203f218d16bb90878ecca4338e566ab329bf7be906493ce77b1551a",
  "mediaUrl": "https://ipfs.io/ipfs/bafybeigi3k77t5h5aefwpzvx3uiomuavdvqwn5rb5uhd7i7xcq466wvute",
  "mediaHash": "0x64ccc40de203f218d16bb90878ecca4338e566ab329bf7be906493ce77b1551a",
  "mediaType": "image/webp",
  "aiMetadata": {
    "characterFileUrl": "https://ipfs.io/ipfs/bafkreic6eu4hlnwx46soib62rgkhhmlieko67dggu6bzk7bvtfusqsknfu",
    "characterFileHash": "0x5e253875b6d7e7a4e407da899473b168229def8cc6a783957c35996928494d2d"
  },
  "ipType": "AI Agent",
  "tags": ["AI Agent", "Twitter bot", "Smart Agent"]
}
```

### Adding Terms to your AI Agent

Upon registering your AI Agent, you can add license terms to it. However you can add more license terms to your AI Agent afterwards as well. Follow the below tutorials to learn how to do this:

<CardGroup cols={2}>
  <Card title="Using the SDK" href="/developers/typescript-sdk/attach-terms" icon="house">
    Learn how to attach terms to your AI Agent using the SDK.
  </Card>

  <Card title="Using the Smart Contracts" href="/developers/smart-contracts-guide/attach-terms" icon="house">
    Learn how to attach terms to your AI Agent using the Smart Contracts.
  </Card>
</CardGroup>

## Implementing ATCP/IP

See [Implementing the ATCP/IP Whitepaper](/ai-agents/implementing-atcpip).


# "Explain Like I'm Five"

<Frame
  caption={
    <>
      Credit to the original tweet{" "}
      <a href="https://x.com/devrelius/status/1812865477657694513">here</a>
    </>
  }
>
  <img src="/images/eli5.png" alt="explain like im five" />
</Frame>

<Frame
  caption={
    <>
      Credit to the original tweet{" "}
      <a href="https://x.com/jacobmtucker/status/1905602225600430206">here</a>
    </>
  }
>
  <img src="/images/concepts/hdspip.png" alt="How Does Story Protect IP?" />
</Frame>


# Aeneid - Testnet

# Resources

**Network Name**: Story Aeneid Testnet

**Chain ID**: 1315

**Chainlist Link**: [https://chainlist.org/chain/1315](https://chainlist.org/chain/1315)

## RPCs

| RPC Name           | RPC URL                                  | Official |
| :----------------- | :--------------------------------------- | :------: |
| Story              | `https://aeneid.storyrpc.io`             |    ✅    |
| Story by QuickNode | `https://www.quicknode.com/chains/story` |          |

## Explorers

| Explorer                                                                                                                       | URL                                        | Official |
| :----------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- | :------: |
| [Blockscout Explorer ↗️](https://aeneid.storyscan.io)                                                                          | `https://aeneid.storyscan.io`              |    ✅    |
| [IP Explorer ↗️](https://aeneid.explorer.story.foundation) (only for IP-related actions like licensing, minting licenses, etc) | `https://aeneid.explorer.story.foundation` |    ✅    |

## Faucet

| Faucet                                                                                  | Amount |
| :-------------------------------------------------------------------------------------- | :----- |
| [Google Cloud Faucet ↗️](https://cloud.google.com/application/web3/faucet/story/aeneid) | 10 IP  |
| [Official Faucet ↗️](https://aeneid.faucet.story.foundation/)                           | 10 IP  |

## Staking Dashboard

| Dashboard URL                                               | Official |
| :---------------------------------------------------------- | :------: |
| [Story Dashboard](https://aeneid.staking.story.foundation/) |    ✅    |

## Contract deployment addresses

- [Proof of Creativity](/developers/deployed-smart-contracts)


# Mainnet

# Resources

**Network Name**: Story Mainnet

**Chain ID**: 1514

**Chainlist Link**: [https://chainlist.org/chain/1514](https://chainlist.org/chain/1514)

## RPCs

| RPC Name           | RPC URL                                  | Official |
| :----------------- | :--------------------------------------- | :------: |
| Story              | `https://mainnet.storyrpc.io`            |    ✅    |
| Story by Ankr      | `https://rpc.ankr.com/story_mainnet`     |          |
| Story by QuickNode | `https://www.quicknode.com/chains/story` |          |

## Block Explorers

| Explorer                                                                                                                | URL                                       | Official |
| :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- | :------: |
| [BlockScout Explorer ↗️](https://www.storyscan.io/)                                                                     | `https://www.storyscan.io/`               |    ✅    |
| [IP Explorer ↗️](https://explorer.story.foundation) (only for IP-related actions like licensing, minting licenses, etc) | `https://explorer.story.foundation`       |    ✅    |
| [OKX Explorer ↗️](https://www.okx.com/web3/explorer/story)                                                              | `https://www.okx.com/web3/explorer/story` |          |
| [Stakeme Explorer ↗️](https://storyscan.app/)                                                                           | `https://storyscan.app/`                  |          |

## Staking Dashboard

| Dashboard URL                                        | Official |
| :--------------------------------------------------- | :------: |
| [Story Dashboard](https://staking.story.foundation/) |    ✅    |
| [Origin Stake](https://ipworld.io/)                  |          |
| [Node.Guru](https://story.explorers.guru/)           |          |

## Contract deployment addresses

- [Proof of Creativity](/developers/deployed-smart-contracts)

# Further Sections

- [Mainnet Status Page](https://status.story.foundation/)
- [Node Setup](/network/operating-a-node/node-setup-mainnet)
- [Validator Operations](/network/become-a-validator)
- [Staking Design](/network/tokenomics-staking)


# Run a Localnet

# Overview

You can easily set up your own local Story network using docker compose, consisting of one boot node and four validator nodes. With this local network, you can test the consensus layer of the Story network or deploy your application using the precompiled primitive, the IP graph, to conduct various tests. Additionally, you can reset the network at any time as needed.

# Run a Local Story Network

<Note>

For more detailed information for running Story local network, please refer the repository: [https://github.com/piplabs/story-localnet](https://github.com/piplabs/story-localnet)

</Note>

## Prerequisite

To set up a local network, [Docker](https://docs.docker.com/get-started/get-docker/) is required.

## Step 1 - Start Docker

Please run Docker.

## Step 2 - Clone Repository

You need to clone three repositories: `story`, `story-geth`, and `story-localnet`.\
Make sure all three repositories are located within the same subfolder.

```bash
# clone repositories
git clone https://github.com/piplabs/story.git
git clone https://github.com/piplabs/story-geth.git
git clone https://github.com/piplabs/story-localnet.git
```

## Step 3 - Start Nodes

Navigate to story-localnet project and start the local network.

```bash
# move to story-localnet
cd story-localnet

# start story local network
./start.sh
```

## Step 4 - Terminate Nodes

If you want to stop the Story local network, you can do so by executing the script below.

```bash
# terminate story local network
./terminate.sh
```

---

## How to Allocate Token to Your Account from Genesis

You may need to allocate IP tokens to your account for testing in the local network.\
To allocate tokens to your account in the genesis block, follow these steps:

1. Add your account information to the alloc section in `config/story/genesis-geth.json`:

```json
"<hex-encoded-account-address>": {
  "nonce": "0x0",
  "balance": "<hex-encoded-balance>",
  "code": "0x",
  "storage": {}
}
```

2. Run the `update-genesis-hash.sh` script to update the genesis block hash:

```bash
./update-genesis-hash.sh
```

---

## How to interact with Story Local Network

By default, the Story local network has the following ports open for interaction.

| Port  | Service    | Role                                                                   |
| :---- | :--------- | :--------------------------------------------------------------------- |
| 8545  | story-geth | Endpoint of RPC server for Story execution client                      |
| 1317  | story-node | Endpoint of API server for interacting with the Story consensus client |
| 26657 | story-node | Endpoint of cosmos-sdk RPC server for Story consensus client           |

---

## Monitoring Systems

This setup includes a monitoring stack to provide centralized metrics and logs\
visualization for the blockchain network. Tools include **Prometheus**,
**Loki**, **Promtail**, and **Grafana**, all integrated through Docker Compose.

### **Components and Access Information**

| Service    | Role                                                              | Default Port                   | Access URL              |
| :--------- | :---------------------------------------------------------------- | :----------------------------- | :---------------------- |
| Prometheus | Collects metrics from nodes and itself for performance monitoring | `9090`                         | `http://localhost:9090` |
| Loki       | Aggregates and stores logs from the network nodes via Promtail    | `3100`                         | `http://localhost:3100` |
| Promtail   | Scrapes logs from Docker containers and sends them to Loki        | `9080` (API), `9095` (Metrics) | `http://localhost:9080` |
| Grafana    | Provides a dashboard interface for metrics and logs visualization | `3000`                         | `http://localhost:3000` |


# Network Info

# Overview

Story Network is a purpose-built layer 1 blockchain achieving the best of EVM and Cosmos SDK. It is 100% EVM-compatible alongside deep execution layer optimizations to support graph data structures, purpose-built for handling complex data structures like IP quickly and cost-efficiently. It does this by:

- using precompiled primitives to traverse complex data structures like IP graphs within seconds at marginal costs
- a consensus layer based on the mature CometBFT stack to ensure fast finality and cheap transactions
- a modular architecture that decouples consensus from execution via Ethereum’s Engine-API

# Available Network

<CardGroup cols={3}>

<Card title="Mainnet" href="/network/network-info/mainnet" icon="house" />
<Card
  title="Aeneid Testnet"
  href="/network/network-info/aeneid"
  icon="wrench"
/>
<Card
  title="Run a localnet"
  href="/network/network-info/localnet"
  icon="gear"
/>

</CardGroup>


# Infrastructure Partners

## RPC Providers

<CardGroup cols={1}>
  <Card
    title="QuickNode"
    href="https://www.quicknode.com/chains/story"
    icon="house"
  >
    QuickNode provides hosted Story RPC nodes under their free and paid plans,
    granting flexible and reliable access to the network. For high-throughput or
    mission-critical applications, Dedicated Clusters deliver premium
    performance with unmetered billing, elevated rate limits, and robust
    infrastructure.
  </Card>
</CardGroup>

## Cross-chain

<CardGroup cols={3}>
  <Card title="LayerZero" href="https://docs.layerzero.network/v2/developers/evm/technical-reference/deployed-contracts?chains=odyssey-testnet" icon="house" iconColor="#000000">
    LayerZero is a technology that enables applications to move data across blockchains, uniquely supporting censorship-resistant messages and permissionless development through immutable smart contracts.
  </Card>

{" "}

<Card
  title="deBridge"
  href="https://debridge.finance/"
  icon="house"
  iconColor="#fbff3a"
>
  Blazingly fast bridging for anyone that likes to be one step ahead.
</Card>

  <Card title="Stargate" href="https://stargate.finance/" icon="house" iconColor="#ffffff">
    Stargate is a fully composable liquidity transport protocol that lives at the heart of Omnichain DeFi.
  </Card>
</CardGroup>

## Onramp/Offramp

<CardGroup cols={2}>
  <Card title="Transak" href="https://transak.com/" icon="house" iconColor="#1461db">
    Enable users to buy or sell crypto from your app.
  </Card>

  <Card title="Halliday" href="https://halliday.xyz/" icon="house" iconColor="#392df8">
    The Commerce Automation Network for Modular Chains.
  </Card>
</CardGroup>

## Indexers/Data

<CardGroup cols={3}>
  <Card title="Simplehash" href="https://simplehash.com/" icon="house" iconColor="#5046e5">
    Instant access to Token and NFT market prices, metadata and media. 80+ chains.
  </Card>

{" "}

<Card
  title="Goldsky"
  href="https://goldsky.com/"
  icon="house"
  iconColor="#ffbf60"
>
  Crypto Data Live-Streamed.
</Card>

{" "}

<Card
  title="Zettablock"
  href="https://zettablock.com/"
  icon="house"
  iconColor="#3c4ff6"
>
  A unified platform for open and trustfree AI development, empowering an
  accessible ecosystem of models and datasets.
</Card>

  <Card title="Zapper" href="https://protocol.zapper.xyz/chains/story" icon="house" iconColor="#8A2BE2">
    Zapper is a multi-chain portfolio tracker and analytics tool for DeFi.
  </Card>
</CardGroup>

## Oracles/VRF

<CardGroup cols={3}>
  <Card title="Gelato" href="https://www.gelato.network/" icon="house" iconColor="#ff3b57">
    Build scalable, custom enterprise-grade Rollups with Gelato's Web3 Services natively integrated.
  </Card>

{" "}

<Card
  title="Redstone"
  href="https://www.redstone.finance/"
  icon="house"
  iconColor="#ae0722"
>
  Modular oracles for DeFi.
</Card>

{" "}

<Card
  title="Pyth"
  href="https://www.pyth.network/"
  icon="house"
  iconColor="#e6dafe"
>
  Secure your smart contracts with reliable, low-latency market data from
  institutional sources. Build apps with high-fidelity oracle feeds designed for
  mission-critical systems.
</Card>

  <Card title="Uma" href="https://uma.xyz/" icon="house" iconColor="#fe4d4c">
    A decentralized truth machine.
  </Card>
</CardGroup>

## Dev Tools

<CardGroup cols={2}>
  <Card title="Protofire" href="https://protofire.io/" icon="house" iconColor="#f54704">
    Protofire boosts TVL and usage for Web3 projects with our Dev DAO, reducing costs and enhancing quality.
  </Card>

  <Card title="Wagmi" href="https://wagmi.sh/" icon="house" iconColor="#000000">
    Type Safe, Extensible, and Modular by design. Build high-performance blockchain frontends.
  </Card>
</CardGroup>

## Wallets/AA

<CardGroup cols={3}>
  <Card title="Dynamic" href="https://www.dynamic.xyz/" icon="house" iconColor="#4779ff">
    Dynamic offers a suite of tools for effortless log in, wallet creation and user management. Designed for users. Built for developers.
  </Card>

{" "}

<Card
  title="Pimlico"
  href="https://www.pimlico.io/"
  icon="house"
  iconColor="#7115aa"
>
  The world's most popular account abstraction infrastructure platform
</Card>

{" "}

<Card
  title="ZeroDev"
  href="https://zerodev.app/"
  icon="house"
  iconColor="#23a4f0"
>
  ZeroDev is the most powerful toolkit for building with smart accounts,
  including both "smart EOAs" (EIP-7702) and "smart contract accounts"
  (ERC-4337).
</Card>

{" "}

<Card title="Tomo" href="https://tomo.inc/" icon="house" iconColor="#f21f7f">
  The all-in-one wallet designed to bring the mass adoption.
</Card>

{" "}

<Card
  title="Privy"
  href="https://www.privy.io/"
  icon="house"
  iconColor="#000000"
>
  Privy is a powerful authentication and key management platform to securely
  onboard, activate, and manage your users at scale.
</Card>

{" "}

<Card
  title="Keplr"
  href="https://www.keplr.app/"
  icon="house"
  iconColor="#0657fa"
>
  Introducing Keplr, the fast, simple, secure wallet that plugs you into any
  blockchains and apps wherever you go. Pioneering its ways in the multichain
  future from day one.
</Card>

  <Card title="Turnkey" href="https://www.turnkey.com/" icon="house" iconColor="#000000">
    Secure, flexible, and scalable wallet infrastructure.
  </Card>
</CardGroup>


# Pyth

# Price Feeds

Pyth Network provides real-time financial market data to smart contracts across 100+ blockchains, sourcing prices from over 100 exchanges and market makers. With 850+ price feeds covering equities, commodities, and cryptocurrencies, Pyth aggregates and updates prices multiple times per second.

See Pyth's [Documentation](https://docs.pyth.network/price-feeds/price-feeds) guide to integrate your application with their price feeds.

## Smart Contracts

### Mainnet

#### [ERC1967Proxy.sol](https://www.storyscan.io/address/0xD458261E832415CFd3BAE5E416FdF3230ce6F134)

```
0xD458261E832415CFd3BAE5E416FdF3230ce6F134
```

#### [PythUpgradable.sol](https://www.storyscan.io/address/0x5f3c61944CEb01B3eAef861251Fb1E0f14b848fb)

```
0x5f3c61944CEb01B3eAef861251Fb1E0f14b848fb
```

### Testnet (Aeneid)

#### [ERC1967Proxy.sol](https://aeneid.storyscan.io/address/0x36825bf3Fbdf5a29E2d5148bfe7Dcf7B5639e320)

```
0x36825bf3Fbdf5a29E2d5148bfe7Dcf7B5639e320
```

#### [PythUpgradeable.sol](https://aeneid.storyscan.io/address/0x98046Bd286715D3B0BC227Dd7a956b83D8978603)

```
0x98046Bd286715D3B0BC227Dd7a956b83D8978603
```

<br />

# VRF

Pyth Entropy(VRF) service enables on-chain generation of provably fair random numbers. To integrate Pyth Entropy, you need to invoke an on-chain function to request a random number from Entropy. This function accepts a randomly generated number, which can be created off-chain and sent to the Entropy contract. In return, the contract provides a sequence number. Once the request is processed, Pyth Entropy will send a callback to your contract, delivering the generated random number.

See Pyth's [How to Generate Random numbers in EVM dApps](https://docs.pyth.network/entropy/generate-random-numbers/evm) guide to integrate your application with Pyth Entropy.

## Smart Contracts

### Mainnet

#### [ERC1967Proxy.sol](https://www.storyscan.io/address/0xdF21D137Aadc95588205586636710ca2890538d5)

```
0xdF21D137Aadc95588205586636710ca2890538d5
```

#### [EntropyUpgradeable.sol](https://www.storyscan.io/address/0x4374e5a8b9C22271E9EB878A2AA31DE97DF15DAF)

```
0x4374e5a8b9C22271E9EB878A2AA31DE97DF15DAF
```

### Testnet (Aeneid)

#### [ERC1967Proxy.sol](https://aeneid.storyscan.io/address/0x5744Cbf430D99456a0A8771208b674F27f8EF0Fb)

```
0x5744Cbf430D99456a0A8771208b674F27f8EF0Fb
```

#### [EntropyUpgradeable.sol](https://aeneid.storyscan.io/address/0x74f09cb3c7e2A01865f424FD14F6dc9A14E3e94E)

```
0x74f09cb3c7e2A01865f424FD14F6dc9A14E3e94E
```


# Redstone

# Price Feeds

Redstone delivers real-time financial data to smart contracts on 70+ blockchains, covering crypto, RWAs, LRTs, BTCFi, and other emerging assets. Combining institutional and crypto-native data, Redstone ensures reliability through multi-layered validation, including anomaly detection, market depth analysis, and cross-source variance checks.

See Redstone's [Documentation](https://docs.redstone.finance/docs/introduction) guide to integrate your application with their price feeds.

## Smart Contracts

### ETH

#### TransparentUpgradeableProxy

```
0x22d47686b3AEC9068768f84EFD8Ce2637a347B0A
```

#### StoryPriceFeedEthWithoutRoundsV1

```
0xb9D0073aCb296719C26a8BF156e4b599174fe1d5
```

### BTC

#### TransparentUpgradeableProxy

```
0xc44be6D00307c3565FDf753e852Fc003036cBc13
```

#### StoryPriceFeedBtcWithoutRoundsV1

```
0xE23eCA12D7D2ED3829499556F6dCE06642AFd990
```

### USDC

#### TransparentUpgradeableProxy

```
0xED2B1ca5D7E246f615c2291De309643D41FeC97e
```

#### StoryPriceFeedUsdcWithoutRoundsV1

```
0x31a36CdF4465ba61ce78F5CDbA26FDF8ec361803
```

### USDT

#### TransparentUpgradeableProxy

```
0x7A9b672fc20b5C89D6774514052b3e0899E5E263
```

#### StoryPriceFeedUsdtWithoutRoundsV1

```
0xe8D9FbC10e00ecc9f0694617075fDAF657a76FB2
```


# Gelato

# VRF

Gelato VRF provides verifiable randomness for blockchain applications by utilizing Drand, a decentralized and trusted source of random numbers. It ensures that developers receive truly random values that are both provable and tamper-resistant.

See Gelato's [Documentation](https://docs.gelato.network/web3-services/vrf) guide to integrate your application with their price feeds.

## Smart Contracts

### Functions and VRF

#### Mainnet

##### [EIP173Proxy.sol](https://www.storyscan.io/address/0xafd37d0558255aA687167560cd3AaeEa75c2841E)

```
0xafd37d0558255aA687167560cd3AaeEa75c2841E
```

##### [Automate.sol](https://www.storyscan.io/address/0xab2c44495F5F954149b94C750ca20B64ea60B51c)

```
0xab2c44495F5F954149b94C750ca20B64ea60B51c
```

### Relays

#### Mainnet

##### GelatoRelay

Relay method: `callWithSyncFee`

###### EIP173Proxy.sol

```
0xcd565435e0d2109feFde337a66491541Df0D1420
```

#####

###### GelatoRelay.sol

```
0xA75983F686999843804a2ECC0E93C35d39a4F750
```

##### GelatoRelayERC2771.sol

Relay method: `callWithSyncFeeERC2771`

```
0x8aCE64CEA52b409F930f60B516F65197faD4B056
```

##### GelatoRelayConcurrentERC2771.sol

Relay method: `callWithSyncFeeERC2771` with `isConcurrent: true`

```
0xc7739c195618D314C08E8626C98f8573E4E43634
```

##### GelatoRelay1BalanceERC2771.sol

Relay method: `sponsoredCallERC2771`

```
0x61F2976610970AFeDc1d83229e1E21bdc3D5cbE4
```


# Multisig

## Story Safe

Users can access Safe via a user-friendly web UI or directly through smart contracts, giving both regular users and developers flexible options for managing multisig wallets.

### Using Safe's Web App

Use Safe’s intuitive web app to easily propose, review, and execute multisig transactions — no coding required!

<Card title="Story Safe" href="https://safe.story.foundation/welcome" horizontal icon="vault">

Go to the web app and try it out.

</Card>

### Smart Contract Integration

For direct interaction with Safe's smart contracts, see the official documentation for technical guidance and examples to build or automate Safe workflows.

<Card title="Safe Docs" href="https://docs.safe.global/home/what-is-safe" horizontal icon="book">

Check out Safe's documentation to learn more.

</Card>


# Additional Resources

# Additional Resources

## Github

- [Story Github](https://github.com/piplabs/story)
- [Story-geth Github](https://github.com/piplabs/story-geth)

## SIP Repository

- [SIP Repository](https://github.com/storyprotocol/SIPs)

## Community Forum

- [Story Forum](https://forum.story.foundation/)

# Troubleshooting

Welcome to Story node troubleshooting! This section covers common problems and solutions when running Story nodes.

### Node Setup

<Accordion title="What are the hardware requirements?">

See the [system specs](/network/operating-a-node/node-setup-mainnet)

</Accordion>

<Accordion title="What's the max expected TPS?">

\~700

</Accordion>

<Accordion title="Is it fully EVM-compatible? Is there any customization already being made on the IP blockchain? Or are there any coming customization to be applied?">

Yes, it's EVM-compatible. Story's execution client is a fork of Geth with our custom precompiles, which enhance the IP graph's performance while maintaining strict EVM compatibility. Other Ethereum execution clients, such as RETH and Erigon, can be supported later.

</Accordion>

<Accordion title="Which is your consensus mechanism?">

Our consensus mechanism is CometBFT

</Accordion>

<Accordion title="Batches support? Limit on batch request?">

Batch RPCs are supported - for Geth there is a 1K limit and on the consensus side there is 10 request limit

</Accordion>

<Accordion title="WS connections? (if yes, how do they work)">

Yes, WS is enabled on the execution client, and is recommended for subscription use-cases. It is open on port 8546

</Accordion>

<Accordion title="How many different paths does node serves (several path with diff methods RPC)?">

Please see Geth's latest JSON-RPC documentation for a full comprehensive list [here](https://ethereum.org/en/developers/docs/apis/json-rpc/#web3_clientversion). In the future, we may add more.

</Accordion>

<Accordion title="Caching rules for RPC method?">

We recommend employing standard in-memory caching with a 1-10 min TTL based on the RPC method

</Accordion>

<Accordion title="What is the best method to get latest block and check node is healthy and in sync?">

Use `eth_syncing` RPC call on the execution client to check if the node is sync and `eth_blockNumber` for getting the latest block

</Accordion>

<Accordion title="What are the heaviest RPC methods? How much time does it take to respond to request with such method?">

`eth_call` / `eth_getLogs` / `eth_getBlockByNumber` \
 We are still running latency tests to get a sense of response times.

</Accordion>

<Accordion title="Is archive node provisioning a requirement? If yes how big?">

No, not at the moment.

</Accordion>

<Accordion title="Are there snapshots available for full / archive?">

Not yet, but we are working on it.

</Accordion>

<br />

### Common Issues

<Accordion title="Database Initialization Failure">

**Error:**

```bash
ERRO !! Fatal error occurred, app died️ unexpectedly !! err="create db: failed to initialize database:
```

**Solution:**

1. Save your validator state:

```bash
cp $HOME/.story/story/data/priv_validator_state.json $HOME/.story/story/priv_validator_state.json.backup
```

> 🚧 Be very careful with this file, especially if your validator is already signing blocks.

- Check your the database backend type, your node must support the same as you are using the snapshot:

```bash
cat $HOME/.story/story/config/story.toml
```

Default is `app-db-backend = "goleveldb"`. The fallback is the `db_backend` value set in CometBFT's `config.toml`.

```bash
cat $HOME/.story/story/config/config.toml
```

</Accordion>

<Accordion title="High Gas Fees">

**Problem:** Need to adjust gas fees on RPC node

**Solution:**
Add the `--rpc.txfee` flag to your geth startup command:

```bash
sudo tee /etc/systemd/system/story-geth.service > /dev/null <<EOF
[Unit]
Description=Story-Geth Node
After=network.target

[Service]
User=$USER
Type=simple
WorkingDirectory=$HOME/.story/geth
ExecStart=$(which geth) --story --syncmode full --rpc.txfee 2
Restart=on-failure
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
```

</Accordion>

<Accordion title="Failed to send PacketPing">

**Error:**

```bash
ERRO Failed to send PacketPing module=p2p peer=19fa6dd52e72e4e85bbb873b705282cf73217a6b@158.220.80.96:40128 err="write tcp 139.59.139.135:26656->158.220.80.96:40128: write: broken pipe"
```

Solution:

- If the node is synchronized, you can ignore this error. Your client may be a little behind.
- If the node stops, you should restart the services.

</Accordion>

<Accordion title="Cosmovisor: failed to read upgrade info">

An error occurs when starting the cosmovisor:

```bash
panic: failed to read upgrade info from disk unexpected end of JSON input
```

Solution:

- You must ensure that the installed cosmovisor version must be at least [v1.7.0.](https://docs.cosmos.network/main/build/tooling/cosmovisor)
- Then check your info file (edit version `v0.13.0` in your case):

```bash
cat $HOME/.story/story/cosmovisor/upgrades/v0.13.0/upgrade-info.json
```

If you don\`t have create new one:

```bash
echo '{"name":"v0.13.0","time":"0001-01-01T00:00:00Z","height":858000}' > $HOME/.story/story/cosmovisor/upgrades/v0.13.0/upgrade-info.json
```

Find out more about automatic updates with cosmovisor [here](/network/operating-a-node/node-setup-mainnet#custom-automation).

</Accordion>

<Accordion title="IPC endpoint closed">

Error:

```bash
INFO HTTP server stopped
INFO IPC endpoint closed
```

Solution:

- It looks like port 8551 stopping, the background process running `iptables` blocking ip and port and access posix.
- For solution try uninstall `ufw posix` and `iptables`:

```bash
iptables -I INPUT -s localhost -j ACCEPT
```

</Accordion>

<Accordion title="Found signature from the same key">

Error:

```bash
panic: Faile to consensus  state: found signature from the same key
```

Solution:

- The validator has been double signed. It is currently not possible to restore the validator after it has been double signed.
- To avoid such situations, see this post on how to correctly [migrate a validator to another machine](/network/become-a-validator#migrating-a-validator-to-another-machine).

</Accordion>

<Accordion title="Failed to validate create flags: missing required flag(s): moniker">

Error:

```bash
4-11-26 08:42:20.302 ERRO !! Fatal error occurred, app died️ unexpectedly !! err="failed to validate create flags: missing required flag(s): moniker" stacktrace="[errors.go:39 flags.go:173 validator.go:168 validator.go:384 command.go:985 command.go:1117 command.go:1041 command.go:1034 cmd.go:34 main.go:10 proc.go:271 asm_amd64.s:1695]"
```

Solution:

- You missed flag `--moniker`.
- The command to create a new validator should look like this:

```bash
./story validator create --stake ${AMOUNT_TO_STAKE_IN_WEI} --moniker ${VALIDATOR_NAME}
```

See more options [here](/network/become-a-validator#validator-creation).

</Accordion>

<Accordion title="Error adding vote">

Error:

```bash
ERRO failed to process message msg_type= *consensus.VoteMessage err:" error adding vote"
```

Solution:

- It looks like your node is down. To get started, check the current versions of the binaries [here](/network/operating-a-node/node-setup-mainnet).
- If you have up-to-date binary - try updating peers, this usually happens when a node loses p2p communication:

```bash
PEERS="..."
sed -i -e "/^\[p2p\]/,/^\[/{s/^[[:space:]]*persistent_peers *=.*/persistent_peers = \"$PEERS\"/}" $HOME/.story/story/config/config.toml
```

</Accordion>

<Accordion title="Error signing vote">

Error:

```bash
ERRO failed signing vote module=consensus height=403750 round=0 vote="Vote{23:B12C6AE31E8E 403750/00/SIGNED_MSG_TYPE_PREVOTE(Prevote) FA591EB1E540 000000000000 000000000000 @ 2024-11-08T16:58:10.375918193Z}" err="error signing vote: height regression. Got 403750, last height 420344"
```

Solution:

- Looks like you have a problem with your `priv_validator_state` of validator.
  > 🚧 Be very careful with this file, especially if your validator is already signing blocks.
- You can make a copy of your state with a command:

```bash
cp $HOME/.story/story/data/priv_validator_state.json $HOME/.story/story/priv_validator_state.json.backup
```

Check your validator state:

```bash
cat $HOME/.story/story/data/priv_validator_state.json
```

- If you get this error, you can reset your state (🚧 ONLY IF YOUR VALIDATOR HAS NOT YET SIGNET BLOCKS).
- Stop node.

```bash
sudo tee $HOME/.story/story/data/priv_validator_state.json > /dev/null <<EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
```

- Start node.

</Accordion>

<Accordion title="Unknown flag: --home">

Error:

```bash
ERRO !! Fatal error occurred, app died️ unexpectedly !! err="unknown flag: --home"
```

Solution:

- It looks like a misconfiguration. You must try to remove the `--home` flag from the startup command.
- Your systemd to run might look like this:

</Accordion>

<Accordion title="Failed to register the Ethereum service">

Error:

```bash
Fatal: Failed to register the Ethereum service: incompatible state scheme, stored: path, provided: hash
```

Solution:

- You have problems with the state of validator or a corrupted database.
- Try using a snapshot.
  > 🚧 Be very careful with this file, especially if your validator is already signing blocks.
- We have described how to reset your state [here](/network/more/troubleshooting#error-signing-vote).

## Failed to reconnect to peer

Error:

```bash
24-09-25 06:38:45.235 ERRO Failed to reconnect to peer. Beginning exponential backoff module=p2p addr=e0600fa5f2129e647ef30a942aac1695201ff135@65.109.115.98:26656 elapsed=2m29.598884906s
```

Solution:

- If the node is synchronized and not far behind, you can ignore this error.
- If the node is lagging or has stopped completely, try updating peers, this usually happens when a node loses p2p communication:

```bash
PEERS="..."
sed -i -e "/^\[p2p\]/,/^\[/{s/^[[:space:]]*persistent_peers =./persistent_peers = \"$PEERS\"/}" $HOME/.story/story/config/config.toml
```

</Accordion>

<Accordion title="Processing finalized payload halted while evm syncing">

Warn:

```bash
WARN Processing finalized payload halted while evm syncing (will retry) payload_height=...
```

Solution:

- It just means that story-geth is syncing, you can ignore this warn.
- However, if it takes a long time, we recommend that you stop the processes one at a time and start them again later in the following order:

```bash
sudo systemctl stop story-geth story
sudo systemctl daemon-reload
sudo systemctl start story-geth
sudo systemctl enable story-geth

sudo systemctl daemon-reload
sudo systemctl start story
sudo systemctl enable story
```

</Accordion>

<Accordion title="Upgrade handler is missing">

Error:

```bash
ERRO error in proxyAppConn.FinalizeBlock      module=consensus err="module manager preblocker: wrong app version 0, upgrade handler is missing for upgrade plan"
```

Solution:

- Looks like you missed an update.
- To get started, check the current versions of the binaries [here](/network/operating-a-node/node-setup-mainnet).

</Accordion>

<Accordion title="Home directory contains unexpected file">

Error:

```bash
ERRO !! Fatal error occurred, app died️ unexpectedly !! err="home directory contains unexpected file(s), use --force to initialize anyway"
```

Solution:

- This means that you have already initialized the node.
- `$HOME/.story/story` directory created, and there are files in it. Delete it, or try with it.

</Accordion>

<Accordion title="Err='create comet node: create node">

Error:

```bash
ERRO !! Fatal error occurred, app died️ unexpectedly ! err="create comet node: create node
```

Solution:

- It appears that your node is using incorrect versions.
- Check the current versions of the binaries [here](/network/operating-a-node/node-setup-mainnet).
- And most likely you need to perform a rollback binary to current versions.

</Accordion>

<Accordion title="WAL does not contain">

Error:

```bash
ERRO catchup replay: WAL does not contain
```

Solution:

- Looks like an `AppHash` issue.
- To get started, upgrade to the current versions of the binaries [here](/network/operating-a-node/node-setup-mainnet).
- If your versions are newer than the current ones, perform a rollback.

</Accordion>

<Accordion title="Err='load engine JWT file: read jwt file">

Error:

```bash
ERRO !! Fatal error occurred, app died️ unexpectedly !! err="load engine JWT file: read jwt file: open /root/.story/geth/odyssey/geth/jwtsecret: no such file or directory
```

Solution:

- It seems your node can't get `jwtsecret`.
- Check your `WorkingDirectory` in your `geth-service` , by default `WorkingDirectory=$HOME/.story/geth`.
- Check all paths, you can get your `jwtsecret`with command (for odyssey network):

```bash
cat .story/geth/odyssey/geth/jwtsecret
```

</Accordion>

<Accordion title="Couldn't connect to any seeds">

Error:

```bash
ERRO Couldn't connect to any seeds module=p2p
```

Solution:

- If the node is synchronized and not far behind, you can ignore this error.
- If the node is lagging or has stopped completely, try updating seeds/peers, it usually happens when a node loses p2p communication (we recommend that you stop the node and delete the addrbook).

```bash
rm -rf $HOME/.story/story/config/addrbook.json
SEEDS="..."
PEERS="..."
sed -i -e "/^\[p2p\]/,/^\[/{s/^[[:space:]]*seeds *=.*/seeds = \"$SEEDS\"/}" \
       -e "/^\[p2p\]/,/^\[/{s/^[[:space:]]*persistent_peers *=.*/persistent_peers = \"$PEERS\"/}" $HOME/.story/story/config/config.toml
```

</Accordion>

<Accordion title="Processing finalized payload failed err='rpc forkchoice updated">

Warn:

```bash
WRN Processing finalized payload; evm syncing
WRN Processing finalized payload failed: evm fork choice update (will retry) status="" err="rpc forkchoice updated v3: beacon syncer reorging"
```

Solution:

- Everything is fine, it just means that `story-geth` is syncing, which takes some time.
- If the node is not far behind, you can ignore this warning.

## Dial tcp 127.0.0.1:9090

Warn:

```bash
WRN error getting latest block error:"rpc error: dial tcp 127.0.0.1:9090"
```

Solution:

- The logs show a connection failure on port `9090`.
- Check the listening ports:

```bash
sudo ss -tulpn  | grep LISTEN
```

- If other node uses `9090`, then modify it to another.
- Normally, this WARNING should not affect the performance of your node.

</Accordion>

<Accordion title="Wrong AppHash">

Error:

```bash
ERRO Error in validation module=blocksync err="wrong Block[dot]Header[dot]AppHash  Expected [...]
```

Solution:

- `Wrong AppHash` type logs means the story node version you are using is wrong.
- Upgrade to the current versions of the binaries [here](/network/operating-a-node/node-setup-mainnet).
- If your versions are newer than the current ones, perform a rollback.

</Accordion>

<Accordion title="Connection failed sendRoutine / Stopping peer">

Error:

```bash
ERRO Connection failed @ sendRoutine module=p2p peer=...
ERRO Stopping peer for error module=p2p peer=...
```

Solution:

- If the node is synchronized and not far behind, you can ignore this error.
- If the node is lagging or has stopped completely, try updating peers, this usually happens when a node loses p2p communication:

```bash
PEERS="..."
sed -i -e "/^\[p2p\]/,/^\[/{s/^[[:space:]]*persistent_peers =./persistent_peers = \"$PEERS\"/}" $HOME/.story/story/config/config.toml
```

</Accordion>

<Accordion title="Moniker must be valid non-empty">

Error:

```bash
ERRO !! Fatal error occurred, app died️ unexpectedly ! err="create comet node: create node: info.Moniker must be valid non-empty
```

Solution:

- Looks like a problem with your node moniker.
- Be sure to use `""` when executing init:

```bash
story init --network "..." --moniker "..."
```

- Go to config, find the moniker and put it inside `""` only:

```bash
sudo nano ~/.story/story/config/config.toml
```

</Accordion>

<Accordion title="Invalid address (26656)">

Error:

```bash
Fatal error occurred, app died️ unexpectedly ! err="create comet node: create node: invalid address (26656):
```

Solution:

- The logs report a connection failure on port `26656`.
- Check the listening ports:

```bash
sudo ss -tulpn  | grep LISTEN
```

- If another node is using `26656`, change it to another and keep the default `26656` for story in the `P2P configuration` options in `config`:

```bash
sudo nano ~/.story/story/config/config.toml
```

</Accordion>

<Accordion title="Eth_coinbase does not exist">

Warn:

```bash
WARN Beacon client online, but no consensus updates received in a while. Please fix your beacon client to follow the chain!
Served eth_coinbase eth_coinbase does not exist
```

Solution:

- This error indicates that the network has stopped.

</Accordion>

<Accordion title="Verifying proposal failed">

Warn:

```bash
WARN Verifying proposal failed: push new payload to evm (will retry) status="" err="new payload: rpc new payload v3: Post \"http://localhost:8551\": round trip: dial tcp 127.0.0.1:8551: connect: connection refused" stacktrace="[errors.go:39 jwt.go:41 client.go:259 client.go:180 client.go:724 client.go:590 http.go:229 http.go:173 client.go:351 engineclient.go:101 msg_server.go:183 proposal_server.go:34 helpers.go:30 proposal_server.go:33 tx.pb.go:299 msg_service_router.go:175 tx.pb.go:301 msg_service_router.go:198 prouter.go:74 abci.go:520 cmt_abci.go:40 abci.go:85 local_client.go:164 app_conn.go:89 execution.go:166 state.go:1381 state.go:1338 state.go:2055 state.go:910 state.go:836 asm_amd64.s:1695]"
WARN Verifying proposal
```

Solution:

- It looks like port 8551 stopping, the background process running `iptables` blocking ip and port and access posix.
- For solution try uninstall `ufw posix` and `iptables`:

```bash
iptables -I INPUT -s localhost -j ACCEPT
```

</Accordion>


# Full Node

This section will guide you through how to setup a Story node for mainnet. Story draws inspiration from ETH PoS in decoupling execution and consensus clients. The execution client `story-geth` relays EVM blocks into the `story` consensus client via Engine API, using an ABCI++ adapter to make EVM state compatible with that of CometBFT. With this architecture, consensus efficiency is no longer bottlenecked by execution transaction throughput.

The `story` and `geth` binaries, which make up the clients required for running Story nodes, are available from our latest `release` pages:

- **`story-geth`execution client:**
  - Release Link: [**Click here**](https://github.com/piplabs/story-geth/releases)
  - Latest Stable Binary (v1.0.2): [**Click here**](https://github.com/piplabs/story-geth/releases/tag/v1.0.2)
- **`story`consensus client:**
  - Releases link: [**Click here**](https://github.com/piplabs/story/releases)
  - Latest Stable Binary (v1.1.1): [**Click here**](https://github.com/piplabs/story/releases/tag/v1.1.1)

# Story Node Installation Guide

## Pre-Installation Checklist

- [ ] Verify system meets hardware requirements
- [ ] Operating system: Ubuntu 22.04 LTS
- [ ] Required ports are available
- [ ] Sufficient disk space available
- [ ] Root or sudo access

## Quick Reference

- Installation time: \~30 minutes
- Network: Story Mainnet or Story Aeneid Testnet
- Required versions:
  - Check Latest Release

## 1. System Preparation

### 1.1 System Requirements

For optimal performance and reliability, we recommend running your node on either:

- A Virtual Private Server (VPS)
- A dedicated Linux-based machine

### System Specs

| Hardware  | Minimal Requirement |
| --------- | ------------------- |
| CPU       | Dedicated 8 Cores   |
| RAM       | 32 GB               |
| Disk      | 500 GB NVMe Drive   |
| Bandwidth | 25 MBit/s           |

### 1.2 Required Ports

_Ensure all ports needed for your node functionality are needed, described below_

- `story-geth`
  - 8545
    - Required if you want your node to interface via JSON-RPC API over HTTP
  - 8546
    - Required for websockets interaction
  - 30303 (TCP + API)
    - MUST be open for p2p communication
- `story`
  - 26656
    - MUST be open for consensus p2p communication
  - 26657
    - Required if you want your node interfacing for Tendermint RPC
  - 26660
    - Needed if you want to expose prometheus metrics

### 1.3 Install Dependencies

```bash
# Update system
sudo apt update && sudo apt-get update

# Install required packages
sudo apt install -y \
  curl \
  git \
  make \
  jq \
  build-essential \
  gcc \
  unzip \
  wget \
  lz4 \
  aria2 \
  gh
```

### 1.4 Install Go

For Odyssey, we need to install Go 1.22.0

```bash
# Download and install Go 1.22.0
cd $HOME

# Set Go version
GO_VERSION="1.22.0"

# Download Go binary
wget "https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz"

# Remove existing Go installation and extract new version
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go${GO_VERSION}.linux-amd64.tar.gz"

# Clean up downloaded archive
rm "go${GO_VERSION}.linux-amd64.tar.gz"

# Add Go to PATH
echo "export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin" >> ~/.bash_profile
source ~/.bash_profile

# Verify installation
go version
```

## 2. Story Node Installation

### 2.1 Install Story-Geth

1. Download and setup binary

```bash
cd $HOME
wget https://github.com/piplabs/story-geth/releases/download/v1.0.1/geth-linux-amd64
sudo mv ./geth-linux-amd64 story-geth
sudo chmod +x story-geth
sudo mv ./story-geth $HOME/go/bin/
source $HOME/.bashrc

# Verify installation
story-geth version
```

You will see the version of the geth binary.

```
Geth
version: 1.0.1-stable
...

```

(Mac OS X only) The OS X binaries have yet to be signed by our build process, so you may need to unquarantine them manually:

```bash
sudo xattr -rd com.apple.quarantine ./geth
```

2. Configure and start service

<Tabs>
  <Tab title="Mainnet">
    ```bash
           # Setup systemd service
    sudo tee /etc/systemd/system/story-geth.service > /dev/null <<EOF
    [Unit]
    Description=Story Geth Client
    After=network.target

    [Service]
    User=${user}
    ExecStart=${path_to_geth_binary} --story --syncmode full
    Restart=on-failure
    RestartSec=3
    LimitNOFILE=4096

    [Install]
    WantedBy=multi-user.target
    EOF

    # Start service
    sudo systemctl daemon-reload
    sudo systemctl enable story-geth
    sudo systemctl start story-geth

    # Verify service status
    sudo systemctl status story-geth
    ```

  </Tab>

  <Tab title="Aeneid testnet">
    ```bash
    # Setup systemd service
    sudo tee /etc/systemd/system/story-geth.service > /dev/null <<EOF
    [Unit]
    Description=Story Geth Client
    After=network.target

    [Service]
    User=${user}
    ExecStart=${path_to_geth_binary} --aeneid --syncmode full
    Restart=on-failure
    RestartSec=3
    LimitNOFILE=4096

    [Install]
    WantedBy=multi-user.target
    EOF

    # Start service
    sudo systemctl daemon-reload
    sudo systemctl enable story-geth
    sudo systemctl start story-geth

    # Verify service status
    sudo systemctl status story-geth
    ```

  </Tab>
</Tabs>

### 2.2 Install Story Consensus Client

#### Cosmovisor installation

For updating the story client, we recommend using Cosmovisor.

1. Install Cosmovisor

```bash
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.6.0
cosmovisor version
```

2. Configure Cosmovisor

```bash
# Set daemon configuration
export DAEMON_NAME=story
export DAEMON_HOME=$HOME/.story/story
export DAEMON_DATA_BACKUP_DIR=${DAEMON_HOME}/cosmovisor/backup
sudo mkdir -p \
  $DAEMON_HOME/cosmovisor/backup \
  $DAEMON_HOME/data


# Persist configuration
echo "export DAEMON_NAME=story" >> $HOME/.bash_profile
echo "export DAEMON_HOME=$HOME/.story/story" >> $HOME/.bash_profile
echo "export DAEMON_DATA_BACKUP_DIR=${DAEMON_HOME}/cosmovisor/backup" >> $HOME/.bash_profile
echo "export DAEMON_ALLOW_DOWNLOAD_BINARIES=false" >> $HOME/.bash_profile
```

#### Install Story Client

```bash
cd $HOME
wget https://github.com/piplabs/story/releases/download/v1.0.0/story-linux-amd64
sudo mv story-linux-amd64 story
sudo chmod +x story
sudo mv ./story $HOME/go/bin/
source $HOME/.bashrc
story version
```

> You should expect to see version 1.0.0-stable

(Mac OS X Only) The OS X binaries have yet to be signed by our build process, so you may need to unquarantine them manually:

```bash
sudo xattr -rd com.apple.quarantine ./story
```

#### Init Story with Cosmovisor

<Tabs>
  <Tab title="Mainnet">
    ```bash
    cosmovisor init ./story
    cosmovisor run init --network story --moniker ${moniker_name}
    cosmovisor version
    ```
  </Tab>

  <Tab title="Aeneid testnet">
    ```bash
    cosmovisor init ./story
    cosmovisor run init --network aeneid --moniker ${moniker_name}
    cosmovisor version
    ```
  </Tab>
</Tabs>

#### Custom Configuration

To override your own node settings, you can do the following:

- `${STORY_DATA_ROOT}/config/config.toml` can be modified to change network and consensus settings
- `${STORY_DATA_ROOT}/config/story.toml` to update various client configs
- `${STORY_DATA_ROOT}/priv_validator_key.json` is a sensitive file containing your validator key, but may be replaced with your own

#### Custom Automation

Below we list a sample `Systemd` configuration you may use on Linux

```bash
# story
sudo tee /etc/systemd/system/story.service > /dev/null <<EOF
[Unit]
Description=Story Cosmovisor
After=network.target

[Service]
Type=simple
User=$USER
Group=$GROUP
ExecStart=/usr/local/bin/cosmovisor run run \
--api-enable \
--api-address=0.0.0.0:1317
Restart=on-failure
RestartSec=5s
LimitNOFILE=65535
Environment="DAEMON_NAME=$DAEMON_NAME"
Environment="DAEMON_HOME=$DAEMON_HOME"
Environment="DAEMON_ALLOW_DOWNLOAD_BINARIES=false"
Environment="DAEMON_RESTART_AFTER_UPGRADE=true"
Environment="DAEMON_DATA_BACKUP_DIR=$DAEMON_HOME/cosmovisor/backup"
WorkingDirectory=$DAEMON_HOME

[Install]
WantedBy=multi-user.target
EOF

```

<Tabs>
  <Tab title="With Cosmovisor">
    ```bash
    # story
    sudo tee /etc/systemd/system/story.service > /dev/null <<EOF
    [Unit]
    Description=Story Cosmovisor
    After=network.target

    [Service]
    Type=simple
    User=${USER}
    Group=${GROUP}
    ExecStart=${path_to_story_binary} run run \
    --api-enable \
    --api-address=0.0.0.0:1317
    Restart=on-failure
    RestartSec=5s
    LimitNOFILE=65535
    Environment="DAEMON_NAME=$DAEMON_NAME"
    Environment="DAEMON_HOME=$DAEMON_HOME"
    Environment="DAEMON_ALLOW_DOWNLOAD_BINARIES=false"
    Environment="DAEMON_RESTART_AFTER_UPGRADE=true"
    Environment="DAEMON_DATA_BACKUP_DIR=$DAEMON_HOME/cosmovisor/backup"
    WorkingDirectory=$DAEMON_HOME

    [Install]
    WantedBy=multi-user.target
    EOF

    ```

  </Tab>

  <Tab title="Without Cosmovisor">
    ```bash
    # story
    sudo tee /etc/systemd/system/story.service > /dev/null <<EOF
    [Unit]
    Description=Story Cosmovisor
    After=network.target

    [Service]
    Type=simple
    User=${USER}
    Group=${GROUP}
    ExecStart=${path_to_story_binary} run
    Restart=on-failure
    RestartSec=5s
    LimitNOFILE=65535
    WorkingDirectory=$HOME/.story/story

    [Install]
    WantedBy=multi-user.target
    EOF

    ```

  </Tab>
</Tabs>

#### Start the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable story
sudo systemctl start story

# Monitor logs
journalctl -u cosmovisor -f -o cat
```

#### Debugging

If you would like to check the status of `story` while it is running, it is helpful to query its internal JSONRPC/HTTP endpoint. Here are a few helpful commands to run:

- `curl localhost:26657/net_info | jq '.result.peers[].node_info.moniker'`
  - This will give you a list of consesus peers the node is sync'd with by moniker
- `curl localhost:26657/health`
  - This will let you know if the node is healthy - `{}` indicates it is

## 3. Verify Installation

### 3.1 Check Geth Status

```bash
# Check sync status
curl -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' \
  http://localhost:8545

```

### 3.2 Check Consensus Client

```bash
# Check node status
curl localhost:26657/status

# Check peer connections
curl localhost:26657/net_info | jq '.result.peers[].node_info.moniker'
```

## Clean status

If you ever run into issues and would like to try joining the network from a cleared state, run the following:

### Geth

<Tabs>
  <Tab title="Mainnet">
    ```bash
    rm -rf ${GETH_DATA_ROOT} && ./geth --story --syncmode full
    ```

    Mac OS X: `rm -rf ~/Library/Story/geth/* && ./geth --story    --syncmode full`

    Linux: `rm -rf ~/.story/geth/* && ./geth --story --syncmode full`

  </Tab>

  <Tab title="Aeneid Testnet">
    ```bash
    rm -rf ${GETH_DATA_ROOT} && ./geth --aeneid --syncmode full
    ```

    Mac OS X: `rm -rf ~/Library/Story/geth/* && ./geth --aeneid    --syncmode full`

    Linux: `rm -rf ~/.story/geth/* && ./geth --aeneid --syncmode full`

  </Tab>
</Tabs>

### Story

<Tabs>
  <Tab title="Mainnet">
    ```bash
    rm -rf ${STORY_DATA_ROOT} && ./story init --network story && ./story run
    ```

    Mac OS X: `rm -rf ~/Library/Story/story/* && ./story init --network story && ./story run`

    Linux: `rm -rf ~/.story/story/* && ./story init --network story && ./story run`

  </Tab>

  <Tab title="Aeneid Testnet">
    ```bash
    rm -rf ${STORY_DATA_ROOT} && ./story init --network aeneid && ./story run
    ```

    Mac OS X: `rm -rf ~/Library/Story/story/* && ./story init --network aeneid && ./story run`

    Linux: `rm -rf ~/.story/story/* && ./story init --network aeneid && ./story run`

  </Tab>
</Tabs>


# Node Upgrade
There are three types of upgrades

1. Upgrade the story geth client
2. Upgrade the story client manually
3. Schedule the upgrade with Cosmovisor

### Upgrade the story geth client

```bash
# Stop the services
sudo systemctl stop story
sudo systemctl stop story-geth

# Download the new binary
wget ${STORY_GETH_BINARY_URL}
sudo mv ./geth-linux-amd64 story-geth
sudo chmod +x story-geth
sudo mv ./story-geth $HOME/go/bin/story-geth
source $HOME/.bashrc

# Restart the service
sudo systemctl start story-geth
sudo systemctl start story
```

### Upgrade the story client manually

```bash
# Stop the service
sudo systemctl stop story

# Download the new binary
wget ${STORY_BINARY_URL}
sudo mv story-linux-amd64 story
sudo chmod +x story
sudo mv ./story $HOME/go/bin/story

# Schedule the update
sudo systemctl start story
```

### Schedule the upgrade with Cosmovisor

The following steps outline how to schedule an upgrade using Cosmovisor:

1. Create the upgrade directory and download the new binary

```bash
# Download the new binary
wget ${STORY_BINARY_URL}

# Schedule the upgrade
source $HOME/.bash_profile
cosmovisor add-upgrade ${UPGRADE_NAME} ${UPGRADE_PATH} \
  --force \
  --upgrade-height ${UPGRADE_HEIGHT}
```

2. Verify the upgrade configuration

```bash
# Check the upgrade info
cat $HOME/.story/data/upgrade-info.json
```

The upgrade-info.json should show:

```json
{
  "name": "v1.0.0",
  "time": "2025-02-05T12:00:00Z",
  "height": 858000
}
```

3. Monitor the upgrade

```bash
# Watch the node logs for the upgrade
journalctl -u story -f -o cat
```

Note: Cosmovisor will automatically handle the binary switch once the specified block height is reached. Before the upgrade, confirm that your node is fully synced and has enough disk space available.

# Release Notes
This page provides information on the story execution and consensus client software release information. You may find execution client releases in [story-geth](https://github.com/piplabs/story-geth/releases) repo, and consensus client releases in [story](https://github.com/piplabs/story/releases) repo.

### Production releases

There are generally four types of releases:
* Major: It requires hardfork upgrade with a predefined upgrade height. Node operators need to upgrade before or on the height. The release will increase minor version number.
* Minor: It doesn't require hardfork upgrade. Node operators are required to upgrade binaries as soon as possible. The release will increase patch version number.
* Fix: It is an urgent fix. Node operators are required to upgrade binaries as soon as possible. The release will increase minor version or patch version number.
* Optional: It is an optional fix. Node operators can upgrade binaries based on needs. The release will increase patch version number.

Each release comes with a release note describing a list of new features or fixes. Released software binaries are also attached in the release note. We currently provide binaries supporting four types of systems: darwin-amd64, darwin-arm64, linux-amd64, and linux-arm64. You may also build your binaries using the commit hash in the release note.

### Release entries

Refer to the following release matrix to run nodes for Mainnet and Aeneid Testnet.

| Network | story-geth | story  |
|---------|------------|--------|
| Mainnet	| v1.0.1	   | v1.1.0 |
| Aeneid 	| v1.0.1	   | v1.1.0 |

# Operating Your Node
## **1. Setting Up a Geth Archive Node**
To run a Geth archive node, use `--gcmode=archive` instead of `--gcmode=full`. This ensures that Geth retains all historical blockchain state data, making it ideal for indexing services and blockchain analytics.

- `--syncmode=full`: Ensures a complete blockchain sync.
- `--gcmode=archive`: Retains full historical state data without pruning.

---

## **2. Enabling RPC (HTTP) and WebSocket in Geth**
### **HTTP (RPC) Options**
| Option | Description |
|--------|------------|
| `--http` | Enables the HTTP-RPC server. |
| `--http.addr=0.0.0.0` | Binds the HTTP server to all network interfaces. |
| `--http.port=8545` | Sets the HTTP-RPC port (default: 8545). |
| `--http.vhosts=*` | Allows requests from any domain (use with caution in production). |
| `--http.api=web3,eth,txpool,net,engine,debug` | Specifies the available APIs for HTTP requests. |

### **WebSocket (WS) Options**
| Option | Description |
|--------|------------|
| `--ws` | Enables the WebSocket server. |
| `--ws.addr=0.0.0.0` | Binds the WebSocket server to all network interfaces. |
| `--ws.port=8546` | Sets the WebSocket port (default: 8546). |
| `--ws.origins=*` | Allows WebSocket connections from any domain (use with caution in production). |
| `--ws.api=web3,eth,txpool,net,engine,debug` | Specifies the available APIs for WebSocket connections. |

These configurations ensure external applications can interact with the Geth node using both HTTP-RPC and WebSocket.

---

## **3. Monitoring Geth and Story Protocol**
### **Geth Monitoring Configuration**
- `--metrics`: Enables Prometheus-compatible metrics for Geth.
- `--metrics.addr=0.0.0.0`: Binds the metrics server to all interfaces.
- `--metrics.port=6060`: Exposes metrics on port `6060`.

### **Story Protocol Monitoring**
- Modify `config.toml` and set:
  ```toml
  prometheus = true
  ```
- The default Prometheus metrics port for Story Protocol is `26660`.

With these settings, both Geth and Story Protocol expose monitoring metrics that can be collected using Prometheus and visualized with Grafana.

# Staking Design

# Purpose

This document walks through the staking specification for Story. The goal is to provide clarity to network participants and technical partners on how Story's staking mechanics work and how users can interface with our chain.

# Tokenomics

## Genesis

The story genesis allocation will consist of 1 billion tokens, distributed among ecosystem participants, the foundation, investors, and the core team. Please refer this document for the detailed [Token Distribution](https://www.story.foundation/blog/introducing-ip).

## Locked vs Unlocked tokens

Unlocked tokens have no restrictions imposed on them and can be used for gas consumption, transfers, and staking.

Unlike unlocked tokens, locked tokens cannot be transferred or traded and are unlocked based on an unlock schedule. However, locked tokens may be staked to earn staking rewards, with the locked staking reward rate being half of that of unlocked tokens.

Staked locked and unlocked tokens have the same voting power. That means that a validator with 100 staked locked tokens has the same network voting power as a validator with 100 staked unlocked tokens.

Both types of tokens can be slashed if their validators get slashed.

## Token emissions

A fixed number of tokens will be allocated for emissions in the first year, with the quantity determined by the foundation at Genesis. For subsequent years, the number of emitted tokens will be controlled by an emissions algorithm whose parameters may be updated via governance or subject to change via hard forks. The emissions per block are controlled by the following two parameters:

- blocks_per_year: 10368000 blocks
  - The number of blocks expected to be produced in a year
- inflations_per_year: 20,000,000 tokens
  - The total number of inflationary tokens to be emitted in a year

New emissions will flow to two places:

1. Block Rewards
2. Community Pool

## Token burn

Since Story uses a fork of geth as the execution client, the burning mechanism follows Ethereum's EIP-1559.

# Staking

> 🔗 [Stake with the Staking Dashboard ↗️](https://staking.story.foundation/)

Story supports the below staking-related operations

- Create validator
- Update validator commission
- Stake
- Stake on behalf
- Unstake
- Unstake on behalf
- Redelegate
- Redelegate on behalf
- Set withdraw address
- Set reward address
- Unjail
- Unjail on behalf

Before explaining the behavior of each of these operations, some high-level concepts like **Token Staking Types**, **Validator Set Status**, **Unbonding**, and **Staking Period** will be explained first:

## Token Staking Types

As staking is enabled for both locked and unlocked tokens, validators must choose which type of token staking they want to support. Once a token staking type is selected, validators cannot switch to a different type.

## Validator Set Status

In Story, validators are grouped into one of two sets, (1) the active (bonded) validator set, which participates in consensus and receives block rewards, or (2) the non-active (unbonded) validator set, which does not contribute to the consensus process. To be selected as part of the active validator set, a validator must be one of the top 64 validators ranked by staked tokens.

## Unbonding

Unstaking for delegators is subject to an unbonding process. Users must wait for an unbonding time before any tokens return to their accounts.

This is the same for validators who self-delegate to themselves. They also need to go through the unbonding process when they want to unstake.

The unbonding time is 14 days. During the unbonding period, the delegator/validator will not earn block rewards. But they may still be slashed.

For each validator/delegator pair, the maximum ongoing unbonding transactions is 14. More unbonding requests beyond this limit will fail.

## Staking period

Delegators can decide how flexible and how long they want to stake their tokens. By default, for both locked and unlocked tokens, delegators can stake and then unstake immediately and get their token back after the unbonding time. We call this **flexible staking** in this document.

For unlocked tokens, a few more fixed staking periods are supported: 90 days, 360 days, and 540 days. In this case, users can only call unstake after the staking period is mature. Any call earlier than the mature day will be discarded. Unstaking from a mature staking period is still subject to the unbonding process, meaning users will get their staked tokens back after 14 days of unbonding time.

Staking in these fixed staking periods earns more rewards. The longer the period, the bigger the reward weight multiplier. Reward multiplier for different periods:

- Locked flexible period - **0.5**
- Flexible period - **1.0**
- 90 days - **1.1**
- 360 days - **1.5**
- 540 days - **2**

For locked tokens, only flexible staking is allowed and the reward multiplier is **0.5**. If a user delegates their locked tokens to a staking period, we will convert that to a flexible staking delegation.

After the staking period ends, users can choose not to unstake. In this case, they will continue earning the same reward rate based on the reward rate of the corresponding staking period until they unstake manually. They can unstake at any time after the staking period ends. For example, if the 1-year staking period's reward rate is 0.02% per block, after staking for 1 year, users can still earn 0.02% per block of the reward until they unstake.

## Decimal for stake amounts

The decimal for stake operations (stake, unstake, redelegate, etc.) is 9. If a user specifies a smaller value, the dust will be refunded back to the users. Or if there is no token transfer involved, the specified value will be rounded down to 9 decimals.

# Staking Operations

## Create validator

To become a validator, the validator must first run a validator node based on the latest released story binaries, then call the CreateValidator function with an initial staking amount, moniker, and commission rate. It also needs to set the max commission rate and max commission rate change to make sure it doesn't change the commission rate later dramatically. The minimum commission rate that a validator can set is 5%.

The initial staking amount needs to be larger than a threshold, which is 1024 IP. The amount will be deducted from the caller's wallet. It can only be staked to a flexible period.

If a validator tries to call create validator function the second time, it will be ignored.

## Update validator commission

This operation allows validators to edit their validator commission rate. If the updated commission rate is larger than max commission rate or the commission rate change delta is larger than max commission rate change, the operation will fail.

A fee of 1 IP will be charged for updating a validator to prevent spamming. The fee will be burnt by the contract.

The commission rate can only be updated once per day. It will not throw an error from the contract. But it won't take effect in the consensus layer.

## Stake

Both the validator and delegator can stake tokens to a validator. A validator can stake to itself, which is called self-delegation. Users can decide if they want to stake with a fixed staking period or stake without a period (flexible staking).

If a fixed period is chosen, a delegation id will be returned to the users. Users must use this delegation id to unstake tokens from this stake operation. If flexible staking is chosen, the returned delegation id will be 0.

The staking amount needs to be larger than a threshold, which is 1024 IP.

If a delegator delegates to a non-existent validator, the tokens will NOT be refunded.

If users specify the token amount that has more than 9 decimal units, the actual staking amount will be rounded down to 9 decimal and refund the remaining back to the users.

## Unstake

When staking without a staking period, users can unstake anytime. The tokens will be distributed to the user's account after the unbonding time.

A fee of 1 IP will be charged for unstaking to prevent spamming. The fee will be burnt by the contract.

When staking with a staking period, users can only unstake after the staking period is mature. The tokens will be distributed to the user's account after the unbonding time. Unstaking requests before the staking period matures will be ignored.

The minimum unstaking amount is 1024 IP. After the unstaking request is processed, if the remaining staked amount is less than 1024 IP, the remaining part will also be unstaked together.

The unstaking request will first go through the unbonding process, which is 14 days. After that, the unbonded requests are sent to a withdrawal queue, distributing a maximum of 32 withdrawals per block. If there are more than 32 withdrawal requests in the withdrawal queue, the next 32 withdrawal requests will be processed in the next block.

Partial unstake of a delegation is supported. For example, if a 1-year long delegation has 1 million tokens, after 1 year, users can unstake 500k from this delegation and keep the remaining staked to continue earning rewards.

Unstake can fail if the validator, delegator and delegation id passed in is incorrect.

Unstake can also fail if the maximum concurrent unbonding request (currently 14) has been reached for the validator/delegator pair.

If the unstake amount passed in is larger than the total unstakable tokens, the current total unstakable amounts will be unstaked. For example, if users unstake 1024 IP and only have 1023 IP stake, 1023 IP will be withdrawn.

If a validator exits, by either being offline and getting jailed, or not having enough stakes to be in the top 64 validator set, the delegators can unstake their tokens if the tokens are not in a staking period or their staking period is mature. Otherwise, delegators must wait until the staking period matures to unstake.

If users specify the token amount that has more than 9 decimal units, the actual unstaking amount will be rounded down to 9 decimal.

## Redelegate

Redelegate operation allows a delegator to move its staked tokens from one validator to another. The tokens can be redelegated to the new validator immediately and start earning rewards. However, the redelegated tokens are still subject to the unbonding process, IF the source validator is in the active validator set or unbonding from the active validator set. During this 14 days unbounding time, it will be slashed if the original validator gets slashed.

A fee of 1 IP will be charged for redelegation to prevent spamming. The fee will be burnt by the contract.

The minimum redelegation amount is 1024 IP. If a delegator's initial stake is 1024 IP but later gets slashed, it can still redelegate its tokens to another validator even if the token amount is less than 1024 IP.

Similarly to unstaking, if the redelegation amount passed in is larger than the total redelegatable tokens, the total redelegatable amounts will be redelegated. If the remaining balance after redelegation is less than 1024 IP, all remaining tokens will be redelegated together.

The delegation id will stay the same after the redelegation.

Redelegation has its own maximum ongoing unbonding transaction limit per delegator/source validator/destination validator pair, which is also 14.

Delegators can choose to redelegate their tokens to another active validator even if their tokens are still in an immature staking period. Their staking period maturation date and reward rate will stay the same.

Redelegation can only be triggered when the source and destination validators support the same token type.

If users specify the token amount that has more than 9 decimal units, the actual reledegated amount will be rounded down to 9 decimal.

## Set withdrawal/reward address

Delegators can call the staking contract to set a withdrawal address. The unstaked tokens will be sent to this withdrawal address. Similarly, delegators can set a separate reward address. All reward distributions will be sent to this address.

A fee of 1 IP will be charged for updating either the withdrawal address or the reward address to prevent spamming. The fee will be burnt by the contract.

The address change will take effect in the next block.

## Slash/Unjail

Slashing penalizes bad behaviors on the validators by slashing out a fraction of their staked tokens. Two types of behaviors can get slashed in Story: **double sign** and **downtime**.

- **double sign**: If a validator double signs for a block, they will get slashed 5% of their tokens and get permanently jailed (called tombstoned).
- **downtime**: If a validator is offline for too long and misses 95% of the past 28,800 blocks, they will get slashed 0.02% of their tokens and get jailed.

A validator will also get jailed after self-undelegation if the validator's remaining self-delegation amount is smaller than the minimum self-delegation (1024 IP).

A jailed validator cannot participate in the consensus and earn any reward. But they can unjail themselves after a cooldown time, which is currently set to 10 minutes. After 10 minutes, it can call story's staking contract to unjail itself IF their stake is more than minimum stake amount (1024 IP), after which it can participate in the consensus again if it's still within the top 64 validators.

A jailed validator can still withdraw all their stakes.

Delegators can still stake and unstake from a jailed validator as long as there are remaining stakes on this jailed validator. The jailed validator will only be removed from the chain (hence not able to be staked/unstaked) when there is no remaining stake on it.

A fee of 1 IP will be charged for unjailing a validator to prevent spamming. The fee will be burnt by the contract.

## On behalf functions

Most of the staking-related operations can be done from another wallet on behalf of the validators or delegators. Most of these on-behalf functions are permissionless since they spend tokens from the wallet that calls the on-behalf operations, not from the actual validators or delegators.

## Add operator

If a delegator wants to allow another wallet to unstake or redelegate on their behalf, they must call the staking contract to add that wallet as the operator for their delegator. After that, the operator can unstake and redelegate the delegator's tokens on behalf of the delegator.

The same applies to a validator who wants to allow another wallet to unjail on its behalf.

A fee of 1 IP will be charged for adding an operator.

## An additional data field

Each function will include an additional unformatted `data` input field to accommodate potential future changes. It can avoid changing user interfaces in the future.

## Validator key format

Validator public keys are secp256k1 keys. The keys have a 33 bytes compressed version and 65 bytes uncompressed version. When interacting with the story's smart contracts, a 33 bytes compressed key is used to identify validators.

# Rewards

## Rewards Pool Allocation

For every block, a fixed proportion of token inflation will go to the rewards distribution pool, which will be shared among all 64 active validators according to each of their share weights. _These allocated tokens will then be shared among the validator and its delegators in a fashion described by the next section._ The validator share weight is calculated based on the total token staking amount, and whether or not the token staking type is locked or unlocked.

As an example, assume that we have 100 tokens allocated for the validator rewards distribution pool, and assume that we only have 3 active validators:

- validatorA with 10 locked tokens staked
- validatorB with 10 locked tokens staked
- validatorC with 10 unlocked tokens staked

To calculate how many tokens each validator receives, we first calculate each of their weighted shares, which is defined as the number of staked tokens multiplied by their rewards multiplier (0.5 if staking locked tokens, 1 if staking unlocked tokens). This gives us:

- validatorA with 10 \* 0.5 = 5 shares
- validatorB with 10 \* 0.5 = 5 shares
- validatorC with 10 \* 1 = 10 shares

With the weighted and total shares calculated, we can then get the total number of inflationary tokens allocated for each validator:

- validatorA with 100 \* (5 / 20) = 25 tokens
- validatorB with 100 \* (5 / 20) = 25 tokens
- validatorC with 100 \* (10 / 20) = 50 tokens

The formula for calculating the total number of tokens allocated for a validator is as follows:

<Image
  align="center"
  src="https://files.readme.io/833d419fc139ba363c56aef263dcca571fe449ab824a2349a69d7419ee658bd0-Screenshot_2024-10-30_at_8.13.27_PM.png"
/>

where

- R_i is the total inflationary token rewards for validator i
- S_i is the staked tokens for validator i
- M_i is the rewards multiplier (0.5 for locked tokens, 1 for unlocked tokens)
- R_total is the total inflationary tokens allocated for the rewards pool

## Validator And Delegator Rewards

Total rewards allocations (_whose calculations are shown in the prior section_) for each validator are shared between the validator itself and all of its delegators:

- The validator takes a fixed percentage commission, set by the validator itself
- Remaining rewards are distributed among delegators according to their share weights

Calculation of delegator rewards is similar to that of validator rewards, where the proportion of tokens received for each delegator out of the remaining validator rewards is calculated based on each delegator's staking multiplier (described in the staking section).

As an example, assume a validator has 100 total rewards allocated to it, with a validator commission of 20%, and 3 delegators delegating to it:

- delegatorA with 10 tokens staked and a staking multiplier of 1
- delegatorB with 10 tokens staked and a staking multiplier of 1
- delegatorC with 10 tokens staked and a staking multiplier of 2

To calculate how many tokens each delegator receives, we first calculate each of their weighted shares, which is defined as the number of staked tokens multiplied by their staking rewards multiplier. This gives us:

- delegatorA with 10 \* 1 = 10 shares
- delegatorB with 10 \* 1 = 10 shares
- delegatorC with 10 \* 2 = 20 shares

With the weighted and total shares calculated, we can then get the total number of inflationary tokens allocated for each delegator, noting that the total number of tokens to be distributed among delegators is give by 100 - (100 \* 0.20) = 80:

- delegatorA with 80 \* (10 / 40) = 20 tokens
- delegatorB with 80 \* (10 / 40) = 20 tokens
- delegatorC with 80 \* (20 / 40) = 40 tokens

The formula for calculating the delegator token reward can be found below:

<Image
  align="center"
  src="https://files.readme.io/429c0eff2f0acddcabfa3e6259e427b47156aed244020bfb7f11a5b63387fec9-Screenshot_2024-10-30_at_8.15.51_PM.png"
/>

where

- D_i is the total inflationary token rewards for delegator i
- S_i is the staked tokens for delegator i
- M_i is the staked rewards multiplier for delegator i
- R_total is the total inflationary tokens allocated for the validator
- C is the commission rate for the validator

The validator commission is also treated as a reward and will follow the same auto-reward distribution rule described below. The minimal validator commission is set to 5% to avoid a cut-throat competition of lower commission rates among validators.

The reward calculation results will be rounded down to gwei. Anything smaller than 1 gwei will be truncated.

## Auto reward distribution

The reward is accumulated per block and can be distributed per block. However, it will only be automatically distributed to the delegator's account when it is larger than a threshold. The default and also minimal threshold is 8 IP, which means that only if the delegator's reward is more than 8 IP, it will be sent to the delegator's account.

The reward distribution will go to a reward distribution queue, which only processes a fixed amount of reward distribution requests per block. The reward distribution per block is 32.

The staking reward cannot be manually withdrawn by design.

# Community Pool

A percentage of the newly minted tokens in every block will go to a community pool contract. The foundation will determine how to use the tokens sent to the pool. The maximum community pool percentage that can be set is 20%.

The community pool contract address: **0xcccccc0000000000000000000000000000000002**

# Singularity

The first 1,580,851 blocks after the genesis is called Singularity, during which everyone can create a validator and stake tokens but the active validator set will only have the genesis validators. There is also no new token emission, hence no reward. Unstake and redelegate are also not supported.

The Genesis validator set consists of 8 validators, setup by the foundation and trusted staking institutions. 4 of them support locked tokens and the other 4 support unlocked tokens. Each of them has an initial stake of 0.001 IP. Each of them will set a commission rate. During the Singularity, the genesis valdiators will need to self delegate at least 1024 IP to perform validator operations like editing validator commission rate.

After Singularity, the top 64 validator nodes with the highest stakes will be selected to participate in consensus and receive rewards.

Slashing/Jail won't happen during Singularity.

# Staking contract

Story's staking contract will handle all validators/delegators related operations. It's deployed to address: **0xcccccc0000000000000000000000000000000001**

The contract interfaces are defined here: [https://github.com/piplabs/story/blob/main/contracts/src/protocol/IPTokenStaking.sol](https://github.com/piplabs/story/blob/main/contracts/src/protocol/IPTokenStaking.sol)


# Engine API
The Engine API is a collection of JSON-RPC methods that facilitate communication between the execution layer (EL) and the consensus layer (CL) of an EVM node. Story's execution layer, which offers full EVM compatibility, supports all standard JSON-RPC methods defined by the [Ethereum Engine API](https://github.com/ethereum/execution-apis/blob/main/src/engine/common.md). Meanwhile, Story's consensus layer, built on Cosmos modules, utilizes the Engine API to coordinate with the execution layer.

## Functionalities

The Engine API facilitates seamless interaction between the EL and the CL by providing essential coordination mechanisms, including:

* **Handshake**
* **Synchronization**
* **Block Validation**
* **Block Proposal**

## Execution Layer Implementation

The EL in Story implements the following standard Engine API methods to support these functionalities:

* `engine_exchangeCapabilities`: Exchanges supported methods.
* `engine_getClientVersion`: Exchanges client version data.
* `engine_newPayload`: Inserts the given payload into the local chain.
* `engine_forkchoiceUpdate`: Updates the canonical chain marker and generates the payload with given attributes.
* `engine_getPayload`: Retrieves the pre-generated payload.

## Consensus Layer Interaction

How does Story's Consensus Layer (CL) interact with these methods? The answer lies in CometBFT ABCI++.

CometBFT is a state machine replication engine which provides consensus and security for Cosmos modules. ABCI++, also known as ABCI 2.0, is the interface between CometBFT and the actual state machine being replicated(i.e. EL's state machine).

ABCI++ comprises of a set of methods that interact with the Engine API, as outlined below:

### **1. PrepareProposal** (Proposing a New Block)

* The CL checks whether a payload is already being generated using `payloadID`.
* If not, the CL calls `engine_forkchoiceUpdate` to trigger a new payload generation.
* The CL then calls `engine_getPayload` with `payloadID` to fetch the payload and propose a new block.

### **2. ProcessProposal** (Processing a New Block)

* The CL calls `engine_newPayload` to  delivers the new block to the EL.
* The EL validates payload of the new block, executes transactions deterministically and updates its state.

### **3. FinalizeBlock** (Finalizing a Decided Block)

* The CL calls `engine_newPayload` to  delivers the finalized block to the EL.
* If the block has not yet been incorporated into the EL, the EL validates payload of the new block, executes transactions deterministically and updates its state.
* Since CometBFT provides instant finality, the CL calls `engine_forkchoiceUpdate` to finalize the block.
* Finally, the CL calls `engine_forkchoiceUpdate` again, with extra attributes,  to start an optimistic build of the next block if enabled, and if the validator is the next proposer.

This interaction ensures smooth coordination between the EL and the CL, maintaining the integrity and efficiency of Story's blockchain network.

# evmstaking

## Abstract

This document specifies the internal `x/evmstaking` module of the Story blockchain.

In Story blockchain, the gas token resides on the execution layer (EL) to pay for transactions and interact with smart contracts. However, the consensus layer (CL) manages the consensus staking, slashing, and rewarding. This module exists to facilitate CL-level staking-related logic, such as delegating to validators with custom lock periods.

## Contents

1. **[State](#state)**
2. **[Two Queue System](#two-queue-system)**
3. **[Withdrawal Queue Content](#withdrawal-queue-content)**
4. **[End Block](#end-block)**
5. **[Processing Staking Events](#processing-staking-events)**
6. **[Withdrawing Delegations](#withdrawing-delegations)**
7. **[Withdrawing Rewards](#withdrawing-rewards)**
8. **[Withdrawing UBI](#withdrawing-ubi)**

## State

### Withdrawal Queue

Type: `Queue[types.Withdrawal]`

The (stake) withdrawal queue stores the pending unbonded stakes to be burned on CL and minted on EL. Stakes that are unbonded after 14 days of unstaking period are added to the queue to be processed.

### Reward Withdrawal Queue

Type: `Queue[types.Withdrawal]`

The reward withdrawal queue stores the pending rewards from stakes to be burned on CL and minted on EL. All rewards above a threshold are eligible to be queued in this queue, but there exists a parameter of maximum additions per block.

### Parameters

```protobuf protobuf
message Params {
  uint32 max_withdrawal_per_block = 1 [
    (gogoproto.moretags) = "yaml:\"max_withdrawal_per_block\""
  ];
  uint32 max_sweep_per_block = 2 [
    (gogoproto.moretags) = "yaml:\"max_sweep_per_block\""
  ];
  uint64 min_partial_withdrawal_amount = 3 [
    (gogoproto.moretags) = "yaml:\"min_partial_withdrawal_amount\""
  ];
  string ubi_withdraw_address = 4 [
    (gogoproto.moretags) = "yaml:\"ubi_withdraw_address\""
  ];
}
```

- `max_withdrawal_per_block` is the maximum number of withdrawals (reward and unstakes, each) to process per block. This parameter prevents nodes from processing a large amount of withdrawals at once, which could exceed the max chain timeout.
- `max_sweep_per_block` is the maximum number of validator-delegator delegations to sweep per block. This parameter prevents nodes from processing a large amount of delegations at once.
- `min_partial_withdrawal_amount` is the minimum amount required for rewards to get added to the reward withdrawal queue.
- `ubi_withdrawal_address` is the UBI contract address to which UBI withdrawals should be deposited.

### Delegator Withdraw Address

Type: `Map[string, string]`

The delegator-withdraw address mapping tracks the address to which a delegator receives their withdrawn stakes. The (stake) withdrawal queue uses this map to determine the `execution_address` in the `Withdrawal` struct used in building an EVM block payload.

While the delegator can change the withdraw address at any time, existing stake withdraw requests in the (stake) withdrawal queue will maintain their original values.

### Delegator Reward Address

The delegator-reward address mapping tracks the address to which a delegator receives their reward stakes, similar to the delegator-withdraw mapping.

While the delegator can change the reward address at any time, existing reward withdraw requests in the reward withdrawal queue will maintain their original values.

Type: `Map[string, string]`

### Delegator Operator Address

Type: `Map[string, string]`

The delegator-operator address mapping tracks the address to which a delegator has given the privilege to delegate (stake), undelegate (unstake), and redelegate on behalf of themselves.

### IP Token Staking Contract

Type: `*bindings.IPTokenStaking`

IPTokenStaking contract is used to filter and parse staking-related events from EL.

## Two Queue System

The module departs from traditional Cosmos SDK staking module's unstaking system, where all unbonded entries (stakes that have unbonded after 14 days of unbonding period) are immediately distributed into delegators account. Instead, Story's unstaking system assimilates Ethereum 2.0's unstaking system, where 16 full or partial (reward) withdrawals are processed per slot.

In a single queue of withdrawals, reward withdrawals can significantly delay stake withdrawals. Hence, Story blockchain implements a two-queue system where a max amount to process per block is enforced per queue. In other words, the stake/ubi withdrawal and reward withdrawal queues can each process the max parameter per block.

## Withdrawal Queue Content

Since the module only processes unstakes/rewards/ubi and stores them in queues, the actual dequeueing for withdrawal to the execution layer is carried out in the [evmengine](/network/node-architecture/cosmos-modules/evmengine-module) module. More specifically, a proposer dequeues the max number of withdrawals from each queue and adds them to the EVM block payload, which gets executed by EL via the [Engine API](/network/node-architecture/engine-api). When validators receive proposed block payload from the proposer, they individually peek the local queues and compare them against the received block's withdrawals. Mismatching withdrawals indicate non-determinism in staking logics and should result in chain halt.

In other words, the `evmstaking` module is in charge of parsing, processing, and inserting withdrawal requests to two queues, while the `evmengine` module is in charge of validating and dequeuing withdrawal requests, as well as depositing them to corresponding withdrawal addresses in EL.

## End Block

The `EndBlock` ABCI2 call is responsible for fetching the unbonded entries (stakes that have unbonded after 14 days) from the [staking](/network/node-architecture/cosmos-modules/staking-module) module and inserting them into the (stake) withdrawal queue. Furthermore, it processes stake reward withdrawals into the reward withdrawal queue and UBI withdrawals into the (stake) withdrawal queue.

If the network is in the [Singularity period](/network/tokenomics-staking#singularity), the End Block is skipped as there are no staking rewards and withdrawals available during this period. Otherwise, refer to [Withdrawing Delegations](#withdrawing-delegations) and [Withdrawing Rewards](#withdrawing-rewards) for detailed withdrawal processes.

## Processing Staking Events

The module parses and processes staking events emitted from the [IPTokenStaking contract](https://github.com/piplabs/story/blob/main/contracts/src/protocol/IPTokenStaking.sol), which are collected by the [evmengine](/network/node-architecture/cosmos-modules/evmengine-module) module. The list of events are:

### Staking events

- Create Validator
- Deposit (delegate)
- Withdraw (undelegate)
- Redelegate
- Unjail: anyone can request to unjail a jailed validator by paying the unjail fee in the contract.

These operations incur a fixed gas cost to prevent spam.

### Parameter events

- Update Validator Commission: update the validator commission.
- Set Withdrawal Address: delegator can modify their withdrawal address for future unstakes/undelegations.
- Set Reward Address: delegator can modify their withdrawal address for future reward emissions.
- Set Operator: delegator can modify their operator with privileges of delegation, undelegation, and redelegation.
- Unset Operator: delegator can remove operator.

These operations incur a fixed gas cost to prevent spam.

## Withdrawal

Both withdrawal queues hold withdrawals of type:

```protobuf protobuf
message Withdrawal {
  option (gogoproto.equal) = true;
  option (gogoproto.goproto_getters) = false;

  uint64 creation_height = 1;
  string execution_address = 2 [
    (cosmos_proto.scalar) = "cosmos.AddressString",
    (gogoproto.moretags) = "yaml:\"execution_address\""
  ];
  uint64 amount = 3 [
    (gogoproto.moretags) = "yaml:\"amount\""
  ];
  WithdrawalType withdrawal_type = 4 [
    (gogoproto.moretags) = "yaml:\"withdrawal_type\""
  ];
  string validator_address = 5 [
    (gogoproto.moretags) = "yaml:\"validator_address\""
  ];
}
```

- `creation_height` is the block height at which the withdrawal is created.
- `execution_address` is the EVM address receiving the withdrawn fund, which is burned in CL.
- `amount` is the amount to burn on CL and mint on EL.
- `withdrawal_type` is the type of withdrawal: $0$ for unstakes, $1$ for reward, and $2$ for UBI.
- `validator_address` is the EVM validator address.

### Withdrawing Delegations

Delegations that have unbonded after 14 days of unbonding period (ie. unbonded entries) gets added to the (stake) withdrawal queue at the end of each block. If validator is totally-unstaked, ie. all delegations and self-delegations are unbonded, then validator's commission is also withdrawn.

### Withdrawing Rewards

Inflation rewards allocated to delegations are auto-swept at the end of each block. If a delegation's accrued reward is greater than the parameterized threshold, the reward is added to the reward withdrawal queue to be credited to the delegator's EVM reward address.


# mint
## Contents

1. [Contents](#contents)
2. [State](#state)
3. [Begin Block](#begin-block)
4. [Parameters](#parameters)
5. [Events](#events)

## State

### Params

* Params: `mint/params -> legacy_amino(params)`

```protobuf protobuf
message Params {
  option (amino.name) = "client/x/mint/Params";

  // type of coin to mint
  string mint_denom = 1;
  // inflation amount per year
  string inflations_per_year = 2 [
    (cosmos_proto.scalar)  = "cosmos.Dec",
    (gogoproto.customtype) = "cosmossdk.io/math.LegacyDec",
    (gogoproto.nullable)   = false
  ];
  // expected blocks per year
  uint64 blocks_per_year = 3;
}
```

## Begin Block

Minting parameters are calculated and inflation paid at the beginning of each block.

### Inflation amount calculation

Inflation amount is calculated using an "inflation calculation function" that's\
passed to the `NewAppModule` function. If no function is passed, then the SDK's
default inflation function will be used (`DefaultInflationCalculationFn`). In case a custom
inflation calculation logic is needed, this can be achieved by defining and
passing a function that matches `InflationCalculationFn`'s signature.

```go
type InflationCalculationFn func(ctx sdk.Context, minter Minter, params Params, bondedRatio math.LegacyDec) math.LegacyDec
```

## Parameters

The minting module contains the following parameters:

| Key               | Type            | Example             |
| ----------------- | --------------- | ------------------- |
| MintDenom         | string          | "stake"             |
| InflationsPerYear | string (dec)    | "20000000000000000" |
| BlocksPerYear     | string (uint64) | "10368000"          |

* `MintDenom` is the coin denominator used.
* `InflationsPerYear` is the target inflation per year, in 1e18 decimals.
* `BlocksPerYear` is the target number of blocks per year.

## Events

The minting module emits the following events:

### BeginBlocker

| Type | Attribute Key | Attribute Value |
| :--- | :------------ | :-------------- |
| mint | amount        | "1000"          |

# evmengine

## Abstract

This document specifies the internal `x/evmengine` module of the Story blockchain.

As Story Network separates the consensus and execution client, like Ethereum, the consensus client (CL) and execution client (EL) needs to communicate to sync to the network, propose proper EVM blocks, and execute EVM-triggered EL actions in CL.

The module exists to facilitate all communications between CL and EL using the [Engine API](/network/node-architecture/engine-api), from staking and upgrades to driving block production and consensus in CL and EL.

## Contents

1. **[State](#state)**
2. **[Prepare Proposal](#prepare-proposal)**
3. **[Process Proposal](#process-proposal)**
4. **[Post Finalize](#post-finalize)**
5. **[Messages](#messages)**
6. **[UBI](#ubi)**
7. **[Upgrades](#upgrades)**

## State

### Build Delay

Type: `time.Duration`

Build delay determines the wait duration from the start of `PrepareProposal` ABCI2 call before fetching the next EVM block data to propose from EL via the [Engine API](/network/node-architecture/engine-api). Applicable to the current proposer only. If the node has a block optimistically built beforehand, the build delay is not used.

### Build Optimistic

Type: `bool`

Enable optimistic building of a block if true. A node will deterministically build the next block if it finds itself as the next proposer in the current block. Optimistic building starts with requesting the next EVM block data (for the next CL block) immediately after the `FinalizeBlock` of ABCI2.

### Head Table

Type: `ExecutionHeadTable`

Head table stores the latest execution head data to be used for partial validation of EVM blocks received from other validators. When the chain initializes, the execution head is populated with the genesis execution hash loaded from `genesis.json`.

The following execution head is stored in the table.

```protobuf protobuf
message ExecutionHead {
  option (cosmos.orm.v1.table) = {
    id: 1;
    primary_key: { fields: "id", auto_increment: true }
  };

  uint64 id               = 1; // Auto-incremented ID (always and only 1).
  uint64 created_height   = 2; // Consensus chain height this execution block was created in.
  uint64 block_height     = 3; // Execution block height.
  bytes  block_hash       = 4; // Execution block hash.
  uint64 block_time       = 5; // Execution block time.
}
```

### Upgrade Contract

Type: `*bindings.UpgradeEntrypoint`

Upgrade contract is used to filter and parse upgrade-related events from EL.

### UBI Contract

Type: `*bindings.UBIPool`

UBI contract is used to filter and parse UBI-related events from EL.

### Mutable Payload

Type: struct

Mutable payload stores the optimistic block built, if optimistic building is enabled.

#### Genesis State

The module's `GenesisState` defines the state necessary for initializing the chain from a previously exported height.

```protobuf protobuf
message GenesisState {
  Params params = 1 [(gogoproto.nullable) = false];
}

message Params {
  bytes execution_block_hash = 1 [
    (gogoproto.moretags) = "yaml:\"execution_block_hash\""
  ];
}
```

## Prepare Proposal

At each block, if the node is the proposer, ABCI2 triggers `PrepareProposal` which

1. Loads staking & reward withdrawals from the [evmstaking](/network/node-architecture/cosmos-modules/evmstaking-module) module.
2. Builds a valid EVM block.
   - If optimistic building: loads the optimistically built block.
   - Non-optimistic: requests and retrieves an EVM block from EL.
3. Collects the EVM logs of the previous/parent block.
4. Assembles `MsgExecutionPayload` with the built EVM block and previous EVM logs.
5. Returns a transaction containing the assembled `MsgExecutionPayload` data.

This CL block is then propagated to all other validators.

## Process Proposal

At each block, if the node is not a proposer but a validator, ABCI2 triggers `ProcessProposal` with received commits (which should be a transaction of `MsgExecutionPayload` data in the honest case).

The node first validates that the received commit has only one transaction with at least 2/3 of votes committed. Then, the node validates that the one transaction only contains one unmarshalled `MsgExecutionPayload` data. Finally, the node processes the received data and broadcasts its acceptance of the proposal to the network. If any of the validation or processing fails, the node rejects the proposal.

More specifically, the node processes the received `MsgExecutionPayload` data in the following manner:

1. Validates the fields of the received `MsgExecutionPayload` (outlined in [Messages](#msgexecutionpayload)).
2. Compare local stake & reward withdrawals with the received withdrawals data.
3. Push the received execution payload to EL via the Engine API and wait for payload validation.
4. Update the EL forkchoice to the execution payload's block hash.
5. Process staking events using the [evmstaking](/network/node-architecture/cosmos-modules/evmstaking-module) module.
6. Process upgrade events.
7. Update the execution head to the execution payload (finalized block).

## Post Finalize

If optimistic building is enabled, `PostFinalize` is triggered immediately after `FinalizeBlock` set through custom ABCI callback. During this process, the node peeks the staking and reward queues from the evmstaking module, and builds a new execution payload on top of the current execution head. It sets the optimistic block to be used in the next block's `PrepareProposal` phase and returns the response from the forkchoice update.

## Messages

In this section we describe the processing of the evmengine messages and the corresponding updates to the state. All created/modified state objects specified by each message are defined within the state section.

### MsgExecutionPayload

```protobuf protobuf
message MsgExecutionPayload {
  option (cosmos.msg.v1.signer) = "authority";
  string            authority           = 1;
  bytes             execution_payload   = 2;
  repeated EVMEvent prev_payload_events = 3;
}

message EVMEvent {
  bytes          address = 1;
  repeated bytes topics  = 2;
  bytes          data    = 3;
  bytes          tx_hash = 4;
}
```

This message is expected to fail if:

- authority is invalid (not evmengine authority)
- execution payload fails to unmarshal to [ExecutableData](https://github.com/piplabs/story/blob/c38b80c13579d3df7174ea10c3368ef0692f52da/client/x/evmengine/types/executable_data.go#L17-L35) for reasons such as invalid fields
- execution payload's block number does not match CL head's block number + 1
- execution payload's block parent hash does not match CL head's hash
- execution payload's timestamp is invalid
- execution payload's RANDAO does not match CL head's hash (ie. parent hash)
- execution payload's `Withdrawals`, `BlobGasUsed`, and `ExcessBlobGas` fields are nil
- execution payload's `Withdrawals` count does not match local node's sum of dequeued stake & reward withdrawals

The message must contain previous block's events, which gets processed at the current CL block (in other words, execution events from EL block n-1 are processed at CL block n). In the future, the message will remove `prev_payload_events` and rely on [Engine API](/network/node-architecture/engine-api) to get the current finalized EL block's events.

Also note that EVM events are processed in CL in the order they are generated in EL.

## UBI

All UBI-related changes must be triggered from the canonical UBI contract in the EVM execution layer. This module handles the execution handling of those triggers in CL. Read more about [UBI for validators](/network/tokenomics-staking#ubi-for-validators)

### Set UBI Distribution

The `UBIPool` contract emits the UBI distribution set event, which is parsed by the module to set the UBI percentage in the distribution module.

## Upgrades

All chain upgrade-related logics must be triggered from the canonical upgrade contract in the EVM execution layer. This module handles the execution handling of those triggers in CL.

### Software Upgrade

The `UpgradeEntrypoint` contract emits the software upgrade event, which is parsed by the module to schedule an upgrade at a given height for a given binary name. Currently, all upgrades must either be set via forks or by the software upgrade events; the latter process is a multisig-controlled process, which will transition into a voting-based process in the future.

### Cancel Upgrade

Similar to the software upgrade, the module processes the cancel upgrade event from EVM logs of the previous block, and clears an existing upgrade plan.


# staking

## Abstract

The staking module has been modified to accommodate for the following changes below. Refer to the Cosmos SDK's [staking module docs](https://docs.cosmos.network/main/build/modules/staking) for more information.

## Reward Multiplier

### Validators

Validators can choose to accept either locked tokens or unlocked tokens as delegations. Validators for locked tokens are conditioned to half the inflation allocation of validators for unlocked tokens.

Since each validator receives different inflation distribution based on delegations, the inflation distribution I<sub>v<sub>i</sub></sub> for validator v<sub>i</sub> in the rewards pool is calculated as follows:

<Image
  align="center"
  src="https://files.readme.io/3ee4914a7cc6036ceebbdd31ce93e525984a08364f8c3ab2152b86b3bcd5df7e-Screenshot_2025-02-11_at_8.30.07_AM.png"
/>

where

- I<sub>v<sub>i</sub></sub> is the total inflationary token rewards for v<sub>i</sub>
- S<sub>v<sub>i</sub></sub> is the staked tokens for v<sub>i</sub>
- M<sub>v<sub>i</sub></sub> is the rewards multiplier for v<sub>i</sub>
  - 0.5 for locked tokens
  - 1 for unlocked tokens
- R<sub>n</sub> is the total inflationary tokens allocated for the rewards pool in block n, calculated in the [mint](/network/node-architecture/cosmos-modules/mint-module) module

### Delegations

Delegators can delegate with four different staking lock times, which results in different staking reward multiplier for each delegation (delegator-validator pair of stakes). The inflation distribution for each delegation D<sub>i</sub> is calculated as follows:

<Image
  align="center"
  src="https://files.readme.io/002ae69aa3b3e52a33747452fe0c0b91b9120f20155deb19b56fb7917132b8de-Screenshot_2025-02-11_at_8.34.44_AM.png"
/>

where

- S<sub>d<sub>i</sub></sub> is the staked tokens of delegation d<sub>i</sub> on validator v<sub>d</sub>
- M<sub>d<sub>i</sub></sub> is the rewards multiplier of d<sub>i</sub> on v<sub>d</sub>
- I<sub>v</sub> is the total inflationary token rewards for v<sub>d</sub>
- C<sub>v</sub> is the commission rate for v<sub>d</sub>

#### Time-weighted Reward Multiplier M<sub>d<sub>i</sub></sub>

- _Flexible_ (no lockup): 1
- _Short_ (90 days): 1.1
- _Medium_ (360 days): 1.5
- _Long_ (540 days): 2.0


# List of Modules

# List of Modules

Here is a list of all production-grade modules that can be used on the Story blockchain, along with their respective documentation:

- [evmengine](/network/node-architecture/cosmos-modules/evmengine-module) - Handles Cosmos-side logics on each EVM state transition via the [Engine API](/network/node-architecture/engine-api).
- [evmstaking](/network/node-architecture/cosmos-modules/evmstaking-module) - Handles staking and network emission logics with queues.
- [mint](/network/node-architecture/cosmos-modules/mint-module)

## Cosmos SDK (modified)

Story network uses the following Cosmos SDK modules with some modifications:

- [staking](/network/node-architecture/cosmos-modules/staking-module)
- [distribution](https://docs.cosmos.network/main/build/modules/distribution)

## Cosmos SDK (unmodified)

Story network uses the following Cosmos SDK modules without non-trivial modifications:

- [auth](https://docs.cosmos.network/main/build/modules/auth)
- [bank](https://docs.cosmos.network/main/build/modules/bank)
- [consensusparams](https://docs.cosmos.network/main/build/modules/consensus)
- [gov](https://docs.cosmos.network/main/build/modules/gov)
- [slashing](https://docs.cosmos.network/main/build/modules/slashing)
- [upgrade](https://docs.cosmos.network/main/build/modules/upgrade)


# Precompiles

## Introduction

Precompiled contracts are specialized smart contracts implemented directly in the execution layer of a blockchain. Unlike user-deployed smart contracts that execute EVM bytecode, precompiled contracts offer optimized native implementations for complex cryptographic and computational operations. This significantly improves efficiency and reduces gas costs. Precompiled contracts exist at fixed addresses within the execution client and each precompile has a predefined gas cost based on its computational complexity, ensuring predictable execution fees.

Story Protocol introduces two precompiled contracts:

- `p256Verify` precompile to support signature verifications in the secp256r1 elliptic curve.
- `ipgraph` precompile to enhance on-chain intellectual property management.

In addition, Story Protocol’s execution layer supports all standard EVM precompiled contracts, ensuring full compatibility with Ethereum-based tooling and applications.

## Precompiled Contracts

| Address | Functionality                                                 |
| ------- | ------------------------------------------------------------- |
| byte1   | `ecrecover`- ECDSA signature recovery                         |
| byte2   | `sha256` - SHA-256 hash computation                           |
| byte3   | `ripemd160` - RIPEMD-160 hash computation                     |
| byte4   | `identity` - Identity function                                |
| byte5   | `modexp` - Modular exponentiation                             |
| byte6   | `bn256Add` - BN256 elliptic curve addition                    |
| byte7   | `bn256ScalarMul` - BN256 elliptic curve scalar multiplication |
| byte8   | `bn256Pairing` - BN256 elliptic curve pairing check           |
| byte9   | `blake2f` - Blake2 hash function                              |
| byte10  | `kzgPointEvaluation` - KZG polynomial commitment evaluation   |
| byte0   | `p256Verify` - Secp256r1 signature verification               |
| byte1   | `ipgraph` - Intellectual property management                  |

## p256Verify precompile

Refer to [RIP-7212](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md) for more information.

## IPgraph precompile

The `ipgraph` precompile enables efficient querying and modification of IP relationships and royalty structures while minimizing gas costs.

This precompile provides multiple functions based on the function selector—the first 4 bytes of the input.

| Function Selector        | Description                                                     | Gas computation formula                               | Gas Cost                           |
| :----------------------- | :-------------------------------------------------------------- | :---------------------------------------------------- | :--------------------------------- |
| `addParentIp`            | Adds a parent IP record                                         | `intrinsicGas + (ipGraphWriteGas * parentCount)`      | Larger than 1100                   |
| `hasParentIp`            | Checks if an IP is parent of another IP                         | `ipGraphReadGas * averageParentIpCount`               | 40                                 |
| `getParentIps`           | Retrieves parent IPs                                            | `ipGraphReadGas * averageParentIpCount`               | 40                                 |
| `getParentIpsCount`      | Gets the number of parent IPs                                   | `ipGraphReadGas`                                      | 10                                 |
| `getAncestorIps`         | Retrieves ancestor IPs                                          | `ipGraphReadGas * averageAncestorIpCount * 2`         | 600                                |
| `getAncestorIpsCount`    | Gets the number of ancestor IPs                                 | `ipGraphReadGas * averageParentIpCount * 2`           | 80                                 |
| `hasAncestorIp`          | Checks if an IP is ancestor of another IP                       | `ipGraphReadGas * averageAncestorIpCount * 2`         | 600                                |
| `setRoyalty`             | Sets royalty details of an IP                                   | `ipGraphWriteGas`                                     | 1000                               |
| `getRoyalty`             | Retrieves royalty details of an IP                              | `varies by royalty policy`                            | LAP:900, LRP:620, other:1000       |
| `getRoyaltyStack`        | Retrieves royalty stack of an IP                                | `varies by royalty policy`                            | LAP:50, LRP: 600, other:1000       |
| `hasParentIpExt`         | Checks if an IP is parent of another IP through external call   | `ipGraphExternalReadGas * averageParentIpCount`       | 8400                               |
| `getParentIpsExt`        | Retrieves parent IPs through external call                      | `ipGraphExternalReadGas * averageParentIpCount`       | 8400                               |
| `getParentIpsCountExt`   | Gets the number of parent IPs through external call             | `ipGraphExternalReadGas`                              | 2100                               |
| `getAncestorIpsExt`      | Retrieve ancestor IPs through external call                     | `ipGraphExternalReadGas * averageAncestorIpCount * 2` | 126000                             |
| `getAncestorIpsCountExt` | Gets the number of ancestor IPs through external call           | `ipGraphExternalReadGas * averageParentIpCount * 2`   | 16800                              |
| `hasAncestorIpExt`       | Checks if an IP is ancestor of another IP through external call | `ipGraphExternalReadGas * averageAncestorIpCount * 2` | 126000                             |
| `getRoyaltyExt`          | Retrieves royalty details of an IP through external call        | `varies by royalty policy`                            | LAP:189000, LRP:130200, other:1000 |
| `getRoyaltyStackExt`     | Retrieves royalty stack of an IP through external call          | `varies by royalty policy`                            | LAP:10500, LRP:126000, other:1000  |

Refer to the [Royalty Module](/concepts/royalty-module) for detailed information on royalty policies.


# Node Architecture

Story is a purpose-built modular blockchain fully EVM compatible using Cosmos SDK and CometBFT to achieve fast block time and one-shot finality. A Story node consists of two clients: `story-geth` as the execution client (EL) and a `story` as the consensus client (CL). These clients communicate via the [Engine API interface](/network/node-architecture/engine-api) defined by [Ethereum](https://hackmd.io/@danielrachi/engine_api).

`story-geth` is a fork of the Geth client, with the addition of the [IPGraph Precompile](/network/node-architecture/precompile) and [RIP-7212](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md) precompile. It handles transaction execution, broadcasting and state storage while maintaining full compatibility with the Ethereum Virtual Machine (EVM) and supporting all Ethereum JSON-RPC methods.

`story` is built on the Cosmos SDK and CometBFT. The Cosmos SDK provides a modular framework for building blockchain applications, enabling seamless integration of new modules and features while allowing the network to be easily extended and customized. `story` client introduces upgrades and additional Cosmos SDK modules to support Engine API integration and novel staking mechanisms. CometBFT, a high-performance, scalable, and secure consensus engine, has been extensively tested within the Cosmos ecosystem. CometBFT and Cosmos SDK communicate through ABCI++ interface(link to ABCI++ spec).

<img src="/images/network/node-architecture.png" />

<Warning>
  Do not use `RANDAO` for pseudo-randomness, instead use onchain VRF (Pyth or
  Gelato). Currently, `RANDAO` value is set as the parent block hash and thus is
  not random for X-1 block.
</Warning>


# Welcome to Story Network

<CardGroup cols={2}>
  <Card title="Add Story Mainnet" href="https://chainid.network/chain/1514/" icon="house">
    Connect your wallet to Story's mainnet.
  </Card>

  <Card title="Add Story 'Aeneid' Testnet" href="https://chainid.network/chain/1315/" icon="house">
    Connect your wallet to Story's 'Aeneid' testnet.
  </Card>
</CardGroup>

# Story Network (L1)

Welcome to the Hub for Story Network, the Story Chain.

This section is designed to help you understand the fundamentals of Story Network. We've structured the content into two parts:

1. Understanding the Architecture
2. Operating a Node

Story Network is a purpose-built Layer 1 blockchain that seamlessly integrates the best of both the Ethereum Virtual Machine (EVM) and Cosmos SDK. It offers full EVM compatibility while incorporating deep execution layer optimizations to efficiently support graph-based data structures. These optimizations make it particularly well-suited for handling complex intellectual property (IP) data structures in a cost-effective and scalable manner.

<Frame>
  <iframe
    src="https://www.youtube.com/embed/JWd5TCOHfhU"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
    className="w-full aspect-video"
  ></iframe>
</Frame>

## Key Features

- **EVM Compatibility**: Full compatibility with Ethereum Virtual Machine
- **Optimized Data Structures**: Precompiled primitives for efficient IP graph traversal
- **Fast Finality**: CometBFT-based consensus layer for quick transaction finality
- **Modular Architecture**: Decoupled consensus from execution using Ethereum's Engine-API

## Documentation Sections

### Getting Started

- [Node Architecture](/network/node-architecture)
- [Network Info](/network/network-info)
- [Whitepaper](https://www.story.foundation/whitepaper.pdf)

### Node Operations

- [Operating a node](/network/operating-a-node)
  - Full Node Setup
  - Archive Node Setup
  - Node Upgrade Guide
  - Release Notes

### Validation

- [Become a validator](/network/become-a-validator)
  - Validator Setup
  - Validator Operations

### Network Economics

- [Staking Design](/network/tokenomics-staking)
  - Token Economics
  - Staking Mechanisms
  - Rewards Structure

### Resources

- [Additional Resources](/network/more/additional-resources)
  - GitHub Repositories
  - SIP Repository
  - Community Forum
- [Troubleshooting](/network/more/troubleshooting)
  - Common Issues
  - Troubleshooting
  - Best Practices

## Network Information

The Story Network is currently available in multiple environments:

- Mainnet (Production)
- Aeneid (Testnet)
- Localnet (Development)

For detailed network information and connection details, please refer to the respective network documentation sections.


# Become a Validator

## Quick Links

<CardGroup cols={2}>
  <Card
    title="Story Geth Releases"
    icon="github"
    href="https://github.com/piplabs/story-geth/releases"
  >
    Download the latest Story Geth client releases
  </Card>
  <Card
    title="Story Releases"
    icon="github"
    href="https://github.com/piplabs/story/releases/"
  >
    Download the latest Story consensus client releases
  </Card>
</CardGroup>

# Overview

This section will guide you through how you can run your own validator. Validator operations may be done via the `story` consensus client.

<Note>
  The below operations do not require running a node! However, if you would like
  to participate in staking rewards, you must run a validator node.
</Note>

Before proceeding, it is important to familiarize yourself with the difference between a delegator and a validator:

- A **validator** is a full node that participates in consensus whose signed key resides in the `priv_validator_key.json` file under your `story` data directory. To print out your validator key details you may refer to the [validator key export section](/network/become-a-validator#validator-key-export)
- A **delegator** refers to an account operator that holds `IP` and wishes to participate in consensus rewards but without needing to run a validator themselves.

In the same folder as where your `story` binary resides, add a `.env` file with a `PRIVATE_KEY` whose account has `IP` funded. **We recommend using your delegator account for all below operations.**

<Note>
  You may also issue transactions as the validator itself. To get the EVM
  private key corresponding to your validator, please refer to the [Validator
  Key Export](#validator-key-export) section.
</Note>

The `.env` file should look like the following _(make sure not to add a 0x prefix):_

```bash
# ~/.env
PRIVATE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

With this, you are all set to perform different validator operations! Below, we will guide you through all of those supported via the CLI:

## Validator Key Export

By default, when you run `./story init` a validator key is created for you. To view your validator key, run the following command:

```bash
./story validator export [flags]
```

This will print out your validator public key file in compressed and uncompressed formats. By default, we use the hex-encoded compressed key for public identification.

```text
Compressed Public Key (hex): 03bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a63984
Compressed Public Key (base64): A73HuJQLq+kibVLX+imaH689ZKgvgJiJJWyPFGlYpjmE
Uncompressed Public Key (hex): 04bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a6398496b9e2af0a3a1d199c3cc1d09ee899336a530c185df6b46a9735b25e79a493af
EVM Address: 0x9EacBe2C3B1eb0a9FC14106d97bd3A1F89efdDCc
Validator Address: storyvaloper1p470h0jtph4n5hztallp8vznq8ehylsw9vpddx
Delegator Address: story1p470h0jtph4n5hztallp8vznq8ehylswtr4vxd
```

**Available Flags:**

- `--export-evm-key`: (string) Exports the derived EVM private key of your validator into the default data config directory
- `--export-evm-key-path`: (string) Specifies a different download location for the derived EVM private key of your validator
- `--keyfile`: (string) Path to the Tendermint key file (default "/home/ubuntu/.story/story/config/priv_validator_key.json")

<Tip>
  If you would like to issue transactions as your validator, and not as a
  delegator, you may export the key to your `.env` file and ensure it has IP
  sent to it, e.g. via `./story validator export --export-evm-key --evm-key-path
  .env`
</Tip>

## Validator Creation

To create a new validator, run the following command:

```bash Locked token node
./story validator create
			 --stake ${AMOUNT_TO_STAKE_IN_WEI} \
			 --moniker ${VALIDATOR_NAME} \
       --rpc ${rpc} \
		   --chain-id ${chain_id} \
			 --commission-rate ${rate} \
 			 --unlocked=false
```

```Text Unlocked token node
./story validator create
			 --stake ${AMOUNT_TO_STAKE_IN_WEI} \
			 --moniker ${VALIDATOR_NAME} \
       --rpc ${rpc} \
		   --chain-id ${chain_id} \
			 --commission-rate ${rate} \
```

This will create the validator corresponding to your validator key saved in `priv_validator_key.json`, providing the validator with `{$AMOUNT_TO_STAKE_IN_WEI}` IP to self-stake.

<Note>
  To participate in consensus, at least 1024 IP must be staked (equivalent to
  `1024000000000000000000 wei`)!
</Note>

Below is a list of optional flags to further customize your validator setup:

**Available Flags:**

- `--stake`: Sets the amount the validator will self-delegate in wei (default is `1024000000000000000000` wei).
- `--moniker`: Defines a custom name for the validator, visible to users on the network.
- `--chain-id`: Specifies the Chain ID for the transaction. By default, this is set to `1516`.
- `--commission-rate`: Sets the validator's commission rate in bips (1% = 100 bips). For instance, `1000` represents a 10% commission (default is `1000`).
- `--explorer`: Specifies the URL of the blockchain explorer (default: [https://www.storyscan.io](https://www.storyscan.io)).
- `--keyfile`: Points to the path of the Tendermint key file (default: `$HOME/.story/story/config/priv_validator_key.json`).
- `--max-commission-change-rate`: Sets the maximum rate at which the validator's commission can change, in bips. For example, `100` represents a maximum change of 1% (default is `1000`).
- `--max-commission-rate`: Defines the maximum commission rate the validator can charge, in bips. For instance, `5000` allows a 50% maximum rate (default is `5000`).
- `--private-key`: Uses a specified private key for signing the transaction. If not set, the key in `priv_validator_key.json` will be used.
- `--rpc`: Sets the RPC URL to connect to the network (default: [https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)).
- `--unlocked`: Determines if unlocked token staking is supported (`true` for unlocked staking, `false` for locked staking). By default, this is set to `true`.
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example creation command use

```bash
story validator create
	--stake 1024000000000000000000
  --moniker "timtimtim"
  --commission-rate 700
  --validator-pubkey "<validator_pubkey>" # if you dont have a .env
  --rpc "https://mainnet.storyrpc.io"
	--chain-id 1514
```

### Verifying your validator

Once created, please use the `Explorer URL` to confirm the transaction. If successful, you should see your validator pub key (_found in your`priv_validator_key.json` file)_ listed as part of the following endpoint:

```bash
curl https://testnet.storyrpc.io/validators | jq .
```

Congratulations, you are now one of Story’s very first IP validators!

## Validator Staking

To stake to an existing validator, run the following command:

```bash
./story validator stake \
   --validator-pubkey ${VALIDATOR_PUB_KEY_IN_HEX} \
   --stake ${AMOUNT_TO_STAKE_IN_WEI}
   --staking-period ${STAKING_PERIOD}
```

- Note that your own `${VALIDATOR_PUB_KEY_IN_HEX}`may be found by running the `./story validator export` command as the `Compressed Public Key (hex)`.
- You must stake at least 1024 IP worth (`*1024000000000000000000 wei`) for the transaction to be valid

Once staked, you may use the `Explorer URL` to confirm the transaction. As mentioned earlier, you may use our [validator endpoint](https://mainnet.storyrpc.io/validators) to confirm the new voting power of the validator.

**Available Flags:**

- `--validator-pubkey`: (string) The public key of the validator to stake to
- `--stake`: (string) The amount of IP to stake in wei
- `--chain-id`: (int) Chain ID to use for the transaction (default: 1514)
- `--explorer`: (string) URL of the blockchain explorer
- `--help`, `-h`: Display help information for stake command
- `--private-key`: (string) Private key used for the transaction
- `--rpc`: (string) RPC URL to connect to the network
- `--staking-period`: (stakingPeriod) Staking period (options: "flexible", "short", "medium", "long") (default: flexible)
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example staking command use

```bash
./story validator stake \
  --validator-pubkey 03bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a63984 \
  --stake 1024000000000000000000
  --staking-period "short"
```

## Validator Unstaking

To unstake from a validator, run the following command:

```bash
./story validator unstake \
  --validator-pubkey ${VALIDATOR_PUB_KEY_IN_HEX} \
  --unstake ${AMOUNT_TO_UNSTAKE_IN_WEI} \
	--delegation-id ${ID_STAKING_PERIOD}
```

This will unstake `${AMOUNT_TO_UNSTAKE_IN_WEI}` IP from the selected validator. You must unstake at least 1024 IP worth (`*1024000000000000000000 wei`) for the transaction to be valid.

Like in the staking operation, please use the `Explorer URL` to confirm the transaction and our [validator endpoint](https://mainnet.storyrpc.io/validators) to double-check the newly reduced voting power of the validator.

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction (default: 1514)
- `--delegation-id`: (uint32) The delegation ID (0 for flexible staking)
- `--explorer`: (string) URL of the blockchain explorer (default: "[https://www.storyscan.io](https://www.storyscan.io)")
- `--help`, `-h`: Help for unstake command
- `--private-key`: (string) Private key used for the transaction
- `--rpc`: (string) RPC URL to connect to the network (default: "[https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)")
- `--unstake`: (string) Amount to unstake in wei
- `--validator-pubkey`: (string) Validator's hex-encoded compressed 33-byte secp256k1 public key
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example unstaking command use

```bash
./story validator unstake \
   --validator-pubkey 03bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a63984 \
   --unstake 1024000000000000000000 \
   --delegation-id 1
```

## Validator Stake-on-behalf

To stake on behalf of another delegator, run the following command:

```bash
./story validator stake-on-behalf \
  --delegator-address ${DELEGATOR_EVM} \
  --validator-pubkey ${VALIDATOR_PUB_KEY_IN_HEX} \
  --stake ${AMOUNT_TO_STAKE_IN_WEI} \
  --staking-period ${STAKING_PERIOD} \
  --rpc
  --chain-id
```

This will stake `${AMOUNT_TO_STAKE_IN_WEI}` IP to the validator on behalf of the provided delegator. You must stake at least 1024 IP worth (`*1024000000000000000000 wei`) for the transaction to be valid.

Like in the other staking operations, please use the `Explorer URL` to confirm the transaction and our [validator endpoint](https://mainnet.storyrpc.io/validators) to double-check the increased voting power of the validator.

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction (default: 1514)
- `--delegator-address`: (string) Delegator's EVM address
- `--explorer`: (string) URL of the blockchain explorer (default: "[https://www.storyscan.io](https://www.storyscan.io)")
- `--help`, `-h`: Help for stake-on-behalf command
- `--private-key`: (string) Private key used for the transaction
- `--rpc`: (string) RPC URL to connect to the network (default: "[https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)")
- `--stake`: (string) Amount for the validator to self-delegate in wei
- `--staking-period`: (stakingPeriod) Staking period (options: "flexible", "short", "medium", "long") (default: flexible)
- `--validator-pubkey`: (string) Validator's hex-encoded compressed 33-byte secp256k1 public key
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example Stake-on-behalf command use

```bash
./story validator stake-on-behalf \
   --delegator-address 0xF84ce113FCEe12d78Eb41590c273498157c91520 \
   --validator-pubkey 03e42b4d778cda2f3612c85161ba7c0aad1550a872f3279d99e028a1dfa7854930 \
   --stake 1024000000000000000000 \
   --staking-period "short" \
	 --rpc \
   --chain-id
```

## Validator Unstake-on-behalf

You may also unstake on behalf of delegators. However, to do so, you must be registered as an authorized operator for that delegator. To unstake on behalf of another delegator as an operator, run the following command:

```bash
./story validator unstake-on-behalf \
  --delegator-address ${DELEGATOR_PUB_KEY_IN_HEX} \
  --validator-pubkey ${VALIDATOR_PUB_KEY_IN_HEX} \
  --unstake ${AMOUNT_TO_STAKE_IN_WEI} \
  --rpc \
  --chain-id
```

This will unstake `${AMOUNT_TO_STAKE_IN_WEI}` IP from the validator on behalf of the delegator, assuming you are a registered operator for that delegator. You must unstake at least 1024 IP worth (`*1024000000000000000000 wei`) for the transaction to be valid.

Like in the other staking operations, please use the `Explorer URL` to confirm the transaction and our [validator endpoint](https://mainnet.storyrpc.io/validators) to double-check the decreased voting power of the validator.

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction (default: 1514)
- `--delegator-address`: (string) Delegator's EVM address
- `--explorer`: (string) URL of the blockchain explorer (default: "[https://www.storyscan.io](https://www.storyscan.io)")
- `--help`, `-h`: Help for unstake-on-behalf command
- `--private-key`: (string) Private key used for the transaction
- `--rpc`: (string) RPC URL to connect to the network (default: "[https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)")
- `--unstake`: (string) Amount to unstake in wei
- `--validator-pubkey`: (string) Validator's hex-encoded compressed 33-byte secp256k1 public key
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example Unstake-on-behalf command use

```bash
./story validator unstake-on-behalf \
   --delegator-address 0xF84ce113FCEe12d78Eb41590c273498157c91520 \
   --validator-pubkey 03e42b4d778cda2f3612c85161ba7c0aad1550a872f3279d99e028a1dfa7854930 \
   --unstake 1024000000000000000000 \
   --rpc \
   --chain-id
```

## Validator Unjail

In case a validator becomes jailed, for example if it experiences substantial downtime, you may use the following command to unjail the targeted validator:

```Text Bash
./story validator unjail \
  --private-key ${PRIVATE_KEY} \
  --rpc
  --chain-id
```

Note that you will need at least 1 IP in the wallet submitting the transaction for the transaction to be valid.

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction
- `--explorer`: (string) URL of the blockchain explorer
- `--private-key`: (string) Private key used for the transaction
- `--rpc`: (string) RPC URL to connect to the network
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example unjail command use

```bash
./story validator unjail \
  --validator-pubkey 03bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a63984 \
  --rpc \
  --chain-id
```

## Validator Unjail-on-behalf

If you are an authorized operator, you may unjail a validator on their behalf using the following command:

```bash
./story validator unjail-on-behalf \
  --private-key ${PRIVATE_KEY} \
  --validator-pubkey ${VALIDATOR_PUB_KEY_IN_HEX} \
  --rpc \
  --chain-id
```

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction
- `--explorer`: (string) URL of the blockchain explorer
- `--private-key`: (string) Private key used for the transaction
- `--rpc`: (string) RPC URL to connect to the network
- `--validator-pubkey`: (string) Validator's hex-encoded compressed 33-byte secp256k1 public key
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example unjail-on-behalf command use

```bash
./story validator unjail-on-behalf \
  --private-key 0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef \
  --validator-pubkey 03e42b4d778cda2f3612c85161ba7c0aad1550a872f3279d99e028a1dfa7854930 \
  --rpc \
  --chain-id
```

## Validator Redelegate

To redelegate from one validator to another, run the following command:

```bash
./story validator redelegate \
  --validator-src-pubkey ${VALIDATOR_SRC_PUB_KEY_IN_HEX} \
  --validator-dst-pubkey ${VALIDATOR_DST_PUB_KEY_IN_HEX} \
  --redelegate ${AMOUNT_TO_REDELEGATE_IN_WEI}
  --rpc \
  --chain-id
```

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction (default 1514)
- `--delegation-id`: (uint32) The delegation ID (0 for flexible staking)
- `--explorer`: (string) URL of the blockchain explorer (default "[https://www.storyscan.io](https://www.storyscan.io)")
- `--help`, `-h`: Help for redelegate command
- `--private-key`: (string) Private key used for the transaction
- `--redelegate`: (string) Amount to redelegate in wei
- `--rpc`: (string) RPC URL to connect to the network (default "[https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)")
- `--validator-dst-pubkey`: (string) Dst validator's hex-encoded compressed 33-byte secp256k1 public key
- `--validator-src-pubkey`: (string) Src validator's hex-encoded compressed 33-byte secp256k1 public key
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example redelegate command use

```bash
./story validator redelegate \
  --validator-src-pubkey 03bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a63984 \
  --validator-dst-pubkey 02ed58a9319aba87f60fe08e87bc31658dda6bfd7931686790a2ff803846d4e59c \
  --redelegate 1024000000000000000000 \
  --rpc \
  --chain-id
```

## Validator Redelegate-on-behalf

If you are an authorized operator, you may redelegate from one validator to another on behalf of a delegator using the following command:

```bash
./story validator redelegate-on-behalf \
  --delegator-address ${DELEGATOR_EVM_ADDRESS} \
  --validator-src-pubkey ${VALIDATOR_SRC_PUB_KEY_IN_HEX} \
  --validator-dst-pubkey ${VALIDATOR_DST_PUB_KEY_IN_HEX} \
  --redelegate ${AMOUNT_TO_REDELEGATE_IN_WEI} \
  --rpc \
  --chain-id
```

**Available Flags:**

- `--chain-id`: (int) Chain ID to use for the transaction (default 1514)
- `--delegation-id`: (uint32) The delegation ID (0 for flexible staking)
- `--delegator-address`: (string) Delegator's EVM address
- `--explorer`: (string) URL of the blockchain explorer (default "[https://www.storyscan.io](https://www.storyscan.io)")
- `--help`, `-h`: Help for redelegate-on-behalf command
- `--private-key`: (string) Private key used for the transaction
- `--redelegate`: (string) Amount to redelegate in wei
- `--rpc`: (string) RPC URL to connect to the network (default "[https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)")
- `--validator-dst-pubkey`: (string) Dst validator's hex-encoded compressed 33-byte secp256k1 public key
- `--validator-src-pubkey`: (string) Src validator's hex-encoded compressed 33-byte secp256k1 public key
- `--story-api`: Prevent potential fund losses. By default, you should set `http://localhost:1317`as the value

### Example redelegate-on-behalf command use

```bash
./story validator redelegate-on-behalf \
  --delegator-address 0xf398C12A45Bc409b6C652E25bb0a3e702492A4ab \
  --validator-src-pubkey 03bdc7b8940babe9226d52d7fa299a1faf3d64a82f809889256c8f146958a63984 \
  --validator-dst-pubkey 02ed58a9319aba87f60fe08e87bc31658dda6bfd7931686790a2ff803846d4e59c \
  --redelegate 1024000000000000000000 \
  --rpc \
  --chain-id
```

## Set Operator

Delegators may add operators to unstake or redelegate on their behalf. To add an operator, run the following command:

- `--chain-id` int Chain ID to use for the transaction (default 1514)
- `--explorer` string URL of the blockchain explorer (default "[https://www.storyscan.io](https://www.storyscan.io)")
- `--operator` string Sets an operator to your delegator
- `--private-key` string Private key used for the transaction
- `--rpc` string RPC URL to connect to the network (default "[https://mainnet.storyrpc.io](https://mainnet.storyrpc.io)")

```bash
./story validator set-operator \
  --operator ${OPERATOR_EVM_ADDRESS} \
  --rpc \
  --chain-id \
  --story-api ${STORY_API_URL}
```

Note that you will need at least 1 IP in the wallet submitting the transaction for the transaction to be valid.

### Example add operator command use

```bash
./story validator set-operator \
  --operator 0xf398C12A45Bc409b6C652E25bb0a3e702492A4ab \
  --rpc \
  --chain-id \
  --story-api http://localhost:1317
```

## Unset Operator

To remove an operator, run the following command:

```bash
./story validator unset-operator \
  --operator ${OPERATOR_EVM_ADDRESS} \
  --rpc \
  --chain-id \
  --story-api ${STORY_API_URL}
```

### Example Remove Operator command use

```bash
./story validator remove-operator \
  --operator 0xf398C12A45Bc409b6C652E25bb0a3e702492A4ab \
  --rpc \
  --chain-id \
  --story-api http://localhost:1317
```

## Set Rewards Address

To change the address that your delegator receives staking and withdrawal rewards from, you can run the following:

```bash
./story validator set-rewards-address \
  --rewards-address ${OPERATOR_EVM_ADDRESS} \
  --story-api ${STORY_API_URL}
```

Note that you will need at least 1 IP in the wallet submitting the transaction for the transaction to be valid.

### Example Set Withdrawal Address command use

```bash
./story validator set-rewards-address \
  --rewards-address 0xf398C12A45Bc409b6C652E25bb0a3e702492A4ab
  --story-api http://localhost:1317
```

## Set Withdrawal Address

To change the address that your delegator receives staking and withdrawal rewards from, you can run the following:

```bash
./story validator set-withdrawal-address \
  --withdrawal-address ${OPERATOR_EVM_ADDRESS} \
  --story-api ${STORY_API_URL}
```

Note that you will need at least 1 IP in the wallet submitting the transaction for the transaction to be valid.

### Example Set Withdrawal Address command use

```bash
./story validator set-withdrawal-address \
  --withdrawal-address 0xf398C12A45Bc409b6C652E25bb0a3e702492A4ab
  --story-api http://localhost:1317
```

## Update Validator Commission

To change the commission rate for your validator, you can run the following:

```
./story validator update-validator-commission \
		--commission-rate ${NEW_COMMISSION}
```

### Example Update Validator Commission

```
./story validator update-validator-commission \
		--commission-rate 5000
```

## Enabling Story API

Prerequisites:

1. Ensure your full node is synced and caught up with latest blocks

Steps to enable:

1. Navigate to `${STORY_DATA_ROOT}/config/story.toml`
2. Set `enable = true` under the `[api]` section
3. Restart the node

Then you could use `http://localhost:1317` as the `-story-api` value

## Migrating a validator to another machine

<Warning>
  Before migrating your validator node to a new machine, make sure the current
  node is fully shut down. Attempting to restore an active validator could
  result in "double signing," a critical error that may lead to the slashing of
  your delegated shares.
</Warning>

1. Begin by configuring a new environment for your validator. Ensure that the new full node is fully synced to the latest block on the network.
2. To avoid accidental double-signing, it’s essential to fully shut down the original validator node before activating the new instance. We recommend deleting the Story service file to prevent it from automatically restarting after a system reboot. Additionally, back up both `priv_validator_key.json` and `priv_validator_state.json` and remove it from the current server running the active validator. Skipping these steps could result in missed blocks or other penalties.

```bash
# Step 1: Stop the original validator node
sudo systemctl stop <your_service_file_name>.service

# Step 2: Disable the Story service to prevent automatic restarts
sudo systemctl disable <your_service_file_name>.service

# Step 3: Delete the Story service file to prevent it from starting on reboot
sudo rm /etc/systemd/system/<your_service_file_name>.service

# Step 4: Back up the `priv_validator_key.json` file securely, e.g., using SFTP:
# Use an SFTP client or a secure method to download the file without displaying it in the terminal
# If needed for verification purposes only, you may view it with the following command:
cat ~/.story/story/config/priv_validator_key.json

# Step 5: Remove the `priv_validator_key.json` file from the current server
rm ~/.story/story/config/priv_validator_key.json
```

3. Locate `priv_validator_key.json` and `priv_validator_state.json` in the `~/.story/story/config/` directory on your new machine. Replace this file with the backup copy from your old validator.

<Warning>
  Before proceeding, shut down the old validator on the original server and do
  not restart it!
</Warning>

4. After transferring the private key file, restart the validator node on your new setup. This will reintegrate your validator with the network, enabling it to resume its validation role.


