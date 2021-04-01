// digipeso ICO

// Version of compiler
pragma solidity ^0.4.11;

contract digipeso_ico {
    
    // Introducing the maximum number of digipeso available for sale
    uint public max_digipeso = 1000000;
    
    // Introducing the USD to digipeso conversion conversion rate
    uint public usd_to_digipeso = 1000;
    
    // Introducing the total number of Hadcoins that have been bought by the investors
    uint public total_digipeso_bought = 0;
    
    // Mapping from the investor address to its equity in digipeso and usd
    mapping(address => uint) equity_digipeso;
    mapping(address => uint) equity_usd;
    
    // checking if an investor can buy digipeso
    modifier can_buy_digipeso(uint usd_invested) {
        require (usd_invested * usd_to_digipeso + total_digipeso_bought <= max_digipeso);
        _;
    }
    
    // Getting the equity in digipeso of an investor
    function equity_in_digipeso(address investor) external constant returns (uint) {
        return equity_hadcoins[investor];
    }
    
    function equity_in_usd(address investor) external constant returns (uint) {
        return equity_usd[investor];
    }
    
    // Buying digipeso
    function buy_digipeso(address investor, uint usd_invested) external
    can_buy_digipeso(usd_invested) {
        uint digipeso_bought = usd_invested * usd_to_digipeso;
        equity_digipeso[investor] += digipeso_bought;
        equity_usd[investor] = equity_digipeso[investor] / 1000;
        total_digipeso_bought += digipeso_bought;
    }
    
    // Selling digipeso
    function sell_digipeso(address investor, uint digipeso_sold) external {
        equity_digipeso[investor] -= digipeso_sold;
        equity_usd[investor] = equity_digipeso[investor] / 1000;
        total_digipeso_bought -= digipeso_sold;
    }
}