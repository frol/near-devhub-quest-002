# NEAR DevHub Quest 002

It is the second quest in the NEAR DevHub Quests. Learn more in the [most recent DevHub Live episode](https://www.youtube.com/live/P9pCbtyGKzY?si=STLteoUUMUIC9n5p&t=2397).

It starts on March 7th, 2025, and was deployed to [neardev-quest-002.frol.near](https://explorer.near.org/accounts/neardev-quest-002.frol.near).

<img width="696" alt="image" src="https://github.com/user-attachments/assets/6080821c-b128-437c-b4bd-79417d9bea57" />

## Quest

The quest is simple: withdraw 50 NEAR from the contract.

## Rewards

The rewards are 50 NEAR.

## Development

This quest uses an early version of [near-sdk-py](https://github.com/near/near-sdk-py).

### Prerequisites

- Python 3.9 or higher
- [uv](https://pypi.org/project/uv/)
- [NEAR CLI](https://near.cli.rs)

### Setup

1. Install dependencies:

```sh
uv venv
uv sync
```

2. Build the contract:

```sh
uvx nearc
```

3. Deploy the contract:

```sh
near contract deploy use-file main.wasm
```