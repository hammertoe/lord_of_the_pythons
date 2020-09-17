# Lord of the Pythons

![Party hard!](_images/gandalf_party_hard.gif)

## What?

A Github Action that analyses Python code and detects new variables named after LotR characters and a workflow that pays developers as a reward.

When you push code to a Github repo it goes through all .py files it can find, parses them with an AST and pulls out the variable names. It then cross references them against LotR characters... and if you have increased the number of variables named after LotR characters in this set of commits then you are immediately paid an amount of XRP for your devotion and love.

This action was created for the [DEV: Github Actions hackathon](https://dev.to/devteam/announcing-the-github-actions-hackathon-on-dev-3ljn).

As you might image, it is for the "Wacky" category.

It utilises the [Automatically pay Contributors in XRP via PayId](https://github.com/marketplace/actions/automatically-pay-contributors-in-xrp-via-payid) that was also developer by myself for this same hackathon.

## Why?!

Developers love fantasy like Lord of The Rings, right? Developers like getting paid, right?

So why not combine the two! Now whenever a Python developer adds a new variable named after a Lord of the Rings
character, they will be paid for their love and devotion.

Awesome!

## How to use it?

Create a workflow like this:

```yaml
name: Lord of the Pythons

on:
  # Trigger the workflow on push or pull request,
  # but only for the master branch
  push:
    branches:
      - master


jobs:
  pay:

    runs-on: ubuntu-latest

    steps:

    - name: Checkout code  
      uses: actions/checkout@v2
      with:
        fetch-depth: 5

    - name: Checkout prior code  
      uses: actions/checkout@v2
      with:
        ref: ${{ github.event.before }}
        path: .old-code

    - name: Checkout current code  
      uses: actions/checkout@v2
      with:
        path: .new-code

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: get commit message
      run: |
        echo ::set-env name=commit_log::$(git log --format=%B ${{ github.event.before }}..${{ github.event.after }})

    - name: Get number of new LotR characters
      id: lotr
      use: hammertoe/lord_of_the_pythons@master

    - name: Run PayID
      uses: hammertoe/payid_xrp_action@1.1
      if: ${{ steps.lotr.outputs.num > 0 }}
      with:
        wallet_secret: ${{ secrets.PAYID_WALLET_SECRET }}
        amount: ${{ steps.lotr.outputs.amount }}
        commit_log: ${{ env.commit_log }}
```