const HDWalletProvider = require('@truffle/hdwallet-provider');
const provider = new HDWalletProvider({
   privateKeys: ['9755aeded82ef7503111da8525e40ce203a82149ba82a5dc0f9ca4e9bd7186cd'],
   providerOrUrl: 'https://data-seed-prebsc-1-s1.binance.org:8545',
})


module.exports = {
  networks: {
    binanceTestnet: {
      provider: () => provider,
      network_id: "97",
      gas: 500000
    },
    develop: {
      port: 8545
    }
  } 
};
