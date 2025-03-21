# Story Documentation

This repository contains the official documentation for **Story**, a purpose-built layer 1 blockchain designed specifically for intellectual property.

📚 [Official Documentation](https://docs.story.foundation)

## Proposing Changes

If you see any issues with the docs or would like to add/modify them, please open a Pull Request and tag @jacob-tucker :)

## Train AI on our Docs

If you want to train an AI on our docs, you can use the `combined.md` file. It contains all of our docs in a single `.md` file, and is updated automatically every time a change is made to the repo.

## Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of the repository (where docs.json is)

```
mintlify dev
```

### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`
